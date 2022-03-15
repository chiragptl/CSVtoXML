from Model.DisplayTopic import Topic
from Utils.CSVReader import CSVReader


class XMLGenerator:
    reader = CSVReader()
    path = "Calculator-meta-data-Sheet1.csv"
    displayTopicRes = dict()
    for inputField in reader.readCSV(path):
        print(inputField)
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
        #Generator(displayTopic)
        del displayTopic
    
    #generate xml
    def Generator(inputField):
        XMLcode = {
            #1: getChoiceXML(),
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: ""
        }
        return XMLcode.get(inputField.type, "Invalid Input Choice!")

    def getChoiceXML():
        return ""