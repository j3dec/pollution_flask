class BaseConfig(object):
    # TODO : check  https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
    #  https://blog.miguelgrinberg.com/post/how-to-add-flask-migrate-to-an-existing-project/page/2
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost:5432/pollutiondb3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
