from django.shortcuts import render
from django.views import generic

from main.forms import PersonForm
from main.models import PersonModel

def showperson2(request):
    data=PersonModel.objects.all()
    context = {'personmodel_list':data}
    return render(request, 'main/personmodel_list.html', context)




class ShowPerson(generic.View):
    def get(self, request, *args, **kwargs):
        data = PersonModel.objects.all()
        form=PersonForm()

        context ={'personmodel_list':data}
        return render(request, 'main/personmodel_list.html', context)
    def post(self,request, *args, **kwargs):
        form=PersonForm(request.POST)
        if form.is_valid():
            ces=form.save()
        else:
            return render(request, 'main/personmodel_list.html')
        return render(request, 'main/personmodel_list.html', {'otvet':'Данные сохранены'})

class ShowPersonList(generic.ListView):
    template_name = 'main/show_person_list.html'
    model=PersonModel

class SavePersonList(generic.Createiew):
    model = PersonModel

    fields = ['first_name', 'last_name', ''
