console.log("Enviando desde js")

var socket = io();
socket.on('connect', function () {
    socket.emit('my event', { data: 'I\'m connected!' });
});

socket.emit('m', 'hello')
socket.on('message', function (msg) {
    $('#messages').append('<li>' + msg + '</li>')
})
$('#send').on('click', function () {
    socket.send($('#myMessage').val());
    $('#myMessage').val('');
})