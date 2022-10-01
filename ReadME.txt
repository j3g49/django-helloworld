mysite

USAGE INSTRUCTIONS
===============================================================================
Install Django using the command below
$ sudo pip install django

  1. From the working directory in the terminal, execute the below command to run the server.
  python3 manage.py runserver

  2. To start the application, open the browser and visit http://127.0.0.1:8000/myapp/ to view the JSON format of Hello World message. 

  3. To see the HTML response of Hello World in BOLD, do the below.
  	a. Go to views.py under myapp folder
  	b. update the render function to "return render(request,'index.html')"
  	c. Save the file and re-run the server as mentioned in #1
  ------------------------------------------------------------------------------
