var baseURL = "http://localhost:8080/";

var msg_speech = new SpeechSynthesisUtterance();
var recognition = new webkitSpeechRecognition();
recognition.continuous = true;
recognition.interimResults = true;

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
            'distance': $('input[name="preference-distance"]:checked').val()
        };

        var options = {
            type: "POST",
            url: baseURL + "preferences",
            data: JSON.stringify({'priorities': priorities, 'preferences': preferences})
        };

        var detailsSuccess = function () {
            $("#preferences-form").hide();
            $("#search-tool").show();
            textToSpeech('How may I help you?');
        };
        
        var detailsFailure = function () {
            
        };
        __makeAjaxRequest(options, detailsSuccess, detailsFailure);
    });
    
    
    $("#start-speech").click(function () {
        startSpeechRecognition();
    });

    $("#get-results").click(function () {
        var resultText = $("#search-text");
        if(resultText != "") {
            getRequestResults(resultText);
        }
    });

    function startSpeechRecognition() {
        recognition.start();
    }

    function stopSpeechRecognition() {
        recognition.abort();
    }

    function textToSpeech(text) {
        msg_speech.text = text;
        window.speechSynthesis.speak(msg_speech);
    }

    function getRequestResults(resultText) {
        stopSpeechRecognition();
        var options = {
            type: "POST",
            url: baseURL + "getresults",
            data: resultText
        };

        var detailsSuccess = function (data) {
            if(typeof data == "string") {
                textToSpeech(data);
            }
        };

        var detailsFailure = function () {

        };
        __makeAjaxRequest(options, detailsSuccess, detailsFailure);
    }

    recognition.onresult = function(event) {
        var resultText = event.results["0"]["0"].transcript;
        $("#search-text").val(resultText);
        var isFinal = event.results["0"].isFinal;
        if(isFinal) {
            getRequestResults(resultText);
        }
    };

});

$( function() {
    $("#sortable").sortable();
    $("#sortable").disableSelection();
} );


var __makeAjaxRequest = function(options, successCallback, failureCallback){
    return $.ajax(options)
        .done(successCallback)
        .fail(failureCallback);
};