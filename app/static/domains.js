function domain_jan(){
    document.getElementById("dom_jan").classList.add("active")
    document.getElementById("dom_feb").classList.remove("active")
    document.getElementById("dom_mar").classList.remove("active")
    document.getElementById("dom_apr").classList.remove("active")
    document.getElementById("dom_may").classList.remove("active")
    am4core.useTheme(am4themes_animated);
    var chart = am4core.create("domains", am4plugins_wordCloud.WordCloud);
    var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());
    series.data = [{
      "tag": "toi",
      "weight": 1924
    }, {
      "tag": "cnn",
      "weight": 1886
    }, {
      "tag": "youtube",
      "weight": 1791
    }, {
      "tag": "dlvr.it",
      "weight": 1783
    }, {
      "tag": "reuters",
      "weight": 1448
    }, {
      "tag": "ndtv",
      "weight": 1195
    }, {
      "tag": "indiatimes",
      "weight": 1166
    }];
    series.labels.template.tooltipText = "{word}:\n[bold]{value}[/]";
    series.dataFields.word = "tag";
    series.dataFields.value = "weight";
  }

function domain_feb(){
    document.getElementById("dom_jan").classList.remove("active")
    document.getElementById("dom_feb").classList.add("active")
    document.getElementById("dom_mar").classList.remove("active")
    document.getElementById("dom_apr").classList.remove("active")
    document.getElementById("dom_may").classList.remove("active")
    am4core.useTheme(am4themes_animated);
    var chart = am4core.create("domains", am4plugins_wordCloud.WordCloud);
    var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());
    series.data = [
    {
      "tag": "dlvr.it",
      "weight": 4177
    }, {
      "tag": "toi",
      "weight": 3691
    }, {
      "tag": "youtube",
      "weight": 3634
    }, {
      "tag": "indiatimes",
      "weight": 3333
    }, {
      "tag": "ift",
      "weight": 2443
    }, {
      "tag": "reut",
      "weight": 2414
    }, {
      "tag": "hindustantimes",
      "weight": 2410
    }, {
      "tag": "ndtv",
      "weight": 2112
    }];
    series.labels.template.tooltipText = "{word}:\n[bold]{value}[/]";
    series.dataFields.word = "tag";
    series.dataFields.value = "weight";
  }

function domain_mar(){
    document.getElementById("dom_jan").classList.remove("active")
    document.getElementById("dom_feb").classList.remove("active")
    document.getElementById("dom_mar").classList.add("active")
    document.getElementById("dom_apr").classList.remove("active")
    document.getElementById("dom_may").classList.remove("active")
    am4core.useTheme(am4themes_animated);
    var chart = am4core.create("domains", am4plugins_wordCloud.WordCloud);
    var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());
    series.data = [
       {
      "tag": "youtube",
      "weight": 4440
    }, {
      "tag": "toi",
      "weight": 3698
    }, {
      "tag": "indiatimes",
      "weight": 3160
    }, {
      "tag": "hindustantimes",
      "weight": 3131
    }, {
      "tag": "ndtv",
      "weight": 2921
    }, {
      "tag": "dlvr.it",
      "weight": 2481
    }, {
      "tag": "bbc",
      "weight": 2379
    }, {
      "tag": "indiatoday",
      "weight": 1610
    }, {
      "tag": "republicworld",
      "weight": 2302
    }, {
      "tag": "indiatoday",
      "weight": 2285
    }];
    series.labels.template.tooltipText = "{word}:\n[bold]{value}[/]";
    series.dataFields.word = "tag";
    series.dataFields.value = "weight";
  }

function domain_apr(){
    document.getElementById("dom_jan").classList.remove("active")
    document.getElementById("dom_feb").classList.remove("active")
    document.getElementById("dom_mar").classList.remove("active")
    document.getElementById("dom_apr").classList.add("active")
    document.getElementById("dom_may").classList.remove("active")
    am4core.useTheme(am4themes_animated);
    var chart = am4core.create("domains", am4plugins_wordCloud.WordCloud);
    var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());
    series.data = [{
      "tag": "youtube",
      "weight": 7631
    }, {
      "tag": "ndtv",
      "weight": 5333
    }, {
      "tag": "indiatimes",
      "weight": 4525
    }, {
      "tag": "instagram",
      "weight": 4028
    }, {
      "tag": "republicworld",
      "weight": 3669
    }, {
      "tag": "toi",
      "weight": 3288
    }, {
      "tag": "hindustantimes",
      "weight": 3183
    }, {
      "tag": "indianexpress",
      "weight": 2680
    }, {
      "tag": "ift",
      "weight": 2645
    }, {
      "tag": "bbc",
      "weight": 2313
    }];
    series.labels.template.tooltipText = "{word}:\n[bold]{value}[/]";
    series.dataFields.word = "tag";
    series.dataFields.value = "weight";
}



function domain_may(){
  document.getElementById("dom_jan").classList.remove("active")
  document.getElementById("dom_feb").classList.remove("active")
  document.getElementById("dom_mar").classList.remove("active")
  document.getElementById("dom_apr").classList.remove("active")
  document.getElementById("dom_may").classList.add("active")
  am4core.useTheme(am4themes_animated);
  var chart = am4core.create("domains", am4plugins_wordCloud.WordCloud);
  var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());
  series.data = [
    {"tag": "youtu", "weight": 7286},
    {"tag": "ndtv", "weight": 7224},
    {"tag": "indiatimes", "weight": 4500},
    {"tag": "instagram", "weight": 3950},
    {"tag": "republicworld", "weight": 3377},
    {"tag": "hindustantimes", "weight": 3351},
    {"tag": "ift", "weight": 3208},
    {"tag": "pscp", "weight": 3002},
    {"tag": "toi", "weight": 2984},
    {"tag": "indianexpress", "weight": 2854},
    {"tag": "theguardian", "weight": 2688},
    {"tag": "dlvr", "weight": 2442},
    {"tag": "bbc", "weight": 2248}
    ];
  series.labels.template.tooltipText = "{word}:\n[bold]{value}[/]";
  series.dataFields.word = "tag";
  series.dataFields.value = "weight";
}