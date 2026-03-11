from django.shortcuts import render

# Create your views here.
def dashboard(request):
    # This dictionary will eventually hold our sensor data
    context = {
        'system_status': 'Operational',
        'unit_name': 'GNC-Control-01'
    }
    return render(request, 'hmi/dashboard.html', context)