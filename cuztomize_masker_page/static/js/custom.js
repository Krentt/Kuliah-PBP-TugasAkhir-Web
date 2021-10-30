function getSelectValue(){
    var selectedValue = document.getElementById("model").value;
    document.getElementById("image").src = "/static/images/"+selectedValue+".jpeg";

    $.ajax({
        url: '/data-deskripsi/',
        dataType: 'json',
        success: function (data) {
            if (selectedValue == "SURGICAL"){
                $("#description").html(data.SURGICAL);
            } else if (selectedValue == "SPONGE"){
                $("#description").html(data.SPONGE);
            } else if (selectedValue == "PITTA"){
                $("#description").html(data.PITTA);
            } else if (selectedValue == "CLOTH"){
                $("#description").html(data.CLOTH);
            } else {
                alert("ERROR")
            }
        }
    });
}