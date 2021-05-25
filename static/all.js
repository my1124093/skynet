let device = [];
let device_marker = [];
let count = 0;

$(document).ready(function(){
    initMap();
    socket();
});
function initMap() {
    var map = new BMap.Map("allmap");
    let lis = $('#device-ul').children();
    let num = lis.length;
    if (num > 0) {
        let x = 0;
        let y = 0;
        for (let i = 0; i < num; ++i) {
            x += Number(lis[i].dataset.x);
            y += Number(lis[i].dataset.y);
            device_marker[i] = new BMap.Point(lis[i].dataset.x,
                                              lis[i].dataset.y);
        }
        let init_center_point = new BMap.Point(x/num, y/num);
        map.centerAndZoom(init_center_point, 14);
    } else {
        map.centerAndZoom("武汉", 15);
    }
    for (let i = 0; i < num; ++i) {
        console.log(device_marker[i]);
        map.addOverlay(new BMap.Marker(device_marker[i]));
    }
}



function socket() {
    let webSocket = $.simpleWebSocket({ url: 'ws://localhost:3000/' });

    
}

function update_info(data){
    
}
