$(document).ready(function () {
    /*$("#content").animate({top:'100px'}, "slow");
    console.log('sds');

    $("#button").click(function () {
        $("#content").animate({left:'-105px'}, 5000);
    })*/

    $("#start").click(function () {
        $("#welcome-content").hide(1000);
        $("#preferences-form").show(1000);
    })

});

$( function() {
    $( "#sortable" ).sortable();
    $( "#sortable" ).disableSelection();
} );