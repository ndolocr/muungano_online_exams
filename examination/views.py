from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.text import slugify

from logs.models import ExaminationLogs
from examination.models import Examination
from examination_body.models import ExaminationBody
# Create your views here.

def create(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        acronym = request.POST.get('acronym', '')
        examination_body_id = request.POST.get('examination_body', '')   

        try:
            examination_body = ExaminationBody.objects.get(pk=examination_body_id)

            queryset = Examination.objects.create(
                name = name,
                acronym = acronym,
                slug = slugify(name),
                examination_body = examination_body
            )

            logs = ExaminationLogs.objects.create(
                action = "Create",
                action_by = user,
                examination = queryset,
                values = f"Name - {name}, Acronym - {acronym}, Slug - {slugify(name)}"
            )
            return redirect("examination_app:view_all")            
        except Exception as e:
            context = {"Error": "Error occured while saving examination record"}
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

def update(request, pk):
    try:
        queryset = Examination.objects.get(pk=pk)
        examination_body = ExaminationBody.objects.all().order_by('acronym')
        context = {"queryset": queryset, "examination_body": examination_body}
    except ObjectDoesNotExist as o:
        context = {"error": f"Examination record not found! --{o}"}
    except Exception as e:
        context = {"error": f"Error occured while trying to get Examination record! --> {e}"}
    return render(request, 'examination/update.html', context)

def update_post(request):
    try:                    
        if request.method == "POST":
            user = request.user
            pk = request.POST.get('pk', '')
            print(f"PK -- > {pk}")
            name = request.POST.get('name', '')
            print(f"Name -- > {name}")
            acronym = request.POST.get('acronym', '')
            print(f"Acronym -- > {acronym}")
            examination_body_id = request.POST.get('examination_body', '')
            print("Examination Body ID --> ", examination_body_id)
            
            try:
                examination_body = ExaminationBody.objects.get(pk=examination_body_id)
                queryset = Examination.objects.get(pk=pk)
                queryset.name = name                
                queryset.acronym = acronym
                queryset.slug = slugify(name)
                queryset.examination_body = examination_body   
                queryset.save()

                logs = ExaminationLogs.objects.create(
                    action = "Update",
                    action_by = user,
                    examination = queryset,
                    values = f"Name - {name}, Acronym - {acronym}, Slug - {slugify(name)}, Examination Body - {examination_body.acronym}"
                )

                return redirect("examination_app:view_all")                
            except Exception as s:
                context = {"error": f"Error occured while trying to Update Examination record! --> {s}"}
    except ObjectDoesNotExist as o:
        context = {"error": f"Examination Body record not found! --{o}"}
    except Exception as e:
        context = {"error": f"Error occured while trying to get Examination Body record! --> {e}"}
    return render(request, 'examination_body/update.html', context)