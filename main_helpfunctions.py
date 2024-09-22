from sendMSG import sendMessage
import find_options as fo
from ranking import returnBestOptions

def sendMSG(Basiswert, Emmitent, data):
    firstMSG = "Beste Option " + Basiswert + " " + Emmitent
    #print(firstMSG)
    #print(data)
    sendMessage(firstMSG)
    sendMessage(data)
    return

def firstSteps(rawData):
    betterData = fo.find_candidates(rawData, False)
    BestOption = returnBestOptions(betterData)
    return BestOption