# import library xmlrpc client
import xmlrpc.client

# import config file
from config import *

# Create proxy to client
rpcServer = xmlrpc.client.ServerProxy(CONFIG_URL)

# Create variabel version_client
version_client = VERSION_CLIENT

# Display version client
print("The version on this client is " + str(version_client))

confirmationInput = input("Do you want to update version (Y/N)? ")
while confirmationInput == "Y":
    print()
    print("Checking version from server...")
    
    # Display version server
    print("The version on server is " + str(rpcServer.get_new_version_server()))
    print()

    # Checking version server and version client
    if rpcServer.check_version_server(version_client):
        print("Client already with the latest version")
    else:
        # Updated version client
        version_client = rpcServer.get_new_version_server()
        print("Updated version from server...")
        print("The version on this client is " + str(version_client))
          
    confirmationInput = input("Do you want to update version again (Y/N)? ")


if confirmationInput == "N":
    # Cancel updated version client
    print("Cancel updated version from server...")
    print("The version on this client is " + str(version_client))
else:
    print("Updated version client error")


