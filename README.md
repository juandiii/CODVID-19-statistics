# Statistics for papers of CODVID-19

## Summary

COVID-19 is an infectious disease caused by a new discovered conovirus.

The CODVID-19 virus is spread primarily though droplets of saliva or discharge from the nose when a infected person coughs or sneezes.

Source: WHO [World Health Organization](https://www.who.int/health-topics/coronavirus)

This project is to calculate all the words in the papers as abstract, body text.

1. Download dataset articles in [Semantics Scholar](https://pages.semanticscholar.org/coronavirus-research)

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
                                            paper_id abstract                                          body_text  abstract_count_words  body_count_words
    count                                       2350     2350                                               2350           2350.000000       2350.000000
    unique                                      2350     1573                                               2215                   NaN               NaN
    top     1694b4f8e456f966ff1fe215161bae59e59148df           Coronaviruses are a group of enveloped viruses...                   NaN               NaN
    freq                                           1      646                                                  3                   NaN               NaN
    mean                                         NaN      NaN                                                NaN            153.529362       4139.938298
    std                                          NaN      NaN                                                NaN            144.923875       7583.474619
    min                                          NaN      NaN                                                NaN              0.000000          1.000000
    25%                                          NaN      NaN                                                NaN              0.000000       1990.250000
    50%                                          NaN      NaN                                                NaN            157.000000       3127.000000
    75%                                          NaN      NaN                                                NaN            234.750000       4983.000000
    max                                          NaN      NaN                                                NaN           2805.000000     241076.000000
    ```