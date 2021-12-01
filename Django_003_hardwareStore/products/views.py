from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def list(request):
    return render(request,'products/index.html')

