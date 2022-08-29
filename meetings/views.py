
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

from .forms import MeetingForm

class VideoCreateView(CreateView):
    form_class = MeetingForm
  
    template_name = 'create.html'
    success_url = reverse_lazy('meet:create')
    success_message = 'Successfully Created Meetings.'
