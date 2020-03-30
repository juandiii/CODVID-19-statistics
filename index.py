import matplotlib.pyplot as plt
from Processing import Processing
from Analyze import Analyze

plt.style.use('ggplot')

root_path = '/Users/juandiii/development/python/proyecto_final_mineria'


def main(is_print=False):
    params = {'root_path': root_path}
    processing_ = Processing(params)
    stats = Analyze(processing_.dict_, columns=['title',
                                                'paper_id', 'abstract', 'body_text'])

    if is_print is True:
        print(stats.df_covid.describe(include='all'))

    return stats


if __name__ == "__main__":
    main(is_print=True)
