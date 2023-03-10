from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectCreate(CreateView):
    template_name = 'projects/project_create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDetail(DetailView):
    template_name = 'projects/project.html'
    model = Project
    paginate_by = 10
    paginate_orphans = 1


class ProjectUpdate(UpdateView):
    template_name = 'projects/project_update.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    template_name = 'projects/project_confirm_delete.html'
    model = Project
    success_url = reverse_lazy('index')
