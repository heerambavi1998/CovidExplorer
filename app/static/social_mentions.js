function ment_jan(){
    document.getElementById("ment_jan").classList.add("active")
    document.getElementById("ment_feb").classList.remove("active")
    document.getElementById("ment_mar").classList.remove("active")
    document.getElementById("ment_apr").classList.remove("active")
    am4core.useTheme(am4themes_animated);
    var chart = am4core.create("mentions", am4plugins_wordCloud.WordCloud);
    var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());
    series.data = [{
      "tag": "@spectatorindex",
      "weight": 13751
    }, {
      "tag": "@ani",
      "weight": 7888
    }, {
      "tag": "@who",
      "weight": 6662
    }, {
      "tag": "@mohfw_india",
      "weight": 6193
    }, {
      "tag": "@rahulgandhi",
      "weight": 4687
    }, {
      "tag": "@pmoindia",
      "weight": 2921
    }, {
      "tag": "@pib_india",
      "weight": 2563
    }, {
      "tag": "@airindiain",
      "weight": 2432
    }, {
      "tag": "@timesofindia",
      "weight": 2191
    }, {
      "tag": "@raksharamaiah",
      "weight": 2103
    }];
    series.labels.template.tooltipText = "{word}:\n[bold]{value}[/]";
    series.dataFields.word = "tag";
    series.dataFields.value = "weight";
  }

function ment_feb(){
      document.getElementById("ment_jan").classList.remove("active")
      document.getElementById("ment_feb").classList.add("active")
      document.getElementById("ment_mar").classList.remove("active")
      document.getElementById("ment_apr").classList.remove("active")
      am4core.useTheme(am4themes_animated);
      var chart = am4core.create("mentions", am4plugins_wordCloud.WordCloud);
      var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());

      series.data = [    {
                        "tag": "@realdonaldtrump",
                        "weight": 12892
                      }, {
                        "tag": "@spectatorindex",
                        "weight": 10768
                      }, {
                        "tag": "@narendramodi",
                        "weight": 9385
                      }, {
                        "tag": "@ani",
                        "weight": 9378
                      }, {
                        "tag": "@who",
                        "weight": 8166
                      }, {
                        "tag": "@askanshul",
                        "weight": 6639
                      }, {
                        "tag": "@majorgauravarya",
                        "weight": 6636
                      }, {
                        "tag": "@drsjaishankar",
                        "weight": 5742
                      }, {
                        "tag": "@rahulgandhi",
                        "weight": 5114
                      }, {
                        "tag": "@imrankhanpti",
                        "weight": 4779
                      }, {
                        "tag": "@swamy39",
                        "weight": 4714
                      }, {
                        "tag": "@timesofindia",
                        "weight": 4604
                      }, {
                        "tag": "@pmoindia",
                        "weight": 4516
                      }];
      series.labels.template.tooltipText = "{word}:\n[bold]{value}[/]";
      series.dataFields.word = "tag";
      series.dataFields.value = "weight";
    }      

function ment_mar(){
  document.getElementById("ment_jan").classList.remove("active")
  document.getElementById("ment_feb").classList.remove("active")
  document.getElementById("ment_mar").classList.add("active")
  document.getElementById("ment_apr").classList.remove("active")
  am4core.useTheme(am4themes_animated);
  var chart = am4core.create("mentions", am4plugins_wordCloud.WordCloud);
  var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());
  series.data = [{
    "tag": "@narendramodi",
    "weight": 97899
  }, {
    "tag": "@pmoindia",
    "weight": 29148
  }, {
    "tag": "@ani",
    "weight": 25196
  }, {
    "tag": "@rahulgandhi",
    "weight": 22515
  }, {
    "tag": "@amitshah",
    "weight": 15918
  }, {
    "tag": "@realdonaldtrump",
    "weight": 13456
  }, {
    "tag": "@ipspankajnain",
    "weight": 12041
  }, {
    "tag": "@mohfw_india",
    "weight": 10873
  }, {
    "tag": "@who",
    "weight": 10841
  }, {
    "tag": "@arvindkejriwal",
    "weight": 9561
  }, {
    "tag": "@drharshvardhan",
    "weight": 8652
  }, {
    "tag": "@pit_news",
    "weight": 8227
  }, {
    "tag": "@spectator_index",
    "weight": 7893
  }];
  series.labels.template.tooltipText = "{word}:\n[bold]{value}[/]";
  series.dataFields.word = "tag";
  series.dataFields.value = "weight";  
  }

function ment_apr(){
    document.getElementById("ment_jan").classList.remove("active")
    document.getElementById("ment_feb").classList.remove("active")
    document.getElementById("ment_mar").classList.remove("active")
    document.getElementById("ment_apr").classList.add("active")
    am4core.useTheme(am4themes_animated);
    var chart = am4core.create("mentions", am4plugins_wordCloud.WordCloud);
    var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());
    series.data = [{
      "tag": "@narendramodi",
      "weight": 106826
    }, {
      "tag": "@pmoindia",
      "weight": 34473
    }, {
      "tag": "@ani",
      "weight": 31026
    }, {
      "tag": "@rahulgandhi",
      "weight": 20089
    }, {
      "tag": "@realdonaldtrump",
      "weight": 20053
    }, {
      "tag": "opindia_com",
      "weight": 15506
    }, {
      "tag": "@arvindkejriwal",
      "weight": 10961
    }, {
      "tag": "@sardesairajdeep",
      "weight": 10312
    }, {
      "tag": "@incindia",
      "weight": 10103
    }, {
      "tag": "@askanshul",
      "weight": 9915
    }, {
      "tag": "@who",
      "weight": 9564
    }, {
      "tag": "@norbertelekes",
      "weight": 9264
    }, {
      "tag": "@amitshah",
      "weight": 9160
    }];
    series.labels.template.tooltipText = "{word}:\n[bold]{value}[/]";
    series.dataFields.word = "tag";
    series.dataFields.value = "weight";
  }