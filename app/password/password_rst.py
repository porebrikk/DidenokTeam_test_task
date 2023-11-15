from flask import request
from flask_restx import Resource, Namespace

from app.password.password_db import hint_model, password_model, Hint

controller = Namespace("pass_storage", path="/password")


@controller.route("/")
class HintLister(Resource):
    @controller.marshal_list_with(hint_model)
    def get(self) -> list[Hint]:
        service_name = request.args.get('service_name')
        return Hint.find_by_part(service_name)


@controller.route("/<service_name>")
class HintAPI(Resource):
    @controller.marshal_with(hint_model)
    def get(self, service_name: str) -> Hint | None:
        return Hint.find_by_name(service_name)

    @controller.response(400, "No password entered")
    @controller.expect(password_model)
    @controller.marshal_with(password_model)
    def post(self, service_name: str) -> Hint:
        password = controller.payload["password"]
        hint = Hint.find_by_name(service_name)
        if hint is None:
            if password is None:
                controller.abort(400, "No password entered")
            password = Hint.create(service_name, password)
        else:
            password = hint.update(password)
        return password
