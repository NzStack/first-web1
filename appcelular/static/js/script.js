$(document).ready(function(){
	// agregando clase active al la primera categoria 
	$('.category_list .category_item[category="all"]').addClass('ct_item-active');
	// filtran2
	$('.category_item').click(function(){ /*filtar y asignar item activado*/
		var catProduct = $(this).attr('category'); /* al hacer click llama al atributo */		

		// agregando clase active al seleccionado
		$('.category_item').removeClass('ct_item-active');
		$(this).addClass('ct_item-active');

		// ocultando equipos 
		$('.product-item').css('transform', 'scale(0)'); //efecto
		function hideProduct(){
			$('.product-item').hide();
		} setTimeout(hideProduct,400); // valores a asignar para vizualizar el efecto

		// mostrando equipos
		function showProduct(){
			$('.product-item[category="'+catProduct+'"]').show();
			$('.product-item[category="'+catProduct+'"]').css('transform', 'scale(1)');
		} setTimeout(showProduct,400);
	});

	// mostrar todos los equipos 

	$('.category_item[category="all"]').click(function(){
		function showAll(){
			$('.product-item').show();
			$('.product-item').css('transform', 'scale(1)');
		} setTimeout(showAll,400);
	});
});