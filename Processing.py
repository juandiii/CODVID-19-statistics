from FileReader import FileReader
import glob
import json
import os


def save_file(prep_paper, name_file):
    with open("/Users/juandiii/development/python/proyecto_final_mineria/prep_json/{}".format(name_file), "w") as fileName:
        json.dump(
            prep_paper, fileName)


class Processing:
    def __init__(self, params):
        self.dict_ = {'title': [], 'paper_id': [],
                      'abstract': [], 'body_text': []}
        self.prep_paper = {}
        self.root_path = params['root_path']
        self.all_json = self.get_all_json()
        for idx, entry in enumerate(self.all_json):
            if idx % (len(self.all_json) // 10) == 0:
                print(f'Processing index: {idx} of {len(self.all_json)}')
            content = FileReader(entry)
            self.prep_paper['paper_id'] = content.paper_id
            self.prep_paper['title'] = content.title
            self.prep_paper['abstract'] = content.abstract
            self.prep_paper['body_text'] = content.body_text

            save_file(self.prep_paper, os.path.basename(entry))

            # self.dict_['paper_id'].append(content.paper_id)
            # self.dict_['title'].append(content.title)
            # self.dict_['abstract'].append(content.abstract)
            # self.dict_['body_text'].append(content.body_text)

    def get_all_json(self):
        return glob.glob(
            f'{self.root_path}/noncomm_use_subset/*.json', recursive=True)
