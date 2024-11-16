from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,PostForm
from django.contrib.auth import authenticate,login,logout
from .models import Post
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponseBadRequest

# Create your views here.
def home(request):

    name='rakhi'
    nums=[1,2,3,4,5,6,7,8]
    context = {'name':name,'nums':nums}
    return render(request,'home.html',context)

def user_register(request):
    form = UserRegistrationForm()
    context = {'form':form}
    
    if request.method=='GET':
        return render(request,'register.html',context)
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context['error']='invalid form submission try again'
            return render(request,'register.html',context)

       


def user_login(request):

    if request.method=='GET':
        return render(request,'login.html')
    
    if request.method=='POST':
        username=request.POST.get('user_name')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')

        else:
            error='invalid username or password '
            context={'error':error}
            return render(request,'login.html',context)


def user_logout(request):
    logout(request)
    return redirect('home')


def display_post(request):

    #post is table we fetch all usin selct * 
    post_list=Post.objects.all()
    context={'post_list':post_list}
    return render(request,'display_post.html',context)



@login_required(login_url='login')
def create_post(request):
    form = PostForm()
    context = {'form':form}
    
    if request.method=='GET':
        return render(request,'create_post.html',context)





    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('display_post')    
        else:
            context['error']='invalid form submission try again'
            return render(request,'create_post.html',context)


@login_required(login_url='login')
def update_post(request,id):
    try:
         post=Post.objects.get(pk=id)#fetching from db searching likw select where id =1
    except Post.DoesNotExist:
        return HttpResponseBadRequest('page doesnt doesnt <a href="/">click here</a>')

    if post.author != request.user :
        return HttpResponseBadRequest('you cannot acess this page ')

    form=PostForm(instance=post)
    context={'form':form}
    if request.method=='GET':
        return render(request,'Update_post.html',context)
    
    
    if request.method=='POST':
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.created_at=datetime.now()   #update time
            post.save()
            return redirect('display_post')
        else:
            context['error']='invalid form submission try again'
            return render(request,'update_post.html',context)

   
@login_required(login_url='login')
def delete_post(request,id):
    try:
        post=Post.objects.get(pk=id)
    except post.DoesNotExist:
        return HttpResponseBadRequest('page doesnt doesnt <a href="/">click here</a>')
    
    if post.author != request.user:
        return HttpResponseBadRequest('you cannot delte the post ')
    
    post.delete()

    return  redirect('display_post')


