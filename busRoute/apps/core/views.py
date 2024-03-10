from typing import Any
from django.views.generic import TemplateView
from django.templatetags.static import static

import folium
# from folium.plugins import Draw


class MapView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        # coordinates = [
        #     {"location": [-10.43029, -45.174006],
        #         "tooltip": "TRAJETO SAÍDA DO IFPI",
        #         "popup": "IFPI - Campus Corrente"},
        #     {"location": [-10.438233, -45.173019],
        #         "tooltip": "1ª Parada",
        #         "popup": "Posto de Combustível Primavera"},
        #     {"location": [-10.454374, -45.171460],
        #         "tooltip": "2ª Parada",
        #         "popup": "Praça Principal do Vermelhão"},
        #     {"location": [-10.439672, -45.168913],
        #         "tooltip": "3ª Parada",
        #         "popup": "Supermercado Rocha"},
        #     {"location": [-10.443239, -45.160735],
        #         "tooltip": "4ª Parada",
        #         "popup": "Praça da Igreja Batista"},
        #     {"location": [-10.445506, -45.157068],
        #         "tooltip": "5ª Parada",
        #         "popup": "15ª Regional de Educação"},
        #     {"location": [-10.451376, -45.146146],
        #         "tooltip": "6ª Parada",
        #         "popup": "Posto de Combustível do Aeroporto"},
        #     {"location": [-10.454766, -45.137556],
        #         "tooltip": "7ª Parada",
        #         "popup": "Escola Municipal Orley Cavalcante Pacheco"},
        # ]

        out_route = 'data/out_route.geojson'
        return_route = 'data/return_route.geojson'
        maker_route = 'data/maker_route.geojson'

        m = folium.Map(location=(-10.439829, -45.16325), zoom_start=14)

        # draw = Draw(export=True)
        # draw.add_to(m)

        icon_url = static('img/834px-Bus_stop_symbol.svg.ico')

        # for coord in coordinates:
        #     folium.Marker(
        #         location=coord["location"],
        #         tooltip=coord["tooltip"],
        #         popup=coord["popup"],
        #         icon=folium.DivIcon(html=f"""
        #                       <div>
        #                          <img src="{icon_url}" style="width: 40px; height: 40px;" />
        #                       </div>
        #                       """),
        #     ).add_to(m)

        folium.GeoJson(out_route, name="Rota de Saída",
                       style_function=lambda x: {'color': 'green'}).add_to(m)
        folium.GeoJson(return_route, name="Rota de Retorno",
                       style_function=lambda x: {'color': 'red'}).add_to(m)

        folium.GeoJson(maker_route, name="Maker Router",
                       tooltip=folium.GeoJsonTooltip(
                           fields=['Local']),
                       marker=folium.Marker(
                           icon=folium.DivIcon(html=f"""
                              <div>
                                 <img src="{icon_url}" style="width: 35px; height: 35px;" />
                              </div>
                              """),
                       )).add_to(m)

        map_html = m._repr_html_()

        return {'map': map_html}
