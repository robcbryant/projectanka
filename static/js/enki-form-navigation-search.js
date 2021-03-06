//===================================================================================================================================================================================
//
//  This essentially adds an API/AJAX based search bar to locate forms by their name/ID
//
//  --As the user types letters into the search box, it will automatically query the server for a list of forms of that formtype (the first 5 results)
//  --using a case-insensitive 'icontains' filter. It displays them in a pop up drown down that when clicked on, links the user to the appropriate form page by its given ID
//
//===================================================================================================================================================================================


$('#form-nav-search-form').submit(function(e){
     e.preventDefault();
     $target = $('#search-box-list').children().first();
     if (typeof $target.children().first().attr('href') !== "undefined") window.location.href = $target.children().first().attr('href');
    //Else do nothing
});


 function queryServerForMatchingForms(searchbox, projectID, formtypeID){
    //First get all the associated data we'll need to send to the server
    var searchString = $(searchbox).val();
    var jsonData = {"projectID" : projectID, "formtypeID" : formtypeID, "query" : searchString};
    console.log(jsonData);
    //Send and AJAX Request
    $.ajax({ 
             url   : "http://67.205.135.223/admin/get_form_search_list/",
             type  : "POST",
             data  : jsonData, // data to be submitted
             success : function(returnedQuery)
             {
                //$("#search-box-list").show();
                console.log(returnedQuery.form_list);
                //Create a dropdown of no more than 5 items
                $newSelect = $($(searchbox).parent().children().first());
                console.log($newSelect);
                $newSelect.empty();
                $newSelect.hide();
                //Only do something if "form_list" is in the json data
                if(returnedQuery['form_list'] != null){
                    for (i=0; i< returnedQuery.form_list.length; i++){
                        var currentForm = returnedQuery.form_list[i];
                        if (currentForm.label.length > 24){ 
                            if (i == 0) $newListItem = $('<div class="search-box-item first-result"><a style="font-size:10px;" href="http://67.205.135.223/admin/project/'+currentForm.projectPK +'/formtype/'+ currentForm.formtypePK +'/form_editor/'+ currentForm.formPK +'/">'+ currentForm.label +'</a>(Press Enter to Go)</div>');
                            else        $newListItem = $('<div class="search-box-item"><a style="font-size:10px;" href="http://67.205.135.223/admin/project/'+currentForm.projectPK +'/formtype/'+ currentForm.formtypePK +'/form_editor/'+ currentForm.formPK +'/">'+ currentForm.label +'</a></div>');
                        } else {
                            if (i == 0) $newListItem = $('<div class="search-box-item first-result"><a href="http://67.205.135.223/admin/project/'+currentForm.projectPK +'/formtype/'+ currentForm.formtypePK +'/form_editor/'+ currentForm.formPK +'/">'+ currentForm.label +'</a>(Press Enter to Go)</div>');
                            else        $newListItem = $('<div class="search-box-item"><a href="http://67.205.135.223/admin/project/'+currentForm.projectPK +'/formtype/'+ currentForm.formtypePK +'/form_editor/'+ currentForm.formPK +'/">'+ currentForm.label +'</a></div>');                           
                        }
                        $newSelect.append($newListItem);
                    }
                    //For another robust solution--let's modify the text size to be smaller if it's longer than 30 characterSet
                    $newSelect.children().each( function() {
                       if ($(this).children().first().text().length > 30) $(this).children().first().addClass('form-nav-search-sml-txt'); 
                    });
                    $newSelect.show();
                }
             },

            // handle a non-successful response
            fail : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });    
    
}
 

 $(document).mouseup(function(e) 
{
    var container = $("#search-box-list");
    var adminToolBarContainer = $('#form-quick-search-tool .admin-search-list');
    // if the target of the click isn't the container nor a descendant of the container
    if ((!container.is(e.target) || !adminToolBarContainer.is(e.target) ) && (container.has(e.target).length === 0 || adminToolBarContainer.has(e.target).length == 0)) 
    {
        container.hide();
        adminToolBarContainer.hide();
    }
    
    
}); 


//This function will locate the previous and next buttons and give them their appropriate url address based on
//--an API endpoint 'get_previous_next_form'
function loadPreviousAndNextFormValues(){
    
    //setup our json
    //If there is no form PK we're in the view form type view so don't worry about next previous navigation
    if ("GV_formPK" in window){
        var jsonData = {"project_pk" : GV_projectPK, "formtype_pk" : GV_formtypePK, "form_pk" : GV_formPK};
        //Setup our element variables for editing
        $previousLink = $('#previous-form-link');
        $nextLink = $('#next-form-link');
        
        
        //perform our AJAX request to the endpoint to get the values
        $.ajax({ 
                 url   : "http://67.205.135.223/admin/get_previous_next_forms/",
                 type  : "POST",
                 data  : jsonData, // data to be submitted
                 success : function(returnedQuery)
                 {
                    console.log(returnedQuery);
                    //if our returned query contains an 'ERROR' key, then create fake links with a '#'
                    if (returnedQuery['ERROR']){
                        $previousLink.attr("href", "#");
                        $nextLink.attr("href", "#");
                    //Otherwise we are in the clear--edit our links/labels!
                    } else {
                        //Handle the Previous Form Link--and make the font size adaptive to the length of the label
                        $previousLink.attr("href", "http://67.205.135.223/admin/project/"+returnedQuery.project_pk+"/formtype/"+returnedQuery.formtype_pk+"/form_editor/"+returnedQuery.previous_pk+"/");
                        if(returnedQuery.previous_label.length >= 12)$previousLink.parent().css('font-size', '12px');
                        if(returnedQuery.previous_label.length > 16) {$previousLink.parent().prepend(returnedQuery.previous_label.substring(0,12)+"...");$previousLink.parent().prop('title', returnedQuery.previous_label);}
                        else $previousLink.parent().prepend(returnedQuery.previous_label);
                        
                        //Handle the Next Form Link--and make the font size adaptive to the length of the label
                        $nextLink.attr("href", "http://67.205.135.223/admin/project/"+returnedQuery.project_pk+"/formtype/"+returnedQuery.formtype_pk+"/form_editor/"+returnedQuery.next_pk+"/");
                        if(returnedQuery.next_label.length >= 12)$nextLink.parent().css('font-size', '12px');
                        if(returnedQuery.next_label.length > 16) {$nextLink.parent().append(returnedQuery.next_label.substring(0,12)+"..."); $nextLink.parent().prop('title', returnedQuery.next_label);} 
                        else $nextLink.parent().append(returnedQuery.next_label);
                    }
                 },

                // handle a non-successful response
                fail : function(xhr,errmsg,err) {
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                    $previousLink.attr("href", "#");
                    $nextLink.attr("href", "#");
                }
            });   
    }
}





//***********************************************************************************************************************************************************************
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
    //console.log(csrftoken);
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



//We have to do this last -- AFTER the CSRF token is created

$(document).ready(loadPreviousAndNextFormValues);