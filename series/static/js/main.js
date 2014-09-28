$(document).on('ready', function(){
	console.log("hola");
});

$('.serie').on('mouseenter', function(){
	$(this).children('.foto-serie').css("opacity", "0.5");
	$(this).children('#titulo-serie').css({"display" : "block"});
});

$('.serie').on('mouseleave', function(){
	$(this).children('.foto-serie').css({"opacity" : "1" , "background" : "black"});
	$(this).children('#titulo-serie').css({"display" : "none"});
});
