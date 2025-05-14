from flask import Blueprint, request, jsonify
from .models import db, Player, Match, PlayerMatch

bp = Blueprint('routes', __name__)

@bp.route('/create-match', methods=['POST'])
def create_match():
    data = request.json
    team_a = data['team_a']  # list of names
    team_b = data['team_b']
    winner = data['winner_team']  # 'A' or 'B'

    match = Match(winner_team=winner)
    db.session.add(match)
    db.session.commit()

    def add_players(team, team_name):
        for name in team:
            player = Player.query.filter_by(name=name).first()
            if not player:
                player = Player(name=name)
                db.session.add(player)
                db.session.commit()
            result = 'win' if winner == team_name else 'loss'
            pm = PlayerMatch(match_id=match.id, player_id=player.id, team=team_name, result=result)
            db.session.add(pm)

    add_players(team_a, 'A')
    add_players(team_b, 'B')
    db.session.commit()

    return jsonify({'message': 'Match recorded!'}), 201
