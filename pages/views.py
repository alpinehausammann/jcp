from django.shortcuts import render, get_object_or_404
from .models import Page, NewContent

def page_detail(request, pk):
    page = get_object_or_404(Page,pk=pk)
    page_title = page.title
    return render(request, 'pages/page_detail.html', {'page': page})

# Create your views here.
