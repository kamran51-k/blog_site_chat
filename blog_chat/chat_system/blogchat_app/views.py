from django.shortcuts import render,redirect

from blogchat_app.models import  PostModel, AboutModel
from .forms import RegisterForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url = 'login_page')
# def base_view(request):
# 	context = {}
# 	base_queryset = NavbarModel.objects.all()
# 	logo_queryset = LogoModel.objects.all()
# 	post_queryset = PostModel.objects.all()
# 	context['post_queryset'] = post_queryset
# 	context['logo_queryset'] = logo_queryset
# 	context['base_queryset'] = base_queryset
# 	return render(request, 'base.html',context)

def index_view(request):
    context = {}
    post_queryset = PostModel.objects.all()
    context['post_queryset'] = post_queryset
    return render(request, 'index.html',context)


def post_detail_view(request,post_id):
    context = {}
    detail_queryset = PostModel.objects.filter(id=post_id).first()
    context['detail_queryset'] = detail_queryset
    return render(request,'post_detail.html',context)


def register_request(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index_page")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = RegisterForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index_page")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index_page")

def about_view(request):
    context = {}
    about_queryset = AboutModel.objects.all()
    context['about_queryset'] = about_queryset
    return render(request,'about.html',context)

def contact_view(request):

	return render(request,'contact.html')


def edit_profile_view(request):
	
	return render(request, 'edit_profile.html')