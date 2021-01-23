from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import message
from django.contrib import messages


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

