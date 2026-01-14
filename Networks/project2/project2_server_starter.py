# necessary imports
import http.server
from pathlib import Path

class SimpleServer(http.server.BaseHTTPRequestHandler):
    """
    This function has been provided to you in lieu of the standard python
    print() function. The print function will cause issues with the autograder
    due to how it processes standard output, so using it will cause you to fail.
    Instead use the command self.debug(message) while you are building and
    testing your code, and then when you go to submit it you can change the
    self.debug_state to False to disable all printing.
    """
    def debug(self, message):
        self.debug_state = True # change this value to False when you submit to the autograder
        if self.debug_state == True:
            print(message)

    ############### PLACE ANY ADDITIONAL HELPER FUNCTIONS HERE ###############
    """
    You are free to make any additional helper functions you believe will
    help you complete this project. It is recommended that for your own sanity
    and ours (in the event you need help) that you place them all in one location
    instead of scattering them all over.

    Any additional functions you make MUST be part of the class as the
    autograder will not see them otherwise. This means that your function at a 
    minimum must have the argument "self". Then when you want to access your 
    new function somewhere in your code you will call self.new_function().
        
    """
    ###############       PROVIDED FUNCTIONS BELOW HERE        ###############
            

    def determine_response_code(self):
        """
        As the name implies, this function is where you should have whatever 
        logic you need to determine what the appropriate response code for a 
        given GET request is. For the purposes of part 1 you only need to 
        handle the cases where a resource exists (200) or it doesn't (404).
        However, you should leave some room to expand the available responses
        as you will need to handle different cases in part 2 of the project.

        We have provided some code to create a variable called basePath below.
        The code will automatically determine where your server code resides,
        which means you can use it to construct additional paths. This is 
        necessary because when you submit your code to the autograder it will
        be moved to a different location. If you choose to implement a different
        solution by doing something like using the OS.path module that is fine 
        but DO NOT HARD CODE IT. An example of how to use the basePath variable 
        has also been provided.
        
        """
        
        # determine the base path where your code exists
        basePath = Path(__file__).parent.absolute()
        
        # if the request is for the root "/" it should be served index.html
        if self.path == '/':
            objPath = basePath / 'index.html'

        #### YOUR CODE HERE ####
        # otherwise the request is for something else and we should create the path
        else:
            # this method let's the path library deal with the / in the request
            # which is a more robust approach than simply saying objPath = basePath / self.path[1:]
            objPath = Path(str(basePath) + self.path) 

        # check if the resource exists
        if objPath.exists() and objPath.is_file():
            self.path = objPath
            self.response_code = 200
        else:
            # resource doesn't exist and we should replace it with notfound.html
            self.path = objPath / 'notfound.html'
            self.response_code = 404

        # we have determined the path and the response code so this function is done for now
        

    def determine_content_type(self):
        """
        This function should contain your logic for determining what the content
        type of the requested resource is. You can reference the instructions
        pdf for the types you need to be able to handle, and you can reference
        https://www.geeksforgeeks.org/http-headers-content-type/ for how to 
        format the content types (such as text/html).
        """
        # here is an example of how to store the results to get you started
        self.content_type = 'text/plain'

        #### YOUR CODE HERE ####
        # you can use the mime library for this or a variety of techniques
        # such as a dictionary and the .get method or a switch case, 
        # but here is an extremely simple approach that everyone can understand.
        ct = str(self.path).split('.')[-1]
        if ct == 'html':
            self.content_type = 'text/html'
        elif ct == 'xml':
            self.content_type = 'text/xml'
        elif ct == 'jpg' or ct == 'jpeg' or ct == 'jfif' or ct == 'pjpeg' or ct == 'pjp':
            self.content_type = 'image/jpeg'
        elif ct == 'png':
            self.content_type = 'image/png'
        elif ct == 'mp4':
            self.content_type = 'video/mp4'
        elif ct == 'ico':
            self.content_type = 'img/x-icon'
        else:
            self.content_type = 'text/plain'

        # is anything missing?

        
    def send_response_headers(self):
        """"
        This function should combine the information you have determined
        in determine_response_code and determine_content_type with some logic to
        actually dynamically build and send the appropriate headers. For part 1 
        you need to have logic to build the following headers:
        - 'Content-Length'
        - 'Content-Type'
        - 'Connection'

        In part 2 you will need to account for some additional headers, so make
        sure your design allows for expansion.
        """
        #### YOUR CODE HERE ####
        
        # send the response code
        self.send_response(self.response_code)
        # create and send the 3 headers
        self.send_header('Content-Length', Path(self.path).stat().st_size)
        self.send_header('Content-Type', self.content_type)
        self.send_header('Connection', 'close')

        # this should be the last line of your code and tells the underlying 
        # code you are done building your headers.
        self.end_headers()  

    def do_GET(self):
        """
        This function serves as the control function for the rest of your code.
        The underlying code handling TCP connections will automatically call
        this function. It should contain whatever logic you deem necessary to 
        execute the rest of your code in an appropriate order.

        We have provided a snippet of code that will actually handle sending the
        requested resource to the client. It is up to you to implement the rest.
        Good luck!
        """
        self.debug("GET request received from: " + self.client_address[0])
        
        #### YOUR CODE HERE ####

        # determine the response code
        self.determine_response_code()
        # determine the content type
        self.determine_content_type()
        #send the response / headers
        self.send_response_headers()
        # send the actual file
        if self.response_code == 200 or self.response_code == 404:
            try:
                with open(self.path, 'br') as f:
                    msg = f.read()
                    self.wfile.write(msg)
            except:
                self.debug('Unknown error while trying to open' + self.path)
                pass



# You don't need to modify anything below here.
if __name__ == "__main__":
    # this says respond to any IP on port 8080
    srv_info = ('', 8080)

    # this creates the webserver instance (object)
    webserver = http.server.HTTPServer(srv_info, SimpleServer)

    # this starts the webserver. You can stop it with ctrl + c
    webserver.serve_forever()