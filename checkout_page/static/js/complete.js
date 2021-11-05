$document.ready(function(){
    $(".calcprice").click(function(){
        $.ajax({
            url: 'calc',
            type: 'GET',
            success: function(response) {
                $(".calcprice").text(response.harga)
            }
        })
    })
})

$('.calcprice').on('click', function() {
    $.ajax({
        url: 'calc',
        type: 'GET',
        success: function(response) {
            $(".calcprice").text(response.harga)
        }
    })
})

$('.calcprice').on('click', function() {
    $.ajax({
        url: 'calc2',
        type:'GET',
        success: function(response) {
            $(".calcprice").text(response.harga)
        }
      });
});