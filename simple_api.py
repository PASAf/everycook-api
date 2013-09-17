#!/usr/bin/env python
from sqlalchemy.ext.declarative import declarative_base, DeferredReflection
#from sqlalchemy import Column, Float, Integer
#from sqlalchemy import String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from sqlalchemy.orm import relationship
import flask.ext.restless

engine = create_engine(
    'mysql://root:root@localhost/ec',
    encoding='ISO-8859-1',
    convert_unicode=True)
Base = declarative_base(cls=DeferredReflection)


class RecipeTypes(Base):
    __tablename__ = 'recipe_types'
    

class RecToCoi(Base):
    __tablename__ = 'rec_to_coi'


class Ingredients(Base):
    __tablename__ = 'ingredients'


class Steps(Base):
    __tablename__ = 'steps'


class Recipes(Base):
    __tablename__ = 'recipes'

Base.prepare(engine)

from flask import Flask
#from flask import request, session, g, redirect, url_for, \
     #abort, render_template, flash, jsonify

app = Flask(__name__)
app.config.from_object(__name__)
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
manager = flask.ext.restless.APIManager(app, session=session)

manager.create_api(RecipeTypes, methods=['GET'])
manager.create_api(Recipes, methods=['GET'])
manager.create_api(Steps, methods=['GET'])
manager.create_api(Ingredients, methods=['GET'])
manager.create_api(RecToCoi, methods=['GET'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
