import matplotlib.pyplot as plt
from FileReader import FileReader
from Proccesing import Proccesing
from Analyze import Analyze
import numpy as numpy
import pandas as pd
plt.style.use('ggplot')

root_path = '/Users/juandiii/development/python/proyecto_final_mineria'


def main(is_print=False):
    params = {'root_path': root_path}
    proccesing_ = Proccesing(params)
    stats = Analyze(proccesing_.dict_, columns=[
        'paper_id', 'abstract', 'body_text'])

    if is_print is True:
        print(stats.df_covid.describe(include='all'))

    return stats


if __name__ == "__main__":
    main(is_print=True)
