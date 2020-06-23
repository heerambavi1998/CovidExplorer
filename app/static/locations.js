function loc_jan(){
    document.getElementById("loc_jan").classList.add("active")
    document.getElementById("loc_feb").classList.remove("active")
    document.getElementById("loc_mar").classList.remove("active")
    document.getElementById("loc_apr").classList.remove("active")
    document.getElementById("loc_may").classList.remove("active")
    am4core.useTheme(am4themes_animated);
    var chart = am4core.create("locations", am4maps.MapChart);
    var title = chart.titles.create();
    title.text = "[bold font-size: 20]Twitter Activity Distrubtion in India[/]";
    title.textAlign = "middle";

var mapData = [
{ "id":"IN-MH", "name":"Maharashtra", "value":5243, "color":chart.colors.getIndex(11) },
  { "id":"IN-UP", "name":"Uttar Pradesh", "value":4423, "color":chart.colors.getIndex(13) },
  { "id":"IN-GJ", "name":"Gujarat", "value":2558, "color": chart.colors.getIndex(10) },
  { "id":"IN-TG", "name":"Telangana", "value":5967, "color":chart.colors.getIndex(12) },
  { "id":"IN-JH", "name":"Jharkhand", "value":615, "color":chart.colors.getIndex(11) },
  { "id":"IN-AS", "name":"Assam", "value":811, "color": chart.colors.getIndex(10) },
  { "id":"IN-AP", "name":"Andhra Pradesh", "value":1476, "color":chart.colors.getIndex(11) },
  { "id":"IN-AR", "name":"Arunachal Pradesh", "value":34, "color":chart.colors.getIndex(12) },
  { "id":"IN-AN", "name":"Andaman and Nicobar Islands", "value":24, "color":chart.colors.getIndex(12) },
  { "id":"IN-BR", "name":"Bihar", "value":1627, "color":chart.colors.getIndex(12) },
  { "id":"IN-CH", "name":"Chandigarh", "value":2377, "color":chart.colors.getIndex(13) },
  { "id":"IN-CT", "name":"Chhattisgarh", "value":452, "color":chart.colors.getIndex(11) },
  //{ "id":"IN-DD", "name":"Daman and Diu", "value":22605732, "color":"#8aabb0" },
  { "id":"IN-DN", "name":"Dadra and Nagar Haveli", "value":16, "color":"#8aabb0" },
  { "id":"IN-DL", "name":"Delhi", "value":23778, "color":chart.colors.getIndex(11) },
  { "id":"IN-GA", "name":"Goa", "value":685, "color":chart.colors.getIndex(11) },
  { "id":"IN-HP", "name":"Himachal Pradesh", "value":261, "color": chart.colors.getIndex(10) },
  { "id":"IN-HR", "name":"Haryana", "value":1885, "color":chart.colors.getIndex(11) },
  { "id":"IN-JK", "name":"Jammu and Kashmir", "value":582, "color":chart.colors.getIndex(12) },
  { "id":"IN-KA", "name":"Karnataka", "value":6622, "color": chart.colors.getIndex(10) },
  { "id":"IN-KL", "name":"Kerela", "value":1747, "color":chart.colors.getIndex(13) },
  { "id":"IN-ML", "name":"Meghalaya", "value":88, "color":chart.colors.getIndex(12) },
  { "id":"IN-MN", "name":"Manipur", "value":142, "color":chart.colors.getIndex(13) },
  { "id":"IN-MP", "name":"Madhya Pradesh", "value":1570, "color": chart.colors.getIndex(10) },
  { "id":"IN-MZ", "name":"Mizoram", "value":127, "color":chart.colors.getIndex(11) },
  { "id":"IN-NL", "name":"Nagaland", "value":182, "color":chart.colors.getIndex(12) },
  { "id":"IN-OR", "name":"Odisha", "value":434, "color":chart.colors.getIndex(12) },
  { "id":"IN-PB", "name":"Punjab", "value":914, "color": chart.colors.getIndex(10) },
  { "id":"IN-PY", "name":"Puducherry", "value":174, "color": chart.colors.getIndex(10) },
  { "id":"IN-RJ", "name":"Rajasthan", "value":1659, "color":chart.colors.getIndex(12) },
  //{ "id":"IN-SK", "name":"Sikkim", "value":34349561, "color":chart.colors.getIndex(14) },
  { "id":"IN-TN", "name":"Tamil Nadu", "value":9530, "color":chart.colors.getIndex(12) },
  { "id":"IN-TR", "name":"Tripura", "value":200, "color":chart.colors.getIndex(12) },
  { "id":"IN-UT", "name":"Uttarakhand", "value":492, "color": chart.colors.getIndex(10) },
  { "id":"IN-WB", "name":"West Bengal", "value":3216, "color": chart.colors.getIndex(10) },
];

chart.geodata = am4geodata_indiaLow;
chart.projection = new am4maps.projections.Miller();
var polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());
polygonSeries.useGeodata = true;
polygonSeries.nonScalingStroke = true;
polygonSeries.strokeWidth = 0.5;
polygonSeries.calculateVisualCenter = true;
var imageSeries = chart.series.push(new am4maps.MapImageSeries());
imageSeries.data = mapData;
imageSeries.dataFields.value = "value";
var imageTemplate = imageSeries.mapImages.template;
imageTemplate.nonScaling = true
var circle = imageTemplate.createChild(am4core.Circle);
circle.fillOpacity = 0.7;
circle.propertyFields.fill = "color";
circle.tooltipText = "{name}: [bold]{value}[/]";
imageSeries.heatRules.push({
  "target": circle,
  "property": "radius",
  "min": 8,
  "max": 30,
  "dataField": "value",
})
imageTemplate.adapter.add("latitude", function(latitude, target) {
  var polygon = polygonSeries.getPolygonById(target.dataItem.dataContext.id);
  if(polygon){
    return polygon.visualLatitude;
   }
   return latitude;
})
imageTemplate.adapter.add("longitude", function(longitude, target) {
  var polygon = polygonSeries.getPolygonById(target.dataItem.dataContext.id);
  if(polygon){
    return polygon.visualLongitude;
   }
   return longitude;
})
}


function loc_feb(){
    document.getElementById("loc_jan").classList.remove("active")
    document.getElementById("loc_feb").classList.add("active")
    document.getElementById("loc_mar").classList.remove("active")
    document.getElementById("loc_apr").classList.remove("active")
    document.getElementById("loc_may").classList.remove("active")
    am4core.useTheme(am4themes_animated);
    var chart = am4core.create("locations", am4maps.MapChart);
    var title = chart.titles.create();
    title.text = "[bold font-size: 20]Twitter Activity Distrubtion in India[/]";
    title.textAlign = "middle";

var mapData = [
  { "id":"IN-AS", "name":"Assam", "value":104, "color": chart.colors.getIndex(10) },
  { "id":"IN-AP", "name":"Andhra Pradesh", "value":2340, "color":chart.colors.getIndex(11) },
  { "id":"IN-AR", "name":"Arunachal Pradesh", "value":104, "color":chart.colors.getIndex(12) },
  { "id":"IN-AN", "name":"Andaman and Nicobar Islands", "value":20, "color":chart.colors.getIndex(12) },
  { "id":"IN-BR", "name":"Bihar", "value":4279, "color":chart.colors.getIndex(12) },
  { "id":"IN-CH", "name":"Chandigarh", "value":5619, "color":chart.colors.getIndex(13) },
  { "id":"IN-CT", "name":"Chhattisgarh", "value":1668, "color":chart.colors.getIndex(11) },
  { "id":"IN-DN", "name":"Dadra and Nagar Haveli", "value":55, "color":"#8aabb0" },
  //{ "id":"IN-DD", "name":"Daman and Diu", "value":22605732, "color":"#8aabb0" },
  { "id":"IN-DL", "name":"Delhi", "value":56160, "color":chart.colors.getIndex(11) },
  { "id":"IN-GA", "name":"Goa", "value":1584, "color":chart.colors.getIndex(11) },
  { "id":"IN-HP", "name":"Himachal Pradesh", "value":1423, "color": chart.colors.getIndex(10) },
  { "id":"IN-GJ", "name":"Gujarat", "value":6720, "color": chart.colors.getIndex(10) },
  { "id":"IN-HR", "name":"Haryana", "value":12206, "color":chart.colors.getIndex(11) },
  { "id":"IN-JH", "name":"Jharkhand", "value":1563, "color":chart.colors.getIndex(11) },
  { "id":"IN-JK", "name":"Jammu and Kashmir", "value":1405, "color":chart.colors.getIndex(12) },
  { "id":"IN-KA", "name":"Karnataka", "value":15487, "color": chart.colors.getIndex(10) },
  { "id":"IN-KL", "name":"Kerela", "value":3061, "color":chart.colors.getIndex(13) },
  { "id":"IN-MH", "name":"Maharashtra", "value":13729, "color":chart.colors.getIndex(11) },
  { "id":"IN-ML", "name":"Meghalaya", "value":109, "color":chart.colors.getIndex(12) },
  { "id":"IN-MN", "name":"Manipur", "value":301, "color":chart.colors.getIndex(13) },
  { "id":"IN-MP", "name":"Madhya Pradesh", "value":5919, "color": chart.colors.getIndex(10) },
  { "id":"IN-MZ", "name":"Mizoram", "value":271, "color":chart.colors.getIndex(11) },
  { "id":"IN-NL", "name":"Nagaland", "value":332, "color":chart.colors.getIndex(12) },
  { "id":"IN-OR", "name":"Odisha", "value":1088, "color":chart.colors.getIndex(12) },
  { "id":"IN-PB", "name":"Punjab", "value":2451, "color": chart.colors.getIndex(10) },
  { "id":"IN-PY", "name":"Puducherry", "value":325, "color": chart.colors.getIndex(10) },
  { "id":"IN-RJ", "name":"Rajasthan", "value":5334, "color":chart.colors.getIndex(12) },
  //{ "id":"IN-SK", "name":"Sikkim", "value":34349561, "color":chart.colors.getIndex(14) },
  { "id":"IN-TG", "name":"Telangana", "value":12798, "color":chart.colors.getIndex(12) },
  { "id":"IN-TN", "name":"Tamil Nadu", "value":17762, "color":chart.colors.getIndex(12) },
  { "id":"IN-TR", "name":"Tripura", "value":624, "color":chart.colors.getIndex(12) },
  { "id":"IN-UP", "name":"Uttar Pradesh", "value":11419, "color":chart.colors.getIndex(13) },
  { "id":"IN-UT", "name":"Uttarakhand", "value":1671, "color": chart.colors.getIndex(10) },
  { "id":"IN-WB", "name":"West Bengal", "value":7387, "color": chart.colors.getIndex(10) },
];

chart.geodata = am4geodata_indiaLow;
chart.projection = new am4maps.projections.Miller();
var polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());
polygonSeries.useGeodata = true;
polygonSeries.nonScalingStroke = true;
polygonSeries.strokeWidth = 0.5;
polygonSeries.calculateVisualCenter = true;
var imageSeries = chart.series.push(new am4maps.MapImageSeries());
imageSeries.data = mapData;
imageSeries.dataFields.value = "value";
var imageTemplate = imageSeries.mapImages.template;
imageTemplate.nonScaling = true
var circle = imageTemplate.createChild(am4core.Circle);
circle.fillOpacity = 0.7;
circle.propertyFields.fill = "color";
circle.tooltipText = "{name}: [bold]{value}[/]";
imageSeries.heatRules.push({
  "target": circle,
  "property": "radius",
  "min": 8,
  "max": 30,
  "dataField": "value",
})
imageTemplate.adapter.add("latitude", function(latitude, target) {
  var polygon = polygonSeries.getPolygonById(target.dataItem.dataContext.id);
  if(polygon){
    return polygon.visualLatitude;
   }
   return latitude;
})
imageTemplate.adapter.add("longitude", function(longitude, target) {
  var polygon = polygonSeries.getPolygonById(target.dataItem.dataContext.id);
  if(polygon){
    return polygon.visualLongitude;
   }
   return longitude;
})
  }

function loc_mar(){
    document.getElementById("loc_jan").classList.remove("active")
    document.getElementById("loc_feb").classList.remove("active")
    document.getElementById("loc_mar").classList.add("active")
    document.getElementById("loc_apr").classList.remove("active")
    document.getElementById("loc_may").classList.remove("active")
    am4core.useTheme(am4themes_animated);
var chart = am4core.create("locations", am4maps.MapChart);
var title = chart.titles.create();
title.text = "[bold font-size: 20]Twitter Activity Distrubtion in India[/]";
title.textAlign = "middle";

var mapData = [
  { "id":"IN-AS", "name":"Assam", "value":3833, "color": chart.colors.getIndex(10) },
  { "id":"IN-AP", "name":"Andhra Pradesh", "value":10713, "color":chart.colors.getIndex(11) },
  { "id":"IN-AR", "name":"Arunachal Pradesh", "value":121, "color":chart.colors.getIndex(12) },
  { "id":"IN-AN", "name":"Andaman and Nicobar Islands", "value":67, "color":chart.colors.getIndex(12) },
  { "id":"IN-BR", "name":"Bihar", "value":10932, "color":chart.colors.getIndex(12) },
  { "id":"IN-CH", "name":"Chandigarh", "value":9185, "color":chart.colors.getIndex(13) },
  { "id":"IN-CT", "name":"Chhattisgarh", "value":2478, "color":chart.colors.getIndex(11) },
  { "id":"IN-DN", "name":"Dadra and Nagar Haveli", "value":123, "color":"#8aabb0" },
  //{ "id":"IN-DD", "name":"Daman and Diu", "value":22605732, "color":"#8aabb0" },
  { "id":"IN-DL", "name":"Delhi", "value":109463, "color":chart.colors.getIndex(11) },
  { "id":"IN-GA", "name":"Goa", "value":2827, "color":chart.colors.getIndex(11) },
  { "id":"IN-HP", "name":"Himachal Pradesh", "value":1786, "color": chart.colors.getIndex(10) },
  { "id":"IN-GJ", "name":"Gujarat", "value":16498, "color": chart.colors.getIndex(10) },
  { "id":"IN-HR", "name":"Haryana", "value":14499, "color":chart.colors.getIndex(11) },
  { "id":"IN-JH", "name":"Jharkhand", "value":3553, "color":chart.colors.getIndex(11) },
  { "id":"IN-JK", "name":"Jammu and Kashmir", "value":5009, "color":chart.colors.getIndex(12) },
  { "id":"IN-KA", "name":"Karnataka", "value":31929, "color": chart.colors.getIndex(10) },
  { "id":"IN-KL", "name":"Kerela", "value":4926, "color":chart.colors.getIndex(13) },
  { "id":"IN-MH", "name":"Maharashtra", "value":29842, "color":chart.colors.getIndex(11) },
  { "id":"IN-ML", "name":"Meghalaya", "value":194, "color":chart.colors.getIndex(12) },
  { "id":"IN-MN", "name":"Manipur", "value":416, "color":chart.colors.getIndex(13) },
  { "id":"IN-MP", "name":"Madhya Pradesh", "value":10444, "color": chart.colors.getIndex(10) },
  { "id":"IN-MZ", "name":"Mizoram", "value":286, "color":chart.colors.getIndex(11) },
  { "id":"IN-NL", "name":"Nagaland", "value":495, "color":chart.colors.getIndex(12) },
  { "id":"IN-OR", "name":"Odisha", "value":2779, "color":chart.colors.getIndex(12) },
  { "id":"IN-PB", "name":"Punjab", "value":5934, "color": chart.colors.getIndex(10) },
  { "id":"IN-PY", "name":"Puducherry", "value":906, "color": chart.colors.getIndex(10) },
  { "id":"IN-RJ", "name":"Rajasthan", "value":12575, "color":chart.colors.getIndex(12) },
  //{ "id":"IN-SK", "name":"Sikkim", "value":34349561, "color":chart.colors.getIndex(14) },
  { "id":"IN-TG", "name":"Telangana", "value":34366, "color":chart.colors.getIndex(12) },
  { "id":"IN-TN", "name":"Tamil Nadu", "value":33705, "color":chart.colors.getIndex(12) },
  { "id":"IN-TR", "name":"Tripura", "value":1145, "color":chart.colors.getIndex(12) },
  { "id":"IN-UP", "name":"Uttar Pradesh", "value":26384, "color":chart.colors.getIndex(13) },
  { "id":"IN-UT", "name":"Uttarakhand", "value":4296, "color": chart.colors.getIndex(10) },
  { "id":"IN-WB", "name":"West Bengal", "value":14607, "color": chart.colors.getIndex(10) },
];

chart.geodata = am4geodata_indiaLow;
chart.projection = new am4maps.projections.Miller();
var polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());
polygonSeries.useGeodata = true;
polygonSeries.nonScalingStroke = true;
polygonSeries.strokeWidth = 0.5;
polygonSeries.calculateVisualCenter = true;
var imageSeries = chart.series.push(new am4maps.MapImageSeries());
imageSeries.data = mapData;
imageSeries.dataFields.value = "value";
var imageTemplate = imageSeries.mapImages.template;
imageTemplate.nonScaling = true
var circle = imageTemplate.createChild(am4core.Circle);
circle.fillOpacity = 0.7;
circle.propertyFields.fill = "color";
circle.tooltipText = "{name}: [bold]{value}[/]";
imageSeries.heatRules.push({
  "target": circle,
  "property": "radius",
  "min": 8,
  "max": 30,
  "dataField": "value",
})
imageTemplate.adapter.add("latitude", function(latitude, target) {
  var polygon = polygonSeries.getPolygonById(target.dataItem.dataContext.id);
  if(polygon){
    return polygon.visualLatitude;
   }
   return latitude;
})
imageTemplate.adapter.add("longitude", function(longitude, target) {
  var polygon = polygonSeries.getPolygonById(target.dataItem.dataContext.id);
  if(polygon){
    return polygon.visualLongitude;
   }
   return longitude;
})
  }

function loc_apr(){
    document.getElementById("loc_jan").classList.remove("active")
    document.getElementById("loc_feb").classList.remove("active")
    document.getElementById("loc_mar").classList.remove("active")
    document.getElementById("loc_apr").classList.add("active")
    document.getElementById("loc_may").classList.remove("active")
    am4core.useTheme(am4themes_animated);
var chart = am4core.create("locations", am4maps.MapChart);
var title = chart.titles.create();
title.text = "[bold font-size: 20]Twitter Activity Distrubtion in India[/]";
title.textAlign = "middle";

var mapData = [
  { "id":"IN-AS", "name":"Assam", "value":6541, "color": chart.colors.getIndex(10) },
  { "id":"IN-AP", "name":"Andhra Pradesh", "value":10852, "color":chart.colors.getIndex(11) },
  { "id":"IN-AR", "name":"Arunachal Pradesh", "value":82, "color":chart.colors.getIndex(12) },
  { "id":"IN-AN", "name":"Andaman and Nicobar Islands", "value":20, "color":chart.colors.getIndex(12) },
  { "id":"IN-BR", "name":"Bihar", "value":16020, "color":chart.colors.getIndex(12) },
  { "id":"IN-CH", "name":"Chandigarh", "value":13087, "color":chart.colors.getIndex(13) },
  { "id":"IN-CT", "name":"Chhattisgarh", "value":4282, "color":chart.colors.getIndex(11) },
  { "id":"IN-DN", "name":"Dadra and Nagar Haveli", "value":112, "color":"#8aabb0" },
  //{ "id":"IN-DD", "name":"Daman and Diu", "value":22605732, "color":"#8aabb0" },
  { "id":"IN-DL", "name":"Delhi", "value":131945, "color":chart.colors.getIndex(11) },
  { "id":"IN-GA", "name":"Goa", "value":3400, "color":chart.colors.getIndex(11) },
  { "id":"IN-HP", "name":"Himachal Pradesh", "value":2164, "color": chart.colors.getIndex(10) },
  { "id":"IN-GJ", "name":"Gujarat", "value":22264, "color": chart.colors.getIndex(10) },
  { "id":"IN-HR", "name":"Haryana", "value":17684, "color":chart.colors.getIndex(11) },
  { "id":"IN-JH", "name":"Jharkhand", "value":5873, "color":chart.colors.getIndex(11) },
  { "id":"IN-JK", "name":"Jammu and Kashmir", "value":7258, "color":chart.colors.getIndex(12) },
  { "id":"IN-KA", "name":"Karnataka", "value":36575, "color": chart.colors.getIndex(10) },
  { "id":"IN-KL", "name":"Kerela", "value":5793, "color":chart.colors.getIndex(13) },
  { "id":"IN-MH", "name":"Maharashtra", "value":39050, "color":chart.colors.getIndex(11) },
  { "id":"IN-ML", "name":"Meghalaya", "value":384, "color":chart.colors.getIndex(12) },
  { "id":"IN-MN", "name":"Manipur", "value":510, "color":chart.colors.getIndex(13) },
  { "id":"IN-MP", "name":"Madhya Pradesh", "value":14238, "color": chart.colors.getIndex(10) },
  { "id":"IN-MZ", "name":"Mizoram", "value":278, "color":chart.colors.getIndex(11) },
  { "id":"IN-NL", "name":"Nagaland", "value":717, "color":chart.colors.getIndex(12) },
  { "id":"IN-OR", "name":"Odisha", "value":4805, "color":chart.colors.getIndex(12) },
  { "id":"IN-PB", "name":"Punjab", "value":9235, "color": chart.colors.getIndex(10) },
  { "id":"IN-PY", "name":"Puducherry", "value":1574, "color": chart.colors.getIndex(10) },
  { "id":"IN-RJ", "name":"Rajasthan", "value":17865, "color":chart.colors.getIndex(12) },
  //{ "id":"IN-SK", "name":"Sikkim", "value":34349561, "color":chart.colors.getIndex(14) },
  { "id":"IN-TG", "name":"Telangana", "value":37763, "color":chart.colors.getIndex(12) },
  { "id":"IN-TN", "name":"Tamil Nadu", "value":42070, "color":chart.colors.getIndex(12) },
  { "id":"IN-TR", "name":"Tripura", "value":1742, "color":chart.colors.getIndex(12) },
  { "id":"IN-UP", "name":"Uttar Pradesh", "value":37034, "color":chart.colors.getIndex(13) },
  { "id":"IN-UT", "name":"Uttarakhand", "value":5714, "color": chart.colors.getIndex(10) },
  { "id":"IN-WB", "name":"West Bengal", "value":21031, "color": chart.colors.getIndex(10) },
];

chart.geodata = am4geodata_indiaLow;
chart.projection = new am4maps.projections.Miller();
var polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());
polygonSeries.useGeodata = true;
polygonSeries.nonScalingStroke = true;
polygonSeries.strokeWidth = 0.5;
polygonSeries.calculateVisualCenter = true;
var imageSeries = chart.series.push(new am4maps.MapImageSeries());
imageSeries.data = mapData;
imageSeries.dataFields.value = "value";
var imageTemplate = imageSeries.mapImages.template;
imageTemplate.nonScaling = true
var circle = imageTemplate.createChild(am4core.Circle);
circle.fillOpacity = 0.7;
circle.propertyFields.fill = "color";
circle.tooltipText = "{name}: [bold]{value}[/]";
imageSeries.heatRules.push({
  "target": circle,
  "property": "radius",
  "min": 8,
  "max": 30,
  "dataField": "value",
})
imageTemplate.adapter.add("latitude", function(latitude, target) {
  var polygon = polygonSeries.getPolygonById(target.dataItem.dataContext.id);
  if(polygon){
    return polygon.visualLatitude;
   }
   return latitude;
})
imageTemplate.adapter.add("longitude", function(longitude, target) {
  var polygon = polygonSeries.getPolygonById(target.dataItem.dataContext.id);
  if(polygon){
    return polygon.visualLongitude;
   }
   return longitude;
})
}


function loc_may(){
  document.getElementById("loc_jan").classList.remove("active")
  document.getElementById("loc_feb").classList.remove("active")
  document.getElementById("loc_mar").classList.remove("active")
  document.getElementById("loc_apr").classList.remove("active")
  document.getElementById("loc_may").classList.add("active")
  am4core.useTheme(am4themes_animated);
var chart = am4core.create("locations", am4maps.MapChart);
var title = chart.titles.create();
title.text = "[bold font-size: 20]Twitter Activity Distrubtion in India[/]";
title.textAlign = "middle";

var mapData = [
{ "id":"IN-AS", "name":"Assam", "value":8162, "color": chart.colors.getIndex(10) },
{ "id":"IN-AP", "name":"Andhra Pradesh", "value":11010, "color":chart.colors.getIndex(11) },
{ "id":"IN-AR", "name":"Arunachal Pradesh", "value":104, "color":chart.colors.getIndex(12) },
{ "id":"IN-AN", "name":"Andaman and Nicobar Islands", "value":54, "color":chart.colors.getIndex(12) },
{ "id":"IN-BR", "name":"Bihar", "value":15433, "color":chart.colors.getIndex(12) },
{ "id":"IN-CH", "name":"Chandigarh", "value":13857, "color":chart.colors.getIndex(13) },
{ "id":"IN-CT", "name":"Chhattisgarh", "value":4168, "color":chart.colors.getIndex(11) },
{ "id":"IN-DN", "name":"Dadra and Nagar Haveli", "value":122, "color":"#8aabb0" },
//{ "id":"IN-DD", "name":"Daman and Diu", "value":22605732, "color":"#8aabb0" },
{ "id":"IN-DL", "name":"Delhi", "value":124311, "color":chart.colors.getIndex(11) },
{ "id":"IN-GA", "name":"Goa", "value":3530, "color":chart.colors.getIndex(11) },
{ "id":"IN-HP", "name":"Himachal Pradesh", "value":1678, "color": chart.colors.getIndex(10) },
{ "id":"IN-GJ", "name":"Gujarat", "value":20159, "color": chart.colors.getIndex(10) },
{ "id":"IN-HR", "name":"Haryana", "value":15218, "color":chart.colors.getIndex(11) },
{ "id":"IN-JH", "name":"Jharkhand", "value":5513, "color":chart.colors.getIndex(11) },
{ "id":"IN-JK", "name":"Jammu and Kashmir", "value":5550, "color":chart.colors.getIndex(12) },
{ "id":"IN-KA", "name":"Karnataka", "value":32913, "color": chart.colors.getIndex(10) },
{ "id":"IN-KL", "name":"Kerela", "value":5530, "color":chart.colors.getIndex(13) },
{ "id":"IN-MH", "name":"Maharashtra", "value":38212, "color":chart.colors.getIndex(11) },
{ "id":"IN-ML", "name":"Meghalaya", "value":375, "color":chart.colors.getIndex(12) },
{ "id":"IN-MN", "name":"Manipur", "value":554, "color":chart.colors.getIndex(13) },
{ "id":"IN-MP", "name":"Madhya Pradesh", "value":14796, "color": chart.colors.getIndex(10) },
{ "id":"IN-MZ", "name":"Mizoram", "value":269, "color":chart.colors.getIndex(11) },
{ "id":"IN-NL", "name":"Nagaland", "value":797, "color":chart.colors.getIndex(12) },
{ "id":"IN-OR", "name":"Odisha", "value":3943, "color":chart.colors.getIndex(12) },
{ "id":"IN-PB", "name":"Punjab", "value":11021, "color": chart.colors.getIndex(10) },
{ "id":"IN-PY", "name":"Puducherry", "value":1170, "color": chart.colors.getIndex(10) },
{ "id":"IN-RJ", "name":"Rajasthan", "value":17324, "color":chart.colors.getIndex(12) },
//{ "id":"IN-SK", "name":"Sikkim", "value":34349561, "color":chart.colors.getIndex(14) },
{ "id":"IN-TG", "name":"Telangana", "value":33306, "color":chart.colors.getIndex(12) },
{ "id":"IN-TN", "name":"Tamil Nadu", "value":34213, "color":chart.colors.getIndex(12) },
{ "id":"IN-TR", "name":"Tripura", "value":2303, "color":chart.colors.getIndex(12) },
{ "id":"IN-UP", "name":"Uttar Pradesh", "value":34501, "color":chart.colors.getIndex(13) },
{ "id":"IN-UT", "name":"Uttarakhand", "value":4352, "color": chart.colors.getIndex(10) },
{ "id":"IN-WB", "name":"West Bengal", "value":21165, "color": chart.colors.getIndex(10) },
];

chart.geodata = am4geodata_indiaLow;
chart.projection = new am4maps.projections.Miller();
var polygonSeries = chart.series.push(new am4maps.MapPolygonSeries());
polygonSeries.useGeodata = true;
polygonSeries.nonScalingStroke = true;
polygonSeries.strokeWidth = 0.5;
polygonSeries.calculateVisualCenter = true;
var imageSeries = chart.series.push(new am4maps.MapImageSeries());
imageSeries.data = mapData;
imageSeries.dataFields.value = "value";
var imageTemplate = imageSeries.mapImages.template;
imageTemplate.nonScaling = true
var circle = imageTemplate.createChild(am4core.Circle);
circle.fillOpacity = 0.7;
circle.propertyFields.fill = "color";
circle.tooltipText = "{name}: [bold]{value}[/]";
imageSeries.heatRules.push({
"target": circle,
"property": "radius",
"min": 8,
"max": 30,
"dataField": "value",
})
imageTemplate.adapter.add("latitude", function(latitude, target) {
var polygon = polygonSeries.getPolygonById(target.dataItem.dataContext.id);
if(polygon){
  return polygon.visualLatitude;
 }
 return latitude;
})
imageTemplate.adapter.add("longitude", function(longitude, target) {
var polygon = polygonSeries.getPolygonById(target.dataItem.dataContext.id);
if(polygon){
  return polygon.visualLongitude;
 }
 return longitude;
})
}