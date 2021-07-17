function createNewMap({latitude, longitude, reliability}){
    const map = document.createElement('iframe');
    map.setAttribute('width', window.outerWidth);
    map.setAttribute('height', window.outerHeight);
    map.setAttribute('style', 'border:0');
    map.setAttribute('loading', 'lazy');
    map.setAttribute('allowfullscreen', '');
    map.setAttribute('src', createSource());
    map.setAttribute('id', 'IP-map');
    insertMapInHTML(map);

    function createSource(){
        const apiKey = 'AIzaSyCL_2CvUZnq3IN0EOanojGwsO-9tJXDydY';
        const zoom = Math.round(reliability / 100 * 21);
        const src = `https://www.google.com/maps/embed/v1/view?key=${apiKey}&center=${latitude},${longitude}&zoom=${zoom}&maptype=roadmap`;
        return src;
    }
    function insertMapInHTML(){
        const mapFatherElement = document.querySelector('#map');
        if (mapFatherElement.children.length == 0){
            mapFatherElement.appendChild(map);
        } else {
            mapFatherElement.innerHTML = '';
            insertMapInHTML();
        }
    }
}