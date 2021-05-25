let device = [];
let device_marker = [];
let count = 0;
let person = {};

$(document).ready(function(){
    initMap();
    poll();
});
function initMap() {
    let map = new BMap.Map("allmap");
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



function poll() {
    setInterval(function(){
        $.post('/info', function(data){
             update_info(JSON.parse(data));
        });
    }, 1000);
}

function update_info(data){
    console.log(data);
    let num_person = person.length;
    let num_data = data.length;
    for (let i = 0; i < num_data; ++i) {
        if (undefined == person[data[i].id]) {
            person[data[i].id] = {
                'state': 1,
                'time': data[i]['time'],
                'device': data[i]['device_id']
            };
            $('#person').append('<li id="person-'+data[i].id + '" class="list-group-item list-group-item-success"></li>');
        } else {
        
        }
    }
}

function draw(pid, did, active=1) {
    
}
