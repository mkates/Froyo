//This class stores all the question answers
var Prefs = function Prefs() {
	var zipcode = '12345';
	var answers = [9,9,9,9,9,9,9,9,9,9];
	
	this.getanswer = function(question) {
		return answers[question];
	}
	this.setanswer = function(question,answer) {
		answers[question] = answer;
	}
	this.getallanswers = function() {
		return answers;
	}
	this.getzipcode = function() {
		return zipcode;
	}
}
$(document).ready(function() {
	//$(".progressbar .bar").css("width","60%");
	var test = new Prefs();
	var startquestion = $(".question").first().attr("id");
	startquestion = parseInt(startquestion.charAt(startquestion.length-1));
	var totalquestions = $(".question").length;
	//Show First Question
	$(".question").first().fadeIn();
	var currentquestion = $(".question").first().attr("id");
	currentquestion = parseInt(currentquestion.charAt(currentquestion.length-1));
	
	$(".question .answer_container p").click(function() {
		//Update selection CSS
		$(this).parent().children().removeClass("selected");
		$(this).addClass("selected");
		
		//Get handler for question's div
		var question = $(this).parent().parent();
		//Handler for next question in the DOM
		var nextq = question.next();

		//Get question number and update prefs
		var questionNumber = $(question).attr('id');
		questionNumber = parseInt(questionNumber.charAt(questionNumber.length-1));
		var answer = $(this).attr('id').charAt(2);
		test.setanswer(questionNumber,answer);
		
		//Transition to next question
		$(question).fadeOut('fast',function() {
			if (nextq.attr("id")==="showresults") {
				$("#showresults").fadeIn();
				$(".forward").fadeOut();
			} else {
				$(nextq).fadeIn();
			}
			currentquestion = questionNumber+1;
			console.log(currentquestion);
		});
		
		//Miscellaneous
		$("#answerarray").html("<p>"+test.getallanswers()+"</p>");
		$(".back").fadeIn();
		progress(startquestion,currentquestion,totalquestions);
	});
	$(".back").click(function() {
		lastq = currentquestion - 1;
		//If on the results button
		if ($("#question"+lastq).next().attr("id") === "showresults") {
			//Transition to next question
			$("#showresults").fadeOut('fast',function() {
				$("#question"+lastq).fadeIn();
				currentquestion = lastq;
				progress(startquestion,currentquestion-1,totalquestions);
				if (currentquestion === 0) {
					$(".back").fadeOut();
				};
			});
		//If not on the results page
		} else if (currentquestion > startquestion ) {
			previousQuestion = currentquestion - 1;
			//Transition to next question
			$("#question"+currentquestion).fadeOut('fast',function() {
				$("#question"+previousQuestion).fadeIn();
				currentquestion = previousQuestion;
				progress(startquestion,currentquestion-1,totalquestions);
				if (currentquestion === startquestion) {
					$(".back").fadeOut();
				};
			});
		};
		
		$(".forward").fadeIn();
	});
	$(".forward").click(function() {
		//If you were on the last question
		if ($("#question"+currentquestion).next().attr("id") === "showresults") {
			$("#question"+currentquestion).fadeOut('fast',function() {
				$("#showresults").fadeIn();
			});
			$(this).fadeOut();
			progress(startquestion,currentquestion,totalquestions);
			currentquestion += 1;
			
		//If you were NOT on the last question
		} else {
			newQuestion = currentquestion + 1;
			//Transition to next question
			$("#question"+currentquestion).fadeOut('fast',function() {
				$("#question"+newQuestion).fadeIn();
				progress(startquestion,currentquestion,totalquestions);
				currentquestion = newQuestion;
			});		
			$(".back").fadeIn();
		};
		
	});
	
	var progress = function progress(startq,currentq,totalq) {
		var prog = Math.round(100*((currentq-startq+1)/totalq));
		var questions_complete = currentq-startq+1
		var prog_string = prog+"%";
		console.log(prog_string);
		$(".progressbar .bar").css("width",prog_string);
		$(".progressbar .bar").html(prog_string+" complete ("+questions_complete+"/"+totalq+")");
	};
	
	$(".skipquestions").click(function() {
		submit('list');
	});
	$("#showresults a").click(function() {
		submit('list');
	});
	var submit = function(list) {
		var questionanswers = String(test.getallanswers()).replace(/,/g,"");
		var url= "findpackage?zipcode="+test.getzipcode()+"&prefs="+questionanswers;
		document.location.href = url;
	}

});