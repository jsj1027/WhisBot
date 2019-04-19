import yaml


class yamlLoader:

    def __init__(self, fileName):
        self.fileName = fileName
        self._fileObj = None

    @property
    def fileObj(self):
        return self._fileObj

    @fileObj.setter
    def fileObj(self, fileName=None):
        if(fileName is None):
            return
        with open(str(fileName), "r") as stream:
            try:
                self._fileObj = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
