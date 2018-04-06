from flask import Flask
from flask import render_template # finds and renders files under */templates/
#from deploy import *
import json
from application_support import *
# Initialization 
# Create an application instance (an object of class Flask)  which handles all requests.

directory = '/srv/runme/'
prefix = sys.argv[1]

application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])
def index():
    logger_info(raw_logger, proc_logger)
    return render_template('index.html')


# Server startup
# run() method : launch Flask's webserver.
# Once it is launched, it goes into a loop that waits for requests and services them.
if __name__ == '__main__':
    # create a new directory if the path does not exist
    if not os.path.exists(directory + prefix):
        os.makedirs(directory + prefix)
    # set up raw_logger and proc_logger
    raw_logger = setup_logger(directory, prefix, name = 'raw', log_file = '/Raw.txt')
    proc_logger = setup_logger(directory, prefix, name = 'proc', log_file = '/proc.txt')
    # Ensure that the development web server is started only when the script is executed directly.
    application.run(host='0.0.0.0',port=8080,debug=True)
