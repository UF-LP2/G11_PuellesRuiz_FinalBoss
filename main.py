from src.ship import Ship
from src.cargo import Cargo
from src.cruise import Cruise 
def main() -> None:
  #try:
   # archivo=open("ships.csv","r")
  #except FileNotFoundError:
   # print("Hubo un error al leer el archivo")
    #leer archivo y cargarlo en el vector barcos
    barco1=Ship(10,1)
    barco2=Cruise(1,10,1)
    barco3=Cargo(2,1,10,1)
    barcos=[barco1, barco2, barco3]
    for barco in barcos:
      try:
        barco.is_worth_it()
      except Exception as e:
        print("ERROR:", str(e))
      else:
        print("Merece ser saqueado")


if __name__ == "__main__":
  main()
