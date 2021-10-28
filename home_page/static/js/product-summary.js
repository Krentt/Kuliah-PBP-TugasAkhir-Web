'use strict'

const number_of_max_image = 20;
let delay_time = 400;
let initial_image_number = 0;
let current_image = 0;
let before_width;
let is_delayed_next = false;
let is_delayed_prev = false;
function isTouchDevice() {
    return (('ontouchstart' in window) ||
        (navigator.maxTouchPoints > 0) ||
        (navigator.msMaxTouchPoints > 0));
}

// code from https://stackoverflow.com/questions/2264072/detect-a-finger-swipe-through-javascript-on-the-iphone-and-android
document.addEventListener('touchstart', handleTouchStart, false);        
document.addEventListener('touchmove', handleTouchMove, false);

var xDown = null;                                                        
var yDown = null;

function getTouches(evt) {
return evt.touches ||             // browser API
        evt.originalEvent.touches; // jQuery
}                                                     
                                                                        
function handleTouchStart(evt) {
    const firstTouch = getTouches(evt)[0];                                      
    xDown = firstTouch.clientX;                                      
    yDown = firstTouch.clientY;                                      
};                                                
                                                                        
function handleTouchMove(evt) {
    if ( ! xDown || ! yDown ) {
        return;
    }

    var xUp = evt.touches[0].clientX;                                    
    var yUp = evt.touches[0].clientY;

    var xDiff = xDown - xUp;
    var yDiff = yDown - yUp;
    if ( Math.abs( xDiff ) > Math.abs( yDiff ) ) {/*most significant*/
        if ( xDiff > 0 ) {
            /* right swipe */
            if(!is_delayed_next) {
                next_handler();
                is_delayed_next = true;
                setTimeout(() => {is_delayed_next = false;}, delay_time)
            }
        } else {
            /* left swipe */
            if(!is_delayed_prev) {
                prev_handler();
                is_delayed_prev = true;
                setTimeout(() => {is_delayed_prev = false;}, delay_time)
            }        
        }                       
    }
    /* reset values */
    xDown = null;
    yDown = null;                                             
};




function get_num_visible_image() {
    return Math.floor(parseInt($('#product-summary-container').css('width')) / (parseInt($('.cropper').css('width')) || 112));
}

function get_disp() {
    return parseInt($(".cropper").css('width'));
}

function get_last_disp() {
    let hidden_frac = parseInt($('#product-summary-container').css('width')) / parseInt($('.cropper').css('width')) - get_num_visible_image();
    let disp = get_disp();
    return (2 - hidden_frac) * parseInt(disp) + parseInt($('#product-summary-container').css('padding-left'));
}

let counter = 0;
function load_initial_image() {
    while(current_image < initial_image_number) {
        append_image(current_image, false);
        current_image++;
    }
}


let is_added = false;
function next_handler() {
    if (current_image < number_of_max_image) {
        append_image(counter, true);
        current_image++;
    }

    if(counter  < number_of_max_image - get_num_visible_image() - 2) {
        move_right(get_disp());
        counter++;
    }
    else if (counter == number_of_max_image - get_num_visible_image() - 2 && !is_added) {
        move_right(get_last_disp());
        is_added = true;
    }
    else {
        bounce_right();
    }
}

function move_right(disp) {
    $(".cropper").animate(
        {left:`-=${disp}`}
    )
}


function bounce_right() {
    let bound = Math.floor(parseInt(get_disp()) / 2);
    
    $(".cropper").animate(
        {left:`-=${bound}`},   
    )
    $(".cropper").animate(
        {left:`+=${bound}`},   
    )
    
}

function prev_handler() {
    if(counter == 1 && is_added) {
        move_left(get_last_disp());
        is_added = false;
    }
    else if (counter > 0) {
        move_left(get_disp());
        counter--;
    }
    else {
        bounce_left();
    }

    if(current_image > initial_image_number && (counter < number_of_max_image - get_num_visible_image() - 4)) {
        $("#product-summary-container > div:last-child").detach();
        current_image--;
    }
}

function move_left(disp) {
    $(".cropper").animate(
        {left:`+=${disp}`}
    )
}


function bounce_left() {
    let bound = Math.floor(parseInt(get_disp()) / 2);
    
    $(".cropper").animate(
        {left:`+=${bound}`},   
    )
    $(".cropper").animate(
        {left:`-=${bound}`},   
    )

}


let prev_disp_last = 0;
$(document).ready(function() {
    if(isTouchDevice()) {
        $('.next, .prev').detach();
        $('#product-summary-container').css('width', '90%');
        delay_time = 600;
    }
    $('.next').click(function () {
        if(!is_delayed_next) {
            next_handler();
            is_delayed_next = true;
            setTimeout(() => {is_delayed_next = false;}, delay_time)
        }
    })
    $('.prev').click(function () {
        if(!is_delayed_prev) {
            prev_handler();
            is_delayed_prev = true;
            setTimeout(() => {is_delayed_prev = false;}, delay_time)
        }
    })
    initial_image_number = get_num_visible_image() + 3;
    before_width = parseInt($('#product-summary-container').css('width'));
    load_initial_image();
})


window.onresize = function() {
    if(counter == 0) {
        initial_image_number = get_num_visible_image() + 3;
        load_initial_image();
    }
    if(is_added) {
        move_right(before_width - parseInt($('#product-summary-container').css('width')));
        counter = number_of_max_image - get_num_visible_image() - 1 - (number_of_max_image - (initial_image_number - 3) - 1 - counter);
    }
    before_width = parseInt($('#product-summary-container').css('width'));
    initial_image_number = get_num_visible_image() + 3;
}


function append_image(current_counter, is_shift) {
    var data_jsn = {
        current_counter: current_counter
    };
    $.ajax(
        {
            type: 'GET',
            dataType: 'json',
            url: "ajax/get_image",
            data: data_jsn,
            success: function(response) {
                let data = {
                    src: response['src'],
                    title: response['title'],
                    price: response['price']
                };
                let new_element = create_image(data);
                
                $("#product-summary-container").append(new_element);
                if(is_shift) {
                    if(is_added) {
                        $("#product-summary-container > div:last-child").animate(
                            {left:`-=${(current_counter) * get_disp() + get_last_disp()}`}, 100
                        )
                    }
                    else {
                        $("#product-summary-container > div:last-child").animate(
                            {left:`-=${(current_counter + 1) * get_disp()}`}, 100
                        )
                    }
                }
            }
        }
    )
}

function create_image(data) {
    var template = [
        "<div class='cropper'>", 
            "<div class='card'>", 
                "<img class='card-img-top' src={{src}} loading='auto'>",
                "<h1 class='card-title'>{{title}}</h1>",
                "<p class='card-text'>{{price}}</p>",
            "</div>", 
        "</div>"].join("\n");
    return Mustache.render(template, data);
}