from api.models.database import DatabaseConnection


class RedModel:
    cursor = DatabaseConnection().cursor

    def __init__(self, **kwargs):
        self.flag_id = kwargs.get("flag_id")
        self.created_by = kwargs.get("created_by")
        self.flag_title = kwargs.get("flag_title")
        self.flag_location = kwargs.get("flag_location")
        self.flag_comment = kwargs.get("flag_comment")
        self.created_on = kwargs.get("created_on")
        self.flag_status = kwargs.get("flag_status")
        self.flag_image = kwargs.get("flag_image")
        self.flag_video = kwargs.get("flag_video")

    def add_new_flag(self, flag):
        self.cursor.execute("INSERT INTO redflags(created_by, flag_title, flag_location, flag_comment, flag_status, "
                            "flag_image, flag_video)"
                            " VALUES(%s,%s,%s,%s,%s,%s,%s)", (flag.created_by, flag.flag_title, flag.flag_location,
                                                              flag.flag_comment, flag.flag_status, flag.flag_image,
                                                              flag.flag_video))

    def get_flag_by_id(self, flag_id):
        self.cursor.execute("SELECT * FROM redflags WHERE flag_id=%s", (flag_id,))
        return self.cursor.fetchone()

    def get_flag_by_title(self, flag_title):
        self.cursor.execute("SELECT * FROM redflags WHERE flag_title=%s", (flag_title,))
        return self.cursor.fetchone()

    def get_specific_flag(self, flag_id):
        self.cursor.execute("SELECT * FROM redflags WHERE flag_id=%s", (flag_id,))
        return self.cursor.fetchone()

    def get_all_flags(self):
        self.cursor.execute("SELECT * FROM redflags")
        return self.cursor.fetchall()

    def delete_flag(self, flag_id):
        query = self.cursor.execute("DELETE FROM redflags WHERE flag_id=%s", (flag_id,))
        return query

    def update_location(self, flag_id, flag_location):
        self.cursor.execute("UPDATE redflags SET flag_location=%s WHERE flag_id=%s", (flag_location, flag_id))
        self.cursor.execute("SELECT * FROM redflags WHERE flag_id=%s", (flag_id,))
        return self.cursor.fetchone()

    def update_comment(self, flag_id, flag_comment):
        self.cursor.execute("UPDATE redflags SET flag_comment=%s WHERE flag_id=%s", (flag_comment, flag_id))
        self.cursor.execute("SELECT * FROM redflags WHERE flag_id=%s", (flag_id,))
        return self.cursor.fetchone()









