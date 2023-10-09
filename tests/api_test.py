from api.user_api import UserApi, UserException
from api.json_objects import User


def test_create_user(new_user):
    user_api = UserApi()
    actual_user = user_api.get_users(new_user.id)
    expected_user = User(
        id=new_user.id,
        name="John Smith",
        gender="male",
        email="smith@test.com",
        status="active",
    )
    assert actual_user == expected_user, "User data is not equal."


def test_deactivate_user(new_user):
    user_api = UserApi()
    payload = {
        "name": "John Smith",
        "gender": "male",
        "email": "smith@test.com",
        "status": "inactive",
    }
    user_api.update_user(new_user.id, payload)
    updated_user = user_api.get_users(new_user.id)
    assert updated_user.status == payload.get("status")  # should be 'inactive'


def test_delete_user(new_user):
    user_api = UserApi()
    user_api.delete_user(user_id=new_user.id)
    try:
        user_api.get_users(user_id=new_user.id)
    except UserException as e:
        assert e.status_code == 404  # Expected for deleted user
