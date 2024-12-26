import xmlrpc.client
import os
import threading

PORT = 3000
CLIENT_DATA_LOCATION = "./files/client/"

server_proxy = xmlrpc.client.ServerProxy(f"http://localhost:{PORT}")

def upload_file_to_server(file_name):
    try:
        location = os.path.join(CLIENT_DATA_LOCATION, file_name)
        with open(location, 'rb') as file:
            server_proxy.UploadFile(file_name, xmlrpc.client.Binary(file.read()))
        print(f"\nFile '{file_name}' uploaded from client to server.")
    except OSError:
        print("\nUpload Failed.")

def download_file_from_server(file_name):
    try:
        location = os.path.join(CLIENT_DATA_LOCATION, file_name)
        binary_data = server_proxy.DownloadFile(file_name)
        if binary_data is not None and binary_data != 'Error Occurred' and binary_data.data is not None:
            with open(location, 'wb') as file:
                file.write(binary_data.data)
            print(f"\nFile '{file_name}' downloaded from server to client.")
        else:
            print(f"\nDownload Failed: File '{file_name}' not found on the server or there was an error during download.")
    except OSError:
        print("\nDownload Failed.")

def delete_file_from_server(file_name):
    try:
        result = server_proxy.DeleteFile(file_name)
        if result == "Successful":
            print(f"\nFile '{file_name}' deleted on server.")
        else:
            print(f"\nFile Deletion Failed, please check the filename")
    except OSError:
        print("\nDelete Failed.")

def rename_file_in_server(old_file_name, new_file_name):
    try:
        result = server_proxy.RenameFile(old_file_name, new_file_name)
        if result == "Successful":
            print(f"\nFile '{old_file_name}' has been renamed to '{new_file_name}'.")
        else:
            print(f"\nFile Rename Failed, please check the filename")
    except OSError:
        print(f"\nInvalid File: {old_file_name}")

def start_client_execution():
    while True:
        print(
            "\n\n***********Available Operations******************\n"
            "\n 1. Upload the files"
            "\n 2. Download the files"
            "\n 3. Delete the files"
            "\n 4. Rename the files"
            "\n 5. Exit the files\n"
        )

        selected_option = input("Please choose desired operation number: ")

        if selected_option == "1":
            entered_file_name = input("File Name With Extension: ")
            upload_file_to_server(entered_file_name)
        elif selected_option == "2":
            entered_file_name = input("File Name With Extension: ")
            download_file_from_server(entered_file_name)
        elif selected_option == "3":
            entered_file_name = input("File Name With Extension: ")
            delete_file_from_server(entered_file_name)
        elif selected_option == "4":
            old_file_name = input("Old File Name With Extension: ")
            new_file_name = input("New File Name With Extension: ")
            rename_file_in_server(old_file_name, new_file_name)
        elif selected_option == "5":
            os._exit(0)
        else:
            print("\nYou entered Invalid Input !")

master_thread = threading.Thread(target=start_client_execution)
master_thread.start()
