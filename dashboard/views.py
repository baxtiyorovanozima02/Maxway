from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from . import services

def login_required_decorator(func):
    return login_required(func,login_url='login_page')

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect("home_page")

    return render(request, 'login.html')

@login_required_decorator
def home_page(request):
    categories = services.get_categories()
    kafedras = services.get_kafedra()
    products = services.get_product()
    teachers = services.get_teacher()
    groups = services.get_groups()
    students = services.get_student()
    ctx={
        'counts' : {
            'categories':len(categories),
            'kafedras':len(kafedras),
            'products':len(products),
            'teachers':len(teachers),
            'groups':len(groups),
            'students':len(students)
        }
    }
    return render(request, 'index.html', ctx)

#FACULTY
@login_required_decorator
def category_create(request):
    model = Category()
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()


        actions = request.session.get('actions',[])
        actions += [f"You created category: {request.POST.get('name')}"]
        request.session["actions"] = actions

        category_count = request.session.get('category_count', 0)
        category_count +=1
        request.session["category_count"] = category_count

        return redirect('faculty_list')


    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'category/form.html',ctx)

@login_required_decorator
def category_edit(request,pk):
    model = Category.objects.get(pk=pk)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions',[])
        actions += [f"You edited category: {request.POST.get('name')}"]
        request.session["actions"] = actions
        return redirect('category_list')


    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'category/form.html',ctx)

@login_required_decorator
def category_delete(request,pk):
    model = Category.objects.get(pk=pk)
    model.delete()
    return redirect('category_list')

@login_required_decorator
def category_list(request):
    categories=services.get_categories()
    print(categories)
    ctx={
        "categories":categories
    }
    return render(request,'category/list.html',ctx)

# KAFEDRA
@login_required_decorator
def kafedra_create(request):
    model = Kafedra()
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions',[])
        actions += [f"You created kafedra: {request.POST.get('name')}"]
        request.session["actions"] = actions

        kafedra_count = request.session.get('kafedra_count', 0)
        kafedra_count +=1
        request.session["kafedra_count"] = kafedra_count

        return redirect('kafedra_list')


    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'kafedra/form.html',ctx)

@login_required_decorator
def kafedra_edit(request,pk):
    model = Kafedra.objects.get(pk=pk)
    form = KafedraForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions',[])
        actions += [f"You edited kafedra: {request.POST.get('name')}"]
        request.session["actions"] = actions
        return redirect('kafedra_list')

    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'kafedra/form.html',ctx)

@login_required_decorator
def kafedra_delete(request,pk):
    model = Kafedra.objects.get(pk=pk)
    model.delete()
    return redirect('kafedra_list')

@login_required_decorator
def kafedra_list(request):
    kafedras=services.get_kafedra()
    ctx={
        "kafedras":kafedras
    }
    return render(request,'kafedra/list.html',ctx)

#SUBJECT
@login_required_decorator
def product_create(request):
    model = Product()
    form = ProductForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions',[])
        actions += [f"You created product: {request.POST.get('name')}"]
        request.session["actions"] = actions

        product_count = request.session.get('product_count', 0)
        product_count +=1
        request.session["product_count"] = product_count

        return redirect('product_list')

    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'product/form.html',ctx)

@login_required_decorator
def product_edit(request,pk):
    model = Product.objects.get(pk=pk)
    form = ProductForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions',[])
        actions += [f"You edited product: {request.POST.get('name')}"]
        request.session["actions"] = actions
        return redirect('product_list')


    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'product/form.html',ctx)

@login_required_decorator
def product_delete(request,pk):
    model = Product.objects.get(pk=pk)
    model.delete()
    return redirect('product_list')

@login_required_decorator
def product_list(request):
    products=services.get_product()
    ctx={
        "products":products
    }
    return render(request,'product/list.html',ctx)

#TEACHER
@login_required_decorator
def teacher_create(request):
    model = Teacher()
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions',[])
        actions += [f"You created teacher: {request.POST.get('name')}"]
        request.session["actions"] = actions

        teacher_count = request.session.get('teacher_count', 0)
        teacher_count +=1
        request.session["teacher_count"] = teacher_count


        return redirect('teacher_list')
    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'teacher/form.html',ctx)

@login_required_decorator
def teacher_edit(request,pk):
    model = Teacher.objects.get(pk=pk)
    form = TeacherForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions',[])
        actions += [f"You edited subject: {request.POST.get('name')}"]
        request.session["actions"] = actions
        return redirect('subject_list')


    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'teacher/form.html',ctx)

@login_required_decorator
def teacher_delete(request,pk):
    model = Teacher.objects.get(pk=pk)
    model.delete()
    return redirect('teacher_list')

@login_required_decorator
def teacher_list(request):
    teachers=services.get_teacher()
    ctx={
        "teachers":teachers
    }
    return render(request,'teacher/list.html',ctx)

#GROUP
@login_required_decorator
def group_create(request):
    model = Group()
    form = GroupForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions',[])
        actions += [f"You created group: {request.POST.get('name')}"]
        request.session["actions"] = actions

        group_create = request.session.get('group_create', 0)
        group_create +=1
        request.session["group_create"] = group_create

        return redirect('group_list')
    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'group/form.html',ctx)

@login_required_decorator
def group_edit(request,pk):
    model = Group.objects.get(pk=pk)
    form = GroupForm(request.POST or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions',[])
        actions += [f"You edited group: {request.POST.get('name')}"]
        request.session["actions"] = actions

        return redirect('group_list')
    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'group/form.html',ctx)

@login_required_decorator
def group_delete(request,pk):
    model = Group.objects.get(pk=pk)
    model.delete()
    return redirect('group_list')

@login_required_decorator
def group_list(request):
    groups=services.get_groups()
    ctx={
        "groups":groups
    }
    return render(request,'group/list.html',ctx)

#STUDENT
@login_required_decorator
def student_create(request):
    model = Student()
    form = StudentForm(request.POST or None, request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions',[])
        actions += [f"You created student: {request.POST.get('name')}"]
        request.session["actions"] = actions

        student_create = request.session.get('student_create', 0)
        student_create +=1
        request.session["student_create"] = student_create

        return redirect('student_list')
    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'student/form.html',ctx)

@login_required_decorator
def student_edit(request,pk):
    model = Student.objects.get(pk=pk)
    form = StudentForm(request.POST or None,request.FILES or None, instance=model)
    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions',[])
        actions += [f"You edited student: {request.POST.get('name')}"]
        request.session["actions"] = actions

        return redirect('student_list')
    ctx = {
        "model":model,
        "form":form
    }
    return render(request,'student/form.html',ctx)

@login_required_decorator
def student_delete(request,pk):
    model = Student.objects.get(pk=pk)
    model.delete()
    return redirect('student_list')

@login_required_decorator
def student_list(request):
    students=services.get_student()
    ctx={
        "students":students
    }
    return render(request,'student/list.html',ctx)

@login_required_decorator
def profile(request):
    return render(request,'profile.html')
