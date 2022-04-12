from Model.XmlCreator import XmlCreator
from Model.Document import Document

MainParent=Document.parent


class FloatXmlCreator:
 def create(displayTopic):
     parent=XmlCreator.createElementWithAttribute(MainParent,"var","type","FLOAT")
     XmlCreator.createElementWithText(parent,"name",displayTopic.get_inputField("displayName"))
     XmlCreator.createElementWithText(parent,"label",displayTopic.get_inputField("displayName"))
     if(displayTopic.get_inputField("helpText")!=""):
       XmlCreator.createElementWithText(parent,"help",displayTopic.get_inputField("helpText"))