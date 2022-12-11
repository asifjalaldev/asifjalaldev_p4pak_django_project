jQuery(document).ready(function ($) {
    "use strict";
    /*-----------------------------------------------------------------------------------*/
    /* Horizontal Scrolling
     /* https://github.com/darsain/sly
     /*-----------------------------------------------------------------------------------*/
    var $frame = $('.scrolling-frame'),
        $wrap = $frame.parent();

    // Call Sly on frame
    $frame.sly({
        horizontal: 1,
        itemNav: 'basic',
        smart: 1,
        activateOn: 'click',
        mouseDragging: 1,
        touchDragging: 1,
        releaseSwing: 1,
        startAt: 3,
        scrollBar: $wrap.find('.scrollbar'),
        scrollBy: 1,
        activatePageOn: 'click',
        speed: 300,
        elasticBounds: 1,
        dragHandle: 1,
        dynamicHandle: 1,
        clickBar: 1,

        // Buttons
        prev: $wrap.find('.prev'),
        next: $wrap.find('.next')
    });
});