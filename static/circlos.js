/*
jQuery-Circle-Plugin v0.1 by Jamal hassouni
https://github.com/jamalhassouni
*/
(function ($) {

	// circle animation pluqins by jamal hassouni 
	$.fn.circlos = function () {
		// deafualt options 
		var DEFAULTS = {
			backgroundColor: '#b3cef6', // default background color 
			progressColor: '#c52241', // default progress color 
			percent: 0, // default percent value
			duration: 2000 // default duration value 
		};	
		
		$(this).each(function () {
			var $target  = $(this);
              // options of circle 	
			var options = {
             // if isset value of background if not use the default value of background color 
			backgroundColor: $target.data('color') ? $target.data('color').split(',')[0] : DEFAULTS.backgroundColor,
		     // if isset value of progress if not use the default value of progress color 
			progressColor: $target.data('color') ? $target.data('color').split(',')[1] : DEFAULTS.progressColor,
			  // if isset value of percent  if not use the default value of percent  
			percent: $target.data('percent') ? $target.data('percent') : DEFAULTS.percent,
			 // if isset value of duration if not use the default value of duration
			duration: $target.data('duration') ? $target.data('duration') : DEFAULTS.duration
			};
			 console.log(options);
	         // add divs for structure
			
			var set_progressColor = '#c52241';
			if(options.percent<35)
			{
			 set_progressColor = '#c52241';	
			}
			else
			{
				 if(options.percent<65)
				{
				 set_progressColor = '#E1CB28';	
				}
				 else
				 {
				 	set_progressColor = '#0DB428';
				 }	
			}
			
			$target.append('<div class="background"></div><div class="rotate"></div><div class="left"></div><div class="right"></div><div class=""><span>' + options.percent + '</span></div>');
	         // change style of the circle with the options values 
			$target.find('.background').css('background-color', options.backgroundColor);
			$target.find('.left').css('background-color', options.backgroundColor);
			$target.find('.rotate').css('background-color', set_progressColor);
			$target.find('.right').css('background-color', set_progressColor);
	
			var $rotate = $target.find('.rotate');
			setTimeout(function () {	
				$rotate.css({
					'transition': 'transform ' + options.duration + 'ms linear',
					'transform': 'rotate(' + options.percent * 3.6 + 'deg)'
				});
			},1);		

			if (options.percent > 50) {
				// add animation for the right class and left class 
				var animationRight = 'toggle ' + (options.duration / options.percent * 50) + 'ms step-end';
				var animationLeft = 'toggle ' + (options.duration / options.percent * 50) + 'ms step-start';  
				$target.find('.right').css({
					animation: animationRight,
					opacity: 1
				});
				$target.find('.left').css({
					animation: animationLeft,
					opacity: 0
				});
			} 
		});
	}
})(jQuery);
