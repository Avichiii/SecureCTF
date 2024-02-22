from securectf.joins import Joins
from securectf.models import UserProperties, Users

class Rank(object):
    def __init__(self) -> None:
        self.profiles = Joins()

    def ranking(self):
        users = []
        for profile in self.profiles.profiles():
            if profile.rank == 999999:
                return
            
            dic = {}
            total_points = 0
            user_obj = Users.query.filter_by(username=profile.username).first()
            for challenge_obj in user_obj.completed_challenges: 
                total_points += challenge_obj.points
            
            dic['username'] = profile.username
            dic['points'] = total_points

            users.append(dic)
        
        users_ = sorted(users, key=lambda val: val['points'])

        for index, user_dic in enumerate(users_):
            user_id = Users.query.filter_by(username=user_dic['username']).first()
            UserProperties.query.filter_by(user_id=user_id.id).update({'rank': index})

