$(document).ready(function(e) {

	$('.icon-right').on('click', function() {
		$('.music__info__wrapper').toggleClass('display');
	});

	$('.icon-right').on('click', function() {
		$('.right__panel').toggleClass('right__panel__menuOpen');
		$('.left__panel').toggleClass('left__panel__menuOpen');
	});

	$('.music__menu').on('click', function() {
		$('.music__info__wrapper').removeClass('display');
	});

	$('.icon-right').on('click', function() {
		$('.music__menu').addClass('menu_list_open');
	});

	$('.music__menu').on('click', function() {
		$('.right__panel').removeClass('right__panel__menuOpen');
		$('.left__panel').removeClass('left__panel__menuOpen');
		$('.music__menu').removeClass('menu_list_open');
	});

	var $sync1 = $(".cover"),
		$sync2 = $(".title, .hero__backgorund"),
		flag = false,
		duration = 300;

	$sync1
		.owlCarousel({
			loop: true,
			center: true,
			items: 1,
			nav: false,
			dots: false
		})
		.on('changed.owl.carousel', function(e) {
			if (!flag) {
				flag = true;
				$sync2.trigger('to.owl.carousel', [e.item.index, duration, true]);
				flag = false;
			}
		});

	$sync2
		.owlCarousel({
			loop: true,
			items: 1,
			nav: false,
			dots: false,
			animateOut: 'slideOutDown',
			animateIn: 'slideInDown',
			mouseDrag: false,
			touchDrag: false,
			pullDrag: false
		})
		.on('click', '.owl-item', function() {
			$sync1.trigger('to.owl.carousel', [$(this).index(), duration, true]);
		});

	owl = $('.owl-carousel').owlCarousel();
	$(".button__prev").click(function() {
		owl.trigger('prev.owl.carousel');
	});

	$(".button__next").click(function() {
		owl.trigger('next.owl.carousel');
	});

}); // End Ready