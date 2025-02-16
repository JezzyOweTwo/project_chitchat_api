from flask import Blueprint
server_routes = Blueprint('server_routes', __name__)

# @server_routes.route('/server', methods=['GET'])
# def get_active_connections():
#     return {"message": "List of users"}