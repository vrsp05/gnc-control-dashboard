from django.shortcuts import render
from .forms import ControlForm
from .models import SetPointLog

def dashboard(request):
    current_threshold = 100.0 # Default value
    system_status = 'Operational'

    if request.method == 'POST':
        form = ControlForm(request.POST)
        if form.is_valid():
            # Requirement 4: Accessing the cleaned/validated data
            current_threshold = form.cleaned_data['threshold']
            
            # Requirement 5: Modify content based on input
            if current_threshold > 400:
                system_status = 'WARNING: High Threshold Set'
            
            # STRETCH CHALLENGE: Save to the database!
            SetPointLog.objects.create(
                value=current_threshold,
                status_message=system_status
            )
    else:
        form = ControlForm()

    # Retrieve the last 5 logs to show on the UI
    history = SetPointLog.objects.all().order_by('-timestamp')[:5]

    context = {
        'system_status': system_status,
        'unit_name': 'GNC-Control-01',
        'form': form,
        'current_threshold': current_threshold,
        'history': history
    }
    return render(request, 'hmi/dashboard.html', context)