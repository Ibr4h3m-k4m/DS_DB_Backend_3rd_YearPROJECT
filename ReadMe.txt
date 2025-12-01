Instructions to run the backend in your locale pc:

     Requirements:

        -Docker Desktop latest version : it comes with docker and docker-compose.
        -to properly install docker simply watch a youtube video and follow the steps one by one.


    To check if Docker was installed properly , run these to commands :
        docker --version #you should be getting (Docker version 20.10.21) 
        docker-compose --version #you should be getting (Docker Compose version v2.13.0) 

    Now you're all set to start the backend , get into the backend folder and run the following command:
        docker-compose up -d --build 
        # with this , the backend will be running in a separate container , it will take from 5 to 15 min to run the project the first time .


    Runtime assets : 
        the project will be accessible through the url : "http://localhost:8000/"
        to run commands for example making migrations and creating a super user :  
            "docker-compose run web python manage.py makemigrations"
            "docker-compose run web python manage.py createsuperuser" 
        to visualize the backend in Datagrip:
            simply add a new Sql datasource , and just specify the port which is "3366".
            it is recommended to install the Docker plugin in Datagrip.

Notes:
    - I'll be adding a "seed.sql" file to the project very soon that will be executed by Docker at runtime ,
    the purpose of it is to populate the database automatically , especially the users table , so , i'll be updating it every time we finish
    from an increment .
    - you need to clone this repository using the following command "git clone https://github.com/DaoudiAmir/DS-DB_backend.git" 
    - we're gonna be needing a new repository that combines both the front and the backend.
    
Important Note : to clone the repository properly and not encounter any issues running the project with docker, use this commande :
                 "git clone https://github.com/DaoudiAmir/DS-DB_backend.git --config core.autocrlf=input"

to start the server using waitress : waitress-serve --listen=*:8000 dsdb.wsgi:application