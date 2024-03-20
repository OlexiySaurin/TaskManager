from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import TaskForm, CreateUserForm
from .models import Task
from .owner import OwnerListView, OwnerDetailView, OwnerUpdateView, OwnerDeleteView, OwnerCreateView


# register views

def register_view(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    ctx = {'form': form}
    return render(request, "registration/register.html", ctx)

# tasks crud views


class TaskListView(OwnerListView):
    model = Task
    # template is home/task_list.html

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = TaskForm()
        context['create_form'] = form
        return context


class TaskDetailView(OwnerDetailView):
    model = Task
    # template is home/task_detail.html


class TaskCreateView(OwnerCreateView):
    model = Task
    template_name = 'home/task_list.html'
    fields = ['name', 'description']

    # """Overriding get_context_data to change name of creating form to create_form"""
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['create_form'] = context['form']
    #     del context['form']
    #     return context


class TaskUpdateView(OwnerUpdateView):
    model = Task
    fields = ['name', 'description']
    template_name = 'home/task_list.html'

    """Overriding get_context_data to change name of updating form to update_form"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_form'] = context['form']
        context['task_list'] = Task.objects.filter(owner=self.request.user)
        del context['form']
        return context


class TaskDeleteView(OwnerDeleteView):
    model = Task
    # template is home/task_confirm_delete.html

