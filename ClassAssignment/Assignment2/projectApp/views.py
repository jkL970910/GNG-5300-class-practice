from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from .forms import GeeksForm, FormSet, GeeksFormFromModel, GeeksModelImg
from .models import GeeksModel
from django.forms import formset_factory, modelformset_factory
# import Http Response from django
from django.http import HttpResponse
# get datetime
import datetime
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView

def home_view_form(request):
	context = {}
	form = GeeksForm(request.POST or None)
	context['form'] = form
	return render(request, "home_view_form.html", context)

def home_view_img(request):
	context ={}

	# create object of form
	form = GeeksModelImg(request.POST or None, request.FILES or None)
	
	# check if form data is valid
	if form.is_valid():
		# save the form data to model
		form.save()

	context['form']= form
	return render(request, "home_view_img.html", context)

def home_view_model(request):
	context ={}

	# create object of form
	form = GeeksFormFromModel(request.POST or None, request.FILES or None)
	
	# check if form data is valid
	if form.is_valid():
		# save the form data to model
		form.save()

	context['form']= form
	return render(request, "home_view_model.html", context)

def formset_view(request):
	context={}

	GeeksFormSet = formset_factory(FormSet, extra = 3)
	formset = GeeksFormSet(request.POST or None)

	if formset.is_valid():
		for form in formset:
			print(form.cleaned_data)

	context['formset']= formset
	return render(request, "formset_view.html", context)

def modelformset_view(request):
	context ={}

	# creating a formset and 5 instances of GeeksForm
	GeeksFormSet = modelformset_factory(GeeksModel, fields =['title', 'description'], extra = 3)
	formset = GeeksFormSet(request.POST or None)

	if formset.is_valid():
		for form in formset:
			print(form.cleaned_data)
			
	# Add the formset to context dictionary
	context['formset']= formset
	return render(request, "modelformset_view.html", context)

def geeks_template_view(request):
	# create a dictionary to pass
	# data to the template
	context ={
		"data":"Gfg is the best",
		"list":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	}
	# return response with template and context
	return render(request, "geeks_template.html", context)

def geeks_time_view(request):
	# fetch date and time
	now = datetime.datetime.now()
	# convert to string
	html = "Time is {}".format(now)
	# return response
	return HttpResponse(html)

def list_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	context["dataset"] = GeeksModel.objects.all()
		
	return render(request, "list_view.html", context)

class GeeksList(ListView):

	# specify the model for list view
	model = GeeksModel

# pass id attribute from urls
def detail_view(request, id):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	context["data"] = GeeksModel.objects.get(id = id)
		
	return render(request, "detail_view.html", context)

# update view for details
def update_view(request, id):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# fetch the object related to passed id
	obj = get_object_or_404(GeeksModel, id = id)

	# pass the object as instance in form
	form = GeeksFormFromModel(request.POST or None, instance = obj)

	# save the data from the form and
	# redirect to detail_view
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/"+id)

	# add form dictionary to context
	context["form"] = form

	return render(request, "update_view.html", context)

def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "delete_view.html", context)

class GeeksCreate(CreateView):
	# specify the model you want to use
	model = GeeksModel

	# specify the fields
	fields = [
		"title",
		"description"
	]

	# can specify success url
	# url to redirect after successfully
	# updating details
	success_url ="/"


class GeeksDetailView(DetailView):
	# specify the model to use
	model = GeeksModel

# Relative import of GeeksModel
from .models import GeeksModel

class GeeksUpdateView(UpdateView):
	# specify the model you want to use
	model = GeeksModel

	# specify the fields
	fields = [
		"title",
		"description"
	]

	# can specify success url
	# url to redirect after successfully
	# updating details
	success_url ="/"

class GeeksDeleteView(DeleteView):
	# specify the model you want to use
	model = GeeksModel
	
	# can specify success url
	# url to redirect after successfully
	# deleting object
	success_url ="/"

class GeeksFormView(FormView):
	# specify the Form you want to use
	form_class = GeeksForm
	
	# specify name of template
	template_name = "projectApp/geeksmodel_form.html"

	# can specify success url
	# url to redirect after successfully
	# updating details
	success_url ="/thanks/"
