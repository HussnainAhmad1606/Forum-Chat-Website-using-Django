from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import message
from django.contrib import messages

from django.contrib.auth.models import User

# Create your views here.
def home(request):
	return render(request, "index.html")

def messages(request):
	if request.method == "POST":
		userMessage = request.POST.get("message")
		user = request.POST.get("user")
		addMessage = message(user=user, message=userMessage)
		addMessage.save()
		return redirect("messages")

	else:
		allMessages = message.objects.all()
		print(allMessages)
		context = {
		'messages': allMessages
		}
		return render(request, "messages.html", context)


def signup(request):
	if request.method == "POST":
		username = request.POST.get("username")
		email = request.POST.get("email")
		password1 = request.POST.get("pass1")
		password2 = request.POST.get("pass2")
		myuser = User.objects.create_user(username=username, email=email, password=password1)
		myuser.save()
		return redirect("home")

	else:
		return HttpResponse("404 Not Found")

