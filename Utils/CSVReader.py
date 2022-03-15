import csv

class CSVReader:
    def readCSV(self, csvFilePath):
        try:
            file = open(csvFilePath)
            next(file)
            csvReader = csv.reader(file)

            csvData = []
            for row in csvReader:
                csvData.append(row)
                #print(row)
            file.close()
            return csvData
        except FileNotFoundError:
            print("File cant be found path given: " + csvFilePath)
        except IOError:
            print("Failed or interrupted I/O operations")
        except EOFError:
            print("The end of file is reached")
        except Exception:
            print(Exception.with_traceback)
