class Topic:
    def __init__(self, displayName, inputType, inputValue, addtionalLabel, outputBox, displayValue, calculationOnly, helptext, defalutValue, horizontalLine, readOnly):
        self.displayName = displayName
        self.inputType = inputType
        self.inputValue = inputValue
        self.addtionalLabel = addtionalLabel
        self.outputBox = outputBox
        self.displayValue = displayValue
        self.calculationOnly = calculationOnly
        self.helptext = helptext
        self.defalutValue = defalutValue
        self.horizontalLine = horizontalLine
        self.readOnly = readOnly
    
    
    def get_displayName(self):
        return self.displayName
    
    def get_inputType(self):
        return self.inputType
    
    def get_inputValue(self):
        return self.inputValue
    
    def get_addtionalLabel(self):
        return self.addtionalLabel
    
    def get_outputBox(self):
        return self.outputBox
    
    def get_displayValue(self):
        return self.displayValue
    
    def get_calculationOnly(self):
        return self.calculationOnly
    
    def get_helptext(self):
        return self.helptext
    
    def get_defalutValue(self):
        return self.defalutValue
    def get_horizontalLine(self):
        return self.horizontalLine
    def get_readOnly(self):
        return self.readOnly

    
    def set_displayName(self, displayName):
        self.displayName = displayName
    
    def set_inputValue(self, inputType):
        self.inputType = inputType
    
    def set_inputValue(self, inputValue):
        self.inputValue = inputValue
    
    def set_addtionalLabel(self,addtionalLabel):
        self.addtionalLabel = addtionalLabel
    
    def set_outputBox(self, outputBox):
        self.outputBox = outputBox
    
    def set_displayValue(self, displayValue):
        self.displayValue = displayValue
    
    def set_calculationOnly(self, calculationOnly):
        self.calculationOnly = calculationOnly
    
    def set_helptext(self, helptext):
        self.helptext = helptext
    
    def set_defalutValue(self, defalutValue):
        self.defalutValue = defalutValue
    
    def set_horizontalLine(self, horizontalLine):
        self.horizontalLine = horizontalLine
    
    def set_readOnly(self, readOnly):
        self.readOnly = readOnly