from database.dbClass import *
import yaml

editableDBs = {"userexp"}

databases = {
    "config": databaseClass("config.yaml", None),
    "message": databaseClass("database/messages.yaml", None),
    "userexp": databaseClass("database/userExpDatabase.yaml", None)
}


def initDatabases():
    for item in databases:
        if(databases[item].data is None):
            with open(databases[item].filePath, "r") as stream:
                try:
                    databases[item].data = yaml.safe_load(stream)
                    stream.close()
                except yaml.YAMLError as exc:
                    print(exc)


def getDatabase(name):
    return databases[name].data


def updateDatabase(name, itemName, itemData):
    if(name in databases):
        databases[name].data[itemName] = itemData
        with open(databases[name].filePath, 'w') as f:
            yaml.dump(databases[name].data, f)
            f.close()

initDatabases()
