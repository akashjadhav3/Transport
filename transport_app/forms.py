from django import forms
# from django.forms import ModelForm

# from .models import *
class Transport_Form(forms.Form):
	source = forms.CharField(label='Source',max_length=100)
	destination = forms.CharField(label='Destination',max_length=100)
	amount = forms.CharField(label='amount',max_length=100)
	# datee = forms.DateTimeField(label='Date',
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker1'
    #     })
    # )
	# source= forms.CharField(max_length=20,
    #             widget=forms.TextInput(
    #             attrs={
    #                     'class':'input is-large'
    #             }))
    # Destination= forms.CharField(max_length=20,
    #             widget=forms.TextInput(
    #             attrs={
    #                     'class':'input is-large'
    #             }))
    # amount= forms.CharField(max_length=20,
    #             widget=forms.TextInput(
    #             attrs={
    #                     'class':'input is-large'
    #             }))

	# class Meta:
	# 	model = Transport
	# 	fields = '__all__'
