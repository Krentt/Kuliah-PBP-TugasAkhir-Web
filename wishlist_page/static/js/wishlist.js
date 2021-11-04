// Create Django Ajax Call
$("form#createItem").submit(function() {
    var nameInput = $('input[name="formName"]').val().trim();
    var priceInput = $('input[name="formPrice"]').val().trim();
    var countInput = $('input[name="formCount"]').val().trim();
    if (nameInput && priceInput && countInput) {
        // Create Ajax call
        $.ajax({
            url: create_item_url,
            data: {
                'name': nameInput,
                'price': priceInput,
                'count': countInput
            },
            dataType: 'json',
            success: function(data){
                if (data.item) {
                    appendToTable(data.item);
                    console.log('success add!');
                }
            }
        });
    } else {
        alert("All fields must have a valid value.");
    }
    $('form#createItem').trigger("reset");
    $("#createItemModal").css("display", "none");
    $(".modal-backdrop").remove();
    return false;
});

function appendToTable(item) {
    $("#wishlistTable > tbody:last-child").append(`
    <tr id="item-${item.id}">
        <td class="itemCounter itemData" name="counter">${item.counter}</td>
        '<td class="itemName itemData" name="name">${item.name}</td>
        '<td class="itemPrice itemData" name="price"><label class="currency">$</label><label class="harga">${item.price}</label></td>
        '<td class="itemCount itemData" name="count">${item.count}</td>
        '<td style="width: 150px;">
            <button type="button"
                    class="btn btn-warning btn-sm js-edit-item" 
                    onClick="editItem(${item.id})" 
                    data-toggle="modal" 
                    data-target="#updateItemModal">EDIT
            </button>
            <button type="button"
                    class="btn btn-danger btn-sm js-delete-item"
                    onClick="deleteItem(${item.id})">DELETE
            </button>
        </td>
        '<td>
            <button onclick="location.href='/cart/'" type="button" class="btn btn-secondary">
                Add to Cart</button>
        </td>
    </tr>
    `);
}

// Update Django Ajax Call
$("form#updateItem").submit(function () {
    var idInput = $('input[name="formUpdateId"]').val().trim();
    var nameInput = $('input[name="formUpdateName"]').val().trim();
    var priceInput = $('input[name="formUpdatePrice"]').val().trim();
    var countInput = $('input[name="formUpdateCount"]').val().trim();
    if (nameInput && priceInput && countInput) {
        // Create Ajax call
        $.ajax({
            url: update_item_url,
            data: {
                'id': idInput,
                'name': nameInput,
                'price': priceInput,
                'count': countInput
            },
            dataType: 'json',
            success: function(data){
                if (data.item) {
                    updateTable(data.item);
                    console.log('success update');
                }
            }
        });
    } else {
        alert("UPDATE All fields must have a valid value.");
    }
    $('form#updateItem').trigger("reset");
    $("#updateItemModal").css("display", "none");
    $(".modal-backdrop").remove();
    return false;
});

function editItem(id) {
    if (id) {
        tr_id = "#item-" + id;
        item_name = $(tr_id).find(".itemName").text();
        price = $(tr_id).find(".itemPrice").find(".harga").text();
        count = $(tr_id).find(".itemCount").text();
        $('#form-id-update').val(id);
        $('#form-name-update').val(item_name);
        $('#form-price-update').val(price);
        $('#form-count-update').val(count);
    }
}

function updateTable(item) {
    $("#wishlistTable #item-" + item.id).children(".itemData").each(function() {
        var attr = $(this).attr("name");
        if (attr == "name") {
            $(this).text(item.name);
        } else if (attr == "price") {
            $(this).text(item.price);
        } else if (attr == "count") {
            $(this).text(item.count);
        } 
    });
}

// Delete Django Ajax Call
function deleteItem(id) {
    var action = confirm("Are you sure you want to delete this item?");
    if (action != false) {
        $.ajax({
            url: delete_item_url,
            data: {
                'id': id,
            },
            dataType: 'json',
            success: function(data) {
                if (data.deleted) {
                    $("#wishlistTable #item-" + id).remove();
                }
            }
        });
    }
}