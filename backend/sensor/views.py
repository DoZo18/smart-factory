import json
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import SensorData

def dashboard(request):
    limit = int(request.GET.get('limit', 20))
    data      = SensorData.objects.all().order_by('-id')[:limit][::-1]
    data_list = list(data)

    # ข้อมูลสำหรับกราฟ (ตาม limit)
    air_temp          = [d.air_temperature for d in data_list]
    process_temp      = [d.process_temperature for d in data_list]
    rotational_speed  = [d.rotational_speed for d in data_list]
    machine_fail      = [d.machine_failure for d in data_list]
    labels            = [str(d.id) for d in data_list]

    # ข้อมูลทั้งหมดสำหรับ KPI
    all_data = SensorData.objects.all()
    all_air_temp = [d.air_temperature for d in all_data]
    all_process_temp = [d.process_temperature for d in all_data]
    all_rotational_speed = [d.rotational_speed for d in all_data]
    all_machine_fail = [d.machine_failure for d in all_data]

    context = {
        # HTML ใช้
        'limit':                limit,
        'data':                 data,
        'length':               len(all_data),
        'avg_air_temp':         round(sum(all_air_temp) / len(all_air_temp), 2) if all_air_temp else "N/A",
        'avg_process_temp':     round(sum(all_process_temp) / len(all_process_temp), 2) if all_process_temp else "N/A",
        'avg_rotational_speed': round(sum(all_rotational_speed) / len(all_rotational_speed), 2) if all_rotational_speed else "N/A",
        'total_fail':           sum(all_machine_fail),
        'failure_rate':         f"{round(sum(all_machine_fail) / len(all_machine_fail) * 100, 2)}%" if all_machine_fail else "N/A",
        # JavaScript ใช้
        'labels':               json.dumps(labels),
        'air_temp':             json.dumps(air_temp),
        'process_temp':         json.dumps(process_temp),
        'machine_fail':         json.dumps(machine_fail),
    }
    return render(request, 'sensor/dashboard.html', context)


def data_table(request):
    """แสดงข้อมูลตารางทั้งหมดพร้อม pagination"""
    page_number = request.GET.get('page', 1)
    failure_query = request.GET.get('failure', '')
    
    # ดึงข้อมูลทั้งหมดและกรองตาม Failure หากมีการเลือก
    all_data = SensorData.objects.all().order_by('id')
    if failure_query in ['0', '1']:
        all_data = all_data.filter(machine_failure=int(failure_query))
    
    # Pagination - 20 แถวต่อหน้า
    paginator = Paginator(all_data, 20)
    page_obj = paginator.get_page(page_number)
    
    # สำหรับการ predict (ในตอนนี้ใช้ N/A)
    for item in page_obj:
        item.predicted_failure = predict_failure()
    
    context = {
        'page_obj': page_obj,
        'total_records': paginator.count,
        'failure_query': failure_query,
    }
    return render(request, 'sensor/table.html', context)


def predict_failure():
    """
    ฟังก์ชัน predict_failure - ตอนนี้เป็น placeholder
    ในอนาคตสามารถต่อเชื่อมกับ ML model ได้
    """
    return "N/A"

