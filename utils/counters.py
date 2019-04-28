from os import stat
from pathlib import Path

databaseFolder = Path("database")
potatoCountFIle = databaseFolder / "potato_count.txt"
Path.touch(potatoCountFIle) if not Path.exists(potatoCountFIle) else True


def getPotatoCount():
    global potatoCountFIle
    return potatoCountFIle.read_text() if stat(potatoCountFIle).st_size > 0 \
        else 0


def updatePotatoCount():
    currentCount = getPotatoCount()
    updatedCount = int(currentCount) + 1
    potatoCountFIle.write_text(str(updatedCount))
