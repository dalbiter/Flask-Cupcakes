from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import text
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'secret-key'
app.config['DEBUG_TB_INTERECEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_index():
    return '<body>hello</body>'

@app.route('/api/cupcakes')
def list_cupcakes():
    """respond with JSON list of cupcakes"""

    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes/<int:cid>')
def find_cupcake(cid):
    """return JSON for selected cupcake by id"""

    cupcake = db.session.get(Cupcake, cid)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """create new cupcake"""

    new_cupcake = Cupcake(flavor=request.json["flavor"],
                          size=request.json["size"],
                          rating=request.json["rating"],
                          image=request.json["image"])
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(cupcake=new_cupcake.serialize()), 201)