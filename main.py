import pandas as pd
from getTables import getTables
import find_options as fo
from ranking import returnBestOptions
from main_helpfunctions import sendMSG
from main_helpfunctions import firstSteps
#from sendMSG import sendMessage


#print(data_Gold)

#hier werden Arbitrage möglichkeiten gesucht


#####Daten von find_candidates() werden wie folgt ausgegeben:
# Liste mit jeweils einem Dataframe mit zwei Zeilen, pro Listeneintrag
#                                                        [ WKN  Untere Barriere Obere Barriere  Bewertungstag  Geld Kurs Brief Kurs   Spread   Ausübungsart       Emittent
#                                                   0  SW310R   1.575,000 USD  2.225,000 USD    15.03.2024    8,080 EUR  8,280 EUR   2,415 %   Europäisch     Société Générale
#                                                   1  SW310R   1.575,000 USD  2.225,000 USD    15.03.2024    8,080 EUR  8,280 EUR   2,415 %   Europäisch     Société Générale
#                                                   0  SW310R   1.575,000 USD  2.225,000 USD    15.03.2024    8,080 EUR  8,280 EUR   2,415 %   Europäisch     Société Générale
#                                                   1  SW310R   1.575,000 USD  2.225,000 USD    15.03.2024    8,080 EUR  8,280 EUR   2,415 %   Europäisch     Société Générale
#                                                   0  SW310R   1.575,000 USD  2.225,000 USD    15.03.2024    8,080 EUR  8,280 EUR   2,415 %   Europäisch     Société Générale
#                                                   1  SW310R   1.575,000 USD  2.225,000 USD    15.03.2024    8,080 EUR  8,280 EUR   2,415 %   Europäisch     Société Générale
#                                                   0  SW310R   1.575,000 USD  2.225,000 USD    15.03.2024    8,080 EUR  8,280 EUR   2,415 %   Europäisch     Société Générale
#                                                   1  SW310R   1.575,000 USD  2.225,000 USD    15.03.2024    8,080 EUR  8,280 EUR   2,415 %   Europäisch     Société Générale
    


#    Hier optionen auf Gold ___________________________________________________________________________________________________________________
#                                                                                                                   Optionswert     Emmitent
data_G_Societe_Generale = getTables('https://www.onvista.de/derivate/Inline-Optionsscheine/Inline-Optionsscheine-auf-Goldpreis', '53159')
#data_G_DeutscheBank = getTables('https://www.onvista.de/derivate/Inline-Optionsscheine/Inline-Optionsscheine-auf-Goldpreis', '53148')
data_G_UniCredit = getTables('https://www.onvista.de/derivate/Inline-Optionsscheine/Inline-Optionsscheine-auf-Goldpreis', '53143')

data_G_Societe_Generale_Best = firstSteps(data_G_Societe_Generale)
#data_G_DeutscheBank_Best = firstSteps(data_G_DeutscheBank)
data_G_UniCredit_Best = firstSteps(data_G_UniCredit)

sendMSG("Gold", "Societe Generale", data_G_Societe_Generale_Best)
#sendMSG("Gold", "Deutsche Bank", data_G_DeutscheBank_Best)
sendMSG("Gold", "Uni Credit", data_G_UniCredit_Best)

#________________________________________________________________________________________________________________________________________________

#    Hier optionen auf Silber ___________________________________________________________________________________________________________________
data_S_Societe_Generale = getTables('https://www.onvista.de/derivate/Inline-Optionsscheine/Inline-Optionsscheine-auf-Silberpreis', '53159')
# data_S_DeutscheBank = getTables('https://www.onvista.de/derivate/Inline-Optionsscheine/Inline-Optionsscheine-auf-Silberpreis', '53148')
data_S_UniCredit = getTables('https://www.onvista.de/derivate/Inline-Optionsscheine/Inline-Optionsscheine-auf-Silberpreis', '53143')

data_S_Societe_Generale_Best = firstSteps(data_S_Societe_Generale)
#data_S_DeutscheBank_Best = firstSteps(data_S_DeutscheBank)
data_S_UniCredit_Best = firstSteps(data_S_UniCredit)

sendMSG("Silber", "Societe Generale", data_S_Societe_Generale_Best)
#sendMSG("Silber", "Deutsche Bank", data_S_DeutscheBank_Best)
sendMSG("Silber", "UniCredit", data_S_UniCredit_Best)

#________________________________________________________________________________________________________________________________________________
#data_G_DeutscheBank.to_excel("C:/Users/maxmi/OneDrive/Dokumente/Arbitrage Bot/daten.xlsx")
#data.to_csv("C:/Users/maxmi/OneDrive/Dokumente/Arbitrage Bot/daten.csv")e

#morgen to do:
#wenn oB - uB von A > oB - uB von B UND Brief_Kurs von A < Brief_Kurs von B dann Möglicher Kandidat gefunden
# -> Preis muss angepasst werden und arbitrage möglich