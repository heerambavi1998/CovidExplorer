function ment_month(month){
  ment_cloud(month);
  document.getElementById("ment_jan").classList.remove("active")
  document.getElementById("ment_feb").classList.remove("active")
  document.getElementById("ment_mar").classList.remove("active")
  document.getElementById("ment_apr").classList.remove("active")
  document.getElementById("ment_may").classList.remove("active")
  active = "ment_"+month
  document.getElementById(active).classList.add("active")
}

function ment_cloud(month){
    var chart = am4core.create("ment_cloud", am4plugins_wordCloud.WordCloud);
    var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());
  
    jan = [{"tag": "@spectatorindex", "weight": 13751}, {"tag": "@ani",  "weight": 7888}, {  "tag": "@who",  "weight": 6662}, {  "tag": "@mohfw_india",  "weight": 6193}, {  "tag": "@rahulgandhi",  "weight": 4687}, {  "tag": "@pmoindia",  "weight": 2921}, {  "tag": "@pib_india",  "weight": 2563}, {  "tag": "@airindiain",  "weight": 2432}, {  "tag": "@timesofindia",  "weight": 2191}, {  "tag": "@raksharamaiah",  "weight": 2103}];
    feb = [{"tag": "@realdonaldtrump", "weight": 12892}, {"tag": "@spectatorindex",  "weight": 10768}, {  "tag": "@narendramodi",  "weight": 9385}, {  "tag": "@ani",  "weight": 9378}, {  "tag": "@who",  "weight": 8166}, {  "tag": "@askanshul",  "weight": 6639}, {  "tag": "@majorgauravarya",  "weight": 6636}, {  "tag": "@drsjaishankar",  "weight": 5742}, {  "tag": "@rahulgandhi",  "weight": 5114}, {  "tag": "@imrankhanpti",  "weight": 4779}, {  "tag": "@swamy39",  "weight": 4714}, {  "tag": "@timesofindia",  "weight": 4604}, {  "tag": "@pmoindia",  "weight": 4516}];
    mar = [{"tag": "@narendramodi",  "weight": 97899}, {  "tag": "@pmoindia",  "weight": 29148}, {  "tag": "@ani",  "weight": 25196}, {  "tag": "@rahulgandhi",  "weight": 22515}, {  "tag": "@amitshah",  "weight": 15918}, {  "tag": "@realdonaldtrump",  "weight": 13456}, {  "tag": "@ipspankajnain",  "weight": 12041}, {  "tag": "@mohfw_india",  "weight": 10873}, {  "tag": "@who",  "weight": 10841}, {  "tag": "@arvindkejriwal",  "weight": 9561}, {  "tag": "@drharshvardhan",  "weight": 8652}, {  "tag": "@pit_news",  "weight": 8227}, {  "tag": "@spectator_index",  "weight": 7893}];
    apr = [{  "tag": "@narendramodi",  "weight": 106826}, {  "tag": "@pmoindia",  "weight": 34473}, {  "tag": "@ani",  "weight": 31026}, {  "tag": "@rahulgandhi",  "weight": 20089}, {  "tag": "@realdonaldtrump",  "weight": 20053}, {  "tag": "opindia_com",  "weight": 15506}, {  "tag": "@arvindkejriwal",  "weight": 10961}, {  "tag": "@sardesairajdeep",  "weight": 10312}, {  "tag": "@incindia",  "weight": 10103}, {  "tag": "@askanshul",  "weight": 9915}, {  "tag": "@who",  "weight": 9564}, {  "tag": "@norbertelekes",  "weight": 9264}, {  "tag": "@amitshah",  "weight": 9160}];
    may = [{"tag": "@narendramodi", "weight": 55449},{"tag": "@pmoindia", "weight": 28954},{"tag": "@realdonaldtrump", "weight": 24661},{"tag": "@rahulgandhi", "weight": 20796},{"tag": "@ani", "weight": 17418},{"tag": "@opindia_com", "weight": 13400},{"tag": "@incindia", "weight": 13198},{"tag": "@norbertelekes", "weight": 11356},{"tag": "@arvindkejriwal", "weight": 10777},{"tag": "@amitshah", "weight": 10559},{"tag": "@drharshvardhan", "weight": 9435},{"tag": "@cmomaharashtra", "weight": 8680},{"tag": "@bjp4india", "weight": 8551},{"tag": "@ndtv", "weight": 8191},{"tag": "@mohfw_india", "weight": 8029},{"tag": "@sardesairajdeep", "weight": 7192}]
  
    console.log("MENTION"+month)
    series.data = window[month]
    series.labels.template.tooltipText = "{word}:\n[bold]{value}[/]";
    series.dataFields.word = "tag";
    series.dataFields.value = "weight";
  }