let i = 1;
let cnt=1;
let tot=0;
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
            op.classList.add(Element.classList[0]);
            to_append.add(op);
        })
        let name = $("#i"+i+" :selected").text();
        let price = $("#i"+i+" :selected").attr("class").split(/\s+/)[0];
        let quantity = $("input[name=q-i"+i+"]").val();
        i = i + 1;
        to_append.name = "i"+i;
        to_append.id = "i"+i;
        to_append.classList.add('product_select');
        document.getElementById('repeat').appendChild(to_append);
        to_append = document.createElement('input');
        to_append.name = "q-i"+i;
        to_append.type = "number";
        to_append.classList.add('product_price');
        to_append.value = 0;
        to_append.min = 0;
        document.getElementById('repeat').appendChild(to_append);
        document.getElementById('repeat').appendChild(document.createElement('br'))
        $('#table_content').append('<tr>\
                                    <th scope="row">'+cnt+'</th>\
                                    <td>'+name+'</td>\
                                    <td>'+quantity+'</td>\
                                    <td>'+quantity*price+'</td>\
                                    </tr>')
        tot += quantity*price;
        $('#total').html(tot);
        cnt++;
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

$(document).on('input','#phonenumber',function (e) {
    $.ajax({
        type: 'GET',
        url: '/account/check_cust',
        data: {
            'phonenumber':$('#phonenumber').val()
        },
        success: function (data) {
            if(data.result=='found'){
                $('#name').val(data.name);
                $('#name').prop("readonly",true);
            }else{
                $('#name').prop("readonly",false);
            }
        }
    })
});


$(document).on('input','.product_select',function (e) {
   // alert(1);
});

$(document).on('input','.product_price',function (e) {
   // alert(2);
});