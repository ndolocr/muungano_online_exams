from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.text import slugify

from examination.models import Examination
from examination_body.models import ExaminationBody
# Create your views here.

def create(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        acronym = request.POST.get('acronym', '')
        examination_body_id = request.POST.get('examination_body', '')
        examination_body = ExaminationBody.objects.get(pk=ExaminationBody_id)

        try:
            record = Examination.objects.create(
                name = name,
                acronym = acronym,
                slug = slugify(name),
                examination_body = examination_body
            )
            return redirect("examination_app:view_all_examinations")            
        except Exception as e:
            context = {"Error": "Error occured while saving examination body record"}
            return render(request, 'examination/create.html', context)
    else:
        examination_body = ExaminationBody.objects.all().order_by('acronym')
        context = {"examination_body": examination_body}
        return render(request, 'examination/create.html', context)

def view_all(request):
    try:
        record = Examination.objects.all().order_by('-created_on')
        context = {"record": record, "message": ""}
        return render(request, "examination/view_all.html", context)
    except ObjectDoesNotExist:
        context = {"message": "Examinations do not exist"}
        return render(request, "examination/view_all.html", context)

