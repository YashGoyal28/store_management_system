$(document).on('submit', '#create_staff', function(e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: window.location.href,
        data : {
            'username' : $('#username').val(),
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        }
    });
});