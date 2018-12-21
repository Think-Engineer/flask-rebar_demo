# -*- coding: utf-8 -*-
""" REST API - WSGI entry point

    Author(s): Adam Mitchell, adam@think-engineer.com
"""

from rest_api import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)