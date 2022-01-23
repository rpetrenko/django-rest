import logging
from urllib import response
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views.generic.edit import (
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from main import forms
from main import models


logger = logging.getLogger(__name__)


class ContactUsView(FormView):
    template_name = "contact_form.html"
    form_class = forms.ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)


class ProductListView(ListView):
    template_name = "main/product_list.html"
    paginate_by = 2
    model = models.Product

    def get_queryset(self):
        tag = self.kwargs.get("tag", None)
        if tag is None or tag == "all":
            products = models.Product.objects.active()
        else:
            self.tag = get_object_or_404(
                    models.ProductTag, slug=tag
                )

            products = models.Product.objects.active().filter(
                tags=self.tag
            )            
        logger.info(products)

        return products.order_by("name")


class SignupView(FormView):
    template_name = "signup.html"
    form_class = forms.UserCreationForm

    def get_success_url(self):
        redirect_to = self.request.GET.get("next", '/')
        return redirect_to

    def form_valid(self, form):
        response = super().form_valid(form)
        form.save()

        email = form.cleaned_data.get('email')
        raw_password = form.cleaned_data.get('password1')
        logger.info(
            "new signup for email {}".format(email)
        )
        user = authenticate(email=email, password=raw_password)
        login(self.request, user)
        form.send_mail()
        messages.info(
            self.request, "you signed up successfully."
        )
        return response


