mapboxgl.accessToken = 'pk.eyJ1IjoibHZlZ2FkaSIsImEiOiJja3ZuNGJqNzJkdWNvMnBtbjVyYjJjdzluIn0.7IQf0OTZQF_NnVcD3HVo1w';

var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/outdoors-v11',
    center: [longitud, latitud],
    zoom: 10,
})

const nav = new mapboxgl.NavigationControl();
map.addControl(nav);

map.on('load', () => {
    // Add a data source containing GeoJSON data.
    map.addSource('maine', {
        'type': 'geojson',
        'data': geojson
    });
    // Marcador
    const marker1 = new mapboxgl.Marker()
        .setLngLat([longitud, latitud])
        .addTo(map);
        
    // Geojson
    map.addLayer({
        'id': 'maine',
        'type': 'fill',
        'source': 'maine', // reference the data source
        'layout': {},
        'paint': {
            'fill-color': '#0080ff', // blue color fill
            'fill-opacity': 0.5
        }
    });
    map.addLayer({
        'id': 'outline',
        'type': 'line',
        'source': 'maine',
        'layout': {},
        'paint': {
            'line-color': '#000',
            'line-width': 1
        }
    });
});