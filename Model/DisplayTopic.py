

class Topic:

    __inputFields={
        "displayName":"",
        "inputType":"",
        "inputValue":"",
        "addtionalLabel":"",
        "outputBox":"",
        "displayValue":"",
        "calculationOnly":"",
        "helpText":"",
        "defaultValue":"",
        "horizontalLine":"",
        "readOnly":""
    }

    __inputFieldsKeys=list(__inputFields.keys())
    
    def __init__(self,inputFieldValues):
        for i in range(0,len(inputFieldValues)):
            self.__inputFields[self.__inputFieldsKeys[i]]=inputFieldValues[i]

    def get_inputField(self,fieldName):           #getter method
        return self.__inputFields[fieldName]

    def set_inputField(self,fieldName,fieldValue):# setter method
        self.__inputFields[fieldName]=fieldValue
    

