from Model.DisplayTopic import Topic
from Utils.CSVReader import CSVReader
from xml.dom import minidom


#XML Generator:
xmlData = ""
root = minidom.Document();
xml = root.createElement("form")
root.appendChild(xml)
title = root.createElement("title")
title.appendChild(root.createTextNode(""))
xml.appendChild(title)

#generate xml
def Generator(displayTopic = 0): 
    XMLcode = {
        1: getChoiceXML(displayTopic),
        2: getFloatXML(displayTopic),
        3: getMChoiceXML(displayTopic),
        4: getReadOnlyXML(displayTopic),
        5: getNoNewLineXML(displayTopic),
        6: getCommentXML(displayTopic),
        7: getIndentedCommentXML(displayTopic),
        8: getHorizontalLineXML(displayTopic)
    }
    return XMLcode.get(int(displayTopic.inputType), "Invalid Input Choice!")

def getChoiceXML(displayTopic):
    
    varType = root.createElement("var")
    varType.setAttribute("type","CHOICE")
    xml.appendChild(varType)
    
    varTypeName = root.createElement("name")
    varTypeName.appendChild(root.createTextNode(displayTopic.displayName))

    varTypeLabel = root.createElement("label")
    varTypeLabel.appendChild(root.createTextNode(displayTopic.displayName))
    
    varTypeDefault = root.createElement("default")
    varTypeDefault.appendChild(root.createTextNode(""))

    varType.appendChild(varTypeName)
    varType.appendChild(varTypeLabel)
    varType.appendChild(varTypeDefault)

    choices = displayTopic.inputValue.split("|")
    values = displayTopic.calculationOnly.split("|")

    for choice , value in zip(choices,values):
        varTypeChoice = root.createElement("choice")
        choiceName = root.createElement("label")
        choiceName.appendChild(root.createTextNode(choice))
        varTypeChoice.appendChild(choiceName)
        choiceValue = root.createElement("value")
        choiceValue.appendChild(root.createTextNode(value))
        varTypeChoice.appendChild(choiceValue)
        varType.appendChild(varTypeChoice)

def getFloatXML(displayTopic):
    return None

def getMChoiceXML(displayTopic):
    return None

def getReadOnlyXML(displayTopic):
    return None

def getNoNewLineXML(displayTopic):
    return None

def getCommentXML(displayTopic):
    return None

def getIndentedCommentXML(displayTopic):
    return None

def getHorizontalLineXML(displayTopic):
    return None


reader = CSVReader()
path = "Calculator-meta-data-Sheet1.csv"
displayTopicRes = dict()
for inputField in reader.readCSV(path):
    displayName = inputField[0]
    inputType = inputField[1]
    inputValue = inputField[2]
    addtionalLabel = inputField[3]
    outputBox = inputField[4]
    displayValue = inputField[5]
    calculationOnly = inputField[6]
    helptext = inputField[7]
    defalutValue = inputField[8]
    horizontalLine = inputField[9]
    readOnly = inputField[10]
    displayTopic = Topic(displayName, inputType, inputValue, addtionalLabel, outputBox, displayValue, calculationOnly, helptext, defalutValue, horizontalLine, readOnly)
    displayTopicRes[inputField[0]] = displayTopic
    Generator(displayTopic = displayTopic)
    del displayTopic
xmlData = root.toprettyxml(indent="\t")
print(xmlData)