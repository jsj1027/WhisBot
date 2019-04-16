import yaml

yamlFile = None


def openYaml():
    with open("config.yaml", "r") as stream:
        try:
            global yamlFile
            yamlFile = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


def getYaml():
    global yamlFile
    if(yamlFile is None):
        openYaml()
        return yamlFile
    else:
        return yamlFile
