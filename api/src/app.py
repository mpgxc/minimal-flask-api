import requests
from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
app.config["DEBUG"] = True

api = Api(app)


@app.route('/api/user/<username>', methods=['GET'])
def index(username):
    """
    Retorna json contendo os dados do perfil do github!
    """

    github_profile = f'https://api.github.com/users/{username}'

    response_github_user = requests.get(github_profile)

    return jsonify(result=response_github_user.json())

@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"message": "Essa rota não existe!",
                    "error": str(error)}), 404
