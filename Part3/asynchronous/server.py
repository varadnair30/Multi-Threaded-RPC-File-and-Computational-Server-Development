# Import the necessary libraries
import rpyc
from rpyc.utils.server import ThreadedServer
import time

# Define the port for the server
port = 3000

# Create a custom XML-RPC server using RPyC's Service class
class CustomXMLRPCServer(rpyc.Service):
    
    # This method is called when a client connects to the server
    def on_connect(self, conn):
        print(f"\nClient is connected on port {port} ")

    # This method is called when a client disconnects from the server
    def on_disconnect(self, conn):
        print(f"\nClient is disconnected.")

    # Expose the "addFunction" method to clients
    def exposed_addFunction(self, i1, i2):
        print(f"\nPerforming addition: {i1} + {i2}")

        # Perform the addition asynchronously
        self.additionResult = additionAsync(i1, i2)

        # Simulate some processing time
        time.sleep(2)

        # Notify the client that the result is ready and return it
        print(f"\nAddition result is ready for the client. Sum: {self.additionResult}\n")
        return self.additionResult

    # Expose the "sortFunction" method to clients
    def exposed_sortFunction(self, li):
        print(f"\nPerforming array sorting: {li}")

        # Perform the sorting asynchronously
        self.sortingResult = sortAsync(li)

        # Simulate some processing time
        time.sleep(1)

        # Notify the client that the result is ready and return it
        print(f"\nSorting result is ready for the client. Sorted Array: {self.sortingResult}\n")
        return self.sortingResult

# Asynchronous function to perform addition
def additionAsync(i1, i2):
    return int(i1) + int(i2)

# Asynchronous function to perform sorting
def sortAsync(li):
    return sorted(li)

# Create a threaded server with the custom XML-RPC server class
server = ThreadedServer(CustomXMLRPCServer, port=port)

# Start the server and listen for incoming client connections
server.start()
