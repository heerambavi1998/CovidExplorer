function hash_jan(){
    document.getElementById("hash_jan").classList.add("active")
    document.getElementById("hash_feb").classList.remove("active")
    document.getElementById("hash_mar").classList.remove("active")
    document.getElementById("hash_apr").classList.remove("active")
    document.getElementById("hash_may").classList.remove("active")
    am4core.useTheme(am4themes_animated);
    var chart = am4core.create("hashtags", am4plugins_wordCloud.WordCloud);
    var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());
    series.data = [{
      "tag": "#coronavirus",
      "weight": 76199
    }, {
      "tag": "#china",
      "weight": 13104
    }, {
      "tag": "#wuhan",
      "weight": 10229
    }, {
      "tag": "#coronavirusoutbreak",
      "weight": 7766
    }, {
      "tag": "#coronavirusindia",
      "weight": 3885
    }, {
      "tag": "#india",
      "weight": 3680
    }, {
      "tag": "wuhancoronavirus",
      "weight": 2980
    }, {
      "tag": "#coronaoutbreak",
      "weight": 2297
    }, {
      "tag": "#ncov2020",
      "weight": 2142
    }, {
      "tag": "#breaking",
      "weight": 2108
    }, {
      "tag": "#kerela",
      "weight": 1979}];
    series.labels.template.tooltipText = "{word}:\n[bold]{value}[/]";
    series.dataFields.word = "tag";
    series.dataFields.value = "weight";
  }


function hash_feb(){
      document.getElementById("hash_jan").classList.remove("active")
      document.getElementById("hash_feb").classList.add("active")
      document.getElementById("hash_mar").classList.remove("active")
      document.getElementById("hash_apr").classList.remove("active")
      document.getElementById("hash_may").classList.remove("active")
      am4core.useTheme(am4themes_animated);
      var chart = am4core.create("hashtags", am4plugins_wordCloud.WordCloud);
      var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());

      series.data = [{
                        "tag": "#coronavirus",
                        "weight": 106411
                      }, {
                        "tag": "#china",
                        "weight": 25677
                      }, {
                        "tag": "#wuhan",
                        "weight": 18814
                      }, {
                        "tag": "#nomeat_nocoronavirus",
                        "weight": 18519
                      }, {
                        "tag": "#covid19",
                        "weight": 14442
                      }, {
                        "tag": "#coronavirusoutbreak",
                        "weight": 4194
                      }, {
                        "tag": "#india",
                        "weight": 9670
                      }, {
                        "tag": "#coronavirusindia",
                        "weight": 4194
                      }, {
                        "tag": "#coronaviruschina",
                        "weight": 3278
                      }];
      series.labels.template.tooltipText = "{word}:\n[bold]{value}[/]";
      series.dataFields.word = "tag";
      series.dataFields.value = "weight";
    }      

function hash_mar(){
  document.getElementById("hash_jan").classList.remove("active")
  document.getElementById("hash_feb").classList.remove("active")
  document.getElementById("hash_mar").classList.add("active")
  document.getElementById("hash_apr").classList.remove("active")
  document.getElementById("hash_may").classList.remove("active")
  am4core.useTheme(am4themes_animated);
  var chart = am4core.create("hashtags", am4plugins_wordCloud.WordCloud);
  var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());
  series.data = [{
    "tag": "#coronavirus",
    "weight": 181397
  }, {
    "tag": "#covid19",
    "weight": 80495
  }, {
    "tag": "#corona",
    "weight": 18081
  }, {
    "tag": "#indiafightscorona",
    "weight": 14344
  }, {
    "tag": "#india",
    "weight": 13215
  }, {
    "tag": "#coronavirusupdate",
    "weight": 11802
  }, {
    "tag": "#coronavirusoutbreak",
    "weight": 11802
  }, {
    "tag": "#china",
    "weight": 9322
  }, {
    "tag": "#coronaalert",
    "weight": 8626
  }, {
    "tag": "#namaste",
    "weight": 7044
  }];
  series.labels.template.tooltipText = "{word}:\n[bold]{value}[/]";
  series.dataFields.word = "tag";
  series.dataFields.value = "weight";  
  }

function hash_apr(){
    document.getElementById("hash_jan").classList.remove("active")
    document.getElementById("hash_feb").classList.remove("active")
    document.getElementById("hash_mar").classList.remove("active")
    document.getElementById("hash_apr").classList.add("active")
    document.getElementById("hash_may").classList.remove("active")
    am4core.useTheme(am4themes_animated);
    var chart = am4core.create("hashtags", am4plugins_wordCloud.WordCloud);
    var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());
    series.data = [{
      "tag": "#covid19",
      "weight": 151156
    }, {
      "tag": "#coronavirus",
      "weight": 65091
    }, {
      "tag": "#lockdown",
      "weight": 33651
    }, {
      "tag": "#indiafightscorona",
      "weight": 22885
    }, {
      "tag": "#stayhome",
      "weight": 17469
    }, {
      "tag": "#india",
      "weight": 15316
    }, {
      "tag": "#corona",
      "weight": 14546
    }, {
      "tag": "#hydroxychloroquine",
      "weight": 11890
    }, {
      "tag": "#tablighijamaat",
      "weight": 8436
    }, {
      "tag": "#breaking",
      "weight": 6897
    }, {
      "tag": "#staysafe",
      "weight": 6706
    }, {
      "tag": "#stayhomestaysafe",
      "weight": 5892
    }, {
      "tag": "#socialdistancing",
      "weight": 5322
    }];
    series.labels.template.tooltipText = "{word}:\n[bold]{value}[/]";
    series.dataFields.word = "tag";
    series.dataFields.value = "weight";
  }


  function hash_may(){
    document.getElementById("hash_jan").classList.remove("active")
    document.getElementById("hash_feb").classList.remove("active")
    document.getElementById("hash_mar").classList.remove("active")
    document.getElementById("hash_apr").classList.remove("active")
    document.getElementById("hash_may").classList.add("active")
    am4core.useTheme(am4themes_animated);
    var chart = am4core.create("hashtags", am4plugins_wordCloud.WordCloud);
    var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());
    series.data = [
      {"tag": "#covid19", "weight": 135615},
      {"tag": "#coronavirus", "weight": 46268},
      {"tag": "#lockdown", "weight": 30725},
      {"tag": "#covid", "weight": 17448},
      {"tag": "#indiafightscorona", "weight": 16261},
      {"tag": "#india", "weight": 16014},
      {"tag": "#stayhome", "weight": 12842},
      {"tag": "#hydroxychloroquine", "weight": 11698},
      {"tag": "#corona", "weight": 11152},
      {"tag": "#staysafe", "weight": 5667},
      {"tag": "#breaking", "weight": 4774},
      {"tag": "#socialdistancing", "weight": 4080},
      {"tag": "#iforindia", "weight": 4026},
      ];
    series.labels.template.tooltipText = "{word}:\n[bold]{value}[/]";
    series.dataFields.word = "tag";
    series.dataFields.value = "weight";
  }