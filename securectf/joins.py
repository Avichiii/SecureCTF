from securectf.models import Users, Ctf, Category, UserProperties, UsersSocial
from securectf.models import Forum, Community
from securectf import db

class Joins(object):
    def __init__(self) -> None:
        pass

    def challenges(self):
        '''
        
        returns: new table containting specific columns

        '''

        # equevalent of: 
        '''
        SELECT challenge_name, points, description, uploaded_user, \
        category_name FROM Ctf, category WHERE ctf.id = category.challenge_id;
        '''
        challenges = db.session.query(
            Ctf.challenge_name,
            Ctf.points, 
            Ctf.description, 
            Ctf.uploaded_user,
            Ctf.difficulty, 
            Category.category_name
        ).join(Category, Ctf.id == Category.challenge_id)
        # join(Category,) specifies we are joining Category table with Ctf table
        
        return challenges
    

    def categories(self, category):
        '''
        returns: filtered challenges based on specific category

        '''
        challenges = self.challenges()
        filterd_challenges = []
        for challenge in challenges:
            if challenge.category_name == category:
                filterd_challenges.append(challenge)
        
        return filterd_challenges

