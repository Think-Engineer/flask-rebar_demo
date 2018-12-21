# -*- coding: utf-8 -*-
""" REST API - Validation schemas

    Author(s): Adam Mitchell, adam@think-engineer.com
"""

from flask_rebar import ResponseSchema, RequestSchema
from marshmallow import fields, Schema


class GetGenericGreetingSchema(ResponseSchema):
    message = fields.String(required=True)


class GetPersonalisedGreetingSchema(RequestSchema):
    name = fields.String(required=True)


class SendGreetingSchema(RequestSchema):
    name = fields.String(required=True)
    age = fields.Integer(required=True)
    height = fields.Integer(required=False)
