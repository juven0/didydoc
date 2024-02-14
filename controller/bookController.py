from os import walk
from os import path as p

class BookController:
    def __init__(self, PATH) -> None:
        self.PATH = PATH
    
    def loadFiles(self, path):
        pathArray = []
        for pathFile, a, files in walk(path):
            for f in files:
                classe = p.basename(p.dirname(pathFile+'/'+f))
                pathArray.append((f, pathFile+"/"+f, classe))
        return pathArray
    
    def get_all(self):
        path = self.PATH
        return self.loadFiles(path)
    
    def get_by_classe(self, classe):
        path = self.PATH+classe+'/'
        return self.loadFiles(path)