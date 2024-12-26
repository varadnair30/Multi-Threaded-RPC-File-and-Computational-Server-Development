import xmlrpc.client
import os
import threading

port = 3000

rpc_server = xmlrpc.client.ServerProxy(f"http://localhost:{port}")

def additionSync(n1, n2):
    addOp = rpc_server.additionFunction(n1, n2)
    print(f"\n{n1} + {n2} = {addOp}")
    return

def sortSync(input_list):
    sortOp = rpc_server.sortFunction(input_list)
    print(f"\nSorted: {sortOp}")
    return

def execute_client_operations():
    while True:
        print(
            "\n\nAvailable Operations:\n"
            "\n 1. Add"
            "\n 2. Sort"
            "\n 3. Exit\n")
        
        option = input("Please select an option: ")
        
        if option == "3":
            os._exit(0)
        elif option == "1":
            input1 = input("Enter Number 1: ")
            input2 = input("Enter Number 2: ")
                        
            additionSync(int(input1), int(input2))
        elif option == "2":
            print("Example:-> Enter values like this: 40,30,-2,0,8")
            array_input = input("Enter comma separated integer values: ")
            array_values = list(map(int, array_input.split(',')))
            
            sortSync(array_values)
        else:
            print("\nInvalid Input")

main_thread = threading.Thread(target=execute_client_operations)
main_thread.start()
