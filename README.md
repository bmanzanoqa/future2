# 'LOOKING INTO THE FUTURE' APP

## Contents
* [Overview of the Project](#overview-of-the-project)
  * [Design](#design)
  * [Project Requirements](#project-requirements)
* [Deployment Stages](#deployment-stages)
  * [Project Tracking](#project-tracking)
  * [Pipeline Planning](#pipeline-planning)
  * [Docker & Docker-Compose](#docker-and-docker-compose)
  * [Database Layer](#database-layer)
  * [Jenkins & Automating testing](#jenkins-and-automating-testing)
  * [Build and Push stages](#build-and-push-stages)
  * [Swarm and Ansible](#swarm-and-ansible)
  * [Ansible and NGINX](#ansible-and-nginx)
  * [Deploy stage](#deploy-stage)
  * [Rolling update stage](#rolling-update-stage)
* [Images](#images)
* [Authors](#authors)
* [Thank you!](#thank-you)


## Overview of the Project
For my second project in my devops development career I have been asked to create a service-oriented architecture (SOA) for an application, made of 4 services that work together.
My application is called "Looking into the Future". This is a 4 services application where:
  * Service 1 provides us with a webbrowser(front-end).
  * When refreshing the webpage, service1 will send the requests to the other 3 services. 
  * Service 2, 3, and 4 just store some random information.
The idea behind this application is service 1 will send a GET request to services 2 & 3. Service 2 will generate a random date and service 3 will generate a random number, which both will send back to service 1 when service 1 sends them the GET request. These 2 pieces of information will then be sent to service 4 with the post request order to generate some kind of 'future'. Service 4 then will send all this info to Service 1 which then will show the information in the browser to the user.   
Once Service 1 has gathered all info from Services 2,3 and 4 it will then open a db session just to store the data requested.  
To prove there is a DB running in the background the app will be able to get the last 5 requests on the screen

### Project Requirements
The objective of this project is to create a CRUD application with utilisation of supporting tools, such as:
- Jira board to cover the project management side of it showing the tasks needed to complete the project.
- Risk Assessment recording any issues or risks I faced creating the app.
- The application needs to be fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
- If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
- To deploy the app use containerisation and an orchestration tool.  
- Create an Ansible Playbook that will provision the environment that my application needs to run. 
- Create and use a reverse proxy to make your application accessible to the user.


## Project Tracking
As project Management Software I have used Jira. The link to this board can be found in here [Jira Board](https://https://trizmanz.atlassian.net/jira/software/projects/F2/boards/4/roadmap)

![Jira Board Sprint](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/Jira%20Board%20Backlogs%2023.05.21.PNG)

![Jira Board All Sprints](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/Jira%20Board%20All%20Sprints.PNG)

In these 2 boards I have taken a screenshoot of the Backlogs showing the Epics and User Stories this project is based on and a screenshoot of the Dashboard showing where we are with our sprints. A user story is an end goal expressed from the user’s perspective​. I have used the Definition of Ready (DoR)
to establish what a product backlog item needs before it can go into the sprint backlog andd the Definition of Done (DoD) defines what is needed before it can be regarded as complete.

## Database Structure
This project needs a relational database with at least 2 tables, showing the relationship between them. 
The tables created are:
- Exhibitions
- Items

Both tables have a primary key (). The foreign key is in the Items table, showing the relationship to the Exhibitions table.

The relationship is a ```one-to-many``` relationship where an Exhibition can have many Items but an Item can belong or appear in one Exhibition (can't be in 2 places at the same time) .

In the pictures below we can see an Entity Relationship Diagram explaining the relationship between the tables used in this project. This file can be found in [ERD](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/ERD%202%20tables.PNG).

![ERD](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/ERD%202%20tables.PNG)

I created a database in a virtual machine with mysql. The screenshot below shows the data defined for the columns and other actions carried out          

![Tables](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/DB%20Tables.png)  

![Sql Insert INTO](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/SQL%20Insert%20INTO.png)     

![Creating a DB message](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/Creating%20a%20DB.PNG)


## Risk Assessment
We use Risk Assessments to evaluate scenarios that may impact the project in a negative way. By knowing the risk and ways to mitigate them we are able to create a project were risks are less likely to occur. As parts of the projects were getting near completion others risks were added to the template and all of them revisited.This file can be found in [Risk Assessment](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/RA%20latest.PNG).

Below is a screenshot of the Risk Assessment I have carried out for this project. To see an earlier copy of it you can go to this [First Risk Assessment](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/RA%201.PNG). 

![Risk Assessment](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/RA%20latest.PNG)


## CI Pipeline
Continuous integration (CI) allows developers to frequently merge code changes into a central repository where others can contribute.    
The main Version Control System used for this project is GitHub. The VCS is designed to track changes to code over time as contributors add new features to the application. This system allows for cohesive collaboration and the ability to easily revert an application to a previous, stable state if new code breaks something.  
The CI server I have used to handle all the automated building, testing, and deployment of code as it is pushed to the VCS is Jenkings.

In the image below we can see how the developers (me) write the code in a chosen language (we have chosen Python for this project) and this gets push to the git repository and pull back to the local branch so everyone can work independently, contribute in the project and have always the latest version.   As explained above I have used Jira as a project tracking tool which it is supported by GitHub too so the boards can be updated, sprints start and finish and be always on top.   With continuous integration I have used Jenkins as CI server so some parts of the project can be automated by this tool.  Again, Jenkins and GitHub will pull and poll code as the scripts are run, saving time and gaining accuracy.
For the testing side of the peoject I have used pytest as testing environment and as a cloud provider I have used GCP.

![CI Pipeline](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/CI%20Pipeline.PNG)

Just as a note, when pushing files to Git that ca be compromised, usernames and passwords are disabled. Please see bellow:

![PW Protected] (https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/No%20password%20when%20pushing%20files%20to%20Git.PNG)  


### JENKINS
Jenkins is an open-source implementation of a Continuous Integration server written in Java. It works with multiple programming languages and can run on various platforms (Windows, Linux, and macOS). It is widely used as a CI (Continuous Integration) & CD (Continuous Delivery) tool.  
Within this project I have used Jenkins to automatize tasks that are monotonous and can be easily done by running a script.
![Installing Jenkins](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/Installing%20Jenkins.PNG)

![Jenkins Build](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/Jenkins%20Build.PNG)    

![Jenkins Script](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/Jenkins%20script.PNG)   



## Testing
As with most things, testing is the part where, after you have hit your head against the table for a 1000 times because you could not get the app to work when you were developing, then this 'testing' comes around and finishes you. When you thought that everything work, you have that feeling of accomplishment and triumph, you feel like a winner because your app does what you tell it to do... you decide to run 'some tests' and your app crashes. Yes, that is what happened to me every time I tried to run the Integration testing. 
I have used pytest as my testing tool. 

I started with unit testing, runing a total of 12 tests and reaching 95% of the covering report as you can see in the image below. You can also look at the HTML report [here](file:///C:/Users/B/Desktop/MICEXFinal/Supporting%20Files/Coverage%20Report.html).

Below is my first error when running unit testing with pytest....
[First error](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/First%20error%20running%20pytest.png).  
And it finally worked! I think what caused me the most trouble with the unit testing were the validators. 

Here you can see some of the many errors I encountered with doing [integration testing](https://onedrive.live.com/view.aspx?resid=96A94FCBFABC7DB5%2170903&id=documents&wd=target%28MICEX.one%7C5462FF26-5891-4F62-AC9E-01DC3AAB8BC9%2FErrors%7CC861D920-7CD4-41FE-B595-D82E5FE51456%2F%29). 
My machine just refuses to connect.... I would be logged into the terminal of the VM and I would be running a test and even though I am connected to it I will get errors saying it cannot connect. 


Screenshots of my progress are below:  
![Some Time Ago](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/Coverage%201.png)     

![Final report](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/final%20coverage.png)  


# Front-end Line
As per the scope of this project I have created a CRUD application where I am able to Create Items and Exhibitions, Read them, Update boths and Delete them. This should be sufficient for the scope of the project.

I am proud to show the ![First time the app worked](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/First%20time%20home%20page%20worked.PNG). 

It was the most fantastic feeling just to see 'Big Ben' written in the screen.

Below there are some screenshoots of what the app looks like at this stage.

![Home page](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/Home%20Page.PNG)   

![Add Items](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/Add%20Item.PNG)    

![Update Exhibition](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/Update%20Exhibition.PNG)    

As the project has progressed the file directory has changed as shown in the pictures below

![Just before Testing](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/Directories1.png)  


![After Testing](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/Directories2.PNG)

# GCP
I have been using GCP as a cloud provider for this projects. I have created a Virtual Machine Ubuntu 18.04LTS and a MySql Database to house the data needed.
In many occasions I have different issues with conecting to both machines and this will be something I will try to resolve in the near future. Should you want to see at some of those issues just "click me!!"
<details>
<summary>"Click me!!"</summary>
![Logging connection app through GCP](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/Logging%20connecting%20app%20through%20GCP.PNG)      

![unable to connect1](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/Unable%20to%20connect%20to%20DB%2023.04.PNG)


![unable to connect2](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/Unable%20to%20connect%20to%20DB%2023.05%2020.04.PNG)          


![unable to connect3](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/Unable%20to%20connect%20to%20DB%20exp%2023.04.PNG) 


![unable to connect4](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/Unable%20to%20connect%20to%20VM%2023.05%2020.09.PNG) 


![VM running](https://github.com/bmanzanoqa/MICEXFinal/blob/main/Supporting%20Files/VM%20running%20APP.PNG)  

</details>

## Images
Perhaps after all this reading you would like to see some of those items I kep talking about in here? Just 
<details>
<summary>"Click me!!"</summary>

![Famous Buildings1](https://github.com/bmanzanoqa/MICEXFinal/blob/main/images/Famous%20Buildings1.png)

![Great wall of China](https://github.com/bmanzanoqa/MICEXFinal/blob/main/images/Great%20wall%20of%20Chine.png)

![Stitch](https://github.com/bmanzanoqa/MICEXFinal/blob/main/images/Stitch.png)


![Lean Tower of Pisa](https://github.com/bmanzanoqa/MICEXFinal/blob/main/images/Lean%20Tower%20of%20Pisa.png)

![Dumbo](https://github.com/bmanzanoqa/MICEXFinal/blob/main/images/Dumbo.png)

</details>

## Author
Beatriz Manzano finished the first part of this project on the 24/05/2021


## Thank you!
Thank you to my trainers and everyone in my class for all the patience they have had and the help they have always provided.
