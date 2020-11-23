$(document).on('submit', '#edit_form', function(e) {
    e.preventDefault();
    var formData = new FormData(this);
    console.log(formData);
    $.ajax({
        type: 'POST',
        url: '.',
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        success: function(data) {
            window.location.href = '..'
        },
    });
});