#create list of lists
def getLinkList(base_link, IDissuer):
    issuer_vortext = '?idIssuer='
    link_first_page = base_link + issuer_vortext + IDissuer
    link_list = [link_first_page]
    
    i = 1
    while i<=10:
        #https://www.onvista.de/derivate/Inline-Optionsscheine/Inline-Optionsscheine-auf-Goldpreis?page=1&idIssuer=53159
        url_loop = base_link + '?page='
        url_seite = str(i)
        url_issuer = '&idIssuer=' + IDissuer
        url_loopable = url_loop + url_seite + url_issuer
        link_list.append(url_loopable)
        i+=1
    return(link_list)
