import json
from flask import Flask
from flask.views import MethodView
from flask import request, jsonify
from duoFinder import find_queue_players, find_player_para_jogar_comigo

app = Flask(__name__)


@app.route('/')
def helloWorld():
    return 'Hello puta'

class PlayerView(MethodView):

    def get(self, name=None):
        if not name:
            player_name = request.args.get('summonerName', None)
            if player_name:
                return find_queue_players(player_name)
            return jsonify({})
        else:
            # import pdb; pdb.set_trace()
            player = find_queue_players(name).json
            return find_player_para_jogar_comigo(player)


    


app.add_url_rule(
    '/players/',
    view_func=PlayerView.as_view('player_view'),
    methods=['GET']
)

app.add_url_rule(
    '/players/<name>',
    view_func=PlayerView.as_view('player_matches'),
    methods=['GET']
)



