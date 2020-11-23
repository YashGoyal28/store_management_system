let i = 1;
add_field();
function add_field(e){
    options = document.getElementsByClassName('options')
    btn = document.getElementById('add');
    btn.addEventListener('click', e => {
        to_append = document.createElement('select');
        Array.from(options).forEach(Element => {
            op = document.createElement('option');
            op.text = Element.text;
            op.value = Element.value;
            to_append.add(op);
        })
        i = i + 1;
        to_append.name = "i"+i;
        document.getElementById('repeat').appendChild(to_append);
        to_append = document.createElement('input');
        to_append.name = "q-i"+i;
        document.getElementById('repeat').appendChild(to_append);
        document.getElementById('repeat').appendChild(document.createElement('br'))
    });
}

$(document).on('submit', '#bill_form', function(e) {
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