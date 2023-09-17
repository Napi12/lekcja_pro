meme_dict ={
    "LOL" : "odpowiedź na coś zabawnego",
    "CRINGE" : "coś dziwnego lub wstydliwego",
    "ROFL" : "odpowiedź na żart",
    "SHEESH" : "lekka dezaprobata",
    "CREEPY" : "straszny, złowieszczy",
    "AGGRO" : "stać się agresywnym/zły",
}

name = input("wpisz słowo urzywaj wielkich liter")
if word in meme_dict.keys():
    print (word, ":" ,meme_dict[name])
    
else:
    print("nie znam takiego kontaktu")
