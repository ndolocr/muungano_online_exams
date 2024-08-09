from django.shortcuts import render

from instructions.models import Instruction
# Create your views here.

def create_instruction(request):    
    if request.method == "POST":
        instructions = request.POST.get('instructions', '')

        try:
            record = Instruction.objects.create(
                instructions = instructions,
            )
            return redirect("examination_app:view_all_examinations")            
        except Exception as e:
            context = {"Error": "Error occured while saving instructions record"}
            return render(request, 'instructions/create.html', context)
    else:
        return render(request, 'instructions/create.html', context)

def view_all_instructions(request):
    try:
        record = Instruction.objects.all().order_by('-created_on')
        context = {"record": record, "message": ""}
        return render(request, "instructions/view_all.html", context)
    except ObjectDoesNotExist:
        context = {"message": "Instructions do not exist"}
        return render(request, "instructions/view_all.html", context)

def view_single_instruction(request):
    pass
