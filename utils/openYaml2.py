import yaml


class yamlLoader:

    def __init__(self, fileName):
        self._fileName = fileName
        self._fileObj = None

    @property
    def fileObj(self):
        if(self._fileObj is None):
            with open(str(self._fileName), "r") as stream:
                try:
                    self._fileObj = yaml.safe_load(stream)
                    return self._fileObj
                except yaml.YAMLError as exc:
                    print(exc)
        else:
            return self._fileObj

    # @fileObj.setter
    # def fileObj(self):
    #     if(self.fileName is None):
    #         raise AttributeError("you have not set a fileName")
    #     with open(str(fileName), "r") as stream:
    #         try:
    #             self._fileObj = yaml.safe_load(stream)
    #         except yaml.YAMLError as exc:
    #             print(exc)
