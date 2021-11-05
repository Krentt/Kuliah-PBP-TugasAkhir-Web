$(".calcprice").click(function(){
    $.ajax({
        url: '/calc2',
        success: function(response) {
            $(".calcprice").text(response.harga)
        }
    })
})