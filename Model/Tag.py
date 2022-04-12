from Model.Document import Document

root = Document.root

class Tag:

    def __init__(self, name, children=None):
        self.name = name
        self.children = children
        self.createTag()

    def createTag(self):
        tag = root.createElement(self.name)
        self.tag = tag
        self.appendChildren()

    def appendChildren(self):
        if self.children is not None:
            for i in range(len(self.children)):
                self.tag.appendChild(self.children[i])

    def getTag(self):
        return self.tag
