from asyncio import constants
from Model.XmlCreator import XmlCreator
from Model.Document import Document
from Model.Constants import Constants
from Utils.HelperFunctions import HelperFunctions

MainParent = Document.parent


class ChoiceXmlCreator:

    def create(displayTopic):
        inputType = Constants.CHOICE
        if(displayTopic.get_inputField(Constants.INPUTTYPE) == str(3)):
            inputType = Constants.CHOICES
        
        parent = XmlCreator.createElementWithAttribute(
            MainParent, Constants.VAR, "type", inputType)

        XmlCreator.createElementWithText(parent, Constants.NAME, HelperFunctions.getCamelCasing(
            displayTopic.get_inputField(Constants.DISPLAYNAME)))
        XmlCreator.createElementWithText(
            parent, Constants.LABEL, displayTopic.get_inputField(Constants.DISPLAYNAME))
        XmlCreator.createElementWithText(parent, Constants.DEFAULT, "")

        if(displayTopic.get_inputField(Constants.HELP) != ""):
            XmlCreator.createElementWithText(
                parent, Constants.HELP, displayTopic.get_inputField(Constants.HELP))

        choices = displayTopic.get_inputField(Constants.INPUTVALUE).split("|")
        values = displayTopic.get_inputField(Constants.CALCULATIONONLY).split("|")
        
        for choice, value in zip(choices, values):
            parent1 = XmlCreator.createElement(parent, Constants.CHOICES)
            XmlCreator.createElementWithText(parent1, Constants.LABEL, choice)
            XmlCreator.createElementWithText(parent1, Constants.VALUE, value)
