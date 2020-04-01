
var keyword = document.getElementById("keyword").innerHTML;
// var yr_text = document.getElementById("years").innerHTML;
var d = new Date();
var curr_yr = d.getFullYear();
var type = document.getElementById("field").innerHTML;

// yr_text = yr_text.split(";");
// var years = Array.from(yr_text.split(";")).map(item => Number(item))


var year_filter = new rSlider({
    target: '#yr-slider',
    values: {min:1950, max:curr_yr},
    step: 1,
    range: true,
    tooltip: true,
    scale: true,
    labels: false,
    onChange: function (vals) {
        $.get(
            url="search",
            data={yr_s:vals.slice(0,4),
                yr_e:vals.slice(5,9),
                field_f:type,
                searchtext_f : keyword},
            success = function(data) {
                $( "#result" ).html(data);
            }
        )        
    }
});

var years = year_filter.getValue()