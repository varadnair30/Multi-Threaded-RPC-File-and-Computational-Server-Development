from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn as CreateThread

port = 3000

class CustomXMLRPCServer(CreateThread, SimpleXMLRPCServer):
    pass

def additionSync(n1, n2):
    addOp = n1 + n2
    return addOp

def sortingSync(input_list):
    input_list.sort()
    return input_list

with CustomXMLRPCServer(('localhost', port), allow_none=True) as server:
    server.register_introspection_functions()
    server.register_function(additionSync, "additionFunction")
    server.register_function(sortingSync, "sortFunction")
    print(f"\nServer is running on port {port}")
    server.serve_forever()
