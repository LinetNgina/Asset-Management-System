from django.shortcuts import render, redirect
from .forms import MaintenanceForm
from .models import MaintenanceRecord, MaintenanceRequest



def maintenance_view(request):
    if request.method == "POST":
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maintenance_success')
    else:
        form = MaintenanceForm()
    return render(request, 'maintenance.html', {'form': form})

def maintenance_success_view(request):
    return render(request, 'maintenance_success.html')

def dashboard_home(request):
    return render(request, 'home.html')

def database_contents_view(request):
    # Fetch all MaintenanceRecord and MaintenanceRequest objects from the database
    maintenance_records = MaintenanceRecord.objects.all()
    maintenance_requests = MaintenanceRequest.objects.all()

    # Render a template with the fetched data
    return render(request, 'database_contents.html', {
        'maintenance_records': maintenance_records,
        'maintenance_requests': maintenance_requests
    })

def submit_maintenance_form(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            # Extract form data
            category = form.cleaned_data['category']
            asset_id = form.cleaned_data['asset_id']
            comments = form.cleaned_data['comments']
            return_item = form.cleaned_data['return_item']  # Extract the return_item data

            # Save data to MaintenanceRecord model
            maintenance_record = MaintenanceRecord.objects.create(
                category=category,
                asset_id=asset_id,
                comments=comments,
                return_item=return_item  # Save the return_item data
            )

            # Example of saving related MaintenanceRequest (if applicable)
            # Assuming you have a way to link MaintenanceRecord to MaintenanceRequest
            # E.g., submitted_by and submitted_at fields in MaintenanceRequest model
            submitted_by = request.user  # Assuming user is authenticated
            maintenance_request = MaintenanceRequest.objects.create(
                subject=f"Maintenance request for {category} - {asset_id}",
                description=comments,
                submitted_by=submitted_by
            )

            # Redirect to success page or render success template
            return redirect('maintenance_success')

    # If GET request or form invalid, render the form again
    form = MaintenanceForm()
    return render(request, 'maintenance.html', {'form': form})
