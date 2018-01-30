$(document).ready(function(){
	var jqActive = false;
	var reactActive = false;
	var nodeActive = false;
	$('.projects-title').on('click', function(e){
		var section = $(e.target)
		if(section.text() === 'JQuery Apps'){
			if(!jqActive){
				$('.jq-container .projects').css("display", "flex").hide().slideDown('slow', function(){
					jqActive = true;
				});
			} else {
				$('.jq-container .projects').hide('fast', function(){
					jqActive = false;
				});
			}
		} else if(section.text() === 'React Apps') {
			if(!reactActive){
				$('.react-container .projects').css("display", "flex").hide().slideDown('slow', function(){
					reactActive = true;
				});
			} else {
				$('.react-container .projects').hide('fast', function(){
					reactActive = false;
				});
			}
		} else if(section.text() === 'Node Apps') {
			if(!nodeActive){
				$('.node-container .projects').css("display", "flex").hide().slideDown('slow', function(){
					nodeActive = true;
				});
			} else {
				$('.node-container .projects').hide('fast', function(){
					nodeActive = false;
				});
			}
		}
	});
});