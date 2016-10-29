from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

#from .functions import handle_excel_file
from .forms import NewClinicForm
from .models import NewClinic


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = NewClinicForm(request.POST, request.FILES)
        print('request')
        if form.is_valid():
            print('VALID')
            obj = NewClinic()
            obj.clinic_name = form.cleaned_data['clinic_name']
            handle_uploaded_file(request.FILES['excel_file'], obj.clinic_name)
            handle_uploaded_file(request.FILES['zip_file'], obj.clinic_name)

            #handle_excel_file(request.FILES['file'], obj.clinic_name)  # Solve import error in .functions

            obj.save()
            return HttpResponseRedirect('thanks/')
    else:
        form = NewClinicForm()
    return render(request, 'upload/home.html', {'form': form})

def handle_uploaded_file(f, filename):
    if f.name.endswith('.xlsx'):
        with open('EXCELfiles/%s.xlsx' % filename, 'w') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
    else:
        with open('ZIPfiles/%s.zip' % filename, 'w') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

def thanks(request):
    return HttpResponse('Your data has been received. Thank you!')

