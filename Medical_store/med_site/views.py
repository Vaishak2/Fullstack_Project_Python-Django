from django.shortcuts import render
from django.http import Http404
from django.urls import reverse

from med_site.models import Medicine, Doctors
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from django.utils.timezone import datetime



@login_required
def medicine_list(request):
    # View function for list page of medicines.

    all_med = Medicine.objects.all()
    num_med = Medicine.objects.all().count()

    
    context = {
        'all_med': all_med ,
        'num_med': num_med ,    
    }

    # Render the HTML template med_list.html with the data in the context variable
    return render(request, 'medicine_list.html', context=context)

# --------------------------------------------------------------------------------------------
# View function for home page.
@login_required()
def home(request):    
    time_today = datetime.now()
    return render(request, 'home.html',{'time_today':time_today})


# --------------------------------------------------------------------------------------------
# View function for registeration page.
def register(request):            
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else : 
        form = UserCreationForm()       
    return render(request, 'register.html',{'form':form})
# --------------------------------------------------------------------------------------------
# View function for search engine.
# @login_required
def search_bar(request):
    
    if request.method=="POST":
        bar_field=request.POST['bar_field']
        search_data=Medicine.objects.filter(med_name__istartswith=bar_field)
    search = {
        'bar_field': bar_field,
        'search_data': search_data,             
    }

    return render(request, 'search_bar.html',context=search)
# --------------------------------------------------------------------------------------------
# View function for doctors page.
@login_required
def doc_list(request):
    
    all_doc = Doctors.objects.all()    
    num_doc = Doctors.objects.all().count()
    
    doctors = {
        'all_doc': all_doc ,      
        'num_doc': num_doc ,
    }

    return render(request, 'doctors_list.html', context=doctors)
# --------------------------------------------------------------------------------------------
# View function for contact page.
@login_required
def contact(request):
    
    return render(request, 'contact.html',)

# --------------------------------------------------------------------------------------------
class MedicineDetailView(generic.DetailView): # Class based view for medicine details
    model = Medicine
    fields = '__all__' 

# --------------------------------------------------------------------------------------------
class MedicineCreate(CreateView): # Class based view for add medicine
    model = Medicine
    fields = '__all__' 
    success_url = reverse_lazy('medicine_list') 

# --------------------------------------------------------------------------------------------
class MedicineUpdate(UpdateView):  # Class based view for edit medicine
    model = Medicine
    fields = ['med_name', 'purpose', 'unit', 'dosage', 'stock']
    success_url = reverse_lazy('medicine_list')

# --------------------------------------------------------------------------------------------
class MedicineDelete(DeleteView):  # Class based view for delete medicine
    model = Medicine
    success_url = reverse_lazy ('medicine_list')






# def med_update(request,id):
#     med_id = Medicine.objects.get(id=id)
#     form = MedicineForm(request,instance=id)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#         return redirect('medicine_list')
  

#     update = {
#         'form': form ,
#         'med_id': med_id ,      
#     }

#     return render(request, 'medicine_form.html', context=update)

    # def med_delete(request,id):
    #     medicine = Medicine.object.get(id=id)
    #     medicine.delete()
    #     return redirect('med_list')
