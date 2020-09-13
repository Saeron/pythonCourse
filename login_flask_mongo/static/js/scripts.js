$("form[name=signup_form]").submit(fuction(e) {
	var $form = $(this);
	var $error = $form.find(".error");
	var data = $form.serialize();

	$.ajax({
		url: "/user/signup",
		type: "POST",
		data: data,
		dataType: "json",
		success: fuction(resp){
			console.log(resp);
		},
		error: fuction(resp){
			console.log(resp);
		}
	})

	e.preventDefault();

});
