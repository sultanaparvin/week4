# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 20:17:09 2018

@author: Owner
"""
from http.server import BaseHTTPRequestHandler, HTTPServer

class httpServerRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self): 
        # Send response status code 
        self.send_response(200)
        
        #Send headers
        self.send_header('Context-type', 'text/html')
        self.end_headers() 
        message = "Goodbye"
        
        #send message back to client 
        if self.path.lower() == "/hello":
            message = "hi"
        
        #write content as bytes 
        self.wfile.write(bytes(message, "utf8"))
        return 
    
def run():
    print('starting server')
    #server settings
    # choose port 9500
    # port 9500 cannot be use for this application. Other ports like 8081,  9001, etc can be used. 
    server_address = ('127.0.0.1', 9500) 
    httpd = HTTPServer(server_address, httpServerRequestHandler)
    print(' Server is running')
    httpd.serve_forever() 
    
run()