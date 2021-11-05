$document.ready(function(){
    $(".calcprice").click(function(){
        $.ajax({
            url: 'checkout-4',
            type: 'GET',
            success: function(response) {
                $(".btn").text(response.harga)
            }
        })
    })
})

// $('.calcprice').on('click', function() {
//     $.ajax({
//         url: 'checkout-4',
//         type: 'GET',
//         success: function(response) {
//             $(".btn").text(response.harga)
//         }
//     })
// })