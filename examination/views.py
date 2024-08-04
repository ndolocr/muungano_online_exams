from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.text import slugify

from examination.models import Examination
# Create your views here.

def create_examination(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        acronym = request.POST.get('acronym', '')

        try:
            record = Examination.objects.create(
                name = name,
                acronym = acronym,
                slug = slugify(name)
            )
            return redirect("examination_app:view_all_examinations")            
        except Exception as e:
            context = {"Error": "Error occured while saving examination body record"}
            return render(request, 'examination/create.html', context)
    else:
        return render(request, 'examination/create.html')

def view_all_examinations(request):
    try:
        record = Examination.objects.all().order_by('-created_on')
        context = {"record": record, "message": ""}
        return render(request, "examination/view_all.html", context)
    except ObjectDoesNotExist:
        context = {"message": "Examinations do not exist"}
        return render(request, "examination/view_all.html", context)

