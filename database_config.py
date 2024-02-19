from pydoc import describe
from unicodedata import category
from securectf import db, app
from securectf.models import Users, UserProperties, UsersSocial
from securectf.models import Ctf, Community, Category, Forum

with app.app_context():
    db.drop_all()
    db.create_all()

    # users
    samual = Users(
        username="samual sanchese",
        email="samual@gmail.com",
        password="noteasypasssword"
    )

    rick = Users(
        username="rick sanchese",
        email="rick@gmail.com",
        password="supereasypasssword"
    )

    # properties
    samual_properties = UserProperties(
        bio="software engineer",
        level=10,
        rank=2000,
        user_id=1
    )

    rick_properties = UserProperties(
        bio="kernal developer",
        level=10,
        rank=1000,
        user_id=2
    )

    # social
    samual_social = UsersSocial(
        linkedin="linkedin.com\\samual",
        github="github.com\\samual",
        youtube="youtube.com\\samual",
        website="samual.com",
        user_id=1
    )

    rick_social = UsersSocial(
        linkedin="linkedin.com\rick",
        github="github.com\rick",
        youtube="youtube.com\rick",
        website="rick.com",
        user_id=2
    )

    db.session.add_all([samual, rick, samual_properties, rick_properties, samual_social, rick_social])
    db.session.commit()


    for user in Users.query.all():
        print(user)
    
    crackme = Ctf(
        challenge_name='crackme$',
        points=50,
        description='x86-64 binary',
        uploaded_user='samual'
    )

    decryptme = Ctf(
        challenge_name='decryptme$',
        points=50,
        description='cryto is easy',
        uploaded_user='rick'
    )

    db.session.add_all([crackme, decryptme])
    db.session.commit()

    samual.completed_challenges.append(crackme)
    rick.completed_challenges.append(crackme)
    rick.completed_challenges.append(decryptme)

    db.session.commit()

    print(crackme.pawned_challenges)
    
    reverse_engineering = Category(
        category_name="reverse engineering",
        challenge_id=1
    )

    binary_exploitation = Category(
        category_name="binary exploitation",
        challenge_id=2
    )

    db.session.add_all([reverse_engineering, binary_exploitation])
    db.session.commit()


    executable = Forum(
        message="executable is not workig",
        user_id=1
    )

    windows = Forum(
        message="windows dll isnt working aswell",
        user_id=2
    )

    db.session.add_all([executable, windows])
    db.session.commit()

    crackme_solution = Community(
        header="crackme$ solution",
        link="https://github.com/samual",
        username=samual.username,
        challenge=crackme.challenge_name
    )

    db.session.add(crackme_solution)
    db.session.commit()