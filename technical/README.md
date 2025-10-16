## Technical Documentation
The web-based version of the Collections Digitization Glossary was created using Python Flask and published to an Ubuntu Server running Nginx and Gunicorn.
The initial version of the glossary was published on a GitHub Pages website (under /docs). GitHub offers limited support for dynamic features in GitHub Pages. To enable better filtering and control over the functionality of the pages, the glossary was moved to a separate server environment described above.
Please review the requirements.txt file for the list of Python packages used to process and generate the published glossary.
/app - Python Flask Application  
/data - Source glossary and sources data files  
/docs - Previous GitHub pages website    
/technical - This file    
/util - Source file transformation scripts  
  
The glossary is updated regularly, reflected in date-based versioning.

