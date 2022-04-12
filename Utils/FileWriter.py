
class FileWriter:
    @staticmethod
    def writeFile(xmlData):
        save_path_file = "calculator.xml"
        with open(save_path_file, "w") as f:
            f.write(xmlData)
