import simplejson as json
from pathlib import Path

cardDataBase = None

def addCardToDataBase(key, cardDetails):
    global cardDataBase
    if("S" in key):
        cardDataBase["Stories"][f"{key}"] = cardDetails
        cardDataBase["Stories"]["lastNum"] = cardDetails["number"]
    elif("D" in key):
        cardDataBase["Defects"][f"{key}"] = cardDetails
        cardDataBase["Defects"]["lastNum"] = cardDetails["number"]
    cardDBFileName = getCardDBFileName()
    cardDataBaseFile = open(cardDBFileName, 'w')
    json.dump(cardDataBase, cardDataBaseFile)
    return

def createCardDetails(itemDetails, newItemNumber):
    title = itemDetails[1]
    description = itemDetails[2]
    key = itemDetails[0]+str(newItemNumber)
    newCard = {"number":newItemNumber, "title": title, "description": description}
    return key,newCard

def getNewItemNumber(workType):
    return getLastItemNumber(workType)+1

def getLastItemNumber(workType):
    global cardDataBase
    lastItemNumber = 0
    if(workType.upper() == "S"):
        lastItemNumber = cardDataBase["Stories"]["lastNum"]
    if(workType.upper() == 'D'):
        lastItemNumber = cardDataBase["Defects"]["lastNum"]
    return lastItemNumber

def getItemDetails():
    workType = input("Is this a story or a defect? (Not case sensitive): ")
    if(workType.lower() not in ["s","d","story","defect"]):
        raise ValueError("Input entered was not s/d/story/defect. (Not case sensitive): ")
    elif(workType.lower() in ["s","story"]):
        workType = "S"
    elif(workType.lower() in ["d","defect"]):
        workType = "D"
    title = input("What is the Story/Defect title: ")
    description = input("What is the Story/Defect description?: ")
    return [workType,title,description]

def getCardDataBase():
    global cardDataBase
    cardDataBaseFileName = getCardDBFileName()
    cardDataBaseFile = open(cardDataBaseFileName, 'r')
    cardDataBase = json.load(cardDataBaseFile)
    return

def getCardDBFileName():
    cardDataBaseFolder = Path(Path.cwd().as_posix())
    if(cardDataBaseFolder.name is not "trello"):
        cardDataBaseFolder / "trello"
    cardDataBaseFileName = cardDataBaseFolder / "cards.json"
    return cardDataBaseFileName

def main():
    getCardDataBase()
    print(cardDataBase)
    itemDetails = getItemDetails()
    workType = itemDetails[0]
    newItemNumber = getNewItemNumber(workType)
    key, cardDetails = createCardDetails(itemDetails, newItemNumber)
    addCardToDataBase(key, cardDetails)
    print(cardDataBase)
    return

main()