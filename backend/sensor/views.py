import json
from django.shortcuts import render
from .models import SensorData

def dashboard(request):
    limit = int(request.GET.get('limit', 20))
    data      = SensorData.objects.all().order_by('id')[:limit]
    data_list = list(data)

    air_temp          = [d.air_temperature for d in data_list]
    process_temp      = [d.process_temperature for d in data_list]
    rotational_speed  = [d.rotational_speed for d in data_list]
    machine_fail      = [d.machine_failure for d in data_list]
    labels            = [str(d.id) for d in data_list]

    context = {
        # HTML ใช้
        'limit':                limit,
        'data':                 data,
        'avg_air_temp':         round(sum(air_temp) / len(air_temp), 2) if air_temp else "N/A",
        'avg_process_temp':     round(sum(process_temp) / len(process_temp), 2) if process_temp else "N/A",
        'avg_rotational_speed': round(sum(rotational_speed) / len(rotational_speed), 2) if rotational_speed else "N/A",
        'total_fail':           sum(machine_fail),
        'failure_rate':         f"{round(sum(machine_fail) / len(machine_fail) * 100, 2)}%" if machine_fail else "N/A",
        # JavaScript ใช้
        'labels':               json.dumps(labels),
        'air_temp':             json.dumps(air_temp),
        'process_temp':         json.dumps(process_temp),
        'machine_fail':         json.dumps(machine_fail),
    }
    return render(request, 'sensor/dashboard.html', context)

