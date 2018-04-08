class helper():
    def make_scent_profile(inst, q6, q7, tag1, tag2, sillage, image_lnk, vid_lnk, start_time, description):
        return inst.app.post(
            '/scentprofile/0/0',
            data = dict(q6=q6, q7=q7, tag1=tag1, tag2=tag2, sillage=sillage, image_lnk=image_lnk, vid_lnk=vid_lnk, start_time=start_time, description=description),
        )
    def get_scent_profile(inst, q6, q7):
        return inst.app.get(
            '/scentprofile/' + q6 + '/' + q7
        )
    def put_scent_profile(inst, q6, q7, tag1, tag2, sillage, image_lnk, vid_lnk, start_time, description):
        return inst.app.put(
            '/scentprofile/0/0',
            data = dict(q6=q6, q7=q7, tag1=tag1, tag2=tag2, sillage=sillage, image_lnk=image_lnk, vid_lnk=vid_lnk, start_time=start_time, description=description),
        )
    def make_perfume(inst, name, designer, image_lnk, buy_lnk, scent_profile_id):
        return inst.app.post(
            '/perfume/hai',
            data = dict(name=name, designer=designer, image_lnk=image_lnk, buy_lnk=buy_lnk, scent_profile_id=scent_profile_id)
        )
    def get_perfume(inst, name):
        return inst.app.get(
            '/perfume/' + name
        )
    def put_perfume(inst, name, designer, image_lnk, buy_lnk, scent_profile_id):
        return inst.app.put(
            '/perfume/hai',
            data = dict(name=name, designer=designer, image_lnk=image_lnk, buy_lnk=buy_lnk, scent_profile_id=scent_profile_id)
        )
    def quiz_req(inst, q6, q7):
        return inst.app.get(
            '/quiz/' + q6 + '/' + q7,
        )    
    def get_response(inst, quantity):
        return inst.app.get(
            'response/' + quantity,
        )
