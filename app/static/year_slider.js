
var keyword = document.getElementById("keyword").innerHTML;
var d = new Date();
var curr_yr = d.getFullYear();
var type = document.getElementById("field").innerHTML;



var year_filter = new rSlider({
    target: '#yr-slider',
    values: {min:1957, max:curr_yr},
    step: 1,
    range: true,
    tooltip: true,
    scale: true,
    labels: false,
    onChange: function (vals) {
        $.get(
            url="/year_filter",
            data={yr_s:vals.slice(0,4),
                yr_e:vals.slice(5,9),
                field:type,
                searchtext : keyword},
            success = function(data) {
                $( "#result" ).html(data);
            }
        )        
    }
});

var years = year_filter.getValue()