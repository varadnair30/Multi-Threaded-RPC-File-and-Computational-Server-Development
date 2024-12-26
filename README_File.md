Multi-Threaded File Server and Computational Server

This project introduces a multi-threaded file server and a computational server that communicate using Python's Remote Procedure Call (RPC) mechanism.

Requirements:

1. Python3
2. rpyc Library( "pip install rpyc" Run this command for installing rpyc )

Instructions:
1. Unzip the Project: Begin by extracting the project zip file to a specific folder.
2. Open Terminals: Launch two distinct terminal windows.
3. Set the project directory: Use the following command to navigate to the project root directory in both terminals. Replace "YOUR PROJECT ROOT DIRECTORY" with the path to your individual project's root directory.

cd YOUR PROJECT ROOT DIRECTORY

Part 1 Execution:

1. Set the Directory: Use the command below to navigate to Part 1 in both terminals.
   CD Part1

2. Run Server: To start the server, enter the following command on one of the terminals.
   Python Server.py

3. Launch the client in another terminal using the following command: python client.py.

4. Client Operations: Using the client terminal, choose the desired operation: upload, download, delete, or rename.

5. Follow directions: To commence the desired operation, follow the directions presented in the terminal.

6. Check Directories: Check the server (./Part1/files/server) and client (./Part1/files/client) directories for file modifications caused by the conducted action.


Part 2 Execution:

1. Run the following command in both terminals to set the directory: access Part2.
   CD: Part 2

2. Run Server: This command will start the server on one terminal.
   Python server.py

3. Run Client: Use the following command in another terminal: python client.py

4. Client Logs: Check the client terminal for logs that detail modifications made to files in the server directory.

5. Check Directories: Inspect the server (./Part2/files/server) and client (./Part2/files/client) directories to validate file changes that correspond to the conducted action, as presented in the client terminal.

Part 3 Execution:

Synchronous:

1. Set the Directory: Use the following command to navigate to Part3\synchronous in both terminals.
   cd Part 3\synchronous

2. Run Server: Start the server on one terminal using this command.
   Python Server.py

3. Launch the client in another terminal using the following command: python client.py.

4. Client Operations: Using the client terminal, choose the operation to be performed: Add or Sort.

5. Follow directions: To commence the desired operation, follow the directions presented in the terminal.

6. Check Client Terminal: Examine the client terminal for the result of the conducted procedure.

Asynchronous:

1. Use the Set Directory command to navigate to Part3\asynchronous in both terminals.
   cd Part3\Asynchronous

2. Run Server: This command starts the server in a single terminal.
   Python Server.py

3. Launch the client in another terminal using the following command: python client.py.

4. Client Operations: Using the client terminal, choose the operation to be performed: Add or Sort.

5. Follow directions: To commence the desired operation, follow the directions presented in the terminal.

6. Check Client Terminal: Examine the client terminal for the result of the conducted procedure.
