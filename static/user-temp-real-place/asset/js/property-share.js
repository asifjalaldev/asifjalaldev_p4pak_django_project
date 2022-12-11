jQuery(document).ready(function ($) {
    "use strict";
    /*-----------------------------------------------------------------------------------*/
    /* Share Button
     /* https://github.com/carrot/share-button
     /*-----------------------------------------------------------------------------------*/
    var propertyTitle       = $('.single-property-title'),
        propertyDescription = $('.entry-content p:first'),
        propertyThumbnail   = $('.only-for-print img'),
        shareButtonTitle    = $('#share-button-title').text(),
        config = {
            ui: {
                flyout: 'bottom right',
                button_text: shareButtonTitle
            }
        };

    propertyDescription = $.trim(propertyDescription.text());
    if (propertyDescription.length > 100) {
        propertyDescription = propertyDescription.substring(0, 100);
    }

    config.title = propertyTitle.text();
    config.description = propertyDescription;
    config.image = propertyThumbnail.attr('src');

    if ($('body').hasClass('rtl')) {
        config.ui.flyout = 'bottom left';
    }

    new Share(".share-this", config);
});