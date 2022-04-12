from xml.dom import minidom
from Model.Constants import Constants


class Document:
  root=minidom.Document()
  parent=root.createElement(Constants.FORM)
  root.appendChild(parent)




