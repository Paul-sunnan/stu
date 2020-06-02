$(function(){
	// 隐藏所有子标题
	$('.nav-menu').each(function(){
		$(this).children('.nav-content').hide()
	});
	$('.nav-title').each(function(){
		$(this).mouseover(function(){
			var navConso = $(this).parents('.nav-menu').children('.nav-content');
			if (navConso.css('display') != 'none'){
				navConso.hide(400);
			}else{
				navConso.show(400);
			};
		});
	});
});

function AjaxDel(raw){
	var id_info = $(raw).attr('id');
	alert(id_info);
	$.ajax({
		url:'/del_class/',
		type:'get',
		data:{"id":id_info},
		success:function(data){
			alert('删除成功');
		},
	})
};

function show_window(raw){
	divset1 = document.getElementsByClassName('div1');
	for (var i = 0; i < divset1.length; i++) {
		divset1[i].style.display='block';
	};

	divset2 = document.getElementsByClassName('ajax_edit');
	for (var i = 0; i < divset2.length; i++) {
		divset2[i].style.display='block';
	};

	divNext = $(raw).next();
	var id = divNext.attr('id');
	$('#id_cur').text('id:'+id);

	divInfo = $(raw).parent().prev().text();
	$("#name_edit").val(divInfo);
};

function hide_window(){
	divset1 = document.getElementsByClassName('div1');
	for (var i = 0; i < divset1.length; i++) {
		divset1[i].style.display='none';
	};

	divset2 = document.getElementsByClassName('ajax_edit');
	for (var i = 0; i < divset2.length; i++) {
		divset2[i].style.display='none';
	};			
};

function AjaxEdit(){
	alert($('#name_edit').val())

	$.ajax({
		url:"/edit_class/",
		type:"get",
		data:{
			"cid":$('#id_cur').text(),
			"class_name":$('#name_edit').val()
		},
		success:function(data){
			alert(data)
		},
	});
};