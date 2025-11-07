## Technical Documentation
The web-based version of the Collections Digitization Glossary was created using Python Flask 
and published to an Ubuntu Server running Nginx and Gunicorn. Please review the requirements.txt 
file for the list of Python packages used to process and generate the published glossary.  
  
/app - Python Flask Application  
/data - Source glossary and sources data files  
/docs - Previous GitHub pages website    
/technical - This file    
/util - Source file transformation scripts  
  
The glossary is updated regularly, reflected in date-based versioning.

## Production Environment
Python 3.12  
NGINX  
Gunicorn  
Ubuntu Server 22.04 LTS  

## Publication Workflow
The glossary is published as a collection of web pages generated using Python Flask. The codebase is located under the app folder. See the requirements.txt file for the complete stack. 

## Directories
/sources - Source files
/utils - Utility scripts for transforming and publishing source files
/web - html website generated using Python Flask

## Update Procedure

1. Save new glossary terms and glossary sources CSV files to the data\sources directory timestamped with the current date YYYYMMDD.
2. Update the latest glossary and latest source file functions in the globals.py file to point to the new source files.
3. Run the process-csv.py file
4. The transformed versions of the glossary should now be available in the app\data and data\output directories.
5. Test new files by running the app.py file under the app directory.
6. Deploy new CSV files to server
7. Login to server and restart app service.