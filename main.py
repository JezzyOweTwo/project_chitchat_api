from flask import Flask
from routes.server import server_routes
from routes.user import user_routes
from routes.errors import init_errorHandler as errorHandler
from routes.errors import throw
myApp = Flask(__name__)

#initalizes the error handler
errorHandler(myApp)

# middleware to pass all 'server' requests to server route
myApp.register_blueprint(server_routes, url_prefix='/server')

# middleware to pass all 'user' requests to the user route
myApp.register_blueprint(user_routes, url_prefix='/user')

# if neither of the middlewares of activated, the route could not be located
@myApp.route('/<path:path>', methods=['GET', 'POST'])
@myApp.route('/', methods=['GET', 'POST'])
def not_found(path): throw(404)

if (__name__ == "__main__"): 
    myApp.run(debug=True)