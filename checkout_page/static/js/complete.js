$document.ready(function(){
    $(".calcprice").click(function(){
        $.ajax({
            url: 'checkout-4',
            type: 'GET',
            success: function(response) {
                $(".calcprice").text(response.harga)
            }
        })
    })
})

$('.calcprice').on('click', function() {
    $.ajax({
        url: 'checkout-4',
        type: 'GET',
        success: function(response) {
            $(".calcprice").text(response.harga)
        }
    })
})