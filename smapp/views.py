from django.shortcuts import redirect, render
from smapp.forms import AddStudentForm, updateStudentForm, UserRegistrationForm
from smapp.models import Student
from django.contrib.auth.decorators import login_required


@login_required
def add_student_view(request):
    obj = AddStudentForm()
    if request.method == 'POST' :
        
        obj = AddStudentForm(request.POST , request.FILES)
        if obj.is_valid():
            obj.save()
            return redirect('/student/list/')


    return render(request, 'smapp/add.html', {'obj':obj})

@login_required
def student_list(request):
    data = Student.objects.all()
    return render(request, 'smapp/list.html', {'data': data})

@login_required
def student_detail(request, id):
    obj = Student.objects.get(pk = id)
    return render(request, 'smapp/detail.html', {'obj':obj})

@login_required
def update_student(request, id):
    obj = Student.objects.get(pk = id)
    form = updateStudentForm(instance=obj)
    #print(request.POST)
    if request.method == 'POST' :
        form = updateStudentForm(request.POST,request.FILES, instance= obj)
        if form.is_valid():
            form.save()
            return redirect(f'/student/detail/{obj.id}')
    

    return render(request, 'smapp/update.html', {'obj':obj , 'form':form})

@login_required
def delete_student(request, id):
    obj = Student.objects.get(pk = id)
    obj.delete()
    return redirect('/student/list/')


def user_register_view(request):
    form = UserRegistrationForm()
    print(request.POST)
    if request.method == 'POST' :
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/login/')
    return render(request, 'smapp/register.html', {'form':form})




    
