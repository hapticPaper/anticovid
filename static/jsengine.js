function loadDiv(div, route){
    $.ajax({
        type: 'GET',
        url: `${route}`,

        beforeSend: function(xhr){
           $(div).html('<div class="loader"> </div>');
        },

        success: function(msg){
           $(div).html(msg);
        }
      });
}