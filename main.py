from dotenv import load_dotenv
from routes.server import server_routes
from routes.user import user_routes
from init import myApp,init_routes

load_dotenv() #loads the env

#i can probably make a function later on to programmatically get all of the route names and put em in a dictionary.
routes = {"/user":user_routes,"/chat":server_routes}
init_routes(routes,myApp)

# will run the file if executed here
if (__name__ == "__main__"): 
    myApp.run(debug=True)