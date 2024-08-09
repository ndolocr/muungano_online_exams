from django.shortcuts import render

from instructions.models import Instruction
# Create your views here.

def create_instruction(request):
    pass

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
