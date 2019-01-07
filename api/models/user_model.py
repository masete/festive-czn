from api.models.database import DatabaseConnection


class UserAuth:
    cursor = DatabaseConnection().cursor

    def __init__(self, **kwargs):
        self.user_id = kwargs.get("user_id")
        self.first_name = kwargs.get("first_name")
        self.last_name = kwargs.get("last_name")
        self.other_names = kwargs.get("other_names")
        self.email = kwargs.get("email")
        self.phone_number = kwargs.get("phone_number")
        self.user_name = kwargs.get("user_name")
        self.password = kwargs.get("password")
        self.registered_on = kwargs.get("registered_on")
        self.is_admin = kwargs.get("is_admin")

    def add_new_user(self, user):
        self.cursor.execute(
            "INSERT INTO users(first_name, last_name, other_names, email, phone_number, "
            "user_name, password)"
            " VALUES(%s,%s,%s,%s,%s,%s,%s)", (user.first_name, user.last_name, user.other_names,
                                              user.email, user.phone_number, user.user_name,
                                              user.password))

    def get_user_by_email(self, email):
        self.cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        return self.cursor.fetchone()

    def get_user_by_id(self, user_id):
        self.cursor.execute("SELECT * FROM users WHERE user_id=%s", (user_id,))
        return self.cursor.fetchone()
