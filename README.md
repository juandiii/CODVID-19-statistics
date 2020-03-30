# Statistics for papers of CODVID-19

## Summary

COVID-19 is an infectious disease caused by a new discovered conovirus.

The CODVID-19 virus is spread primarily though droplets of saliva or discharge from the nose when a infected person coughs or sneezes.

Source: WHO [World Health Organization](https://www.who.int/health-topics/coronavirus)

This project is to calculate all the words in the papers as abstract, body text.

1. Download dataset articles in [COVID-19 Open Research Dataset](https://pages.semanticscholar.org/coronavirus-research)

    The most important dataset is `Non-commercial use subset` includes PMC Content - 2350 full text

    | Dataset         | Size |
    |-----------------|-----:|
    | Non Commercial  | 40MB |

2. Put folders in this source, but make sure the folder should be `noncomm_use_subset`

2. You need python 3.6.x for run this project.
    ```sh
    pip install -r requirements.txt
    ```

3. Run this project

    ```sh
    python index.py

    Processing index: 0 of 2350
    Processing index: 235 of 2350
    Processing index: 470 of 2350
    Processing index: 705 of 2350
    Processing index: 940 of 2350
    Processing index: 1175 of 2350
    Processing index: 1410 of 2350
    Processing index: 1645 of 2350
    Processing index: 1880 of 2350
    Processing index: 2115 of 2350
        title                                  paper_id abstract                                          body_text  abstract_count_words  body_count_words  count_chars_abstract  count_chars_body_text
    count   2350                                      2350     2350                                               2350           2350.000000       2350.000000                2350.0                 2350.0
    unique  1863                                      2350     1573                                               2215                   NaN               NaN                   NaN                    NaN
    top           8318896fad2acf22ac94d15d6d571dd2f7cf121d           Coronaviruses are a group of enveloped viruses...                   NaN               NaN                   NaN                    NaN
    freq     268                                         1      646                                                  3                   NaN               NaN                   NaN                    NaN
    mean     NaN                                       NaN      NaN                                                NaN            153.529362       4139.938298             2476905.0             63183794.0
    std      NaN                                       NaN      NaN                                                NaN            144.923875       7583.474619                   0.0                    0.0
    min      NaN                                       NaN      NaN                                                NaN              0.000000          1.000000             2476905.0             63183794.0
    25%      NaN                                       NaN      NaN                                                NaN              0.000000       1990.250000             2476905.0             63183794.0
    50%      NaN                                       NaN      NaN                                                NaN            157.000000       3127.000000             2476905.0             63183794.0
    75%      NaN                                       NaN      NaN                                                NaN            234.750000       4983.000000             2476905.0             63183794.0
    max      NaN                                       NaN      NaN                                                NaN           2805.000000     241076.000000             2476905.0             63183794.0
    ```

### Credits

- COVID-19 Open Research Dataset [Semantics Scholar](https://pages.semanticscholar.org/coronavirus-research)

- Thanks to [Ivan Ega Pratama](https://github.com/gpratama) for the code for extract as abstract and body text. [Source code](https://www.kaggle.com/ivanegapratama/covid-eda-initial-exploration-tool)