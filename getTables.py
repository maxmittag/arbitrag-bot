import pandas as pd
import requests
from linklist import getLinkList

def getTables(Basiswert_standart_link, issuer_id):
                            #Base Link für inline-optionen für Gold                                                     #Issuer ID für socialite generale
    LinkList = getLinkList(Basiswert_standart_link, issuer_id)
    
    table_out = pd.DataFrame()
    
    for i in LinkList:
        try:
            #aktuelle tablle von seite i
            table_actual = (pd.read_html(i))[0]
            #Tabellen zusammenfügen
            table_out = pd.concat([table_out,table_actual], ignore_index=True)
        except:
            break
        
    #Sortieren
    table_out = table_out.sort_values(['Untere Barriere'], ascending=True)
    #Bereinigen
    table_out = table_out.dropna(subset=['WKN'])
    table_out = table_out.reset_index()
    
    return(table_out)

