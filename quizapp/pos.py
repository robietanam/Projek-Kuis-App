import json
from posixpath import abspath


#jalur =  '/'.join(str(abspath('quizapp')).split('\\'))
def loadData(PATH,folder = ''):
    with open(folder + "/"+ PATH) as database:
        tmp = json.load(database)
    return tmp

def simpanData(PATH,data,folder = '',mode = False):
    with open(folder + "/"+ PATH,'w+') as database:
        json_object = json.dumps(data, indent = 2,sort_keys = mode)
        database.write(json_object)