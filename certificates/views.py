# Create your views here.
from django.views.generic import CreateView,ListView
from .models import CertificateSetting,CertificateType
from .forms import NewCertificateSettingsForm
# from django.http import HttpResponseRedirect
from django.shortcuts import render

class NewCertificateSettings(CreateView):
    model = CertificateSetting
    form_class = NewCertificateSettingsForm
    template_name = 'certificates/new_certificate_settings.html'
    success_url = '/home/'

    
class certificatesTypesForNewCertificateSettings(ListView):
    model = CertificateType
    template_name = 'certificates/certificates_types_for_settings.html'
    context_object_name = 'CertificateType'

    def get_queryset(self): 
        return CertificateType.objects.all()

    def post(self, request, *args, **kwargs):
        # Manually handle the form submission
        program_id = request.POST.get('program_id')

        
        # Validate the form data and save the new instance
        # if field1 and field2:
        #     new_instance = YourModel.objects.create(field1=field1, field2=field2)
        #     new_instance.save()

        # Add the POST data to the context 
        context = self.get_context_data(object_list=self.get_queryset()) 
        context['program_id'] = program_id
        
        # Redirect to the same view after form submission
        return render(request, self.template_name, context)