# 'LOOKING INTO THE FUTURE' APP

## Contents
* [Overview of the Project](#overview-of-the-project) 
  * [Summary](#summary)
  * [Project Requirements](#project-requirements)
  * [Design](#design)
    * [Kanban board tech](#kanban-board-tech)  
    * [Risk Assessment](#risk-assessment)
    * [Database](#database)
    * [Test plans](#test-plans)
* [Integration](#integration)
  * [Database](#database)
  * [GitHub](#github) 
* [Deployment](#deployment)
  * [Stage1: Planning the pipeline](#pipeline)
  * [Stage2: Docker and Docker-Compose](#docker-and-docker-compose)
  * [Stage3: Database Layer](#database-layer)
  * [Stage4: Jenkins & Automating testing](#jenkins-and-automating-testing)
  * [Stage5: Build and Push stages](#build-and-push-stages)
  * [Stage6: Swarm and Ansible](#swarm-and-ansible)
  * [Stage7: Ansible and NGINX](#ansible-and-nginx)
  * [Stage8: Deploy stage](#deploy-stage)
* [Front End Page](#front-end-page)
* [Future Improvements](#future-improvements)
* [Authors](#authors)
* [Thank you!](#thank-you)   

# Overview of the Project
## Summary
For my second project in my devops development career I have been asked to create a service-oriented architecture (SOA) for an application, made of 4 services that work together.
My application is called "_Looking into the Future_". This is a 4 services application where:
  * Service 1 provides us with a webbrowser (front-end). When refreshing the webpage, service1 will send the requests to the other 3 services. 
  * Service 2, 3, and 4 just store some random information.
The idea behind this application is Service 1 will send a GET request to services 2 & 3. Service 2 will generate a random date and service 3 will generate a random number, which both will send back to Service 1. These 2 pieces of information will then be sent to service 4 with the post request order to generate some kind of 'future'. Service 4 then will send all this info to Service 1 which then will show the information in the browser to the user.   
Once Service 1 has gathered all info from Services 2, 3 and 4 it will then open a db session just to store the data requested.  
To prove there is a DB running in the background the app will be able to get the last 5 requests on the screen.

## Project Requirements
The objective of this project is to create an application with utilisation of supporting tools, such as:
- Jira board to cover the project management side of it showing the tasks needed to complete the project.
- Risk Assessment recording any issues or risks I faced creating the app.
- The application needs to be fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
- If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
- To deploy the app use containerisation and an orchestration tool.  
- Create an Ansible Playbook that will provision the environment that my application needs to run. 
- Create and use a reverse proxy to make your application accessible to the user.

## Design
### _**Project Tracking**_
As project Management Software I have used Jira. The link to this board can be found in here [Jira Board](https://trizmanz.atlassian.net/jira/software/projects/F2/boards/4).

These 2 images below show a screenshoot of the Backlogs with the Epics and User Stories this project is based on and a screenshoot of the Sprint board showing the sprint. A user story is an end goal expressed from the user’s perspective. I have used the Definition of Ready (DoR) to establish what a product backlog item needs before it can go into the sprint backlog andd the Definition of Done (DoD) defines what is needed before it can be regarded as complete.   

![Jira Board Sprint](https://github.com/bmanzanoqa/F2SupportingDocs/blob/dev/Jira/Sprint.PNG)

![Jira Board Backlog](https://github.com/bmanzanoqa/F2SupportingDocs/blob/dev/Jira/Backlog.PNG)


### _**Risk Assessment**_
We use Risk Assessments to evaluate scenarios that may impact the project in a negative way. By knowing the risk and ways to mitigate them we are able to create a project were risks are less likely to occur. As parts of the projects were getting near completion others risks were added to the template and all of them revisited.This file can be found in [Risk Assessment](https://github.com/bmanzanoqa/F2SupportingDocs/blob/dev/Testing-RA/F2%20RA.PNG).    

Below is a screenshot of the Risk Assessment I have carried out for this project. This Risk Assessment has been reviewed in different ocassions during the length of the project as it can be seen on the right hand side of the table.

![Risk Assessment](https://github.com/bmanzanoqa/F2SupportingDocs/blob/dev/Testing-RA/F2%20RA.PNG)  

### _**Database Structure**_
In order to satisfy the MVP for this project I had to make sure there was a database running in the background just storing the data generated by services 2, 3, and 4. To prove this the web browser will show on the screen the last 5 entries generated by the app.  
If we were running a local db we would add '*.db' to the ignore file so it would not be pushed to the public repo keeping data encrypted at all times.    
This project is a very simple application that has just one database with one table as shown in the image below:

![Database Structure](https://github.com/bmanzanoqa/F2SupportingDocs/blob/dev/DB/Database%20structure.PNG) 

This database is running in the background in a MySql virtual machine in GCP.
For its integration with the app, please go here [Database](#database)

### _**Test Plans**_
When creating this app I have used a Python Library called 'unittest.mock which has allow me to mock responses from components such as Application Programming Interfaces (APIs) and to test parts of a micro-service application individually.
The following test plans show and explain how services have been tested and the status of those tests.
![Test Plans](https://github.com/bmanzanoqa/F2SupportingDocs/blob/dev/Testing-RA/Test%20Cases.PNG)  

Test were run with pytest, for each service and produced cov reports. A screenshoot of a report can be seen below:
![Test Coverage Report](https://github.com/bmanzanoqa/F2SupportingDocs/blob/dev/Testing-RA/Test%20coverage%20report.PNG)    
 
# Integration
## Database 
How will the database integrate with the app?
  * The user talks to Service1 on the web page, which sends a GET request to Service2 and Service3, then a POST request to Service4 with the data just received from Service2 and Service3 (date and number). 
  * Once Service1 has received the 3 pieces of information, it will talk to a DB with that information and read some data from it.   
  * And the idea is that those 2 previous steps will happen every time I refresh the web page.  
  * I have used *db.session.add* and *db.session.commit* to add/save new data to the database.  
  * The app will use a query to get the last 5 readings from the DB.
  * Next thing I did was, in *app.py* to set it as an environment variable so I do not have to hard code it and then I ensured the env variable is set up in the container under the 'environment' key in the Docker-compose.yaml

## GitHub
My git repository uses the _**'feature branch'**_ model where I have my *'main'* branch where I have already working code on it, a *'dev'* branch with working code 'ready to go but not quiet deployed yet' and my *'feature_Docker'* branch off *'dev'* where I have actually done my coding, this way I am not doing my work in my deployment ready branch.  
The way to tackle the development is:
1. We create a *'main'* branch that is created when we first create the repo.
2. Before we add anything to the *'main'* branch, any source code, I branched to *'dev'* branch which will be running in parallel with *'main'*
3. Off the *'dev'* branch I have made another branch *'feature_Docker'* where I have been doing all the work
4. When each feature has been working I made a pull request and merge into the *'dev'* branch and this has triggered the pipeline. 
5. Once I have all the features working and I have merge them in *'dev'* and I have a fully working application then I have merged from *'dev'* into *'main'* to show my version 1 of my application.   
![GitHub Branch Model](https://github.com/bmanzanoqa/F2SupportingDocs/blob/dev/GitHub/GitHub%20Branch%20Model.PNG)  

# Deployment
This is my CI Pipeline for this app.

![CI Pipeline](https://github.com/bmanzanoqa/F2SupportingDocs/blob/dev/Jenkins/CI%20Pipeline%20Miro.PNG)    

## Stage1: Planning the pipeline
The basic functionality of the application is that, when I refresh the page, I am going to get a date, a number and what will happen in that day and this is going to be shown in a web browser.

To prepare the pipeline I will be using a Jenkinsfile which is a very handy way to start the plan of what the pipeline will look like. Each step in the pipeline is defined by a 'stage' section. 

I started my Jenkinsfile with 5 stages. These steps work like a validation process:
1. Test
    * First thing Jenkins does is to run pytest. We do not want to build an image for a broken application, we test the app and if it passes then we build the image for it.
    * Needs pytest
    * Needs to run for each service in my repo
    * Produces coverage reports so I know what the coverage is of each of my services
2. Build
	  * Install docker and docker-compose
	  * Create a docker-compose.yaml that will define the way the docker containers work with each other 
    * Command to run ==>> "docker-compose build"
3. Push
    * Similar to Build stage
    * Install docker and docker-compose
    * Command to run ==>> "docker-compose push"
4. Configuration Management
    * Install ansible on jenkins machine for the Jenkins user
    * Command to run ==>> "ansible-playbook -i invenroty.yaml playbook.yaml"
5. Deploy
    * Create swarm infrastructure 
      * Create manager and worker vm  
    * Make sure the 'docker-compose.yaml' exists in the manager machine so when I reference it in the command below it has a file to reference to.  
    * Run 'ssh:docker stack deploy --compose-file docker-compose.yaml future2 (name of my stack)'

At a later stage in the project I decided to add an 'Installation stage' where all the main programs would be installed by jenkins when running the pipeline, saving time and resources. The script will install Docker, Docker Compose, Ansible and will login in Docker Hub so the app can push the images to the Docker Hub Repo.

## Stage2: Docker and Docker-Compose
To conteinarize the application we need to use Docker and Docker-Compose and the way to do this is by using Dockerfile and Docker-Compose.yaml
  * Dockerfile == a dockerfile is a set of instructions executed in a step by step fashion to build Docker images. In this file we need to specify and do the following:
    * the image version (python) (FROM)
    * get the image into a container (COPY) 
    * Set up the working directory to wherever the source code will live (WORKDIR) 
    * Install requirements (RUN)  
    * Show the port the application is listening to (EXPOSE) 
    * Set up ENTRYPOINTS (Every container does (ideally) just one thing, in this case to run the python app)
  * DOCKER-COMPOSE.YAML == It makes the process much quicker. 
    * It will run the containers as a group that can talk to one another. 
    * In order to build the images we need to specify where the dockerfile is that defines how the image is going to be built and you do that by specifying: 
      * 'build' ==> location of where the  dockerfile is specifically   
      * 'image': where we push the image (Docker hub)
![Docker & Docker-compose](https://github.com/bmanzanoqa/F2SupportingDocs/blob/dev/Docker/docker%20%26%20docker-compose%20ps.PNG)   
## Stage3: Database Layer
To access the DB we need to reference an env variable in app.py and then set the env variable in the compose.yaml

## Stage4: Jenkins & Automating testing
Jenkins is an open-source implementation of a Continuous Integration server written in Java. It works with multiple programming languages and can run on various platforms (Windows, Linux, and macOS). 
When building the Jenkins server (which in my case has been installed in a medium Ubuntu 18.04 LTS vm in GCP) I had to make sure Docker had been installed and python too. 
The idea is when I push up any new changes with a bunch of commits on them, I have set up a webhook in github that tell Jenkins 'hey, there have been some new commits, I need you to get to work!' 
A WEBHOOK just sends information about new changes made to the source code (VCS, in this case GitHub). When Jenkins receives those services is when the automation comes in. 
![Jenkins Stage View](https://github.com/bmanzanoqa/F2SupportingDocs/blob/dev/Jenkins/Jenkins%20Stage%20View.PNG)   
![Webhook Logs](https://github.com/bmanzanoqa/F2SupportingDocs/blob/dev/GitHub/Gitahub%20Webhook%20Log.PNG) 

## Stage5: Build and Push stages
In this stage Jenkins will firstly build an image ==> it builds images for each of my Services 1, 2, 3, 4. The idea of the containers is that it holds all the requirements installed already (python, pip...). It means that every time I want to run an application I do not need to download all of the requirements every single time as you bundled all the requirements with the application
Secondly Jenkins will push images  to docker hub ==> Jenkins will push the images to Docker Hub after building them. 
Docker Hub == Artefact repository (location to store your images (GitHub of Docker images)).
Artefact = anything generated by the pipeline

## Stage6: Swarm and Ansible
Docker swarm is a container orchestration tool that allows the user to manage multiple containers deployed across multiple host machines. One of the key benefits associated with the operation of a docker swarm is the high level of availability offered for applications. 
Ansible is a configuration manager which makes sure everything is in place, set up and works correctly. By creating  an Ansible Playbook this will provision the environment that my application needs to run. This playbook defines what roles apply to what machines and the invenrtory file is used to define hosts in the infrastructure to connect with and configure.
In my pipeline, after pushing the images, Ansible will make sure that the swarm and nginx machines are set up correctly.  
Ansible knows what the right configuration is based on what the playbook says. A playbook is like a shopping list given to somebody else, you tell them what you want but not the steps to get the stuff.  
Ansible will make sure one that one of the machines in the swarm is a Manager and one (or more) is a Worker and that they are connected in a swarm and the worker can join the swarm  
The point of the swarm is that it can run lots of containers and all can talk to one another. It is a deployment solution that can run all my containers over those machines (M & W). They can communicate nice and easily.   
This means you have redundancy in terms of the hardware and your containers meaning they are fail proof. If one of the workers goes down there is always another to pick up the pace.   
![Ansible/Swarm/Nginx](https://github.com/bmanzanoqa/F2SupportingDocs/blob/dev/AnsibleSwarmNginx/Ansible-Swarm-Nginx.PNG)   
## Stage7: Ansible and NGINX
The beauty of this stage is that once I have installed Nginx, I will not have to touch Ansible again.
I am using the nginx virtual machine as a reverse proxy server and a load balancer to make my application accessible to the user. This server sits in front of web servers and forwards client requests (e.g. web browsers) to those web servers which at the same time increases security, performance, and reliability.   

## Stage8: Deploy stage
Everything is now ready to go. The only thing left is to tell the swarm to pull down the images and run them up according to our compose.yaml file configuration. I have done this using a stack. 
A stack is a collection of services, a collection of containers that run of the same image creating a service. As the images are part of one service we are able to control how we, for instance, upgrade those images just by contacting the service. Just get the new image, contact the service and tell it to upgrade it to a new version with just one command instead of having to contact every single replica. 
If a service is a collection of containers of the same image a stack is just a collection of services
Rather than having to run 4 commands to run 4 different services we can run one command to deplioy a stack.
To define the stack with multiple services we use the docker-compose.yaml file
And Jenkins will do this for us.
We need to perform the command (docker stack deploy) in the swarm manager vm via ssh

# Front End Page
Version 1 of the app looks like this:   
![Version 1](https://github.com/bmanzanoqa/F2SupportingDocs/blob/dev/Architectures-Designs-Updates/App%20v1.PNG)    
Following the MVP, Version 2 of the app will show changes to the 4 services:    
    * Service1 will change colour   
    * Service2 will change the range of numbers from 1-10 to 1-50   
    * Service3 will change the month the 'future' is told   
    * Service 4 will have capitalized 'futures'
The reult can be seen below:

![Version2](https://github.com/bmanzanoqa/F2SupportingDocs/blob/dev/Architectures-Designs-Updates/Will%20-pass.PNG) 

## Future improvements

- Implement a 'refresh Page' button 
- Implement a button to change the months
- Better App interaction
- More testing plans
  
## Author
![Beatriz Manzano](https://github.com/bmanzanoqa/F2SupportingDocs/blob/dev/Other/download%20crop.png)

Beatriz Manzano finished this project on the 14/06/2021


## Thank you!
I would like to give an special mention to @HarryVolker without whom I may not have been able to complete this project!!   
Also a very warm thank you to @BenHesketh for his support.  
Thank you to my trainers and everyone in my class for all the patience they have had and the help they have always provided.

