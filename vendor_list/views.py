from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from.forms import List_Form
from.models import Vendor_List

def index(request):
	my_item = Vendor_List.objects.order_by('id')
	form = List_Form()
	context = {'my_item':my_item,
		'form': form
	}
	return render(request,'vendor_list/index.html',context)

@require_POST
def add_new_item(request):
	form = List_Form(request.POST)

	if form.is_valid():
		text = form.cleaned_data.get('text')
		my_new_item = Vendor_List(item=text)
		my_new_item.save()
	return redirect('vendor_list-index')

def bought_item(request,item_id):
	my_item = Vendor_List.objects.get(pk=item_id) #pk é primary key pq é a posição do item
	my_item.complete = True
	my_item.save()
	return redirect('vendor_list-index')

def delete_item(request):
	Vendor_List.objects.filter(complete__exact=True).delete()
	return redirect('vendor_list-index')

def delete_all(request):
	Vendor_List.objects.all().delete()
	return redirect('vendor_list-index')
