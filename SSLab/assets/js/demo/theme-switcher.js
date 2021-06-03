$(document).ready(function() {
    /* ======= Style Switcher ======= */   
    $('#config-trigger').on('click', function(e) {

        var $panel = $('#config-panel');
        var panelVisible = $('#config-panel').is(':visible');
        if (panelVisible) {
            $panel.hide();          
        } else {
            $panel.show();
        }
        e.preventDefault();

    });
    
    $('#config-close').on('click', function(e) {
        e.preventDefault();
        $('#config-panel').hide();
    });
    
    
    
    $('#color-options a').on('click', function(e) { 
        var $styleSheet = $(this).attr('data-style');
        var $logoImage = $(this).attr('data-logo');
		$('#theme-style').attr('href', $styleSheet);
		$('#logo').attr('src', $logoImage);		
				
		var $listItem = $(this).closest('li');
		$listItem.addClass('active');
		$listItem.siblings().removeClass('active');
		
		e.preventDefault();
		
	});
});