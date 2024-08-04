from django.shortcuts import render

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
        except Exception as e:
            context = {"Error": "Error occured while saving examination body record"}
            return render(request, 'examination/create.html', context)
    else:
        return render(request, 'examination/create.html')