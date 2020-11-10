
const socket = io();
socket.on('connect', function() {
    socket.emit('my event', {data: 'I\'m connected!'});
});

socket.on('start', (data) => {
    alert(data['name']);
    console.log(data);
    document.querySelector('#guess_game').style.display = 'block';
});

function submit_guess_game() {
    let num = document.querySelector('#guess_input').value;
    console.log(num);
    socket.emit('submit guess', {data: num});
    document.querySelector('#guess_game').style.display = 'none';
}

    /*
    socket.on('my request', (data) => {
        console.log(data)
    });

    function print_log(){
       socket.emit('print_log', {name:'pls log this'});
    }*/
