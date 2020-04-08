import matplotlib.pyplot as plt
from Processing import Processing
from Analyze import Analyze
import PreparationData as dp
import pandas as pd
import getch
import os
import platform
import pickle
import random
import pyLDAvis.gensim
from gensim import corpora, models
from ReaderFileTrain import ReaderFileTrain, GetFiles
from sklearn.feature_extraction.text import CountVectorizer


from sklearn.decomposition import LatentDirichletAllocation as LDA

plt.style.use('ggplot')

root_path = '/Users/juandiii/development/python/proyecto_final_mineria'
params = {'root_path': root_path}


def main(is_print=False):
    print("Proccesing...")
    processing_ = Processing(params)
    # papers = processing_.dict_

    # for idx, paper in enumerate(papers['body_text']):
    #     process_text = dp.process_text(paper)


def training_model():
    print("Get Files")
    data = GetFiles(params).dict_

    data = pd.DataFrame(
        data, columns=['paper_id', 'title', 'abstract', 'body_text'])

    text_data = []

    for tokens in data['body_text']:
        for token in tokens:
                text_data.append(token)

    dictionary = corpora.Dictionary(text_data)
    corpus = [dictionary.doc2bow(text) for text in text_data]

    pickle.dump(corpus, open('corpus.pkl', 'wb'))
    dictionary.save('dictorionary.gensim')

    model = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)
    model.save('model5.gensim')

    topics = model.print_topics(num_words=4)

    for topic in topics:
       print(topic)

def loadModel(is_display=False):
    print("Loading...")
    dictionary = corpora.Dictionary.load('dictorionary.gensim')
    corpus = pickle.load(open('corpus.pkl', 'rb'))
    lda = models.LdaModel.load('model5.gensim')

    topics = lda.print_topics(num_words=4)

    for topic in topics:
       print(topic)

    if is_display is True:
        # pyLDAvis.enable_notebook()
        lda_display = pyLDAvis.gensim.prepare(lda, corpus, dictionary, sort=False)
        print("Load")
        pyLDAvis.save_html(lda_display, 'display.html')

if __name__ == "__main__":
    if platform.system() == "Windows":
        os.system("cls")
    if platform.system() == "Darwin" or platform.system() == "Linux":
        os.system("clear")
    print("Proyecto final de minería")
    print("1: Preparacion de datos\n2: Entrenar\n3: Ver los tópicos de los papers de los 5 más importantes")
    choice = getch.getch()
    if choice == '1':
        main(is_print=False)
    if choice == '2':
        training_model()
    if choice == '3':
        loadModel(is_display=False)
    # main(is_print=True)
