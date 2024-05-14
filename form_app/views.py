from django.shortcuts import render,redirect
from form_app.forms import UserDetailsForm

# Create your views here.

def user_input_view(request):
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserDetailsForm()
    return render(request, 'form_app/input.html', {'form' : form})

def success_view(request):
    return render(request, 'form_app/success.html')
