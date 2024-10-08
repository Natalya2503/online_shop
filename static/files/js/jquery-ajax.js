
// добавление товара в корзину

$(document).ready(function(){
    $(document).on('click', '.add-to-cart', function(e){
        e.preventDefault();

        var goodsInCartCount = $('#goods-in-cart-count');
        var cartCount = parseInt(goodsInCartCount.text() || 0);

        var product_id = $(this).data('product-id');
        var add_to_cart_url = $(this).attr('href');

        $.ajax({
            type: 'POST',
            url: add_to_cart_url,
            data: {
                product_id: product_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function(data){
                cartCount++;
                goodsInCartCount.text(cartCount);

                var cartItemsContainer = $('#cart-items-container');
                cartItemsContainer.html(data.cart_items_html);
            },
            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },

          



        });


    });

    // удаление товара из корзины

    $(document).on('click', '.remove-from-cart', function(e){
        e.preventDefault();
    
        var goodsInCartCount = $('#goods-in-cart-count');
        var cartCount = parseInt(goodsInCartCount.text() || 0);
    
        var cart_id = $(this).data('cart-id');
        var remove_from_cart = $(this).attr('href');
    
        $.ajax({
            type: 'POST',
            url: remove_from_cart,
            data: {
                cart_id: cart_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function(data){
                cartCount -= data.quantity_deleted;
                goodsInCartCount.text(cartCount);
    
                var cartItemsContainer = $('#cart-items-container');
                cartItemsContainer.html(data.cart_items_html);
            },
            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    });

    // изменение товара в корзине

    $(document).on("click", ".decrement", function () {
    
        var url = $(this).data("cart-change-url");
    
        var cartID = $(this).data("cart-id");
       
        var $input = $(this).closest('.input-group').find('.number');
      
        var currentValue = parseInt($input.val());
      
        if (currentValue > 1) {
            $input.val(currentValue - 1);

            updateCart(cartID, currentValue - 1, -1, url);
        }
    });

    // Обработчик события для увеличения значения
    $(document).on("click", ".increment", function () {

        var url = $(this).data("cart-change-url");
       
        var cartID = $(this).data("cart-id");
       
        var $input = $(this).closest('.input-group').find('.number');
      
        var currentValue = parseInt($input.val());

        $input.val(currentValue + 1);


        updateCart(cartID, currentValue + 1, 1, url);
    });

    function updateCart(cartID, quantity, change, url) {
        $.ajax({
            type: "POST",
            url: url,
            data: {
                cart_id: cartID,
                quantity: quantity,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },

            success: function (data) {
              

               
                var goodsInCartCount = $("#goods-in-cart-count");
                var cartCount = parseInt(goodsInCartCount.text() || 0);
                cartCount += change;
                goodsInCartCount.text(cartCount);

               
                var cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);

            },
            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    }

  

})






