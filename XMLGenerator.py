from Model.DisplayTopic import Topic
from Model.ChoiceXmlCreator import ChoiceXmlCreator
from Model.ReadOnlyXmlCreator import ReadOnlyXmlCreator
from Model.FloatXmlCreator import FloatXmlCreator


class XmlGenerator:
    @staticmethod
    def Generator(listOfRows):
        for inputField in listOfRows:
            displayTopic = Topic(inputField)
            inputType = int(displayTopic.get_inputField("inputType"))
            if(inputType == 1):
                ChoiceXmlCreator.create(displayTopic)
            elif(inputType == 2):
                FloatXmlCreator.create(displayTopic)
            elif(inputType == 3):
                ChoiceXmlCreator.create(displayTopic)
            elif(inputType == 4):
                ReadOnlyXmlCreator.create(displayTopic)
            elif(inputType == 5):
                ReadOnlyXmlCreator.create(displayTopic)
            elif(inputType == 6):
                ReadOnlyXmlCreator.create(displayTopic)
            elif(inputType == 7):
                ReadOnlyXmlCreator.create(displayTopic)
            elif(inputType == 8):
                ReadOnlyXmlCreator.create(displayTopic)

            del displayTopic
