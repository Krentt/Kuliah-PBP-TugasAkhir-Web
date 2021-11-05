$document.ready(function(){
    $(".calcprice").click(function(){
        $.ajax({
            url: 'checkout-4',
            type: 'get',
            success: function(response) {
                $(".btn").text(response.harga)
            }
        })
    })
})