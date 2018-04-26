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
    def print_error(cls, resp, status):
        if resp.status_code != status:
            resp_json = json.loads(resp.data.decode())
            print(resp_json['error_message'])

    @classmethod
    def make_notbought(cls, inst, q1, q2, q3, name):
        return inst.app.post(
                    '/notbought',
                    data = dict(q1=q1, q2=q2, q3=q3, name=name)
                )

    @classmethod
    def get_notbought(cls, inst):
        return inst.app.post(
                    '/notbought',
                )

