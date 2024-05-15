function initMap(mapId, data) {
    const map = L.map(mapId).setView([20, 0], 2); // Set a default view

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap'
    }).addTo(map);

    // Add a geoJson layer
    L.geoJson(getGeoJson(data), {
        style: function (feature) {
            return { color: getColor(feature.properties.count) };
        }
    }).addTo(map);
}

function getGeoJson(data) {
    // Convert data to GeoJSON format
    return {
        "type": "FeatureCollection",
        "features": data.map(item => ({
            "type": "Feature",
            "properties": {
                "name": item.country,
                "count": item.count
            },
            "geometry": {
                "type": "Point",
                "coordinates": [getLongitude(item.country), getLatitude(item.country)]
            }
        }))
    };
}

function getColor(count) {
    return count > 50 ? '#800026' :
           count > 20 ? '#BD0026' :
           count > 10 ? '#E31A1C' :
           count > 5 ? '#FC4E2A' :
           '#FFEDA0'; // Default color
}

function getLongitude(country) {
    // Placeholder function to get longitude based on country
    return 0; // Implement actual logic
}

function getLatitude(country) {
    // Placeholder function to get latitude based on country
    return 0; // Implement actual logic
}

// Initialize maps
initMap('mapTitles', titlesPerCountry);
initMap('mapMovies', moviesPerCountry);
initMap('mapShows', showsPerCountry);
