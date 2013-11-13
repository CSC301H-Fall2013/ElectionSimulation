var totalCandidate = 0;
$(document).ready(function() {
	$("#span_add_candidate").click(addCandidate);
	$("#candidate_count").val(0);
});

function replaceAll(pattern, replaceWith, theString){
    while(theString.indexOf(pattern) >= 0){
        theString = theString.replace(pattern, replaceWith);
    }
    return theString;
}

function removeCandidate(itemID){
    candiate_index = $("#" + itemID).attr("tag");
    $("#candiate_" + candiate_index).remove();
}

function addCandidate(){
    candidate_form_template =  $("#candidate_template").html();
    candidate_form_template = replaceAll("\$index\$", totalCandidate, candidate_form_template);
    $("#list_cadidates").html($("#list_cadidates").html() + candidate_form_template);
    $("#span_remove_candidate_" + totalCandidate).click(function() {
        $( this ).slideUp();
    });
    totalCandidate = totalCandidate + 1;
    $("#candidate_count").val(totalCandidate);
}