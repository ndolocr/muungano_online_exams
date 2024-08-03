from django.shortcuts import render
from django.utils.text import slugify 

from examination_body.models import ExaminationBody

# Create your views here.
def create_examination_body(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        acronym = request.POST.get('acronym', '')

        record = ExaminationBody.objects.create(
            name = name,
            acronym = acronym,
            slug = slugify(name)
        )
    return render(request, 'examination_body/create.html')