


//This turns on the Bootstrap Tooltip Functionality
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

    
    function showBusyGraphic(elementToCover){
        $busyIndicator = $('<div id="busy-indicator"><img src="http://67.205.135.223/static/site-images/busy-indicator.gif"></img></div>');
        $(elementToCover).append($busyIndicator);
    }
    
    function removeBusyGraphic(){
        $('#busy-indicator').remove();
    }
    