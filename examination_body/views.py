from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.text import slugify 

from examination_body.models import ExaminationBody

# Create your views here.
def create_examination_body(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        acronym = request.POST.get('acronym', '')

        try:
            record = ExaminationBody.objects.create(
                name = name,
                acronym = acronym,
                slug = slugify(name)
            )
            return redirect("examination_body_app:view_all_examination_body")
        except Exception as e:
            context = {"Error": "Error occured while saving examination body record"}
            return render(request, 'examination_body/create.html', context)
    else:
        return render(request, 'examination_body/create.html')

def view_all_examination_body(request):
    pass