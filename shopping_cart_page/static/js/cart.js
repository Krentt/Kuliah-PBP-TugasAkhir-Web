$('.update-cart').on('click', function() {
    var productId = this.dataset.product
    var action = this.dataset.action
    $.ajax({
        url: '/update_item/',
        dataType: 'json',
        method:'POST',
        headers:{
            'X-CSRFToken':csrftoken,
        },
        data:JSON.stringify({'productId':productId, 'action':action}),
        success: function (data) {
        },
        error: e => {
            console.log(e.responseText);
        }
      });
});