# import SimpleXMLRPCRequestHandler and SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# import config
from config import *

# Create class requestHandler
class RequestHandler(SimpleXMLRPCRequestHandler):
    # Limit on path only "/RPC2" 
    rpc_paths = (CONFIG_PATH)

# Create variabel version_server
version_server = VERSION_SERVER

# Display version server
print("The version on this server is " + str(version_server))

# Create server
rpcServer = SimpleXMLRPCServer((CONFIG_IP_ADDRESS, CONFIG_PORT), requestHandler=RequestHandler)

# Register function "register_introspection_functions()"
rpcServer.register_introspection_functions()

# Create function "updated_version()" for check version server
def check_version_server(version_client):
    if version_client == version_server:
        return True
    else:
        return False

# Create function to return version server
def get_new_version_server():
    return version_server

# Register function
rpcServer.register_function(check_version_server, 'check_version_server')
rpcServer.register_function(get_new_version_server, 'get_new_version_server')

# Running server
rpcServer.serve_forever()