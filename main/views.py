import logging
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


