stocks = {
    'PLW': {'Playway': 316},
    'CDR': {'CD Projekt': 293},
    'TEN': {'Ten Square Games': 301}
}

cdr = stocks['CDR']
cdr['CD Projekt'] = 310


print(stocks['CDR'])