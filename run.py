from flask import Flask, send_from_directory
from app.models import db
from app.routes import bp
import app.config as config
import os

app = Flask(__name__, static_folder='frontend/build', static_url_path='')
app.config.from_object(config)
db.init_app(app)
app.register_blueprint(bp)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
