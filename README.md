# Elyadata Interview Facebook Scraper 

Elyadata Facebook Scraper is a web scraping application that extracts data from Facebook using FastAPI and stores it in a MongoDB database.This project is a step of the Elyadata hiring process.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Dockerization](#dockerization)

## Description

The Elyadata Facebook Scraper is designed to gather data from Facebook Public Profile using web scraping techniques based on ID and ACCESS TOKEN . It utilizes FastAPI as the web framework and MongoDB as the database to store the scraped information.

## Features

- **Web Scraping:** Extracts data from Facebook Public Profile.
- **FastAPI:** Utilizes FastAPI for building a high-performance web API.
- **MongoDB:** Stores scraped data in a MongoDB database.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/JAADARI/scraping_project_elyadata.git
    cd scraping_project_elyadata
    ```

## Usage

1. Start the Docker-Compose:

    ```bash
    sudo docker-compose up
    ```

2. Make Request using Curl Command:

    ```bash
    curl "http://localhost:8000/scrape-facebook/<ID>?access_token=<ACCESS_TOKEN>"   
    ```

3. The MongoDB database is accessible from the Docker Container:
    ```bash
    sudo docker exec -it elyadata_facebook_scraper_mongo_1 mongosh    
    use scraping_db   
    db.facebook_data.find().pretty()
    ```



## Technologies Used

- FastAPI
- MongoDB
- Docker
- Python

## Dockerization

The application is containerized using Docker. The Dockerfile is included in the repository for building the application image. The `docker-compose.yml` file defines the services and their configurations.

To pull and build the Docker image, run:
    
    
   
    sudo docker pull jaadarix/elyadata_project:final
    sudo docker build -t jaadarix/elyadata_project:final .
    
## Screenshots of the project:
### Running the Docker-compose to start both services(App,Mongo):

![dockercompose](https://github.com/JAADARI/scraping_project_elyadata/assets/78422942/e289f424-602e-4705-884f-08da0fc7305d)

### Request using Curl Command:

![scraping succes](https://github.com/JAADARI/scraping_project_elyadata/assets/78422942/ef2b4e57-0511-4bc8-b23b-fd8730edb4bf)

### Preview of the Scraped data:

![scraping](https://github.com/JAADARI/scraping_project_elyadata/assets/78422942/e95fafd0-1b19-43e1-bd28-90cd80e75f3e)

### Checking if the data was succefully added to the containerized database:

![dbmongo](https://github.com/JAADARI/scraping_project_elyadata/assets/78422942/1989d218-40be-4277-9c89-a19be330d2e7)



## Connect with Me

- [LinkedIn](https://www.linkedin.com/in/jaadarix/)
- [Zindi](https://zindi.africa/users/JAADARIX)

