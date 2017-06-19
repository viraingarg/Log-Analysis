# Log-Analysis

This project requires a virtual environment.

To get this environment we have to install Vagrant and Virtual Machine on our System.

"log_analysis_project.py" is the python code which deals with the database querries and provides the desired output.

"views.sql" is the sql file in which all the views queries are stored.

"output.txt" file contains the desired output.

Steps for setup of the virtual environment

Step 1: Clone the project repository and connect to the virtual machine $ git clone https://github.com/mlupin/fullstack-nanodegree-logs-analysis.git

Step 2: $ cd fullstack-nanodegree-logs-analysis $ vagrant up

Step 3: $ vagrant ssh

Step 4: $ cd /vagrant

Step 5: Now load the file containing all the data regarding the log here. Name of the file is newsdata.sql.

Step 6: $ psql -d news -f newsdata.sql

Running the project:

step 7: $ psql -d news -f views.sql

Step 7 is performed to create all the views needed at once.

Step 8: $ python log_analysis_project.py

Step 9: You will get the desired output.
