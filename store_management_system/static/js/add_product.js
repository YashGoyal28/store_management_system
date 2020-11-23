$(document).on('submit', '#product_form', e => {
    e.preventDefault();
    var formData = new FormData(document.getElementById("product_form"));
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