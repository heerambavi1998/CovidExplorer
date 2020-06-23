am4core.ready(function() {
  am4core.useTheme(am4themes_animated);
  var chart = am4core.create("chartdiv", am4charts.XYChart);
  chart.data = [
{"date": "2020-1-21","value":3},{"date": "2020-1-22","value":505},{"date": "2020-1-23","value":5173},{"date": "2020-1-24","value":16214},{"date": "2020-1-25","value":24903},{"date": "2020-1-26","value":25583},{"date": "2020-1-27","value":25041},{"date": "2020-1-28","value":31696},{"date": "2020-1-29","value":48064},{"date": "2020-1-30","value":70818},{"date": "2020-1-31","value":21246},{"date": "2020-2-01","value":38287},
{"date": "2020-2-02","value":65737},{"date": "2020-2-03","value":36334},{"date": "2020-2-04","value":35449},{"date": "2020-2-05","value":22576},{"date": "2020-2-06","value":28533},{"date": "2020-2-07","value":29337},{"date": "2020-2-08","value":25408},{"date": "2020-2-09","value":23413},{"date": "2020-2-10","value":25948},{"date": "2020-2-11","value":26211},{"date": "2020-2-12","value":24298},{"date": "2020-2-13","value":27741},{"date": "2020-2-14","value":32469},{"date": "2020-2-15","value":20106},{"date": "2020-2-16","value":21232},{"date": "2020-2-17","value":27830},{"date": "2020-2-18","value":28486},{"date": "2020-2-19","value":20808},{"date": "2020-2-20","value":26045},{"date": "2020-2-21","value":19461},{"date": "2020-2-22","value":17667},{"date": "2020-2-23","value":0},{"date": "2020-2-24","value":15279},{"date": "2020-2-25","value":12425},{"date": "2020-2-26","value":16928},{"date": "2020-2-27","value":28436},{"date": "2020-2-28","value":40402},{"date": "2020-2-29","value":74402},
{"date": "2020-3-01","value":67766},{"date": "2020-3-02","value":14302},{"date": "2020-3-03","value":127345},{"date": "2020-3-04","value":218699},{"date": "2020-3-05","value":35345},{"date": "2020-3-06","value":28707},{"date": "2020-3-07","value":24008},{"date": "2020-3-08","value":18595},{"date": "2020-3-09","value":20827},{"date": "2020-3-10","value":15608},{"date": "2020-3-11","value":17783},{"date": "2020-3-12","value":19345},{"date": "2020-3-13","value":21122},{"date": "2020-3-14","value":21596},{"date": "2020-3-15","value":22972},{"date": "2020-3-16","value":20886},{"date": "2020-3-17","value":22241},{"date": "2020-3-18","value":20529},{"date": "2020-3-19","value":30095},{"date": "2020-3-20","value":35442},{"date": "2020-3-21","value":40820},{"date": "2020-3-22","value":53951},{"date": "2020-3-23","value":45318},{"date": "2020-3-24","value":52711},{"date": "2020-3-25","value":52827},{"date": "2020-3-26","value":58504},{"date": "2020-3-27","value":55373},{"date": "2020-3-28","value":60082},{"date": "2020-3-29","value":56970},{"date": "2020-3-30","value":57738},{"date": "2020-3-31","value":60802},{"date": "2020-4-01","value":55827},
{"date": "2020-4-02","value":52856},{"date": "2020-4-03","value":55862},{"date": "2020-4-04","value":58635},{"date": "2020-4-05","value":62892},{"date": "2020-4-06","value":65300},{"date": "2020-4-07","value":65689},{"date": "2020-4-08","value":56542},{"date": "2020-4-09","value":58487},{"date": "2020-4-10","value":57368},{"date": "2020-4-11","value":61774},{"date": "2020-4-12","value":51893},{"date": "2020-4-13","value":50704},{"date": "2020-4-14","value":63250},{"date": "2020-4-15","value":50006},{"date": "2020-4-16","value":54829},{"date": "2020-4-17","value":44148},{"date": "2020-4-18","value":50732},{"date": "2020-4-19","value":56775},{"date": "2020-4-20","value":49495},{"date": "2020-4-21","value":52749},{"date": "2020-4-22","value":58349},{"date": "2020-4-23","value":50067},{"date": "2020-4-24","value":50107},{"date": "2020-4-25","value":58068},{"date": "2020-4-26","value":65015},{"date": "2020-4-27","value":53655},{"date": "2020-4-28","value":46169},{"date": "2020-4-29","value":43323},{"date": "2020-4-30","value":48607},{"date": "2020-5-01","value":52701},
{"date": "2020-5-02","value":55655},{"date": "2020-5-03","value":60729},{"date": "2020-5-04","value":56920},{"date": "2020-5-05","value":53042},{"date": "2020-5-06","value":65925},{"date": "2020-5-07","value":45745},{"date": "2020-5-08","value":70276},{"date": "2020-5-09","value":50281},{"date": "2020-5-10","value":44140},{"date": "2020-5-11","value":48945},{"date": "2020-5-12","value":40081},{"date": "2020-5-13","value":40432},{"date": "2020-5-14","value":39558},{"date": "2020-5-15","value":49458},{"date": "2020-5-16","value":60422},{"date": "2020-5-17","value":60959},{"date": "2020-5-18","value":58004},{"date": "2020-5-19","value":70073},{"date": "2020-5-20","value":54993},{"date": "2020-5-21","value":50360},{"date": "2020-5-22","value":60395},{"date": "2020-5-23","value":54759},{"date": "2020-5-24","value":54431},{"date": "2020-5-25","value":110072},{"date": "2020-5-26","value":56022},{"date": "2020-5-27","value":51275},{"date": "2020-5-28","value":47778},{"date": "2020-5-29","value":46341}
];
  chart.dateFormatter.inputDateFormat = "yyyy-MM-dd";
  var dateAxis = chart.xAxes.push(new am4charts.DateAxis());
  var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
  var series = chart.series.push(new am4charts.LineSeries());
  series.dataFields.valueY = "value";
  series.dataFields.dateX = "date";
  series.tooltipText = "{value}"
  series.strokeWidth = 2;
  series.minBulletDistance = 15;
  series.tooltip.background.cornerRadius = 20;
  series.tooltip.background.strokeOpacity = 0;
  series.tooltip.pointerOrientation = "vertical";
  series.tooltip.label.minWidth = 40;
  series.tooltip.label.minHeight = 40;
  series.tooltip.label.textAlign = "middle";
  series.tooltip.label.textValign = "middle";
  var bullet = series.bullets.push(new am4charts.CircleBullet());
  bullet.circle.strokeWidth = 2;
  bullet.circle.radius = 4;
  bullet.circle.fill = am4core.color("#fff");
  var bullethover = bullet.states.create("hover");
  bullethover.properties.scale = 1.3;
  chart.cursor = new am4charts.XYCursor();
  chart.cursor.behavior = "panXY";
  chart.cursor.xAxis = dateAxis;
  chart.cursor.snapToSeries = series;
  chart.scrollbarY = new am4core.Scrollbar();
  chart.scrollbarY.parent = chart.leftAxesContainer;
  chart.scrollbarY.toBack();
  chart.scrollbarX = new am4charts.XYChartScrollbar();
  chart.scrollbarX.series.push(series);
  chart.scrollbarX.parent = chart.bottomAxesContainer;
  dateAxis.start = 0.79;
  dateAxis.keepSelection = true;
  }); // end am4core.ready()