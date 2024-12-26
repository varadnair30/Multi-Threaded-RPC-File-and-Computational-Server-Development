# Import the necessary libraries
import asyncio
import rpyc
import os

# Define the server port
server_port = 3000

# Connect to the server
server_connection = rpyc.connect("localhost", server_port)

# Define a function for background tasks
async def simulate_background_tasks():
    start_with = 0
    end_at = 10
    while start_with < end_at:
        print(f"Simulated Background Task {start_with + 1} running ")
        await asyncio.sleep(2)
        start_with += 1

# Define a function to execute client operations
async def execute_client_operations():
    print(
        "\nList Of Available operations:\n"
        "\n 1. Add"
        "\n 2. Sort"
        "\n 3. Exit\n")

    selected_option = input("Choose any of the above options: ")

    if selected_option == "1":
        number1 = input("Enter number 1: ")
        number2 = input("Enter number 2: ")

        # Asynchronous call to the addFunction on the server
        async_add_op = rpyc.async_(server_connection.root.addFunction)
        addition_result = async_add_op(int(number1), int(number2))

        # Define an asynchronous function to check the status of the addition operation result
        async def addition_result_status(op_res):
            if op_res.ready:
                print(op_res)
                print(f"\nResult: {op_res.value}\n")
                return
            else:
                await asyncio.sleep(5)
                await addition_result_status(op_res)
        print(addition_result)
        await addition_result_status(addition_result)
    elif selected_option == "2":
        print("Hint: Enter values like this: 10, 20, 1, 3")
        array_input = input("Enter comma-separated integer values: ")
        array_input_list = list(map(int, array_input.split(',')))

        # Asynchronous call to the sortFunction on the server
        async_sort_op = rpyc.async_(server_connection.root.sortFunction)
        sorting_result = async_sort_op(array_input_list)

        print(f"\nUnsorted Array: {array_input_list}\n")

        # Define an asynchronous function to check the status of the sorting operation result
        async def sorting_result_status(op_res):
            if op_res.ready:
                print(op_res)
                print(f"\nSorted Array: {op_res.value}\n")
            else:
                await asyncio.sleep(5)
                await sorting_result_status(op_res)
        print(sorting_result)
        await sorting_result_status(sorting_result)
    elif selected_option == "3":
        os._exit(0)        
    else:
        print("\nInvalid Input")

# Define the main function
async def main_function():
    while True:
        # Run both client operations and background tasks concurrently
        await asyncio.gather(execute_client_operations(), simulate_background_tasks())

# Run the main function using asyncio
asyncio.run(main_function())