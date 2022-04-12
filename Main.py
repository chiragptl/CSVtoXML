from Utils.CSVReader import CSVReader
from XMLGenerator import XmlGenerator
from Model.Document import Document
from Utils.FileWriter import FileWriter


reader = CSVReader()
path="Calculator-meta-data-Sheet1.csv"
listOfRows = reader.readCSV(path)                   #reading
XmlGenerator.Generator(listOfRows)                  #generating
xmlData = Document.root.toprettyxml(indent="\t")
FileWriter.writeFile(xmlData)                       #writing
print(xmlData)

    
    

    
