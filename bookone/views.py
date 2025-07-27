from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from bookone.models import Book, Lang, Instance


# Create your views here.
class MainView(View):
    def get(self, request):
        bk = Book.objects.all()
        lg = Lang.objects.all()
        ins = Instance.objects.all()
        ctx = {'book_list': bk, 'lang_list': lg, 'ins_list': ins}
        return render(request, 'bookone/book_list.html', ctx)

# CRUD for Book
class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'bookone/all_form.html'
    success_url = reverse_lazy('bookone:all_list')
class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'bookone/all_form.html'
    success_url = reverse_lazy('bookone:all_list')
class BookDelete(DeleteView):
    model = Book
    context_object_name = 'my_object'
    fields = '__all__'
    template_name = 'bookone/confirm_delete.html'
    success_url = reverse_lazy('bookone:all_list')

# CRUD for Lang
class LangCreate(CreateView):
    model = Lang
    fields = '__all__'
    template_name = 'bookone/all_form.html'
    success_url = reverse_lazy('bookone:all_list')
class LangUpdate(UpdateView):
    model = Lang
    fields = '__all__'
    template_name = 'bookone/all_form.html'
    success_url = reverse_lazy('bookone:all_list')
class LangDelete(DeleteView):
    model = Lang
    context_object_name = 'my_object'
    fields = '__all__'
    template_name = 'bookone/confirm_delete.html'
    success_url = reverse_lazy('bookone:all_list')

# CRUD for Instance
class InsCreate(CreateView):
    model = Instance
    fields = '__all__'
    template_name = 'bookone/all_form.html'
    success_url = reverse_lazy('bookone:all_list')
class InsUpdate(UpdateView):
    model = Instance
    fields = '__all__'
    template_name = 'bookone/all_form.html'
    success_url = reverse_lazy('bookone:all_list')
class InsDelete(DeleteView):
    model = Instance
    context_object_name = 'my_object'
    fields = '__all__'
    template_name = 'bookone/confirm_delete.html'
    success_url = reverse_lazy('bookone:all_list')
