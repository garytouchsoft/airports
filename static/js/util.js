let map;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: {
            lat: airportLatitude,
            lng: airportLongitude
        },
        zoom: 14,
    });
}

