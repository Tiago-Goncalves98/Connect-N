from operator import itemgetter


def registar_jogador(game,nome):
    checker = False
    for i in game["players"]:
        if nome == i["name"]:
            checker = True
            return "Jogador existente."
            
    if checker == False:
        player = {"name": nome, "games":0, "wins":0}
        game["players"].append(player)
        return "Jogador registado com sucesso."

def remover_jogador(game,nome):
    checker = False
    for i in game["players"]:
        if nome == i["name"]:
            checker = True
    
    if checker == False:
        return "Jogador não existente."

    elif checker == True and nome in (i.values() for i in game["currentPlayers"]):
        return "Jogador participa no jogo em curso."
                      
    else:
        for player in game["players"]:
            if nome == player["name"]:
                game["players"].remove(player)
                return "Jogador removido com sucesso."
    

def listar_jogadores(game):
    if not game["players"]:
        return "Não existem jogadores registados."
    else:
        playerlist= sorted(game["players"], key=itemgetter("name"))
        for i in playerlist:
            print( i["name"] + " " + str(i["games"]) + " " + str(i["wins"]))
    return ""
