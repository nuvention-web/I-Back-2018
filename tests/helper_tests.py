import json

class helper():

    @classmethod
    def make_card(cls, inst, name, accord, image_lnk, vid_lnk, start_time, description):
        return inst.app.post(
                    '/card/all',
                    data = dict(name=name, accord=accord, image_lnk=image_lnk, vid_lnk=vid_lnk, start_time=start_time, description=description)
                )

    @classmethod
    def get_card(cls, inst, mode):
        return inst.app.get(
                    '/card/' + mode,
                )

    @classmethod
    def delete_card(cls, inst, name):
        return inst.app.delete(
                    '/card/' + name,
                )
    
    @classmethod
    def edit_card(cls, inst, card_id, name, accord, image_lnk, vid_lnk, start_time, description):
        return inst.app.put(
                    '/card/' + str(card_id),
                    data = dict(name=name, accord=accord, image_lnk=image_lnk, vid_lnk=vid_lnk, start_time=start_time, description=description)
                )

    @classmethod
    def print_error(cls, resp, status):
        if resp.status_code != status:
            resp_json = json.loads(resp.data.decode())
            print(resp_json)

    @classmethod
    def make_notbought(cls, inst, q1, q2, q3, name, quiz_id):
        return inst.app.post(
                    '/notbought/' + str(quiz_id),
                    data = dict(q1=q1, q2=q2, q3=q3, name=name)
                )

    @classmethod
    def get_notbought(cls, inst, mode):
        return inst.app.get(
                    '/notbought/' + mode,
                )
                
    @classmethod
    def delete_notbought(cls, inst, _id):
        return inst.app.delete(
                    '/notbought/' + _id,
                )
             
    @classmethod
    def make_bought(cls, inst, q1, q2, q3, email, name, quiz_id):
        return inst.app.post(
                    '/bought/' + str(quiz_id),
                    data = dict(q1=q1, q2=q2, q3=q3, name=name, email=email)
               )

    @classmethod
    def get_bought(cls, inst, mode):
        return inst.app.get(
                    '/bought/' + mode,
                )
    
    @classmethod
    def delete_bought(cls, inst, _id):
        return inst.app.delete(
                    '/bought/' + _id,
                )
