import pandas as pd
from src.ship import Ship
from src.cargo import Cargo
from src.cruise import Cruise 
def main() -> None:

    barcos_csv=[]
    df = pd.read_csv('ships.csv', delimiter=',')

    barcos = []
    for indice, fila in df.iterrows():
      draft=fila['draft']
      crew=fila['crew']
      if(fila['extra']==''):
        aux_ship=Ship(draft, crew)
        barcos.append(aux_ship)
      else:
        extra=fila['extra']
      if(fila['quality']==''):
        aux_cruise=Cruise(draft, crew, extra)
        barcos.append(aux_cruise)
      else:
        quality=fila['quality']
        aux_cargo=Cargo(extra, quality, draft, crew)
        barcos.append(aux_cargo)
    for barco in barcos:
      try:
        barco.is_worth_it()
      except Exception as e:
        print("ERROR:", str(e))
      else:
        print("Merece ser saqueado")
  

if __name__ == "__main__":
  main()
