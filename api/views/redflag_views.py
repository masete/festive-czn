from flask import request, jsonify
from flask.views import MethodView
from api.models.redflag_models import RedModel


model = RedModel()


class FlagViews(MethodView):

    def post(self):

        data = request.get_json()
        created_by = data.get("created_by")
        flag_title = data.get("flag_title")
        flag_location = data.get('flag_location')
        flag_comment = data.get('flag_comment')
        flag_status = data.get("flag_status")
        flag_image = data.get("flag_image")
        flag_video = data.get("flag_video")

        new_record = RedModel(created_by=created_by, flag_title=flag_title,
                              flag_location=flag_location, flag_comment=flag_comment, flag_status=flag_status,
                              flag_image=flag_image, flag_video=flag_video)
        model.add_new_flag(new_record)
        response_object = {
            'status': '201',
            'message': 'Redflag has been created',
            'data': model.get_flag_by_title(flag_title)
        }

        return jsonify(response_object), 201

    def get(self, flag_id=None):
        if flag_id:
            flag = model.get_flag_by_id(flag_id)
            if not flag:
                return jsonify({"message": "the red flag with that id does not exist"})
            return jsonify({"message": model.get_specific_flag(flag_id)})

        flag1 = model.get_all_flags()
        if not flag1:
            return jsonify({"message": "first add red flags"})
        return jsonify({"flags": flag1})

    def delete(self, flag_id):

        record = model.get_flag_by_id(flag_id)
        if not record:
            return jsonify({"message": "the flag your trying to delete does not exist"})
        deleted = model.delete_flag(flag_id)
        response_object = {
            'status': '201',
            'message': 'red flag has been deleted',
            'data': deleted
        }

        return jsonify(response_object), 201

    # def put(self, flag_id, flag_location):
    #     data = request.get_json()
    #
    #     if ('type' not in data) and ('payload' not in data):
    #         return jsonify({"message": "missing fields"})
    #
    #     self.type = data['payload']
    #
    #     # for type1 in data:
    #     if type == data['type']:
    #         updated = model.update_location(flag_id, flag_location)
    #         return jsonify({"status": "200",
    #                         "message": "flag location has been updated",
    #                         "data": updated})
            # else: flag_comment is data['type']
            #     updated1 = model.update_comment(flag_id, self.flag_comment)
            #     return jsonify({"status": "200",
            #                     "message": "flag comment has been updated",
            #                     "data": updated1})

        # flag_location = data.get("flag_location")

        # updated = model.update_location(flag_id, flag_location)
        # return jsonify({"sttus": "200",
        #                "message": "flag location has been updated",
        #                "data": updated})

    # if ('type' not in data) and ('payload' not in data):
    #     return ErrorFeedback.missing_key

    # self.red_flag_type = data['payload']
    # single_record = [record.__dict__ for record in self.red.redflags if record.__dict__['red_flag_id']
    #                  == red_flag_id]

    # if not single_record:
    #     return jsonify({"message": "no record"}), 400
    # single_record[0][data['type']] = data['payload']
    # return jsonify({"status": "200", "data": [{"edited redflag": single_record, "message":
    #     "red flag record has been edited"}]})

# def put(self, flag_id):
    #     data = request.get_json()
    #
    #     flag_comment = data.get("flag_comment")
    #
    #     updated1 = model.update_comment(flag_id, flag_comment)
    #     return jsonify({"status": "200",
    #                     "message": "flag comment has been updated",
    #                     "data": updated1})






