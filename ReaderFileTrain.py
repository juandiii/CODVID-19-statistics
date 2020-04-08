import json
import glob


class ReaderFileTrain:
    def __init__(self, self_path):
        with open(self_path) as file:
            content = json.load(file)
            self.title = content['title']
            self.paper_id = content['paper_id']
            self.abstract = []
            self.body_text = []

            for entry in content['abstract']:
                self.abstract.append(entry)
            for entry in content['body_text']:
                self.body_text.append(entry)

            # self.abstract = "\n".join(self.abstract)
            # self.body_text = "\n".join(self.body_text)


class GetFiles:
    def __init__(self, params):
        self.dict_ = {'title': [], 'paper_id': [],
                      'abstract': [], 'body_text': []}
        self.root_path = params['root_path']
        self.all_json = self.get_all_json()
        for idx, entry in enumerate(self.all_json):
            if idx % (len(self.all_json) // 10) == 0:
                print(f'Processing index: {idx} of {len(self.all_json)}')
            content = ReaderFileTrain(entry)
            self.dict_['paper_id'].append(content.paper_id)
            self.dict_['title'].append(content.title)
            self.dict_['abstract'].append(content.abstract)
            self.dict_['body_text'].append(content.body_text)

    def get_all_json(self):
        return glob.glob(
            f'{self.root_path}/prep_json/*.json', recursive=True)
