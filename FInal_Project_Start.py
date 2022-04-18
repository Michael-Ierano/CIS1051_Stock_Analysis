def openRead(fileName):
    #this function will open and read a file
    newfile = open(fileName, "r")
    filelst =  newfile.readlines()

    return filelst

Yr2020 = {}
Yr2019 = {}
newNew = openRead("Disney_FS.CSV")

def fileToDict(fileName):
    #This function turns a file into a dictionary of values
    for line in fileName[2:]:
        linelst = line.split(",")
        #print(linelst)
        
        Yr2020[linelst[0]] = float(linelst[1])
        Yr2019[linelst[0]] = float(linelst[2])


    return True

fileToDict(newNew)
#print(Yr2020)
#print(Yr2019)
def FinancialAnalysis(aDictionary):
    #This Function takes in a dictionary and performs ratio analysis
    profitMargin = aDictionary["Net income (loss)"]/aDictionary["Revenues"]

    return "Profit Margin:", round(profitMargin,4)
print(FinancialAnalysis(Yr2019))

