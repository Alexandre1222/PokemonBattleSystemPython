from pokemon import pokemon

def inicio():
  print("Método Inicio foi chamado")
  
print("Bem-vindo ao pokemon battle system.")
print("Deseja jogar?")
jogar = int(input("1 - Sim \n2 - Não\n"))

while jogar == 1:
  inicio()
