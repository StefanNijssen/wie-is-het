geel = input("Is de kaas geel?")
gaten = input("Zitten er gaten in?")
schimmel = input("heeft de kaas blauwe schimmel?")
korst = input("heeft de kaas een korst?")
duur = input("is de kaas belachelijk duur?")
hard = input("is de kaas hard als steen?")

if geel == "ja":
    if gaten == "ja":
        if duur == "ja":
            print("Emmenthaler")
        elif duur == "nee":
            print("Leerdammer")
    elif gaten == "nee":
        if hard == "ja":
            print("Parmigiano Reggiano")
        elif hard == "nee":
            print("Goudse kaas")
elif geel == "nee":
    if schimmel == "ja":
        if korst == "ja":
            print("Bleu de Rochbaron")
        elif korst == "nee":
            print("Foume d'Ambert")
    elif schimmel == "nee":
        if korst == "ja":
            print("Camembert")
        elif korst == "nee":
            print("Mozzarella")
