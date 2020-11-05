$(document).on('submit','#register_form',function(e){
    e.preventDefault();
    $.ajax({
        type : 'POST',
        url : 'register/',
        data : {
            username : $('#username_register').val(),
            email : $('#email_register').val(),
            phonenumber : $('#phonenumber_register').val(),
            store : $('#store_register').val(),
            address : $('#address_register').val(),
            password1 : $('#password_register').val(),
            password2 : $('#cpassword_register').val(),
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(data){
            console.log(data.result);
            if(data.result == 'success'){
                window.location.href = 'home/';
            }else{
                $('#register_error').html(data.message);
            }
        },
        error:function(){

        },
    });
});