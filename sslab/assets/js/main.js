var map;
$(document).ready(function() {

    /* ======= Flexslider ======= */
    $('.flexslider').flexslider({
        animation: "fade"
    });
    
    
    /* ======= Carousels ======= */
    $('#news-carousel').carousel({interval: false});
    $('#videos-carousel').carousel({interval: false});
    $('#testimonials-carousel').carousel({interval: 6000, pause: "hover"});
    $('#awards-carousel').carousel({interval: false});
    
    
    /* ======= Flickr PhotoStream ======= */
    
    $('#flickr-photos').jflickrfeed({
        limit: 12,
        qstrings: {
        id: '138784770@N07' /* Use idGettr.com to find the flickr user id */
        },
        itemTemplate:
            '<li>' +
            '<a href="{{image}}" title="{{title}}" target="_blank">' +
            	'<img src="{{image_s}}" alt="{{title}}" />' +
            '</a>' +
            '</li>'
			
    });

    /* Nested Sub-Menus mobile fix */
   
    $('li.dropdown-submenu > a.trigger').on('click', function(e) {
        var current=$(this).next();
		current.toggle();
		e.stopPropagation(); 
		e.preventDefault(); 
		if (current.is(':visible')) {
    		$(this).closest('li.dropdown-submenu').siblings().find('ul.dropdown-menu').hide();
		}
    });   
    
    
    /* ======= FAQ accordion ======= */  
    $('.card-toggle').on('click', function () {
      if ($(this).find('svg').attr('data-icon') == 'plus-square' ) {
        $(this).find('svg').attr('data-icon', 'minus-square');
      } else {
        $(this).find('svg').attr('data-icon', 'plus-square');
      };
    });  



});
	