# -*- coding: utf-8 -*-
""" REST API - Endpoint routing

    Author(s): Adam Mitchell, adam@think-engineer.com
"""
from flask import current_app, request
from flask_rebar import HeaderApiKeyAuthenticator, Rebar, response

from rest_api.schemas import *


authenticator = HeaderApiKeyAuthenticator(header='X-MyApp-ApiKey')
authenticator.register_key(key='my-super-secret-key')

rebar = Rebar()
registry = rebar.create_handler_registry()


@registry.handles(
    rule='/generic_greeting',
    method='GET',
    marshal_schema={200: GetGenericGreetingSchema()},
    authenticator=authenticator
)
def getGenericGreeting():
    return ({'message': 'Hello, Generic Person!'}, 200)


@registry.handles(
    rule='/personalised_greeting',
    method='GET',
    marshal_schema={200: GetGenericGreetingSchema()},
    query_string_schema=GetPersonalisedGreetingSchema(),
    authenticator=authenticator
)
def getPersonalisedGreeting():
    name = rebar.validated_args['name']

    return ({'message': f'Hello, {name}'}, 200)


@registry.handles(
    rule='/send_greeting',
    method='POST',
    marshal_schema={201: SendGreetingSchema()},
    request_body_schema=SendGreetingSchema(),
    authenticator=authenticator
)
def sendGreeting():
    greeting = rebar.validated_body

    return (greeting, 201)