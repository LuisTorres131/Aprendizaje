#Primera practica
nivel_de_toner_Epson = 75
if nivel_de_toner_Epson < 15:
    print("Nivel de toner bajo, por favor cambiar")
#Segunda practica
nivel_de_toner_Canon = 100
if nivel_de_toner_Canon < 15:
    print("Nivel de toner bajo, por favor cambiar")
elif nivel_de_toner_Canon < 50:
    print("Nivel de toner menos de la mitad, planificar compra")
else: 
    print("Nivel de toner OK")
#Tercera practica
nivel_de_toner_HP = 48
if nivel_de_toner_HP < 15:
    print("Nivel de toner bajo, por favor cambiar")
elif nivel_de_toner_HP < 50:
    print("Nivel de toner menos de la mitad, planificar compra")
else: 
    print("Nivel de toner OK")