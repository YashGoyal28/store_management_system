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

const get_id = e => {
    const id = document.getElementById("get_emp_id").classList[0];
    document.getElementById("emp_id").value = "E" + id;
}

get_id();