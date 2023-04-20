from flask_app import app
from flask_app.controllers import character_controller
from flask_app.controllers import navigation_contoller
if __name__=='__main__':
    app.run(debug=True)
app.secret_key = 'secret'