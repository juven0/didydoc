from os import walk

class BookController:
    def __init__(self, PATH) -> None:
        self.PATH = PATH
    
    def loadFiles(self, path):
        pathArray = []
        for pathFile, a, files in walk(dir):
            for file in files:
                classe = path.basename(path.dirname(pathFile+'/'+file))
                pathArray.append((pathFile+'/'+file, classe))
        return pathArray
    
    def get_all(self):
        path = self.PATH
        return self.loadFiles(path)
    
    def get_by_classe(self, classe):
        path = self.PATH+classe+'/'
        return self.loadFiles(path)