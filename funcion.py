
        
        
import csv

def guardar_o_modificar(categoria, jugador, puntos):
    archivo = "jugadas.csv"

    try:
        # Intento leer el archivo (si existe)
        planilla = {}

        with open(archivo, "r", newline="", encoding="utf-8") as f:
            lector = csv.reader(f)
            next(lector)  # salteo encabezado

            for fila in lector:
                planilla[fila[0]] = [int(fila[1]), int(fila[2])]

    except FileNotFoundError:
        # Si no existe, creo planilla inicial en 0
        planilla = {
            "E": [0, 0],
            "F": [0, 0],
            "P": [0, 0],
            "G": [0, 0],
            "1": [0, 0],
            "2": [0, 0],
            "3": [0, 0],
            "4": [0, 0],
            "5": [0, 0],
            "6": [0, 0]
        }

    # 🔥 Modifico el puntaje
    if jugador == 1:
        planilla[categoria][0] += puntos
    else:
        planilla[categoria][1] += puntos

    # 🔥 Reescribo el archivo completo
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["Categoria", "Jugador 1", "Jugador 2"])

        for cat in planilla:
            escritor.writerow([cat, planilla[cat][0], planilla[cat][1]]) 
            
guardar_o_modificar('E', 1, 10)
        
    