let map = new BMap.Map("allmap");
let device_point = [];

$(document).ready(function(){
    initMap();
    poll();
});
function initMap() {
    let lis = $('#device-ul').children();
    let num = lis.length;
    if (num > 0) {
        let x = 0;
        let y = 0;
        for (let i = 0; i < num; ++i) {
            x += Number(lis[i].dataset.x);
            y += Number(lis[i].dataset.y);
            device_point[i] = new BMap.Point(Number(lis[i].dataset.x),
                                             Number(lis[i].dataset.y));
        }
        let init_center_point = new BMap.Point(x/num, y/num);
        map.centerAndZoom(init_center_point, 14);
    } else {
        map.centerAndZoom("武汉", 15);
    }
    for (let i = 0; i < num; ++i) {
        //device_marker[i] = new BMap.Marker(device_point[i], {icon: device_icon} );
        //map.addOverlay(device_marker[i]);
        addMarker(device_point[i], i);
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
    console.log(data);
    for (let i = 0; i < 2; ++i) {
        console.log(i + ' ' +   data[i]['device_id']);
        if (Number(data[i]['device_id']) >= 0) {
            draw(i, Number(data[i]['device_id']));
        }
    }
}

let my_icon = [
    new BMap.Icon('/static/img/1.png', new BMap.Size(50, 50), {offset: new BMap.Size(0, 0), imageOffset: new BMap.Size(0, 10)}),
    new BMap.Icon('/static/img/3.png', new BMap.Size(50, 50), {offset: new BMap.Size(0, 0), imageOffset: new BMap.Size(10, 0)})
];

let old_did = [-1, -1];
let marker = [undefined, undefined];

function draw(pid, did){
    //console.log('/static/img/' + String(pid)+'.png');
    //

    if (marker[pid] == undefined) {
        marker[pid] = new BMap.Marker(device_point[did], {icon: my_icon[pid]});
        old_did[pid] = did;
        map.addOverlay(marker[pid]);
    } else {
        map.removeOverlay(marker[pid]);
        marker[pid] = new BMap.Marker(device_point[did], {icon: my_icon[pid]});
        map.addOverlay(marker[pid]);
        map.addOverlay(new BMapLib.CurveLine([device_point[old_did[pid]], device_point[did] ], 
                       {strokeColor:"blue", strokeWeight:3, strokeOpacity:0.5}));
        old_did[pid] = did;
    }

    console.log('draw ', pid, ' ', did); 
      
}

function addMarker(point, index){ 
    var myIcon = new BMap.Icon("/static/img/9.png", new BMap.Size(20, 20));      
    var marker = new BMap.Marker(point, {icon: myIcon});    
    map.addOverlay(marker);
}    

