import pandas as pd

def find_candidates(data, Testmode):
    output = []
    numberOfUniqueLowerBarrier = len(data['Untere Barriere'].unique())
    uniqueBarriers = data['Untere Barriere'].unique()
    
    i = 0
    while i < numberOfUniqueLowerBarrier:
        filtered_df = pd.DataFrame()
        filtered_df = data[data['Untere Barriere'] == uniqueBarriers[i]]
        filtered_df = filtered_df.drop(columns=['Merkmale', 'Info', 'index'])
        output.append(filtered_df)
        i += 1
    
    return(find_strikes(output, Testmode))

         
def extract_Dollars_for_Barriers(x):
    
    x = x.replace(".","")
    x = x.replace(",", ".")
    x = x.split(" ", 1)
    x = x[0]
    x = float(x)
    return x

def extract_Dollars_for_Kurs(x):
    x = x.replace(",", ".")
    x = x.split(" ",1)
    x = x[0]
    x = float(x)
    return x

#returnt None wenn nix gefunden wurde
#gibt arbitrageoptionen paarweise mit index 0 und 1 wieder
def find_strikes(data, Testmode):
    emmitent = data[0].iloc[0,8]
    #Testen
    if Testmode:
        #Die folgenden Zeilen sind nur zum testen gedacht
        data[0].iat[1,5] = "0,200 EUR"
        print(data[0])
        #print(data)
        #bis hierhin____________________________________
        
    strikes = []
    length_data_entries = len(data)
    i = 0
    while i < length_data_entries:
        gefundeneStrikes = find_strikes_internal(data[i], i, emmitent)
        if(gefundeneStrikes != None):
            #Hier Änderungen 17:29 FR
            strikes.extend(gefundeneStrikes)
        i+=1
    else:
        pass
    if(len(strikes)>0):
        return strikes

def find_strikes_internal(data, Liste, emmitent):
    #erstmal einfach mit erster Liste machen
    strikes = []
    i=0
    while i<(len(data)-1):
        j=i+1
        while j<len(data):
            #wichtiger vergleich hier:
            #Bewertungstage Vergleiche
            BewertungstagA = str(data.iloc[i,3])
            BewertungstagB = str(data.iloc[j,3])
            #Obere Barriere vergleichen
            ObereBarriereA = extract_Dollars_for_Barriers(data.iloc[i,2])
            ObereBarriereB = extract_Dollars_for_Barriers(data.iloc[j,2])
            #Untere Barriere vergleichen
            UntereBarriereA= extract_Dollars_for_Barriers(data.iloc[i,1])
            UntereBarriereB= extract_Dollars_for_Barriers(data.iloc[j,1])
            #Brief Kurs vergleichen
            BriefKursA     = extract_Dollars_for_Kurs(data.iloc[i,5])
            BriefKursB     = extract_Dollars_for_Kurs(data.iloc[j,5])
            #Geld Kurs vergleichen
            GeldKursA = extract_Dollars_for_Kurs(data.iloc[i,4])
            GeldKursB = extract_Dollars_for_Kurs(data.iloc[j,4])
            if(BewertungstagB == BewertungstagA and ObereBarriereB-UntereBarriereB > ObereBarriereA-UntereBarriereA and BriefKursB < GeldKursA and BriefKursB != 0 and GeldKursB != 0):
                #print("TREFFEER in Liste " + str(Liste) + "!!!")
                strikeer = pd.concat([data.iloc[[i]], data.iloc[[j]]], ignore_index=True)
                strikes.append(strikeer) #strikes = pd.concat([strikes, strikeer], ignore_index=True)
                #nur damit daten nicht falschrum sind
            if(BewertungstagA == BewertungstagB and ObereBarriereA-UntereBarriereA > ObereBarriereB-UntereBarriereB and BriefKursA < GeldKursB and BriefKursA != 0 and GeldKursB != 0):
                #print("TREFFEER in Liste " + str(Liste) + "!!!")
                strikeer = pd.concat([data.iloc[[j]], data.iloc[[i]]], ignore_index=True)
                strikes.append(strikeer)  #strikes = pd.concat([strikes, strikeer], ignore_index=True)
            else:
                #print("leider keiner gefunden")
                pass
            j+=1 
        i+=1
    if(len(strikes)== 0):
        pass
        #print("In Liste " + str(Liste) + " nix gefunden.               Emittent: " + str(emmitent))
    else:
        return strikes