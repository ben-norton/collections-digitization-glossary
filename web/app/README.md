# Web Documentation README
This directory contains a small website for publishing data profiles.

## How to
### Testing
* Open the command line window and navigate to the instance root directory (e.g. (root)/web)
* Make sure the virtual environment is activated (conda activate .data-utils-venv or .\.data-utils-venv\Scripts\activate)
* At the command line, enter $flask run
* Open a browser to localhost:5000
* To end testing and stop the development server, press CTRL+C in the command line window

### Build Pages
* Open a command prompt in the app subdirectory of the instance (e.g. (root)/web/app) 
* Enter *python freeze.py build*
* Copy the entire contents of the build directory (/web/app/build) to the docs folder in the target repository
* Open pages in browser to make sure they rendered correctly
* Copy files in build directory to /docs manually or by running the deploy.bat from windows console

### Important Changes between routes.py and freeze.py
1. In freeze.py, all route names must be bound with both leading and trailing forward slashes.
2. When refreshing freeze.py with changes to routes.py, the leading 'app/' must be removed from every reference to an external files (e.g., markdown content files) 

### Tech Stack
- Python 3.12
- Flask [https://flask.palletsprojects.com/en/stable/](https://flask.palletsprojects.com/en/stable/)
- Frozen Flask [https://frozen-flask.readthedocs.io/en/latest/](https://frozen-flask.readthedocs.io/en/latest/)
- Python markdown2 [https://github.com/trentm/python-markdown2](https://github.com/trentm/python-markdown2)
- And of course, Pandas [https://pandas.pydata.org/](https://pandas.pydata.org/)