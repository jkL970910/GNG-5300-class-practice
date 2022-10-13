# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import GeeksModel, GeeksModelImg

class GeeksForm(forms.Form):
	title = forms.CharField()
	description = forms.CharField()
	views = forms.IntegerField()
	available = forms.BooleanField()
	date = forms.DateField(widget = forms.SelectDateWidget)

# create a ModelForm
class GeeksFormFromModel(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = GeeksModel
		fields = "__all__"

class GeeksFormImg(forms.ModelForm):
	# specify the name of model to use
	class Meta:
		model = GeeksModelImg
		fields = "__all__"

class FormSet(forms.Form):
	title = forms.CharField()
	description = forms.CharField()