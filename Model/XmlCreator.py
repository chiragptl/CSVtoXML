from Model.Document import Document

root=Document.root

class XmlCreator:
     

 def createElement(parent,name):
     element=root.createElement(name)
     parent.appendChild(element)
     return element

 
 def createElementWithText(parent,name,text):
     element=root.createElement(name)
     element.appendChild(root.createTextNode(text))
     parent.appendChild(element)
     return element

 
 def createElementWithAttribute(parent,name,attribute,attributeValue):
     element = root.createElement(name)
     element.setAttribute(attribute,attributeValue)
     parent.appendChild(element)
     return element