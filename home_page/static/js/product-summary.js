'use strict'

let number_of_max_image = 9;
let delay_time = 400;
let initial_image_number = 0;
let current_image = 0;
let before_width;
let is_delayed_next = false;
let is_delayed_prev = false;
let is_cur_img_avail = true;


function isTouchDevice() {
    return (('ontouchstart' in window) ||
        (navigator.maxTouchPoints > 0) ||
        (navigator.msMaxTouchPoints > 0));
}

// Handler for horizontal swipe in touchscreen device 
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



// get number of user visible image
function get_num_visible_image() {
    return Math.floor(parseInt($('#product-summary-container').css('width')) / (parseInt($('.cropper').css('width')) || 112));
}

// 1 displacement = 1 image
function get_disp() {
    return parseInt($(".cropper").css('width'));
}

// last dispalcement -> make the right visible image as pivot
function get_last_disp() {
    let hidden_frac = parseInt($('#product-summary-container').css('width')) / parseInt($('.cropper').css('width')) - get_num_visible_image();
    let disp = get_disp();
    return (1 - hidden_frac) * parseInt(disp) + parseInt($('#product-summary-container').css('padding-left'));
}

// load image when the page is just loaded
let counter = 0;
async function load_initial_image() {
    while(current_image < initial_image_number && current_image < number_of_max_image) {
        let is_continue = await append_image(current_image, false);
        if(!is_continue) 
            break;
        current_image++;
        $('#no-product-message-container').detach();
    }
}


// next button and swipe handler
let is_added = false;
async function next_handler() {

    if (counter == number_of_max_image - get_num_visible_image() - 1 && !is_added) {
        move_right(get_last_disp());
        is_added = true;
        counter++;
    }
    else if(counter  <= number_of_max_image - get_num_visible_image() - 1) {
        move_right(get_disp());
        counter++;
    }
    else {
        bounce_right();
    }
    if (current_image < number_of_max_image) {
        let is_continue = await append_image(counter, true);
        if(is_continue) {
            current_image++ ;    
        }
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


// left button and swipe handler
function prev_handler() { 
    
    if(counter == 1 && is_added) {
        move_left(get_last_disp());
        is_added = false;
        counter--;
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
        counter = initial_image_number - 3 + counter - get_num_visible_image();
    }
    before_width = parseInt($('#product-summary-container').css('width'));
    initial_image_number = get_num_visible_image() + 3;
}


function append_image(current_counter, is_shift) {
    var data_jsn = {
        current_counter: current_image
    };
    return new Promise((resolve, reject) => {
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
                            $("#product-summary-container > div:last-child").css("left",`-=${(current_counter - 1) * get_disp() + get_last_disp()}`);
                        }
                        else {
                            $("#product-summary-container > div:last-child").css("left",`-=${(current_counter) * get_disp()}`);
                        }
                    }
                    resolve(true);
                },
                error: function(response) {
                    
                    number_of_max_image = current_image;
                    reject(false);
                }
            }
        )
    })   
}

// render image html
function create_image(data) {
    var template = [
        "<div class='cropper'>", 
            "<div class='card'>", 
                "<img class='card-img-top' src={{src}}>",
                "<h1 class='card-title'>{{title}}</h1>",
                "<p class='card-text'>{{price}}</p>",
            "</div>", 
        "</div>"].join("\n");
    return Mustache.render(template, data);
}
