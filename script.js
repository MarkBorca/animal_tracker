let map = L.map('map').setView([50.6539,4.5699], 12);
    let osm = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});
osm.addTo(map);

function placeMarker(longitude, latitude, time) {
    let setMarker = L.marker([longitude, latitude]);
    setMarker.addTo(map);
    let popup = setMarker.bindPopup('id: 1 <br> time: ' + time + '<br> longitude: ' + longitude + ' <br> latitude: ' + latitude)
    popup.addTo(map)
}