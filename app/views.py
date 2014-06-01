#========================================
#views.py
#lead (and only) developer: Bobby Joe 3.0
#========================================

# -*- coding: utf-8 -*-

from app import app
from flask import render_template

@app.route('/')
def index():
	return render_template('flask_skeleton.html')
