from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from .models import Event, Category, Comment
from .forms import EventoForm
from users.models import User
from django.core.urlresolvers import reverse, reverse_lazy


# Create your views here.


# def index(request):
#     events = Event.objects.all().order_by('-created')[:6]
#     categories = Category.objects.all()
#     print events
#     print categories
#     return render(request,  'events/index.html', {'events': events,
#                                         'categories': categories})

class IndexView(TemplateView):
    template_name = 'events/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.all().order_by('-created')[:6]
        context['categories'] = Category.objects.all()
        return context


# def main_panel(request):
#     events = Event.objects.filter(organizer__username='manuh').order_by('is_free', '-created')
#     cantidad_eventos = events.count()
#     return render(request, 'events/panel/panel.html', {'events': events, 'cantidad': cantidad_eventos })


class MainPanelView(TemplateView):
    template_name = 'events/panel/panel.html'

    def get_context_data(self, **kwargs):
        context = super(MainPanelView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.filter(organizer = self.request.user).order_by('is_free', '-created')
        context['cantidad'] = context['events'].count()
        return context


# def crear_evento(request):
#     if request.method == 'POST':
#         modelform = EventoForm(request.POST, request.FILES)
#         if modelform.is_valid():
#             u = User.objects.get(pk=1)
#             nuevo_evento = modelform.save()
#             nuevo_evento.organizer = u
#             nuevo_evento.save()
#             return redirect(reverse('events_app:panel'))
#     else:
#         modelform = EventoForm()
#
#     return render(request, 'events/panel/crear_evento.html', {'form': modelform})

class CrearEvento(CreateView):
    form_class = EventoForm
    template_name = 'events/panel/crear_evento.html'
    success_url = reverse_lazy('events_app:panel')

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super(CrearEvento, self).form_valid(form)


# def detalle_evento(request, evento_id):
#     event = get_object_or_404(Event, pk=evento_id)
#     return render(request, 'events/panel/detalle_evento.html', {'event': event})

class EventDetail(DetailView):
    template_name = 'events/panel/detalle_evento.html'
    model = Event


# def editar_evento(request, evento_id):
#     event = get_object_or_404(Event, pk=evento_id)
#
#     if request.method == 'POST':
#         modelform = EventoForm(request.POST, request.FILES, instance=event)
#         if modelform.is_valid():
#             modelform.save()
#             return redirect(reverse('events_app:panel'))
#     else:
#         modelform = EventoForm(instance=event)
#
#     return render(request, 'events/panel/editar_evento.html', {'form': modelform, 'event': event})

class EventEdit(UpdateView):
    template_name = 'events/panel/editar_evento.html'
    model = Event
    form_class = EventoForm
    success_url = reverse_lazy('events_app:panel')
    
    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super(EventEdit, self).form_valid(form)


# def eliminar_evento(request, evento_id):
#     event = get_object_or_404(Event, pk=evento_id)
#
#     if request.method == 'POST':
#         event.delete()
#         return redirect(reverse('events_app:panel'))
#
#     return render(request, 'events/panel/eliminar_evento.html', {'event': event})

class DeleteEvent(DeleteView):
    template_name = 'events/panel/eliminar_evento.html'
    model = Event
    success_url = reverse_lazy('events_app:panel')
    context_object_name = 'event'
