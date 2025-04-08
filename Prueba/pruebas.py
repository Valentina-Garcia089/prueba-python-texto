from codigo import procesar_texto
from pprint import pprint

parrafo1 = "El sol brillaba intensamente; sin embargo, una brisa suave recorría el parque, moviendo las hojas de los árboles. Niños reían, corrían y jugaban en los columpios, mientras algunos adultos, sentados en las bancas, leían o conversaban tranquilamente."

parrafo2 = "Llueve fuerte; el viento sopla, los árboles crujen."

resultado1 = procesar_texto(parrafo1)
resultado2 = procesar_texto(parrafo2)
print("------------------------------------------------------")
pprint(resultado1)
print("------------------------------------------------------")
print("\n")
print("------------------------------------------------------")
pprint(resultado2)

