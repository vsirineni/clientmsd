from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, View
from. models import Client,Comment,Vechicle
from .models import models
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import CommentForm
from django.contrib import messages



# Create your views here.
class ClientListView(LoginRequiredMixin,ListView):
    model = Client
    template_name = 'client_list.html'


class ClientUpdateView(LoginRequiredMixin,UpdateView):
    model = Client
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    template_name = 'client_edit.html'


class ClientDetailView(LoginRequiredMixin,DetailView):
    model = Client
    template_name = 'client_detail.html'
    login_url = 'login'


class ClientDeleteView(LoginRequiredMixin,DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')


class ClientCreateView(LoginRequiredMixin,  CreateView):
    model = Client
    template_name = 'client_new.html'
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@login_required()
def comment(request,pk):
    post = get_object_or_404(Client, pk=pk)
    if request.method =='POST':
        cform = CommentForm(request.POST)
        if cform.is_valid():
            comment = cform.save(commit=False)
            comment.client = post
            comment.author=request.user
            comment.comment = comment.comment
            comment.save()
            print(comment.client)
            messages.success(request, f'Your comment has been updated')
            return redirect('client_detail', pk=post.pk)
    else:
        cform = CommentForm()
        context = {
            'comment': cform
    }
    return render(request, 'comment.html', context)

@login_required()
def clientVechicles(request):
    vec= Vechicle.objects.all()
    context={'vec':vec}
    return render(request, 'Vechicles.html',context)


