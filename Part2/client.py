import xmlrpc.client
from datetime import datetime
import threading
import time
import filecmp
import os

PORT = 3000
SERVER_PROXY = xmlrpc.client.ServerProxy(f"http://localhost:{PORT}")
CLIENT_FILES_LOCATION = "./files/client/"
SERVER_FILES_LOCATION = "./files/server/"

def upload_file_to_server(file_name):
    try:
        with open(CLIENT_FILES_LOCATION + file_name, 'rb') as file_obj:
            return SERVER_PROXY.UploadFile(file_name, xmlrpc.client.Binary(file_obj.read()))
    except OSError:
        print("\nUpload Failed.")
    return

def delete_file_from_server(file_name):
    try:
        return SERVER_PROXY.DeleteFile(file_name)
    except OSError:
        print("\nDelete Failed.")
    return

def automatic_directory_sync():
    while True:
        print(f"\n{datetime.now()} Checking for file changes.")
        dir_comparison = filecmp.dircmp(CLIENT_FILES_LOCATION, SERVER_FILES_LOCATION)
        server_only_index = 0
        client_only_index = 0
        updated_files_index = 0
        files_changed = False

        while server_only_index < len(dir_comparison.right_only):
            result = delete_file_from_server(dir_comparison.right_only[server_only_index])
            if result == "Successful":
                print("File: " + dir_comparison.right_only[server_only_index] + " deleted from server")
                server_only_index += 1
                files_changed = True
            else:
                print("Error Occurred")

        while client_only_index < len(dir_comparison.left_only):
            result = upload_file_to_server(dir_comparison.left_only[client_only_index])
            if result == "Successful":
                print("File: " + dir_comparison.left_only[client_only_index] + " uploaded to server")
                client_only_index += 1
                files_changed = True
            else:
                print("Error Occurred")

        while updated_files_index < len(dir_comparison.diff_files):
            result = upload_file_to_server(dir_comparison.diff_files[updated_files_index])
            if result == "Successful":
                print("File: " + dir_comparison.diff_files[updated_files_index] + " updated on server")
                updated_files_index += 1
                files_changed = True
            else:
                print("Error Occurred")
                
        if files_changed:
            print("Client And Server Are Now Synced")
        else:
            print("No Changes Detected, Client And Server Are On Sync.")

        time.sleep(10)

helper_thread = threading.Thread(target=automatic_directory_sync)
helper_thread.start()
