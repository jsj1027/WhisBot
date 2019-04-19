import yaml


class yamlLoader:

    def __init__(self, fileName=None):
        self._fileName = fileName
        self._fileObj = None

    @property
    def fileName(self):
        return self._fileName

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