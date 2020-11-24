let i = 0;
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
        to_append.id = 'q-i'+i;
        document.getElementById('repeat').appendChild(to_append);
        document.getElementById('repeat').appendChild(document.createElement('br'))
        let name = $("#i"+i+" :selected").text();
        let price = $("#i"+i+" :selected").attr("class").split(/\s+/)[0];
        let quantity = $("input[name=q-i"+i+"]").val();
        $('#table_content').append('<tr id="bill-'+cnt+'">\
                                    <th scope="row">'+cnt+'</th>\
                                    <td>'+name+'</td>\
                                    <td>'+quantity+'</td>\
                                    <td id="bill-'+cnt+'-tot">'+quantity*price+'</td>\
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
            $('#PrintableBill').printThis();
            setTimeout(function () { window.location.href = '.'; }, 10000);
        },
    });
});

$(document).on('input','#phonenumber',function (e) {
    $('#Bill_phonenumber').text($('#phonenumber').val());
    $.ajax({
        type: 'GET',
        url: '/account/check_cust',
        data: {
            'phonenumber':$('#phonenumber').val()
        },
        success: function (data) {
            if(data.result=='found'){
                $('#name').val(data.name);
                $('#Bill_name').text($('#name').val());
                $('#name').prop("readonly",true);
            }else{
                $('#Bill_name').text($('#name').val());
                $('#name').prop("readonly",false);
            }
        }
    })
});

$(document).on('input','#name',function (e) {
     $('#Bill_name').text($('#name').val());
});

$(document).on('input','.product_select',function (e) {
    //alert(1);
    let ID = this.id[1];
    let count = ID;
    let name = $('#'+this.id+' :selected').text();
    let price = $("#"+this.id+" :selected").attr("class").split(/\s+/)[0];
    let quantity = $("input[name=q-"+this.id+"]").val();
    ID = "bill-"+ID;
    tot -= parseInt($('#'+ID+'-tot').text());
    $("#"+ID).html('<th scope="row">'+count+'</th>\
                            <td>'+name+'</td>\
                            <td>'+quantity+'</td>\
                            <td id="bill-'+count+'-tot">'+quantity*price+'</td>');
    tot += quantity*price;
    $('#total').html(tot);
});

$(document).on('input','.product_price',function (e) {
   // alert(2);
    let ID = this.id[3];
    let count = ID;
    let name = $('#'+this.id[2]+this.id[3]+' :selected').text();
    let price = $("#"+this.id[2]+this.id[3]+" :selected").attr("class").split(/\s+/)[0];
    let quantity = $("input[name="+this.id+"]").val();
    ID = "bill-"+ID;
    tot -= parseInt($('#'+ID+'-tot').text());
    $("#"+ID).html('<th scope="row">'+count+'</th>\
                            <td>'+name+'</td>\
                            <td>'+quantity+'</td>\
                            <td id="bill-'+count+'-tot">'+quantity*price+'</td>');
    tot += quantity*price;
    $('#total').html(tot);
});
