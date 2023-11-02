from controllers.func_registros import registar_jogador, listar_jogadores, remover_jogador
from controllers.gamerules import game_starter,forfeit, visualizar_resultado,colocar_peca,show_game_results
from controllers.save_load import save, load

def main():
    game = {
    "players": [],

    "GameState": False, 

    "currentPlayers": [], 

    "currentGame":[],
    
    "Wincon": None
    }

    while True:
        try:
            line = input()
        except EOFError:
            break
        

        commands = line.split(" ")

        if commands[0] == "RJ" and len(commands) == 2:
            nome = commands[1]
            r = registar_jogador(game,nome)
            if r != "":
                print(r)
        
        elif commands[0] == "EJ" and len(commands) == 2:
            nome = commands[1]
            r = remover_jogador(game,nome)
            if r != "":
                print(r)
        
        elif commands[0] == "LJ" and len(commands) == 1:
            r = listar_jogadores(game)
            if r != "":
                print(r)

        elif commands[0] == "IJ" and len(commands) == 3:
            player1 = commands[1]
            player2 = commands[2]
            r = game_starter(game,player1,player2)
            if r != "":
                print(r)
        
        elif commands[0] == "DJ" and len(commands) == 1:
            # r = game_details(game)
            # if r != "":
            #     print(r)
            if game["GameState"] == False:
                print("Não existe jogo em curso.")
            else:
                print(len(game["currentGame"][0]), len(game["currentGame"]))
                show_game_results(game)
        
        elif commands[0] == "D" and len(commands) == 2:
            player1 = commands[1]
            r = forfeit(game,player1)
            if r != "":
                print(r)
        
        elif commands[0] == "D" and len(commands) == 3:
            player1 = commands[1]
            player2 = commands[2]
            r = forfeit(game,player1,player2)
            if r != "":
                print(r)
        
        elif commands[0] == "CP" and len(commands) == 4:
            player = commands[1]
            size = commands[2]
            position = commands[3]
            r = colocar_peca(game,player,size,position)
            if r != "":
                print(r)
        
        elif commands[0] == "CP" and len(commands) == 5:
            player = commands[1]
            size = commands[2]
            position = commands[3]
            direction = commands[4]
            r = colocar_peca(game,player,size,position,direction)
            if r != "":
                print(r)

        elif commands[0] == "V" and len(commands) == 1:
            r = visualizar_resultado(game)
            if r != "":
                print(r)

        elif commands[0] == "G" and len(commands) == 2:
            file_name = commands[1]
            r = save(game,file_name)
            if r != "":
                print(r)

        elif commands[0] == "L" and len(commands) == 2:
            file_name = commands[1]
            r = load(game,file_name)
            if r != None:
                game = r
                print("Jogo carregado.")
            else:
                print("Ocorreu um erro no carregamento.")

        elif commands[0]== "status":
            for line in game["currentGame"]: 
                print(line)
        else:
            print("Instrução inválida.")