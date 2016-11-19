var baseURL = "http://localhost:8080/"

$(document).ready(function () {
    /*$("#content").animate({top:'100px'}, "slow");
    console.log('sds');

    $("#button").click(function () {
        $("#content").animate({left:'-105px'}, 5000);
    })*/

    $("#start").click(function () {
        $("#welcome-content").hide(1000);
        $("#preferences-form").show(1000);
    });
    
    $("#send-preferences").click(function () {
        var priorities = $("#sortable").sortable("toArray");
        for(var i = 0; i <priorities.length; i++) {
            priorities[i] = priorities[i].split("-")[1]
        }
        var preferences = {
            'price': $('input[name="preference-price"]:checked').val(),
            'cuisine': $('input[name="preference-cuisine"]:checked').val(),
            'distance': $('input[name="preference-distance"]:checked').val(),
        };
        $.ajax({
            type: 'POST',
            url: baseURL + "preferences",
            data: JSON.stringify({'priorities': priorities, 'preferences': preferences}),
            dataType: "json",
            success: function(resultData) { alert("Save Complete") }
        })
    });

});

$( function() {
    $("#sortable").sortable();
    $("#sortable").disableSelection();
} );