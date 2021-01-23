from django.shortcuts import render
from django.http import HttpResponse
from .models import message


# Create your views here.
def home(request):
	return render(request, "index.html")

def messages(request):
	allMessages = message.objects.all()
	print(allMessages)
	context = {
	'messages': allMessages
	}
	return render(request, "messages.html", context)

