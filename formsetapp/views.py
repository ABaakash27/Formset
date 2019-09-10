from django.shortcuts import render
from django.views.generic import CreateView
from .models import *
from formsetapp.forms import *
from django.http import HttpResponseRedirect
# Create your views here.
class CustomerCreateView(CreateView):
	model = Customer
	form_class = CustomerForm
	template_name = "customer.html"
	# success_url = "/CustomerCreateView"

	# #template_name = "SugarCane/common_form.html"
	# permission_required = 'cms.add_fieldman'
	# success_message = 'FieldMan added successfully'
	def get_context_data(self, **kwargs):
		context = super(CustomerCreateView, self).get_context_data(**kwargs)
		if self.request.POST:
			context['Order_form'] = OrderFormSet(self.request.POST)
		else:
			context['Order_form'] = OrderFormSet()
			return context

	def post(self,request,*args,**kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		Order_form = OrderFormSet(self.request.POST)
	  

		if (form.is_valid() and Order_form.is_valid()):
			return self.form_valid(form, Order_form)
		else:
			return self.form_invalid(form, Order_form)

	def form_valid(self, form, Order_form):
		self.object = form.save()
		Order_form.instance = self.object
		Order_form.save()
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form, Order_form):
		return self.render_to_response(
			self.get_context_data(form=form, Order_form=Order_form))
