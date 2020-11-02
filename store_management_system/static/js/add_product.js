$(document).on('submit', '#product_form', e => {
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: window.location.href,
        data : {
            'name' : $('#p_name').val(),
            'price' : $('#p_price').val(),
            'description' : $('#p_description').val(),
            'quantity' : $('#p_quantity').val(),
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        }
    })
});