function LDA_jan(){
    am4core.useTheme(am4themes_animated);
  
  // Create chart instance
  var chart = am4core.create("LDA", am4charts.PieChart);
  
  // Add data
  chart.data = [
  {'topic': 11,'occurance': 22219},{'topic': 12,'occurance': 20913},{'topic': 15,'occurance': 20424},{'topic': 7,'occurance': 19063},{'topic': 0,'occurance': 18895},
  {'topic': 5,'occurance': 18692},{'topic': 19,'occurance': 18327},{'topic': 16,'occurance': 17863},{'topic': 8,'occurance': 16925},{'topic': 1,'occurance': 16606},
  {'topic': 4,'occurance': 16138},{'topic': 6,'occurance': 16057},{'topic': 10,'occurance': 15849},{'topic': 9,'occurance': 15020},{'topic': 17,'occurance': 14995},
  {'topic': 3,'occurance': 14714},{'topic': 2,'occurance': 14588},{'topic': 14,'occurance': 13304},{'topic': 13,'occurance': 11820},{'topic': 18,'occurance': 8616},
];

  
  // Add and configure Series
  var pieSeries = chart.series.push(new am4charts.PieSeries());
  pieSeries.dataFields.value = "occurance";
  pieSeries.dataFields.category = "topic";
  chart.innerRadius = am4core.percent(20);
  pieSeries.slices.template.stroke = am4core.color("#4a2abb");
pieSeries.slices.template.strokeWidth = 2;
pieSeries.slices.template.strokeOpacity = 1;
  
  pieSeries.slices.template.events.on("hit", function(ev) {
    var series = ev.target.dataItem.component;
    series.slices.each(function(item) {
      if (item.isActive && item != ev.target) {
        item.isActive = false;
      }
    })
  });
  }


  function LDA_feb(){
    am4core.useTheme(am4themes_animated);
  
  // Create chart instance
  var chart = am4core.create("LDA", am4charts.PieChart);
  
  // Add data
  chart.data = [
  {'topic': 16,'occurance': 72112},{'topic': 10,'occurance': 67755},{'topic': 11,'occurance': 67162},{'topic': 12,'occurance': 59118},{'topic': 9,'occurance': 53993},
  {'topic': 15,'occurance': 47927},{'topic': 17,'occurance': 40797},{'topic': 2,'occurance': 40735},{'topic': 14,'occurance': 40158},{'topic': 7,'occurance': 38299},
  {'topic': 4,'occurance': 37524},{'topic': 18,'occurance': 35972},{'topic': 13,'occurance': 33628},{'topic': 3,'occurance': 31313},{'topic': 0,'occurance': 29471},
  {'topic': 1,'occurance': 27803},{'topic': 19,'occurance': 26808},{'topic': 5,'occurance': 22183},{'topic': 8,'occurance': 19876},{'topic': 6,'occurance': 18613}
];
  
  // Add and configure Series
  var pieSeries = chart.series.push(new am4charts.PieSeries());
  pieSeries.dataFields.value = "occurance";
  pieSeries.dataFields.category = "topic";
  
  pieSeries.slices.template.events.on("hit", function(ev) {
    var series = ev.target.dataItem.component;
    series.slices.each(function(item) {
      if (item.isActive && item != ev.target) {
        item.isActive = false;
      }
    })
  });
  }


  function LDA_mar(){
    am4core.useTheme(am4themes_animated);
  
  // Create chart instance
  var chart = am4core.create("LDA", am4charts.PieChart);
  
  // Add data
  chart.data = [
  {'topic': 2,'occurance': 127597},{'topic': 13,'occurance': 101327},{'topic': 9,'occurance': 89452},{'topic': 3,'occurance': 88715},{'topic': 7,'occurance': 80234},
  {'topic': 11,'occurance': 79860},{'topic': 17,'occurance': 77428},{'topic': 16,'occurance': 76749},{'topic': 14,'occurance': 72145},{'topic': 8,'occurance': 64554},
  {'topic': 15,'occurance': 64050},{'topic': 1,'occurance': 63524},{'topic': 18,'occurance': 62596},{'topic': 12,'occurance': 62493},{'topic': 19,'occurance': 58555},
  {'topic': 10,'occurance': 56253},{'topic': 6,'occurance': 55323},{'topic': 5,'occurance': 49338},{'topic': 0,'occurance': 46608},{'topic': 4,'occurance': 21507}
];
  
  // Add and configure Series
  var pieSeries = chart.series.push(new am4charts.PieSeries());
  pieSeries.dataFields.value = "occurance";
  pieSeries.dataFields.category = "topic";
  
  pieSeries.slices.template.events.on("hit", function(ev) {
    var series = ev.target.dataItem.component;
    series.slices.each(function(item) {
      if (item.isActive && item != ev.target) {
        item.isActive = false;
      }
    })
  });
  }


  function LDA_apr(){
    am4core.useTheme(am4themes_animated);
  
  // Create chart instance
  var chart = am4core.create("LDA", am4charts.PieChart);
  
  // Add data
  chart.data = [
  {'topic': 10,'occurance': 119676},{'topic': 3,'occurance': 114825},{'topic': 16,'occurance': 110578},{'topic': 14,'occurance': 102977},{'topic': 19,'occurance': 101389},
  {'topic': 15,'occurance': 99314},{'topic': 11,'occurance': 95570},{'topic': 2,'occurance': 93748},{'topic': 5,'occurance': 88943},{'topic': 1,'occurance': 83595},
  {'topic': 7,'occurance': 82867},{'topic': 13,'occurance': 78240},{'topic': 4,'occurance': 73914},{'topic': 9,'occurance': 64576},{'topic': 8,'occurance': 62954},
  {'topic': 0,'occurance': 58077},{'topic': 17,'occurance': 57996},{'topic': 12,'occurance': 56985},{'topic': 18,'occurance': 51875},{'topic': 6,'occurance': 51073}
];
  
  // Add and configure Series
  var pieSeries = chart.series.push(new am4charts.PieSeries());
  pieSeries.dataFields.value = "occurance";
  pieSeries.dataFields.category = "topic";
  
  pieSeries.slices.template.events.on("hit", function(ev) {
    var series = ev.target.dataItem.component;
    series.slices.each(function(item) {
      if (item.isActive && item != ev.target) {
        item.isActive = false;
      }
    })
  });
  }


  function LDA_may(){
    am4core.useTheme(am4themes_animated);
  
  // Create chart instance
  var chart = am4core.create("LDA", am4charts.PieChart);
  
  // Add data
  chart.data = [
  {'topic': 7,'occurance': 150183},{'topic': 15,'occurance': 107732},{'topic': 0,'occurance': 107049},{'topic': 1,'occurance': 103587},{'topic': 10,'occurance': 98228},
  {'topic': 3,'occurance': 94989},{'topic': 14,'occurance': 91394},{'topic': 11,'occurance': 90402},{'topic': 16,'occurance': 87932},{'topic': 8,'occurance': 85329},
  {'topic': 4,'occurance': 83504},{'topic': 17,'occurance': 80372},{'topic': 5,'occurance': 76151},{'topic': 6,'occurance': 61474},{'topic': 9,'occurance': 57316},
  {'topic': 2,'occurance': 53287},{'topic': 12,'occurance': 50831},{'topic': 19,'occurance': 50791},{'topic': 13,'occurance': 48132},{'topic': 18,'occurance': 31088}
];
  
  // Add and configure Series
  var pieSeries = chart.series.push(new am4charts.PieSeries());
  pieSeries.dataFields.value = "occurance";
  pieSeries.dataFields.category = "topic";
  
  pieSeries.slices.template.events.on("hit", function(ev) {
    var series = ev.target.dataItem.component;
    series.slices.each(function(item) {
      if (item.isActive && item != ev.target) {
        item.isActive = false;
      }
    })
  });
  }