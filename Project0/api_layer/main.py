"""This module contains the code for my api"""
from flask import Flask, jsonify, request

from custom_exceptions.bad_account_info import BadAccountInfo
from custom_exceptions.id_not_found import IdNotFound
from dal_layer.account_dao.account_doa_imp import AccountDAOImp
from entities.account_class_information import Account
from entities.withdraw_class_information import Withdraw
from service_layer.account_services.account_service_imp import AccountServiceImp

"""
for this application I am going to be making a RESTful web service. REST stands for Representational State Transfer,
and it is a popular way of structuring web application. RESTful webservice inputs (think HTTP Requests) and outputs
(think HTTP Responses) are in a machine friendly format (think JSONa0.
There are 6 differnet constraints to restful web services that help to both guide your development process and that
help you maintain a true RESTful web service.

1. Client-Server architecture
    RESTful web services are not complete applications: they do not handle ANY client logic. your RESTful web service
    should not handle the creating of the request to your service, byt it can handle the response for the request
    that is made

2. Stateless
    RESTful web services do nto keep track of clients: any tracking is handled client-side

3. Cacheable
    information may be cached client side to speed up operations

4. Uniform Interface
    Resources handled by a RESTful web service should easily be identified by the Uniform Resource Identifier
    (URL) that is provided.
    Example uniform URI: GET/ customer/1/account/5 should get the information form account 10 belonging to customer
    identified by the number 2

5. Layerd System
    RESTful web services should be able to call other RESTful web services

6. (optional) Code on Demand
    RESTful web services may return executable code. This si not a common practice, and so it is an optional
    constraint


"""

app: Flask = Flask(__name__)
account_dao = AccountDAOImp()
account_service = AccountServiceImp(account_dao)

"""
TO maintain a uniform interface, I will be using the path "/accounts" for all request to my application that have to
do with account data. I can use different verbs to determine what I am doing with an account data, and that is how Flask
will know what particular service method needs to be called

"""


@app.route("/accounts", methods=["POST"])
def create_account():
    try:
        account_data: dict = request.get_json()
        account = Account(account_data["accountId"], account_data["accountBalance"], account_data["clientId"])
        result = account_service.service_create_account(account)
        result_dictionary = result.convert_to_dictionary()
        result_json = jsonify(result_dictionary)
        return result_json, 201
    except BadAccountInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


@app.route("/teams/<id>", methods=["GET"])
def get_account_by_id(id: int):
    try:
        result: Account = account_service.service_get_account_by_id(id)
        result_dictionary = result.convert_to_dictionary()
        return jsonify(result_dictionary), 200

    except BadAccountInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


app.run()
