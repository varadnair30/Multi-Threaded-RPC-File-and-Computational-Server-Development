

# Introduction
In this project, a multi-threaded file server and computational server with Remote Procedure Call (RPC) communication are created. The project's technological overview, implementation specifics, and operational justifications are all included in the documentation.

# Technologies Used
Python programming language and libraries include xmlrpc and rpyc for synchronous and asynchronous RPC, as well as filecmp for comparison.

# Implementation: 

## Part One: Multi-Threaded File Server
In Part 1, we built a multi-threaded file server that supports the following operations: upload, download, delete, and rename.

**Upload:**

A file is sent from the client to the server by this action.
The client and the server use separate directories for file storage.
The user inputs the filename that will be uploaded from the client to the server after choosing the upload process.

**Download Operation:**

This procedure enables users to download a file from the server to their client.
After selecting the download operation, the user enters the filename that will be downloaded to the client from the server.

**Delete Operation:**

The delete action deletes a file from the server.
After selecting the delete procedure, the user enters the filename that will be erased from the server.

**Rename Operation:**

The rename action changes the name of a file on the server.
After selecting the rename operation, the user selects both the current filename to be renamed on the server and the new filename.
Code Overview:

Client:
•	Import the essential libraries and modules, such as xmlrpc.client, os, and threading, to connect to the server, manage file operations, and support multi-threading.
•	Define constants such as the server port number and the location where client files are saved.
•	The ServerProxy class can be used to create an XML-RPC client proxy that communicates with the server. It connects to the server using the provided port.
•	Define functions for different file operations:
•	UploadFileToServerPart1(fileName): Transfers a file from the client to the server.
•	downloadFileFromServerPart1(fileName) downloads a file from the server to the client.
•	deleteFileFromServerPart1(name_f) deletes a file on the server.
•	The function renameFileInServerPart1(name_f_old, name_f_new) renames a server file.
•	Create a function called startClientExecution() to handle user input and perform operations based on the selected choice.
•	Create a thread masterThread for client execution, which allows the client to do numerous actions concurrently.

Server:
•	Import the essential libraries and modules, such as SimpleXMLRPCServer to build an XML-RPC server, ThreadingMixIn to enable multi-threading, xmlrpc.client, and os.
•	Define constants such as the server's port number and the place where server files are saved.
•	Create a custom class called CustomXMLRPCServer, which inherits from CreateThread and SimpleXMLRPCServer. This custom class supports multi-threading on the server.
•	Implement methods that handle file operations on the server:
•	The function uploadFileToServerPart1(name_file, directory_file) uploads a file to the server.
•	downloadFileFromServerPart1(name_file): Obtains a file from the server.
•	deleteFileFromServerPart1(name_file) deletes a file from the server.
•	renameFileInServerPart1(name_file_old, name_file_new): Renames a server-side file.
•	Make an instance of the custom server class, register any required functions, and specify the server's IP and port number. 
•	Start the server using server.serve_forever(), which keeps it running and ready to answer client queries.

 ![image](https://github.com/user-attachments/assets/680b7071-2217-418e-a0ac-28268418268e)

  ![image](https://github.com/user-attachments/assets/026c3481-7445-42a0-9a05-e8525f2883ce)

  ![image](https://github.com/user-attachments/assets/61b65ae5-7f15-4f9b-8c8c-e5e52ef24251)
      
 ![image](https://github.com/user-attachments/assets/00f1926c-6021-45b6-a15e-001a2ab5e0e1)

![image](https://github.com/user-attachments/assets/7255260f-be01-409f-a4b1-b90e0edd5851)

![image](https://github.com/user-attachments/assets/2ec8ae2a-48d4-4c99-ad38-60de6e59266e)

![image](https://github.com/user-attachments/assets/254e46b6-3b25-4743-9f36-2665ae9d9ece)

![image](https://github.com/user-attachments/assets/b2d215d8-eed8-4c92-8b27-b188aae7637c)



     Part 1


**Part 2: Automatic File Syncing**
Part 2 comprises automatic file synchronization between the client and server. When a client creates, updates, or deletes a file, a helper thread duplicates the changes on the server.
Every 4 seconds, the helper thread checks for file changes in the client directory and updates the server directory if any are identified.

Code Overview:

Client Code:
•	Imports the Python libraries required for XML-RPC communication, timestamp management, multithreading, file comparison, and file operations.
•	Defines constants, including the server's port number, and generates an XML-RPC client proxy for connecting to the server.
•	Specifies the paths to the client and server's file directories where files will be saved.
•	Implements a function (uploadFileToServerPart2) that uploads files to the server and handles file upload failures.
•	Implements a function (deleteFileFromServerPart2) that deletes files from the server while handling errors for unsuccessful deletions.
•	Creates a function (automaticDirectorySync) that keeps directories synchronized between the client and server. It distinguishes between server-only files for deletion, client-only files for upload, and modified client files for upload. Gives comments on synchronization.
•	Uses a helper thread to perform the automaticDirectorySync method concurrently, constantly checking for file changes between the client and server directories.


Server Code:
•	Imports Python libraries, such as SimpleXMLRPCServer for XML-RPC, ThreadingMixIn for multi-threading, and os for file operations.
•	Defines server-specific constants like port number and directory path.
•	Creates a custom class (CustomXMLRPCServer) that inherits from CreateThread and SimpleXMLRPCServer to enable multi-threading on the XML-RPC server.
•	Added a function (uploadFileToServerPart2) to manage file uploads to the server.
•	It creates the entire path to the server file, stores the submitted binary data, and handles faulty file uploads.
•	Added deleteFileFromServerPart2 function to handle server-side file deletions. 
•	It removes the provided file from the server directory and returns a success or error message depending on the outcome.
•	Initializes the server by creating a custom server class instance, registering introspection functions, registering the uploadFileToServerPart2 and deleteFileFromServerPart2 methods, and launching the server.

![image](https://github.com/user-attachments/assets/12b06dd6-7acb-44a5-89a0-424c9cd2a045)

![image](https://github.com/user-attachments/assets/c1d1f518-1d63-4683-9212-c9ef192daa27)

![image](https://github.com/user-attachments/assets/ccf9feb6-d1d7-45d2-8953-ee769d43c49b)


   
       Part 2
 
**Part 3: Computation Server**

In Part 3, we built a computation server that supports two operations: adding two numbers and sorting an array via both synchronous and asynchronous RPCs.

Synchronous RPC
In synchronous RPC, the client requests an operation from the server and expects an immediate answer.

## Code Overview:

Client:
•	Imports xmlrpc.client, os, and threading.
•	Defines the server port as 3000.
•	Creates an XML-RPC client proxy (rpc_server) for communicating with the server.
•	Implements the additionSync function for addition operations and the sortSync function for sorting operations on the server.
•	Handles user input to choose and execute operations (Add or Sort).
•	Client activities are handled concurrently on a different thread (main_thread).

Server:

•	The following libraries are imported: SimpleXMLRPCServer and ThreadingMixIn.
•	Defines the server port as 3000.
•	Creates a custom XML-RPC server class (CustomXMLRPCServer) that inherits from CreateThread and SimpleXMLRPCServer.
•	Implements the additionSync and sortingSync functions for addition and sorting operations, respectively.
•	Creates a custom server class, registers functions, and defines server information (localhost and port).
•	Registers standard introspection functions, gives the additionSync and sortingSync methods appropriate names, and begins processing client requests indefinitely.

![image](https://github.com/user-attachments/assets/d881b61d-1d2b-4dcf-9706-c285299b99fd)

 
Part 3 Synchronous
Asynchronous RPC
In asynchronous RPC, the client requests an action and waits for a response from the server. It can carry out other duties while the server handles the job. When completed, the server transmits the response to the client.

## Code Overview:
Client:
•	Import the required libraries, which include asyncio for asynchronous tasks, rpyc for RPC communication, and os for system-related operations.
•	Define the server's port number as server_port, which is 3000.
•	Connect to the server via rpyc.connect() to initiate contact with the server running on localhost at the specified port.
•	Create an asynchronous function that simulates background processes. It executes a loop for 10 iterations, prints a message, and then sleeps for two seconds between iterations.
•	Define the execute_client_operations() function, which manages user interactions. It shows a list of available operations (Add, Sort, and Exit) and waits for user input.
•	If the user clicks "Add," it prompts for two numbers, makes an asynchronous call to server_connection.root.addFunction, transmits the numbers to the server for addition, then asynchronously checks for the result status, which can take up to 5 seconds.
•	If the user chooses "Sort," the program prompts for a comma-separated list of numbers, makes an asynchronous call to server_connection.root.sortFunction, transmits the list to the server for sorting, then checks for the result status asynchronously, waiting up to 1 second.
•	If the user clicks "Exit," the software terminates.
•	The main_function() function executes execute_client_operations() and simulate_background_tasks() simultaneously using asyncio.gather() in an infinite loop.


Server: 
•	Import the essential libraries, such as rpyc for RPC communication, ThreadedServer from rpyc.utils.server to create a threaded server, and time for time-related operations.
•	Define the server's port number as 3000.
•	Use RPyC's Service class to create a custom XML-RPC server called CustomXMLRPCServer.
•	Implement the on_connect method, which is invoked when a client connects to the server and prints a message to confirm the connection.
•	Implement the on_disconnect method, which is invoked when a client disconnects from the server and produces a message to indicate the disconnection.
•	For remote procedure calls, expose two methods to clients: exposed_addFunction and exposed_sortFunction. These methods conduct addition and sorting operations, respectively, and include print statements to monitor their progress.
•	Define asynchronous functions additionAsync and sortAsync to perform addition and sorting operations, respectively.
•	ThreadedServer creates a threaded server instance named server. It uses the CustomXMLRPCServer class to listen on the specified port.
•	Start the server by calling server.start(), which listens for incoming client connections and handles their RPC queries.

## Learnings:
•	RPC Protocol Knowledge: I gained a thorough understanding of Remote Procedure Call (RPC) protocols, particularly how they permit communication between distributed systems.
•	Project Architecture: I learned how to analyze and describe complicated project structures, such as component divisions and interactions.
•	File Operations: Learned about file handling operations in a client-server architecture, including UPLOAD, DOWNLOAD, DELETE, and RENAME.
•	Multithreading: I've mastered multithreading principles and techniques, especially for managing concurrent client requests and server-side file synchronization.
•	Synchronization Strategies: I learned about file synchronization strategies like real-time updates and timestamp-based reasoning.
•	RPC Libraries: Gained experience utilizing RPC libraries such as xmlrpc and rpyc to implement client-server communication.
•	Error Handling: Learned how to handle errors and manage exceptions, assuring the reliability of both client and server components.
•	Asynchronous Programming: I learned how to efficiently implement asynchronous RPC calls, which allow for asynchronous client-server interactions.

## Challenges Faced:
We encountered difficulties during the implementation of RPC. Understanding and managing the relationship between the server and client. Understanding which ports are open and why a few are unable to open. Determine whether two directories are comparable or whether they have been modified. Identifying effective strategies for managing file uploads and downloads on the server.



