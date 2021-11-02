$('.update-cart').on('click', function() {
    var productId = this.dataset.product
    $.ajax({
        url: '/update_item/',
        dataType: 'json',
        method:'POST',
        headers:{
            'X-CSRFToken':csrftoken,
        },
        data:JSON.stringify({'productId':productId}),
        success: function(data) {
        },
        error: e => {
            console.log(e.responseText);
        }
      });
});

$('.add-item').on('click', function() {
    var productId = this.dataset.product
    $.ajax({
        url: '/add_item/',
        dataType: 'json',
        method:'POST',
        headers:{
            'X-CSRFToken':csrftoken,
        },
        data:JSON.stringify({'productId':productId}),
        success: function(data) {
            var element = document.getElementsByClassName("quantity" + productId)
            element[0].innerHTML = data["jumlah"];
        },
        error: e => {
            console.log(e.responseText);
        }
      });
});

$('.subtract-item').on('click', function() {
    var productId = this.dataset.product
    var element = document.getElementsByClassName("quantity" + productId)
    if (element[0].innerHTML == 1) {
        var action = confirm("Are you sure you want to delete this item?");
        if (action != false) {
            $.ajax({
                url: '/remove_item/',
                dataType: 'json',
                method:'POST',
                headers:{
                    'X-CSRFToken':csrftoken,
                },
                data:JSON.stringify({'productId':productId}),
                success: function(data) {
                    if (data.removeAll) {
                        $(".item-" + productId).remove();
                    }
                },
                error: e => {
                    console.log(e.responseText);
                }
              });
        }
    } else {
        $.ajax({
            url: '/subtract_item/',
            dataType: 'json',
            method:'POST',
            headers:{
                'X-CSRFToken':csrftoken,
            },
            data:JSON.stringify({'productId':productId}),
            success: function(data) {
                element[0].innerHTML = data["jumlah"];
            },
            error: e => {
                console.log(e.responseText);
            }
          });
    }
});

$('.remove-item').on('click', function() {
    var action = confirm("Are you sure you want to delete this item?");
    var productId = this.dataset.product
    if (action != false) {
        $.ajax({
            url: '/remove_item/',
            dataType: 'json',
            method:'POST',
            headers:{
                'X-CSRFToken':csrftoken,
            },
            data:JSON.stringify({'productId':productId}),
            success: function(data) {
                if (data.removeAll) {
                    $(".item-" + productId).remove();
                }
            },
            error: e => {
                console.log(e.responseText);
            }
          });
    }
});