import json
from flask.views import MethodView
from flask import request, jsonify

def loadData():
    with open('../LoLPlayers.json', 'r') as json_file:
        dados = json.load(json_file)
    json_file.close()
    return dados

def find_queue_players(name):
    dados = loadData()
    for dado in dados:
        if dado['summonerName'] == name:
            player = dado
            return jsonify(player)
    return {}

def find_player_para_jogar_comigo(player_dict):
    dados = loadData()
    player_elo = player_dict['tier']
    jogadores_encontrados = []
    for dado in dados:
        if dado['tier'] == player_elo:
            jogadores_encontrados.append(dado)
    return jsonify(jogadores_encontrados)
            

    






# print(dados)
# elo = None
# listaDePlayersComMesmoElo = []


        

# print(elo)

# def capturaPlayers:
#     for dado in dados:
#         if dado['tier'] == elo:
#             listaDePlayersComMesmoElo.append(dado)
#     return 

# print(listaDePlayersComMesmoElo) 

# for jogador in listaDePlayersComMesmoElo:
#     if jogador['summonerName'] != 'Zoldyck Kilua':
#         print(jogador['summonerName'])
     
    
