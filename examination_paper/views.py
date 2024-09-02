from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.text import slugify

from examination.models import Examination
from examination_paper.models import ExaminationPaper
# Create your views here.

def create(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        year = request.POST.get('year', '')        
        subject = request.POST.get('subject', '')
        examination = request.POST.get('examination', '')
        exam_duration = request.POST.get('exam_duration', '')

        print(f"Name --> {name}")
        print(f"Year --> {year}")
        print(f"Subject --> {subject}")
        print(f"Examination --> {examination}")
        print(f"Exam Duration --> {exam_duration}")
        
        try:
            examination_queryset = Examination.objects.get(pk=examination)
            slug_field = f"{examination_queryset.acronym} {year} {subject} {name}"
            queryset = ExaminationPaper.objects.create(
                name = name,
                year = year,                
                subject = subject,
                slug = slugify(slug_field),
                exam_duration = exam_duration,
                examination = examination_queryset,
            )
            return redirect("examination_paper_app:create_instructions", pk=queryset.pk)
        except Exception as e:
            examination = Examination.objects.all()
            message = f"Error Saving Examination Paper record --> {str(e)}"
            print(f"{message}")
            context = {
                "error": message,
                "examination": examination,
            }
            return render(request, 'examination_paper/create.html', context)
    else:
        examination = Examination.objects.all()
        context = {
            "examination": examination,
        }
        return render(request, 'examination_paper/create.html', context)

def create_instructions(request, pk):
    if request.method == "POST":
        pass
    else:
        context = {}
        return render(request, 'examination_paper/create_instructions.html', context)