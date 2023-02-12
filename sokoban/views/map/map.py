from django.views.generic import DetailView

from sokoban.models.map import Map


class MapView(DetailView):
    template_name = 'map_view.html'
    model = Map

    def content_as_list(self):
        return self.content.split(';')
