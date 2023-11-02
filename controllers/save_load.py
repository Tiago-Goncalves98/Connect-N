import pickle

def save(game,NomeFicheiro):
    try:
        with open(NomeFicheiro,'wb') as f:
            pickle.dump(game,f)
            return "Jogo gravado."
    except Exception:
        return "Ocorreu um erro na gravação."

def load(game,NomeFicheiro):
    try:
        with open(NomeFicheiro,'rb') as f:
            game = pickle.load(f)
            return game
    except Exception:
        return None