from pokemon import pokemon


def inicio():
  pokemonPlayer = pokemon("Charizard", 100)
  pokemonEnemy = pokemon("Squirtle", 50)
  
  trocar  = int(input("Antes de iniciarmos a batalha deseja trocar o nome do seu " + pokemonPlayer.nome + "?\n"))
  if trocar == 1:
    nomeNovo = input("Coloque o novo nome do seu pokemon: ")
    pokemonPlayer.nome = nomeNovo
    print("O nome do seu pokemon agora se chama " + pokemonPlayer.nome)
  else:
    print("Tudo bem então, vamos continuar a batalha")
  print("==========================") 
  print("Vai " + pokemonPlayer.nome + " eu escolho você")
  print("Acaba com ele " + pokemonPlayer.nome)
  print("==========================") 

  while pokemonPlayer.Hp > pokemonEnemy.Hp or pokemonPlayer.Hp < pokemonEnemy.Hp:
    Hud(pokemonPlayer.nome, pokemonPlayer.Hp, pokemonEnemy.nome, pokemonEnemy.Hp)
    
print("------------------------------------")
print("Bem-vindo ao pokemon battle system.")
print("Deseja jogar?")
jogar = int(input("1 - Sim \n2 - Não\n"))


while jogar == 1:
  inicio()
