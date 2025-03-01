None

meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "CASCARITA":  "Partido de futbol",
            "SHEESH":  "ligera desaprobación",
            "CREEPY":  "aterrador, siniestro",
            "ENCHILADO":  "persona que comio mucho piccante"
            }

palabra = input("Escribe una palabra que no entiendas (con mayúsculas):")

if palabra in meme_dict.keys():
    print (meme_dict[palabra])
else:
    print("Esa palabra no esta en el diccionario")
