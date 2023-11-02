

def game_starter(game,player1,player2):
    player_names = []
    for i in game["players"]:
        player_names.append(i["name"])
    
    checker = True
    if player1 not in player_names or player2 not in player_names:
        checker = False

    rules = input().lower().split(" ")
    special = input().lower().split(" ")
    length = rules[0]
    heigth = rules[1]
    wincon = rules[2]

    if  game["GameState"] == True:
        return "Existe um jogo em curso."

    elif checker == False:
        return "Jogador não registado."

    elif (int(length) // 2 ) > int(heigth) or int(heigth) > int(length):
        return "Dimensões de grelha inválidas."

    elif int(wincon) > int(length):
        return "Tamanho de sequência inválido."


    elif special[0] != "" and any(int(i) >= int(wincon) for i in special):
        return "Dimensões de peças especiais inválidas."

    else:
        playersort = []
        playersort.append(player1)
        playersort.append(player2)
        playersort.sort()
        game["GameState"] = True
        game["currentPlayers"] = [{"name": playersort[0]}, {"name": playersort[1]}]

        if special[0] != "":
            for piece in special:
                if piece not in (i for i in game["currentPlayers"]):
                    game["currentPlayers"][0].update({piece:special.count(piece)})
                    game["currentPlayers"][1].update({piece:special.count(piece)})

        game["currentGame"] = [[0 for i in range(int(length))] for j in range(int(heigth))]
        game["Wincon"] = wincon
        return f"Jogo iniciado entre {playersort[0]} e {playersort[1]}."

def show_game_results(game):
    for player in game["currentPlayers"]:
        print(player["name"])
        for key in player:
            if key != "name":
                print(key, player[key])


def forfeit(game,*args):
    player_names = []
    for i in game["players"]:
        player_names.append(i["name"])

    active_players = []
    for j in game["currentPlayers"]:
        active_players.append(j["name"])

    checkerRegistado = False
    if all(name in player_names for name in args ):
        checkerRegistado = True

    checkerParticipa = False
    if all(i in active_players for i in args):
        checkerParticipa = True


    if checkerRegistado == False:
        return "Jogador não registado."
    
    elif game["GameState"] == False:
        return "Não existe jogo em curso."

    elif checkerParticipa == False:
        return "Jogador não participa no jogo em curso."
    
    else:
        for i in game["players"]:
            for j in active_players:
                if j == i["name"]:
                    i["games"] += 1
                    if j not in args:
                        i["wins"] += 1
        game["GameState"] = False
        game["currentPlayers"] = [{"player1":None}, {"player2": None}]
        game["currentGame"] = []
        game["Wincon"] = []
        return "Desistência com sucesso. Jogo terminado."

def visualizar_resultado(game):
    if game["GameState"] == False:
        return "Não existe jogo em curso."
    else:
        board = []
        for row in game["currentGame"]:
            board.append([x for x in row])
        for i in range(1,len(game["currentGame"])+1):
            for k in range(1,len(game["currentGame"][0])+1):
                if board[i-1][k-1] == 0:
                    board[i-1][k-1] = "Vazio"
                    print(f"{i} {k} {board[i-1][k-1]}")
                else:
                    print(f"{i} {k} {board[i-1][k-1]}")
    return ""

def visualizar_grelha(game):
    if game["GameState"] == False:
        return "Não existe jogo em curso."
    else:
        board = []
        for row in game["currentGame"]:
            for i in range(len(row)):
                print(row[i],end=" ")
            print("")
    return ""

def peca_check(game,player,size):
    if int(size) != 1:
        for i in game["currentPlayers"]:
            if player == i["name"]:
                if size not in i or i[size] == 0:
                    return True
            

def player_check(game,player):
    active_players = []
    for i in game["currentPlayers"]:
        active_players.append(i["name"])

    if player not in active_players:
        return True


def win_check(game,x,y,player):
    wincon_DNE = 1
    wincon_DNW = 1
    wincon_H = 1
    wincon_V = 1
    wincon_DNE_1 = 0
    wincon_DNE_2 = 0
    wincon_DNW_1 = 0
    wincon_DNW_2 = 0
    wincon_H_1 = 0
    wincon_H_2 = 0
    wincon_V_1 = 0
    wincon_V_2 = 0
    for i in range(y-1,y+2):
        for j in range(x-1,y+2):
            if 0 <= i < len(game["currentGame"]) and 0 <= j < len(game["currentGame"][0]) and (i != y or j != x) and game["currentGame"][i][j] == player:
                if (i == y-1 and j == x+1):
                    wincon_DNE_1 = count_NE_UP(game,j,i)

                elif (i == y+1 and j == x-1):
                    wincon_DNE_2 = count_NE_DOWN(game,j,i)

                elif (i == y-1 and j == x-1):
                    wincon_DNW_1 = count_NW_UP(game,j,i)

                elif (i == y+1 and j == x+1):
                    wincon_DNW_2 = count_NW_DOWN(game,j,i)

                elif (i == y and j == x+1):
                    wincon_H_1 = count_H_RIGHT(game,j,i)

                elif (i == y and j == x-1):
                    wincon_H_2 = count_H_LEFT(game,j,i)
                
                elif (i == y+1 and j == x):
                    wincon_V_1 = count_V_DOWN(game,j,i)

                elif (i == y-1 and j == x):
                    wincon_V_2 = count_V_UP(game,j,i)
            
    wincon_DNE += (wincon_DNE_1 +  wincon_DNE_2)
    wincon_DNW += (wincon_DNW_1 + wincon_DNW_2)
    wincon_H += (wincon_H_1 + wincon_H_2) 
    wincon_V += (wincon_V_1 + wincon_V_2)
    if wincon_DNE >= int(game["Wincon"]) or wincon_DNW >= int(game["Wincon"]) or wincon_H >= int(game["Wincon"]) or wincon_V >= int(game["Wincon"]):
        return True


def count_NE_UP(game,x,y,count=1):
    final_count = count
    for i in range(y-1,y+2):
        for j in range(x-1,x+2):
            if 0 <= i < len(game["currentGame"]) and 0 <= j < len(game["currentGame"][0]) and (i == y-1 and j == x+1) and game["currentGame"][i][j] == game["currentGame"][y][x]:
                final_count += 1
                return count_NE_UP(game,j,i,final_count)     
    return final_count

def count_NE_DOWN(game,x,y,count=1):
    final_count = count
    for i in range(y-1,y+2):
        for j in range(x-1,x+2):
            if 0 <= i < len(game["currentGame"]) and 0 <= j < len(game["currentGame"][0]) and (i == y+1 and j == x-1) and game["currentGame"][i][j] == game["currentGame"][y][x]:
                final_count += 1
                return count_NE_DOWN(game,j,i,final_count)     
    return final_count

def count_NW_UP(game,x,y,count=1):
    final_count = count
    for i in range(y-1,y+2):
        for j in range(x-1,x+2):
            if 0 <= i < len(game["currentGame"]) and 0 <= j < len(game["currentGame"][0]) and (i == y-1 and j == x-1) and game["currentGame"][i][j] == game["currentGame"][y][x]:
                final_count += 1
                return count_NW_UP(game,j,i,final_count)     
    return final_count

def count_NW_DOWN(game,x,y,count=1):
    final_count = count
    for i in range(y-1,y+2):
        for j in range(x-1,x+2):
            if 0 <= i < len(game["currentGame"]) and 0 <= j < len(game["currentGame"][0]) and (i == y+1 and j == x+1) and game["currentGame"][i][j] == game["currentGame"][y][x]:
                final_count += 1
                return count_NW_DOWN(game,j,i,final_count)     
    return final_count


def count_H_RIGHT(game,x,y,count=1):
    final_count = count
    for i in range(y-1,y+2):
        for j in range(x-1,x+2):
            if 0 <= i < len(game["currentGame"]) and 0 <= j < len(game["currentGame"][0]) and (i == y and j == x+1) and game["currentGame"][i][j] == game["currentGame"][y][x]:
                final_count += 1
                return count_H_RIGHT(game,j,i,final_count)     
    return final_count

def count_H_LEFT(game,x,y,count=1):
    final_count = count
    for i in range(y-1,y+2):
        for j in range(x-1,x+2):
            if 0 <= i < len(game["currentGame"]) and 0 <= j < len(game["currentGame"][0]) and (i == y and j == x-1) and game["currentGame"][i][j] == game["currentGame"][y][x]:
                final_count += 1
                return count_H_LEFT(game,j,i,final_count)     
    return final_count



def count_V_DOWN(game,x,y,count=1):
    final_count = count
    for i in range(y-1,y+2):
        for j in range(x-1,x+2):
            if 0 <= i < len(game["currentGame"]) and 0 <= j < len(game["currentGame"][0]) and (i == y+1 and j == x) and game["currentGame"][i][j] == game["currentGame"][y][x]:
                final_count += 1
                return count_V_DOWN(game,j,i,final_count)     
    return final_count

def count_V_UP(game,x,y,count=1):
    final_count = count
    for i in range(y-1,y+2):
        for j in range(x-1,x+2):
            if 0 <= i < len(game["currentGame"]) and 0 <= j < len(game["currentGame"][0]) and (i == y-1 and j == x) and game["currentGame"][i][j] == game["currentGame"][y][x]:
                final_count += 1
                return count_V_UP(game,j,i,final_count)     
    return final_count


def winner_winner_chicken_dinner(game,winner,loser):
    for i in game["players"]:
        if i["name"] == winner:
            i["games"] +=1
            i["wins"] += 1
        elif i["name"] == loser:
            i["games"] +=1



def colocar_peca(game,player,size,position,direction= None):
    
    player_ref = []
    for i in game["currentPlayers"]:
        player_ref.append(i["name"])

    length = len(game["currentGame"][0])
    heigth = len(game["currentGame"])

    if game["GameState"] == False:
        return "Não existe jogo em curso."

    elif player_check(game,player):
        return "Jogador não participa no jogo em curso."

    elif peca_check(game,player,size):
        return "Tamanho de peça não disponível."

    elif direction == "D" and (int(position)-1) + int(size) > length:
        return "Posição irregular."

    elif direction == "E" and (int(position)-1)- int(size) < -1:
        return "Posição irregular."
    
    else:

        if int(size) == 1:
            count = 1
            for row in range(heigth-1,-1,-1):
                if game['currentGame'][row][int(position)-1] == 0:
                    game['currentGame'][row][int(position)-1] = player
                    count -= 1
                    if win_check(game,int(position)-1,row,player):
                        for i in player_ref:
                            if i != player:
                                loser = i
                        winner_winner_chicken_dinner(game,player,loser)
                        print("Sequência conseguida. Jogo terminado.")
                        game["GameState"] = False
                        game["currentPlayers"] = []
                        game["currentGame"] = []
                        game["Wincon"] = None
                        break
                    else:
                        return "Peça colocada."
                        
        
        else:
            if direction == "D" and int(size) != 1:
                count = int(size)
                for column in range(int(position)-1,(int(position)-1)+int(size)):
                    previous = -1
                    for row in range(heigth-1,-1,-1):
                        if game['currentGame'][row][column] == 0 and count > 0 and previous != column:
                            game['currentGame'][row][column] = player
                            previous = column
                            count -=1
                            if win_check(game,column,row,player):
                                for i in player_ref:
                                    if i != player:
                                        loser = i
                                winner_winner_chicken_dinner(game,player,loser)
                                print("Sequência conseguida. Jogo terminado.")
                                game["GameState"] = False
                                game["currentPlayers"] = []
                                game["currentGame"] = []
                                game["Wincon"] = None
                                break

                for current in game["currentPlayers"]:
                    if current["name"] == player:
                        current[size] -= 1
                print("Peça colocada.")
                            
                        
            elif direction == "E" and int(size) != 1:
                count = int(size)
                for column in range(int(position)-1,(int(position)-1-int(size)),-1):
                    previous = -1
                    for row in range(heigth-1,-1,-1):
                        if game['currentGame'][row][column] == 0 and count > 0 and previous != column:
                            game['currentGame'][row][column] = player
                            previous = column
                            count -= 1
                            if win_check(game,column,row,player):
                                for i in player_ref:
                                    if i != player:
                                        loser = i
                                winner_winner_chicken_dinner(game,player,loser)                           
                                print("Sequência conseguida. Jogo terminado.")
                                game["GameState"] = False
                                game["currentPlayers"] = []
                                game["currentGame"] = []
                                game["Wincon"] = None
                                break
                for current in game["currentPlayers"]:
                    if current["name"] == player:
                        current[size] -= 1                                             
                print("Peça colocada.")
    return ""
