from . import models, forms
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy


class InflowListView(ListView):
    model = models.Inflows
    template_name = 'inflow_list.html'
    context_object_name = 'inflow'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)
        return queryset


class InflowCreateView(CreateView):
    model = models.Inflows
    template_name = 'inflow_create.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflow_list')


class InflowDetailView(DetailView):
    model = models.Inflows
    template_name = 'inflow_detail.html'
