from django.shortcuts import render

from .models import SolutionModel

# Create your views here.
def solution_views(request):
    sol = SolutionModel.objects.first()
    return render(request, 'display_solution.html',{'sol' : sol})