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
#### Steps:
* 1. Clone this repo into your development environment. If you have not already, go to your dev. environment and create an ssh key. Copy your puplic key and paste into github(can be found under settings>ssh and gpg keys). For more information please read [github documentation](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account). The image below is the screen shot from azure cloud shell while repo was being cloned. 
![Screen shot cloning a repo](https://github.com/sonercand/flaskapp-azure-ci-cd/blob/main/diagrams/cloning_repo_to_azure.PNG)
Here is the syntax: git clone git@github.com:sonercand/flaskapp-azure-ci-cd.git
* 2. Running make file
  * Make setup: This will create a python virtual environment ![Run MakeSetup](https://github.com/sonercand/flaskapp-azure-ci-cd/blob/main/diagrams/Image%2005-04-2021%20at%2015.55.jpg)
  
  * Activate virtual environment: ![activate env](https://github.com/sonercand/flaskapp-azure-ci-cd/blob/main/diagrams/Image%2005-04-2021%20at%2016.11.jpg)
  
  * Run make all:This will install requirements, and will run pytest and pylint. Once you run make all you should see a screen similar to the one below. ![make all](https://github.com/sonercand/flaskapp-azure-ci-cd/blob/main/diagrams/Image%2005-04-2021%20at%2016.36.jpg)
  
* 3. az webapp up: Creates a webapp and deploys it from local folder.
![webapp up](https://github.com/sonercand/flaskapp-azure-ci-cd/blob/main/diagrams/Image%2005-04-2021%20at%2017.57.jpg)



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


