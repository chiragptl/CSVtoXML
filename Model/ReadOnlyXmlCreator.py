from Model.XmlCreator import XmlCreator
from Model.Document import Document

MainParent = Document.parent


class ReadOnlyXmlCreator:
    def create(displayTopic):
        parent = XmlCreator.createElementWithAttribute(
            MainParent, "var", "type", "READONLY")
        XmlCreator.createElementWithText(parent, "name",
                                         displayTopic.get_inputField("displayName"))
        inputType = displayTopic.get_inputField("inputType")
        label = displayTopic.get_inputField("displayName")

        if(inputType == str(5)):
            label = "-"
        elif(inputType == str(7)):
            label = "--"
        elif(inputType == str(8)):
            label = "---"
        XmlCreator.createElementWithText(parent, "label", label)
