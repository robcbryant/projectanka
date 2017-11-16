

    function showBusyGraphic(elementToCover){
        $busyIndicator = $('<div id="busy-indicator"><img src="http://67.205.135.223/static/site-images/busy-indicator.gif"></img></div>');
        $(elementToCover).append($busyIndicator);
    }
    
    function removeBusyGraphic(){
        $('#busy-indicator').remove();
    }

 $('#form-type-form').submit( function(e){

        e.preventDefault(); // Keep the form from submitting
        
        var formData = $("#form-type-form").serializeArray();
        
        showBusyGraphic($('#form-type-form'));
        
        $.ajax({ 
             url   : 'http://67.205.135.223/admin/save_form_type_changes/',
             type  : "POST",
             data  : formData, // data to be submitted
             success : function(returnedQuery)
             {
                console.log(returnedQuery);
                removeBusyGraphic();
                location.reload();
                
                
             },
            // handle a non-successful response
            fail : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });        
        
 }); 
 
 $('#new-form-type-form').submit( function(e){

        e.preventDefault(); // Keep the form from submitting
        
        var formData = $("#new-form-type-form").serializeArray();
        showBusyGraphic($('#form-type-form'));
        
        $.ajax({ 
             url   : 'http://67.205.135.223/admin/create_new_form_type/',
             type  : "POST",
             data  : formData, // data to be submitted
             success : function(returnedQuery)
             {
                console.log(returnedQuery);
                removeBusyGraphic();
                location.reload();
                
             },
            // handle a non-successful response
            fail : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });        
        
 }); 



var attributeTempUniqueID = 0;

$("#add_recordattribute").click(  function () {                        
    $newInputField = $("#formattributegrid").children().first().clone();
    if ($newInputField.css('display') == 'none' ) {$newInputField.show();} 
    
    $newInputField.children()[0].children[1].name = "frat__" + attributeTempUniqueID + "__new";
    $newInputField.children()[0].children[1].value="New Attribute Label";
    $newInputField.children()[0].children[2].children[1].name = "frat__" + attributeTempUniqueID + "__order";
    $newInputField.children()[0].children[2].children[1].value = Math.floor((Math.random() * 900) + 1);    
    $("#formattributegrid").append( $newInputField );
        
    var $newButton = $newInputField.find(".del-field-button");
    $newButton.click( function() {
        $(this).parent().parent().parent().remove()
    });
    
    var $newCheckBox = $newInputField.find(".reference-conversion");
    $newCheckBox.change(function(){
        if(this.checked) {
        //Turn on the form select element
        $(this).parent().children()[2].disabled = false;
        $(this).parent().children()[2].classList.remove("offline")
    } else {
        //turn off the form select element
        $(this).parent().children()[2].disabled = true;  
        $(this).parent().children()[2].classList.add("offline")        
    }
    });
    attributeTempUniqueID += 1;
});



$("#add_recordreference").click(  function () {    
    var $clonedReference = $("#formreferencegrid").children().first().clone();    
    if ($clonedReference.css('display') == 'none' ) {$clonedReference.show();} 
        $clonedReference.children()[1].firstChild.name = "frrt__" + attributeTempUniqueID + "__new";
        $clonedReference.children()[1].firstChild.value="New Reference Field";
        $clonedReference.children()[3].firstChild.name = "nfrrt__" + attributeTempUniqueID + "__ref";
        $clonedReference.children()[4].children[1].name = "nfrrt__" + attributeTempUniqueID + "__order";
        $clonedReference.children()[4].children[1].value = Math.floor((Math.random() * 900) + 1);  
        $clonedReference.appendTo("#formreferencegrid");            
    
    var $newButton = $clonedReference.find(".del-reference-button");
    $newButton.click( function() {
        $clonedReference.remove()
    });
    var $newCheckBox = $clonedReference.find(".reference-conversion");
    $newCheckBox.change(function(){
        if(this.checked) {
        //Turn on the form select element
        $(this).parent().children()[2].disabled = false;
        $(this).parent().children()[2].classList.remove("offline")
    } else {
        //turn off the form select element
        $(this).parent().children()[2].disabled = true;  
        $(this).parent().children()[2].classList.add("offline")        
    }
    });    
    attributeTempUniqueID += 1;
});

$("#add_mediatypereference").click(  function () {    
    var $clonedReference = $("#formmediareferencegrid").children().first().clone();    
    if ($clonedReference.css('display') == 'none' ) {$clonedReference.show(); } 
    $clonedReference.children()[1].firstChild.name = "frrt__" + attributeTempUniqueID + "__new";
    $clonedReference.children()[1].firstChild.value="New Reference Field";
    $clonedReference.children()[3].firstChild.name = "nfrrt__" + attributeTempUniqueID + "__ref";
    $clonedReference.children()[4].children[1].name = "nfrrt__" + attributeTempUniqueID + "__order";
    $clonedReference.children()[4].children[1].value = Math.floor((Math.random() * 900) + 1);
    $clonedReference.appendTo("#formmediareferencegrid");            

    var $newButton = $clonedReference.find(".del-reference-button");
    $newButton.click( function() {
        $clonedReference.remove()
    });
    var $newCheckBox = $clonedReference.find(".reference-conversion");
    $newCheckBox.change(function(){
        if(this.checked) {
        //Turn on the form select element
        $(this).parent().children()[2].disabled = false;
        $(this).parent().children()[2].classList.remove("offline")
    } else {
        //turn off the form select element
        $(this).parent().children()[2].disabled = true;  
        $(this).parent().children()[2].classList.add("offline")        
    }
    });        
    attributeTempUniqueID += 1;
});

$(".del-field-button").click(  function() {
        var $inputParent =  $(this).parent().parent();
            if($inputParent.children()[1].readOnly == false){
                $inputParent.children()[1].readOnly = true;
                $inputParent.children()[1].name = $inputParent.children()[1].name + "__DEL";
            } else {
                $inputParent.children()[1].readOnly = false;
                $inputParent.children()[1].name = $inputParent.children()[1].name.slice(0,-5);
            }
});


$(".reference-conversion").change(function(){
        if(this.checked) {
        //Turn on the form select element
        $(this).parent().children()[2].disabled = false;
        $(this).parent().children()[2].classList.remove("offline")
    } else {
        //turn off the form select element
        $(this).parent().children()[2].disabled = true;  
        $(this).parent().children()[2].classList.add("offline")        
    }
});

function enabledReferenceReload(thisCheckBox) {
    console.log(thisCheckBox);
    if(thisCheckBox.checked) {
        //Turn on the form select element
        $(thisCheckBox).parent().children()[2].disabled = false;
        $(thisCheckBox).parent().children()[2].classList.remove("offline")
    } else {
        //turn off the form select element
        $(thisCheckBox).parent().children()[2].disabled = true;  
        $(thisCheckBox).parent().children()[2].classList.add("offline")        
    }
}



$(".del-reference-button").click(  function() {
        //Grab our parent 'row' <div>
        var $inputParent =  $(this).parent().parent();
            if($inputParent.children()[1].childNodes[0].readOnly == false){
                $inputParent.addClass("up-for-deletion");
                $inputParent.children()[1].childNodes[0].readOnly = true;
                $inputParent.children()[3].childNodes[0].disabled = true;
                $inputParent.children()[1].childNodes[0].name = $inputParent.children()[1].childNodes[0].name + "__DEL";
            } else {
                $inputParent.removeClass("up-for-deletion");
                $inputParent.children()[1].childNodes[0].readOnly = false;
                $inputParent.children()[3].childNodes[0].disabled = false;
                $inputParent.children()[1].childNodes[0].name = $inputParent.children()[1].childNodes[0].name.slice(0,-5);
            }
});

$(".del-mediareference-button").click(  function() {
        //Grab our parent 'row' <div>
        var $inputParent =  $(this).parent().parent();
            if($inputParent.children()[1].childNodes[0].readOnly == false){
                $inputParent.addClass("up-for-deletion");
                $inputParent.children()[1].childNodes[0].readOnly = true;
                $inputParent.children()[3].childNodes[0].disabled = true;
                $inputParent.children()[1].childNodes[0].name = $inputParent.children()[1].childNodes[0].name + "__DEL";
            } else {
                $inputParent.removeClass("up-for-deletion");
                $inputParent.children()[1].childNodes[0].readOnly = false;
                $inputParent.children()[3].childNodes[0].disabled = false;
                $inputParent.children()[1].childNodes[0].name = $inputParent.children()[1].childNodes[0].name.slice(0,-5);
            }
});


///////////////////////////////////////////////////////////////////////////////////////////////
//  CODE FOR CSRF Protection Header
//  Courtesty of: https://github.com/realpython/django-form-fun/blob/master/part1/main.js
///////////////////////////////////////////////////////////////////////////////////////////////
$(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    console.log(csrftoken);
    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
                console.log(xhr);
            }
        }
    });

});
