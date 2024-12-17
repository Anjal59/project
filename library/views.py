from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

def admin_required(user):
    return user.is_authenticated and user.is_admin()

def office_staff_required(user):
    return user.is_authenticated and user.is_office_staff()

def librarian_required(user):
    return user.is_authenticated and user.is_librarian()

@login_required
@user_passes_test(admin_required)
def admin_dashboard(request):
    return render(request, 'library/admin_dashboard.html')

@login_required
@user_passes_test(office_staff_required)
def office_staff_dashboard(request):
    return render(request, 'library/office_staff_dashboard.html')

@login_required
@user_passes_test(librarian_required)
def librarian_dashboard(request):
    return render(request, 'library/librarian_dashboard.html')

@login_required
@user_passes_test(admin_required)
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student created successfully!')
    else:
        form = StudentForm()
    return render(request, 'core/create_student.html', {'form': form})


