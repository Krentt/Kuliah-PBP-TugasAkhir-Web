const harga_pengiriman = document.getElementById('hargapengiriman')
const harga_totalproduk = document.getElementById('hargatotalproduk')
let result = harga_pengiriman.value + harga_totalproduk.value 
button.addEventListener('submit',e=>{
    e.preventDefault()
    $.ajax({
        url: '',
        success: function(result) {
            $(".calcprice").text(result)
        }
    })
})

// $document.ready(function(){
//     $(".calcprice").click(function(){
//         $.ajax({
//             url: '/calc/',
//             type: 'GET',
//             success: function(response) {
//                 $(".calcprice").text(response.harga)
//             }
//         })
//     })
// })

// $('.calcprice').on('click', function() {
//     $.ajax({
//         url: '/calc/',
//         type: 'get',
//         success: function(response) {
//             $(".calcprice").text(response.harga)
//         }
//     })
// })

// $('.calcprice').on('click', function() {
//     $.ajax({
//         url: '/calc2/',
//         type:'GET',
//         success: function(response) {
//             $(".calcprice").text(response.harga)
//         }
//       });
// });

// $('.calcprice').on('click', function() {
//     $.ajax({
//         url: '/calc2/',
//         type:'get',
//         success: function(response) {
//             $(".calcprice").text(response.harga)
//         }
//       });
// });