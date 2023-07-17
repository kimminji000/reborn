from django.shortcuts import render
from .models import Partner

# Create your views here.
def main(request):
    return render(request, 'main.html')

def partner(request):
    partner = Partner.objects.all()
    return render(request, 'partner.html', {'partners' : partner})