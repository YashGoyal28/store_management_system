$(document).on('submit', '#create_staff', function(e){
    e.preventDefault();
    var formData = new FormData(document.getElementById("create_staff"));
    $.ajax({
        type: 'POST',
        url: window.location.href,
        data : formData,
        cache: false,
        contentType: false,
        processData: false,
        success:function(data){
            if(data.result == 'success'){
                window.location.href = '..'+'/staff_info/';
            }else{
               $('#error').html(data.message);
            }
        },
    });
});

const get_id = e => {
    const id = document.getElementById("get_emp_id").classList[0];
    document.getElementById("emp_id").value = "E" + id;
}

get_id();