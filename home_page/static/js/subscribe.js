$('#footer-subscribe-form').submit(function(event) {
    event.preventDefault();
    var serializedData = $(this).serialize();
    $.ajax({
        type: 'POST',
        dataType: 'json',
        url: 'ajax/subscribe',
        data: serializedData,
        success: function(response) {
            $("#footer-subscribe-form").trigger('reset');
            if(response['message'] != "duplicate") {
                alert(response['message'])
            }
            else {
                alert(`You have already subscribed our newslatter`)
            }
        },
        error: function(response) {
            alert(response['message'])
        }
    })
})

// if ( window.history.replaceState ) {
//     window.history.replaceState( null, null, window.location.href );
//   }
// window.onbeforeunload = function() {
//     return 'Are you sure you want to navigate away from this page?';
// };