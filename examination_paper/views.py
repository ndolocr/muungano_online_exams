from django.shortcuts import render

from examination. models import Examination
from examination_paper import ExaminationPaper
# Create your views here.

def create(request):
    if request.method == "POST":
        pass
    else:
        return render(request, 'examination_paper/create.html')
    #     year = request.POST.get('year', '')
    #     name = request.POST.get('name', '')
    #     section = request.POST.get('section', '')
    #     subject = request.POST.get('subject', '')
    #     exam_duration = request.POST.get('exam_duration', '') 
        
    #     examination_body = ExaminationBody.objects.get(pk=ExaminationBody_id)

    #     try:
    #         record = Examination.objects.create(
    #             name = name,
    #             acronym = acronym,
    #             slug = slugify(name),
    #             examination_body = examination_body
    #         )
    #         return redirect("examination_app:view_all_examinations")            
    #     except Exception as e:
    #         context = {"Error": "Error occured while saving examination body record"}
    #         return render(request, 'examination/create.html', context)
    # else:
    #     examination_body = ExaminationBody.objects.all().order_by('acronym')
    #     context = {"examination_body": examination_body}
    #     return render(request, 'examination/create.html', context)