from django.views.generic import ListView, DetailView
from .models import Item, MEAL_TYPE


class MenuList(ListView):
    queryset = Item.objects.order_by('-date_created')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["meals"] = MEAL_TYPE
        return context

class MenuItemDetail(DetailView):
    model = Item
    template_name = 'menu_item_detail.html'
