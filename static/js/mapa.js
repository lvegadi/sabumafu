mapboxgl.accessToken = 'pk.eyJ1IjoibHZlZ2FkaSIsImEiOiJja3ZuNGJqNzJkdWNvMnBtbjVyYjJjdzluIn0.7IQf0OTZQF_NnVcD3HVo1w';

var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/outdoors-v11',
    center : [longitud,latitud],
    zoom: 9.3,
})    

