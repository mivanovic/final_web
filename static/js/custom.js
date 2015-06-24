$(window).load(function() {
	$(function() {
		$('#foo2').carouFredSel({
			auto: 10000,
			responsive: true,
			width: '100%',
			scroll: 1,
			prev: '#prev2',
			next: '#next2',
			items: {
				height: 'auto',
				width:270,
				visible: {
					min: 1,
					max: 1
				}
			},
			mousewheel: true,
			swipe: {
				onMouse: true,
				onTouch: true
			}
		});
	});
});