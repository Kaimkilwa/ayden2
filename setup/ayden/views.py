from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import *


# Create your views here.
def ContactView(request):
    form = ContactForm
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # commit=False
            # post.author = request.user
            
            # post.save()
            
            return redirect('home')
            success_message = 'Success: Thank for cintact us'
        else:
            form = ContactForm()
    return render(request, 'ayden/index.html', {'form': form})