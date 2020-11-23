$(document).on('submit', '#product_form', e => {
    e.preventDefault();
    var formData = new FormData(this);
    $.ajax({
        type: 'POST',
        url: window.location.href,
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        success: function(data) {
            window.location.href = '.'
        },
    });
});