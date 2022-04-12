from Tag import Tag


class TagWithAttribute(Tag):

    def __init__(self, name, attributeType, attributeValue, children):
        super().__init__(name, children)
        self.attributeType = attributeType
        self.attributeValue = attributeValue
        self.AttributeSetter()

    def AttributeSetter(self):
        for i in range(len(self.attributeType)):
            self.tag.setAttribute(self.attributeType[i],self.attributeValue[i])


