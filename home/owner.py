from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class OwnerListView(LoginRequiredMixin, ListView):
    """
    Subclass the ListView to pass the request to the form.
    """

    def get_queryset(self):
        """ Limit a User to only watching their own data. """
        qs = super(OwnerListView, self).get_queryset()
        return qs.filter(owner=self.request.user).order_by("-updated_at")


class OwnerDetailView(LoginRequiredMixin, DetailView):
    """
    Subclass the DetailView to pass the request to the form.
    """

    def get_queryset(self):
        """ Limit a User to only watching their own data. """
        qs = super(OwnerDetailView, self).get_queryset()
        return qs.filter(owner=self.request.user).order_by("-updated_at")


class OwnerCreateView(LoginRequiredMixin, CreateView):
    """
    Subclass of the CreateView to automatically pass the Request to the Form
    and add the owner to the saved object.
    """

    # Saves the form instance, sets the current object for the view, and redirects to get_success_url().
    def form_valid(self, form):
        new_task = form.save(commit=False)
        new_task.owner = self.request.user
        new_task.save()
        return super(OwnerCreateView, self).form_valid(form)


class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    """
    Subclass the UpdateView to pass the request to the form and limit the
    queryset to the requesting user.
    """

    def get_queryset(self):
        """ Limit a User to only modifying their own data. """
        qs = super(OwnerUpdateView, self).get_queryset()
        return qs.filter(owner=self.request.user).order_by("-updated_at")


class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    """
    Subclass the DeleteView to restrict a User from deleting other
    user's data.
    """

    def get_queryset(self):
        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user).order_by("-updated_at")
