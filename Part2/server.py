from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn as CreateThread
import os

PORT = 3000
SERVER_FILES_LOCATION = "./files/server/"

class CustomXMLRPCServer(CreateThread, SimpleXMLRPCServer):
    pass

def upload_file_to_server(file_name: str, file_data):
    try:
        location = os.path.join(SERVER_FILES_LOCATION, file_name)
        with open(location, 'wb') as file_obj:
            file_obj.write(file_data.data)
        return "Successful"
    except OSError:
        print(f"\nInvalid File: {file_name}")
        return "Error Occurred"

def delete_file_from_server(file_name: str):
    try:
        os.remove(os.path.join(SERVER_FILES_LOCATION, file_name))
        print(f"\nFile: {file_name} deleted.")
        return "Successful"
    except OSError:
        print(f"\nInvalid File: {file_name}")
        return "Error Occurred"

with CustomXMLRPCServer(('localhost', PORT), allow_none=True) as server:
    server.register_introspection_functions()
    server.register_function(upload_file_to_server, "UploadFile")
    server.register_function(delete_file_from_server, "DeleteFile")
    
    print(f"Server is running on {PORT}")
    server.serve_forever()
