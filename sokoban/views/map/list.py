from django.views.generic import ListView

from sokoban.models.map import Map


class MapListView(ListView):
    template_name = 'map_list_view.html'
    model = Map
