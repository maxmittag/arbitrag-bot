import pandas as pd
from find_options import extract_Dollars_for_Kurs

def returnBestOptions(data):
    bestArbitrage = 0
    bestArbitrage_index = 0
    length = 0
    try:
        length = len(data)
    except TypeError:
        return None
    i = 0
    while i < length:
        BriefKA = extract_Dollars_for_Kurs(data[i].iloc[0,5])
        BriefKB = extract_Dollars_for_Kurs(data[i].iloc[1,5])
        min = None
        max = None
        if(BriefKA < BriefKB):
            min = BriefKA
            max = BriefKB
        else:
            min = BriefKB
            max = BriefKA
        
        if (max-min)>bestArbitrage:
            bestArbitrage = max-min
            bestArbitrage_index = i
        i+=2
    return data[bestArbitrage_index]
        