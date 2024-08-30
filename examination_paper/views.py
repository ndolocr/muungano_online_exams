from django.shortcuts import render

from examination_body.views import ExaminationBody
# Create your views here.

def create(request):
    if request.method == "POST":
        pass
    else:
        examination_bodies = ExaminationBody.objects.all()

        context = {
            "examination_bodies": examination_bodies,
        }
        return render(request, 'examination_paper/create.html', context)