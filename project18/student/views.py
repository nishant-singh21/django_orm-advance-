from django.shortcuts import render
from .forms import StudentForm

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'student_success.html')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})
