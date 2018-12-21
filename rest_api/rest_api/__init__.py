# -*- coding: utf-8 -*-
""" REST API

    Author(s): Adam Mitchell, adam@think-engineer.com
"""

from rest_api.routes import rebar
from flask import Flask

app = Flask(__name__)
rebar.init_app(app)

import rest_api
