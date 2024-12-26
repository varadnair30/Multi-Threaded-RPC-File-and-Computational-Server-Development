from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn as CreateThread
import xmlrpc.client
import os

PORT = 3000
SERVER_DATA_LOCATION = "./files/server/"

class CustomXMLRPCServer(CreateThread, SimpleXMLRPCServer):
    pass

def upload_file_to_server(file_name: str, file_data):
    try:
        location = os.path.join(SERVER_DATA_LOCATION, file_name)
        with open(location, 'wb') as file:
            file.write(file_data.data)        
    except OSError:
        print(f"\nInvalid File: {file_name}")
        return "Error Occurred"
    return "Successful"

def download_file_from_server(file_name: str):
    try:
        location = os.path.join(SERVER_DATA_LOCATION, file_name)
        with open(location, 'rb') as file:
            return xmlrpc.client.Binary(file.read())
    except OSError:
        print(f"\nInvalid File: {file_name}")
        return "Error Occurred"

def delete_file_from_server(file_name: str):
    try:
        os.remove(os.path.join(SERVER_DATA_LOCATION, file_name))
        print(f"\nFile: {file_name} deleted.")
    except OSError:
        print(f"\nInvalid File: {file_name}")
        return "Error Occurred"
    return "Successful"

def rename_file_in_server(old_file_name: str, new_file_name: str):
    try:
        os.rename(os.path.join(SERVER_DATA_LOCATION, old_file_name),
                  os.path.join(SERVER_DATA_LOCATION, new_file_name))
        print(f"\nFile: {old_file_name} has been renamed to {new_file_name}.")
    except OSError:
        print(f"\nInvalid File: {old_file_name}")
        return "Error Occurred"
    return "Successful"


with CustomXMLRPCServer(('localhost', PORT), allow_none=True) as server:
    server.register_introspection_functions()
    server.register_function(upload_file_to_server, "UploadFile")
    server.register_function(download_file_from_server, "DownloadFile")
    server.register_function(rename_file_in_server, "RenameFile")
    server.register_function(delete_file_from_server, "DeleteFile")
        
    print(f"Server is running on the {PORT}...")
    server.serve_forever()
