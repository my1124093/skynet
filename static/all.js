$(document).ready(function(){
    getAllDevices();
    initMap();
});

function initMap() {
    let map = new BMap.Map("allmap");
    map.centerAndZoom("武汉", 15);
}

function getAllDevices() {
    $.post('/get-devices', function(data){
        //alert(data);
    });
}

function pollFace() {
       
}

