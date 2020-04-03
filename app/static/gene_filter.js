$(function(){
    $("button").click(function() {
    var keyword = document.getElementById("keyword").innerHTML;
    var type = document.getElementById("field").innerHTML;
    var years = year_filter.getValue();
    var fired_button = $(this).attr("value");
    alert(fired_button);
    $.get(
            url="/gene_filter",
            data={yr_s:years.slice(0,4),
                yr_e:years.slice(5,9),
                field:type,
                searchtext : keyword,
                gene: fired_button},
            success = function(data) {
                $( "#gene_filter_result" ).html(data);
            }
    );
    });
});

