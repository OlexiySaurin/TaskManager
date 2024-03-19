from .models import Task
from .owner import OwnerListView, OwnerCreateView, OwnerDetailView, OwnerUpdateView, OwnerDeleteView


class TaskListView(OwnerListView):
    model = Task
    # template is home/task_list.html


class TaskDetailView(OwnerDetailView):
    model = Task
    # template is home/task_detail.html


class TaskCreateView(OwnerCreateView):
    model = Task
    # List the fields to copy from the Article model to the Article form
    fields = ['name', 'description']
    # template is home/task_form.html


class TaskUpdateView(OwnerUpdateView):
    model = Task
    fields = ['name', 'description']


class TaskDeleteView(OwnerDeleteView):
    model = Task
    # template is home/task_confirm_delete.html
