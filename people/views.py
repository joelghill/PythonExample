from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Template, Context, Engine
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.urls import reverse

from people.models import Person
from people.forms import PersonForm


def hello_world(request):

    return HttpResponse("<b>Hello World!</b>")


class PersonDetailView(DetailView):

    template_name = "person.html"
    model = Person


class PeopleView(ListView):

    template_name = "people_list.html"
    model = Person


# class PeopleCreateView(TemplateView):

#     template_name = "create_person.html"

#     def get(self, request, *args, **kwargs):
#         self.form = PersonForm()
#         return super().get(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):

#         self.form = PersonForm(request.POST)

#         if self.form.is_valid():
#             self.form.save()
#             return redirect('person_details', pk=self.form.instance.pk)

#         context = self.get_context_data(**kwargs)
#         return self.render_to_response(context)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["form"] = self.form
#         return context


class PeopleCreateView(FormView):
    template_name = "create_person.html"
    form_class = PersonForm

    def get_success_url(self) -> str:
        return reverse("person_details", kwargs={"pk": self.form.instance.pk})

    def form_valid(self, form):
        self.form = form
        self.form.save()
        return super().form_valid(form)
