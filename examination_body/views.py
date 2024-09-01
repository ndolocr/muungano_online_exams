from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.text import slugify
from django.core.exceptions import ObjectDoesNotExist

from user_management.models import User
from logs.models import ExaminationBodyLogs
from examination_body.models import ExaminationBody


# Create your views here.
def create(request):
    if request.method == "POST":
        user = request.user
        name = request.POST.get('name', '')
        acronym = request.POST.get('acronym', '')
        try:
            queryset = ExaminationBody.objects.create(
                name = name,
                acronym = acronym,
                slug = slugify(name),
                created_by = user
            )
            
            logs = ExaminationBodyLogs.objects.create(
                action = "Create",
                action_by = user,
                examination_body = queryset,
                values = f"Name - {name}, Acronym - {acronym}, Slug - {slugify(name)}"
            )
            return redirect("examination_body_app:view_all")
        except Exception as e:
            context = {"error": f"Error occured while saving examination body record --> {e}"}
            return render(request, 'examination_body/create.html', context)         
    else:
        context = {}
        return render(request, 'examination_body/create.html', context)

def view_all(request):
    try:
        record = ExaminationBody.objects.all().order_by('-created_on')
        context = {"record": record, "message": ""}
        return render(request, "examination_body/view_all.html", context)
    except ObjectDoesNotExist:
        context = {"error": "Examination bodies do not exist"}
        return render(request, "examination_body/view_all.html", context)

def update(request, pk):
    try:
        queryset = ExaminationBody.objects.get(pk=pk)
        context = {"queryset": queryset}
    except ObjectDoesNotExist as o:
        context = {"error": f"Examination Body record not found! --{o}"}
    except Exception as e:
        context = {"error": f"Error occured while trying to get Examination Body record! --> {e}"}
    return render(request, 'examination_body/update.html', context)

def update_post(request):
    try:                    
        if request.method == "POST":
            user = request.user
            pk = request.POST.get('pk', '')
            name = request.POST.get('name', '')
            acronym = request.POST.get('acronym', '')

            try:
                queryset = ExaminationBody.objects.get(pk=pk)
                queryset.name = name
                queryset.slug = slugify(name)
                queryset.acronym = acronym                
                queryset.save()

                logs = ExaminationBodyLogs.objects.create(
                    action = "Update",
                    action_by = user,
                    examination_body = queryset,
                    values = f"Name - {name}, Acronym - {acronym}, Slug - {slugify(name)}"
                )

                return redirect("examination_body_app:view_all")                
            except Exception as s:
                context = {"error": f"Error occured while trying to Update Examination Body record! --> {s}"}
    except ObjectDoesNotExist as o:
        context = {"error": f"Examination Body record not found! --{o}"}
    except Exception as e:
        context = {"error": f"Error occured while trying to get Examination Body record! --> {e}"}
    return render(request, 'examination_body/update.html', context)