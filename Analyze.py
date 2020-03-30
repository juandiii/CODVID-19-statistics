import pandas as pd


class Analyze:
    def __init__(self, data=None, columns=None):
        if data is None:
            data = {}

        self.df_covid = pd.DataFrame(data, columns=columns)
        self.df_covid['abstract_count_words'] = self.df_covid['abstract'].apply(
            lambda x: len(x.strip().split()))
        self.df_covid['body_count_words'] = self.df_covid['body_text'].apply(
            lambda x: len(x.strip().split()))

        countCharsAbstract = 0
        for idx, value in enumerate(self.df_covid['abstract']):
            for chars in value:
                countCharsAbstract += 1

        countCharsBodyText = 0
        for idx, value in enumerate(self.df_covid['body_text']):
            for chars in value:
                countCharsBodyText += 1

        self.df_covid['count_chars_abstract'] = countCharsAbstract
        self.df_covid['count_chars_body_text'] = countCharsBodyText
