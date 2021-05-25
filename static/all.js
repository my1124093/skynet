let device = [];
let device_marker = [];
let count = 0;
let person = {};
let device_icon = new BMap.Icon('/static/img/9.png', new BMap.Size(10, 10), {
    offset: new BMap.Size(5, 10),
    imageOffset: new BMap.Size(0, 0)
});
let p0_icon = new BMap.Icon('/static/img/0.png', new BMap.Size(5, 5));
let p1_icon = new BMap.Icon('/static/img/1.png', new BMap.Size(5, 5));

$(document).ready(function(){
    initMap();
    //poll();
});
function initMap() {
    let map = new BMap.Map("allmap");
    let lis = $('#device-ul').children();
    let num = lis.length;
    let device_point = [];
    if (num > 0) {
        let x = 0;
        let y = 0;
        for (let i = 0; i < num; ++i) {
            x += Number(lis[i].dataset.x);
            y += Number(lis[i].dataset.y);
            device_point[i] = new BMap.Point(lis[i].dataset.x,
                                             lis[i].dataset.y);
        }
        let init_center_point = new BMap.Point(x/num, y/num);
        map.centerAndZoom(init_center_point, 14);
    } else {
        map.centerAndZoom("武汉", 15);
    }
    for (let i = 0; i < num; ++i) {
        device_marker[i] = new BMap.Marker(device_point[i], {icon: device_icon} );
        map.addOverlay(device_marker[i]);
    }
}



function poll() {
    setInterval(function(){
        $.post('/info', function(data){
             update_info(JSON.parse(data));
        });
    }, 1000);
}

function update_info(data){
    draw(0, data[0]['device_id']);
    draw(1, data[1]['device_id']);
}

function draw(pid, did) {
    
}
