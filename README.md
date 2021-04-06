![Python application test with Github Actions](https://github.com/sonercand/flaskapp-azure-ci-cd/actions/workflows/pythonapp.yml/badge.svg) [![Build Status](https://dev.azure.com/sonercand/flask-ml-deploy/_apis/build/status/sonercand.flaskapp-azure-ci-cd?branchName=main)](https://dev.azure.com/sonercand/flask-ml-deploy/_build/latest?definitionId=8&branchName=main)


# Overview
Building CI/CD pipeline using github actions and azure devops pipelines. Project involves a dummy flask application and azure webapps. 
Any changes to the flask application developped locally would be pushed in to git repository consequently triggering github actions(including activities such as setup Python, installing dependencies, lint with pylint, test with pytest). Then azure pipelines connected to git repository would be triggered to build and deploy the flask application into azure webapp microservice.



## Project Plan
* [Project Trello Board](https://trello.com/b/DTgl4eeb/building-ci-cd-pipeline)
* [Project Plan](https://docs.google.com/spreadsheets/d/1hhWwv4-5kIjGAPCK1zGWjlT58VBuoIrDHjL-ercclaE/edit?usp=sharing)

## Instructions
### Architectural Diagram
![Overview](https://github.com/sonercand/flaskapp-azure-ci-cd/blob/main/diagrams/overview_diagram.jpg)  
* Project Overview Diagram depicting the main components(Local Code, GitHub, Azure DevOps,and Azure WebApps) and how they are tied together.
### Running Instructions
Note: For simplicity azure cloud shell was used to store the local code in this instance however code editing environment could simply be the local machine since the whole process is automated it would not make any difference. 
#### Setting up: code and the environment
Following steps are for setting up the code environment and deploying it to azure platform. In other words prepping up for ci/cd pipeline
##### Steps:
* 1. Clone this repo into your development environment. If you have not already, go to your dev. environment and create an ssh key. Copy your puplic key and paste into github(can be found under settings>ssh and gpg keys). For more information please read [github documentation](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account). The image below is the screen shot from azure cloud shell while repo was being cloned. 
![Screen shot cloning a repo](https://github.com/sonercand/flaskapp-azure-ci-cd/blob/main/diagrams/cloning_repo_to_azure.PNG)
Here is the syntax: git clone git@github.com:sonercand/flaskapp-azure-ci-cd.git
* 2. Running make file
  * Make setup: This will create a python virtual environment ![Run MakeSetup](https://github.com/sonercand/flaskapp-azure-ci-cd/blob/main/diagrams/Image%2005-04-2021%20at%2015.55.jpg)
  
  * Activate virtual environment: ![activate env](https://github.com/sonercand/flaskapp-azure-ci-cd/blob/main/diagrams/Image%2005-04-2021%20at%2016.11.jpg)
  
  * Run make all:This will install requirements, and will run pytest and pylint. Once you run make all you should see a screen similar to the one below. ![make all](https://github.com/sonercand/flaskapp-azure-ci-cd/blob/main/diagrams/Image%2005-04-2021%20at%2016.36.jpg)
  
* 3. az webapp up: Creates a webapp and deploys it from local folder. ![webapp up](https://github.com/sonercand/flaskapp-azure-ci-cd/blob/main/diagrams/Image%2005-04-2021%20at%2017.57.jpg) This will create and deploy webapp within the selected resource group(--resource-group <rg name>).Note: The name parameter(-n <name>) should be unique since it will be a subdomain name on https://<name>.azurewebsites.net.
* 4. Check if everything works. 
   * Check the url created as a result of webapp creation process.You should see this output below: ![html](https://github.com/sonercand/flaskapp-azure-ci-cd/blob/main/diagrams/Image%2005-04-2021%20at%2020.27.jpg)
   * Test output: Check if ./make_predict_azure_app.sh returns the expected result as below: ![output](https://github.com/sonercand/flaskapp-azure-ci-cd/blob/main/diagrams/Image%2005-04-2021%20at%2020.42.jpg)
   * Load Testing: For load testing locust is used. Install locust via pip and create a locust.py file(file name is typically locustfile.py even though in this instance it is just locust). For more details please check [locust quick start guide](https://docs.locust.io/en/stable/quickstart.html). Then in command line run locust --locustfile==locust.py. When locust starts click on the localhost link where you can set the host name, number of users and swarm rate for the load test.![locust page](https://github.com/sonercand/flaskapp-azure-ci-cd/blob/main/diagrams/Image%2006-04-2021%20at%2017.04.jpg) ![locust stats](https://github.com/sonercand/flaskapp-azure-ci-cd/blob/main/diagrams/Image%2006-04-2021%20at%2017.03.jpg)
#### Setting up CI/CD pipelines.
* 1. Set up Github Actions: Click on actions tab on github repo. Then click new workflow button which will take you to a page where you can choose a workflow template or create one for yourself. In this instance, pythonapp.yml is the workflow file which is under .github/workflows. It is triggered on push, runs on ubuntu, sets up python 3.5 and runs make commands. So that when new code pushed into the repo it will automatically be linted and tested.![github actions](https://github.com/sonercand/flaskapp-azure-ci-cd/blob/main/diagrams/Image%2006-04-2021%20at%2017.34.jpg)
* 2. Setting up Azure Devops Pipelines:
   * login to azure devops
   * create a project
   * Click project settings and create service connection. 
   * Create new service connection
   * Select Azure Resource Manager then select service principal. In this step you will select your subscription and resource group to host the service principal.
   * create a new pipeline 
   * select repository (where you host the source code). In this instance it is a github repo so select github and then select the relevant repo. 
   * configure your pipeline to deploy python code to azure webapp.
* 3. Test run to see if everything works all right.  
   * Push a change from local repo with a commit message in this case commit message is minor: test ci/cd:![local change](https://github.com/sonercand/flaskapp-azure-ci-cd/blob/main/diagrams/Image%2006-04-2021%20at%2018.20.jpg)
   * Check azure actions:![actions](https://github.com/sonercand/flaskapp-azure-ci-cd/blob/main/diagrams/Image%2006-04-2021%20at%2018.25.jpg)
   * Check azure devops pipelines:![pipelines](https://github.com/sonercand/flaskapp-azure-ci-cd/blob/main/diagrams/Image%2006-04-2021%20at%2018.28.jpg)
   * Check webapp deployment: ![webpage](https://github.com/sonercand/flaskapp-azure-ci-cd/blob/main/diagrams/Image%2006-04-2021%20at%2021.44.jpg)

 
 
<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


