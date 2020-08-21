# CovidExplorer: A Multi-faceted AI-based Search and Visualization Engine for COVID-19 Information
*CovidExplorer* is a multi-faceted AI-based search and visualization engine. It aims to help researchers understand current state-of-the-art COVID-19 research, identify research articles relevant to their domain, and visualize real-time trends and statistics of COVID-19 cases. It also brings in India-specific topical discussions on social media to study different aspects of COVID-19. The system can be accessed for use [here](http://covidexplorer.in).

## Datasets
- **CORD-19** : ~157,000 scholarly articles, including over 75,000 full-text articles on coronaviruses. The dataset is provided by The White House and a coalition of leading research groups. [Link to Download](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)
- **Tweet Dataset** : ~5.7 million tweets relevant to the COVID-19 pandemic, filtered for an Indian domain. We periodically collect relevant tweet IDs from a publicly available [COVID-19 TweetID corpus](https://github.com/echen102/COVID-19-TweetIDs). The tweet IDs are hydrated using the [DocNow Hydrator tool](https://github.com/docnow/hydrator). We only explore India-specific tweets by using location metadata or the presence of Indian locations (states, cities, towns, and village names) in the tweet text. We also include tweets that are either posted as a reply to the India-specific tweets and tweets for which India-specific tweets were posted as a reply.

## Architecture
<img src="/fig/architecture.png" width="800">

## Functionalities
- **COVID-19 Scholarly Search**:
  - Full-text search
  - Named entity recognition and visualisation
- **India-specific Infection Statistics**
- **Social Media Discussions**
  - Temporal activity and trends
  - Temporal topic evolution
