from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username",
        type=str,
        required=True,
        help="This Field is required"
    )
    parser.add_argument("password",
        type=str,
        required=True,
        help="This Field is required"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"message": "User with username Already Exists"}, 400
        print(**data)
        user = UserModel(**data)
        user.save_to_db()
        return {"message": "User Created Successfully"}, 201