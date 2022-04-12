class HelperFunctions:

    def getCamelCasing(name):
        splitNameUsingSpace = name.split(" ")
        name = splitNameUsingSpace[0][:1].lower()+splitNameUsingSpace[0][1:]
        for i in range(1,len(splitNameUsingSpace)-1):
            name = name + (splitNameUsingSpace[i][:1].upper())+(splitNameUsingSpace[i][1:])
        return name
