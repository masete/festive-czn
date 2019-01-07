from flask.views import MethodView
from flask import request, jsonify
from api.models.user_model import UserAuth

auth = UserAuth()


class UserView(MethodView):

    def post(self):
        data = request.get_json()

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        other_names = data.get("other_names")
        email = data.get("email")
        phone_number = data.get("phone_number")
        user_name = data.get("user_name")
        password = data.get("password")

        exists = auth.get_user_by_email(email)
        if exists:
            return jsonify({"message": "user already exists, just login"})

        user = UserAuth(first_name=first_name, last_name=last_name, other_names=other_names, email=email,
                        phone_number=phone_number, user_name=user_name, password=password)

        auth.add_new_user(user)
        response_object = {
            'status': '201',
            'message': 'New user has been created',
            'data': auth.get_user_by_email(email)
        }

        return jsonify(response_object), 201

    def get(self):

        data = request.get_json()

        email = data.get("email")
        password = data.get("password")

        login = auth.get_user_by_email(email)

        if not login:
            return jsonify({"message": "first register to login, thanks"})
        return jsonify({"message": "you logged in successfully"})









