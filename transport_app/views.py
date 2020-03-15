from django.shortcuts import render, redirect
from django.http import HttpResponse

# from .models import *
from .forms import Transport_Form

# Create your views here.

def index(request):
	# tasks = Transport.objects.all()
	if request.method =='POST':
		filled_form = Transport_Form(request.POST)
		if filled_form.is_valid():
			note = "%s To %s And Amount= %s Saved!!"%(
			filled_form.cleaned_data['source'],
			filled_form.cleaned_data['destination'],
			filled_form.cleaned_data['amount'],

			)
			new_form = Transport_Form()
			context = {'form':new_form,'note':note}#'tasks':tasks}
			return render(request, 'transport_app/index.html', context)
	# 	form = Transport_Form(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 	return redirect('/')
	else:
		form = Transport_Form()
		context = {'form':form}#'tasks':tasks}
		return render(request, 'transport_app/index.html', context)

# def Order(request):
# 	form = Transport_Form()
# 	context = {'form':form}#'tasks':tasks}
# 	return render(request, 'transport_app/index.html', context)


# def updateTask(request, pk):
# 	task = Transport.objects.get(id=pk)
#
# 	form = Transport_Form(instance=task)
#
# 	if request.method == 'POST':
# 		form = Transport_Form(request.POST, instance=task)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/')
#
# 	context = {'form':form}
#
# 	return render(request, 'tasks/update_task.html', context)
#
# def deleteTask(request, pk):
# 	item = Transport.objects.get(id=pk)
#
# 	if request.method == 'POST':
# 		item.delete()
# 		return redirect('/')
#
# 	context = {'item':item}
# 	return render(request, 'tasks/delete.html', context)
#
# def home(request):
# 	return render(request,'tasks/index.html')
