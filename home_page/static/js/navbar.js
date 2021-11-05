//ganti bg sama fg saat hover
$(document).ready(function() {
    //href login logout
    let next = window.location.pathname;
    $("#navbar-login").attr("href", `/login?next=${next}`)
    let prevBackground;
    $('.nav-item').hover(function() {
        prevBackground = $(this).css('background-color');
        $(this).css('background-color', 'rgb(13, 110, 253)');
      }, 
      function() {
        $(this).css('background-color', prevBackground);
        $('#home_btn_navbar > a').css('color', 'white')
      })
})