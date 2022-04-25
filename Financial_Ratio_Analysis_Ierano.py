#TITLE: Financial Ratio Analysis
#Name: Michael Ierano
#Year: Spring 2022
from unittest import skip

def openRead(fileName):
    #this function will open and read a file
    newfile = open(fileName, "r")
    filelst =  newfile.readlines()

    return filelst

# Initialize Dictionaries and Variable for Analysis
Apple2020 = {}
Apple2019 = {}
AppleRatio20 = {}
AppleRatio19 = {}
Micro2020 = {}
Micro2019 = {}
MicroRatio20 = {}
MicroRatio19 = {}
Google2020 = {}
Google2019 = {}
GoogleRatio20 = {}
GoogleRatio19 = {}
Ibm2020 = {}
Ibm2019 = {}
IbmRatio20 = {}
IbmRatio19 = {}
IndAverage20 = {}
IndAverage19 = {}
apple = ''
mirco = ''
google = ''
ibm = ''
AppleScore = 0
MicrosoftScore = 0
GoogleScore = 0
IBMScore = 0
apple = openRead("AppleFS.CSV")
micro = openRead("MicrosoftFS.CSV")
google = openRead("GoogleFS.CSV")
ibm = openRead("IBMFS.CSV")
#print(ibm)

def fileToDict(fileName, dict, dict1):
    #This function turns a file into a dictionary of values
    for line in fileName[1:]:
        linelst = line.split(",")
        #print(linelst)
        
        dict[linelst[0]] = float(linelst[1])
        dict1[linelst[0]] = float(linelst[2])


    return dict , dict1

fileToDict(apple, Apple2020, Apple2019)
fileToDict(micro, Micro2020, Micro2019)
fileToDict(google, Google2020, Google2019)
fileToDict(ibm, Ibm2020, Ibm2019)

#print(Apple2020)
#print(Micro2020)
#print(Google2020)
#print(Apple2020, Micro2020, Google2020, Ibm2020)

def FinancialAnalysis(inDictionary, outDictionary):
    #This Function takes in a dictionary, computes ratios, and converts ratios into new dictionary
    outDictionary["Profitability Ratios       "] = 0
    outDictionary["profitMargin"] = round(inDictionary["Net income"]/inDictionary["Revenue"],3)
    outDictionary["grossMargin"] = round(inDictionary["Gross margin"]/inDictionary["Revenue"],3)
    outDictionary["operatingMargin"] = round(inDictionary["Operating income"]/inDictionary["Revenue"],3)
    outDictionary["ROA       "] = round(inDictionary["Net income"]/inDictionary["Total assets"],3)
    outDictionary["ROE       "] = round(inDictionary["Net income"]/inDictionary["Total equity"],3)
    outDictionary["Liquidity & Solvency Ratios      "] = 0
    outDictionary["currentRatio"] = round(inDictionary["Total current assets"]/inDictionary["Total current liabilities"],3)
    outDictionary["quickRatio"] = round((inDictionary["Total Cash & Marketable Securities"]+inDictionary["Accounts receivable net"])/inDictionary["Total current liabilities"],3)
    outDictionary["cashRatio"] = round(inDictionary["Total Cash & Marketable Securities"]/inDictionary["Total current liabilities"],3)
    outDictionary["Leverage"] = round(inDictionary["Total assets"]/inDictionary["Total equity"],3)
    outDictionary["debtToEquity"] = round(inDictionary["Total liabilities"]/inDictionary["Total equity"],3)
    outDictionary["LTdebtToEquity"] = round(inDictionary["Total non-current liabilities"]/inDictionary["Total equity"],3)
    outDictionary["debtToAssets"] = round(inDictionary["Total liabilities"]/inDictionary["Total assets"],3)
    outDictionary["Turnover Ratios & Operational Efficiency  "] = 0
    outDictionary["ARTurnover"] = round(inDictionary["Revenue"]/inDictionary["Accounts receivable net"], 3)
    outDictionary["daysInAR"] = round(365/outDictionary["ARTurnover"],3)
    outDictionary["InvTurnover"] = round(inDictionary["Cost of sales"]/inDictionary["Inventories"],3)
    outDictionary["daysInINV"] = round(365/outDictionary["InvTurnover"],3)
    outDictionary["operatingCycle"] = round(outDictionary["daysInINV"] + outDictionary["daysInAR"],3)
    outDictionary["totalAssetTurn"] = round(inDictionary["Revenue"]/inDictionary["Total assets"],3)
    

    return outDictionary
#print(FinancialAnalysis(Apple2020, AppleRatio20))
#print(FinancialAnalysis(Apple2019, AppleRatio19))
#print(FinancialAnalysis(Micro2020, MicroRatio20))
#print(FinancialAnalysis(Google2020, GoogleRatio20))
#print(FinancialAnalysis(Ibm2020, IbmRatio20))
#YtoY = (AppleRatio20["currentRatio"] - AppleRatio19["currentRatio"])/AppleRatio19["currentRatio"]
#print(round(YtoY,4))
FinancialAnalysis(Apple2019, AppleRatio19)
FinancialAnalysis(Apple2020, AppleRatio20)
FinancialAnalysis(Micro2020, MicroRatio20)
FinancialAnalysis(Micro2019, MicroRatio19)
FinancialAnalysis(Google2020, GoogleRatio20)
FinancialAnalysis(Google2019, GoogleRatio19)
FinancialAnalysis(Ibm2020, IbmRatio20)
FinancialAnalysis(Ibm2019, IbmRatio19)

def industryAverage():
    # This Function Creates new Ratio Dictionaries from the average of all companies ratios in each year
    for k in AppleRatio20:
        if AppleRatio20[k] == "Profitability Ratios" or AppleRatio20[k] == "Liquidity & Solvency Ratios" or AppleRatio20[k] == "Turnover Ratios":
            pass
        else:
            IndAverage20[k] = round((AppleRatio20[k] + MicroRatio20[k] + GoogleRatio20[k] + IbmRatio20[k])/4,3)

    for k in AppleRatio19:
        if AppleRatio19[k] == "Profitability Ratios" or AppleRatio19[k] == "Liquidity & Solvency Ratios" or AppleRatio19[k] == "Turnover Ratios":
            pass
        else:
            IndAverage19[k] = round((AppleRatio19[k] + MicroRatio19[k] + GoogleRatio19[k] + IbmRatio19[k])/4,3)

    return IndAverage20, IndAverage19

industryAverage()
#print(IndAverage20)
#print(IndAverage19)

def ratioAnalysis(firmName):
    #This function compares 2020 ratios for the selected company aganist 2019 and industry averages for each year
    # Creates a score based on if company ratios are higher then the previous year and idustry averages
    FirmScore = 0
    firmName = firmName.lower()
    if firmName == "apple":
        LiveDictionary = AppleRatio20
        LastYear = AppleRatio19
    elif firmName == "microsoft":
        LiveDictionary = MicroRatio20
        LastYear = MicroRatio19
    elif firmName == "google":
        LiveDictionary = GoogleRatio20
        LastYear = GoogleRatio19
    elif firmName == "ibm":
        LiveDictionary = IbmRatio20
        LastYear = IbmRatio19
    #print(LiveDictionary)
    #print(LastYear)
    for k in LiveDictionary:
        if LiveDictionary[k] == "Profitability Ratios" or LiveDictionary[k] == "Liquidity & Solvency Ratios" or LiveDictionary[k] == "Turnover Ratios":
            pass
        if LiveDictionary[k] > LastYear[k]:
            FirmScore += 1
        if LiveDictionary[k] > IndAverage20[k]:
            FirmScore += 1
        if LastYear[k] > IndAverage19[k]:
            FirmScore += 1
    firmName = firmName.upper()
    print(f"Finacial Ratios: 2020 & 2019")
    for k in LiveDictionary:
        print(k, LiveDictionary[k], LastYear[k],sep='\t')
    print("")
    print(firmName, "has", FirmScore, "ratios above last years numbers or the idustry averages for 2020 and 2019.\n")
    if FirmScore >= 27:
        print(firmName, "financial ratios are higher, on average, than than the rest of the idustry.\n")
        print("This makes", firmName, "a good investment for the future.\n")
    elif FirmScore < 27:
        print(firmName, "financial ratios are lower, on average, than the rest of the industry.\n")
        print("This makes", firmName, "a risky investment for the future. Try a different company.\n")
    
    
    

    return firmName , FirmScore
# print(ratioAnalysis("Apple"))
# print(ratioAnalysis("Microsoft"))
# print(ratioAnalysis("Google"))
# print(ratioAnalysis("IBM"))

#ratioAnalysis("Apple")
#ratioAnalysis("IBM")
done = False
while not done:
    company = input("What company do you want to Analyize? \nEnter Apple, Microsoft, Google, or IBM:")
    company = company.lower()
    while company != "apple" and company != "microsoft" and company != "google" and company != "ibm":
        company = input("Please enter a valid Company: Apple, Microsoft, Google, or IBM:")
        company = company.lower()
    ratioAnalysis(company)
    OtherCompany = input("Would you lile to try another company? Enter Y/Yes/N/No:")
    OtherCompany = OtherCompany.lower()
    if OtherCompany == 'y' or OtherCompany == 'yes':
        pass
    else:
        print("Hope this was helpful, try again soon!")
        done = True


