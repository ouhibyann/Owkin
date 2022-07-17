# Owkin - 2022/07/18 

## Thoughts - This is how my work went.
1/ Flask - as I'm more used to it - and upload a file. Was pretty straightforward, implemented POST request first but will do the get later. <br />
2/ Docker implementation via Python into the service. docker-py library. <br />
3/ security checks -> hard to implement, will work on later. <br />
4/ Process of storing job perfs into data/perf.json and mount volume -> This one was a bit tricky with the docker-py library but managed to do it. <br />
5/ Storing data in DB before sending it to client -> Was okay for the 'failed' job, however for the 'success' one I didn't know how to get the perf value from inside the container or volume. <br />
6/ Retrieving data from DB to send it in get request.


## Container security
I'd use an external security tool to analyse docker image before running it - Snyk.
In this project, I tried to run a 'docker scan image' commande in shell trough a python script - security.py
However, as it was getting more and more complicated, I prefere not to go deeper in this script.
You can find exemple in 'process.py' where it would happend in the whole workflow / process.


## Jobs storage 
You can find and exemple in the models.job file that represent the model of the DB.
The table isstructured as follow: <br />
    job_id (int) | job_status (varchar) | performances (float) | docker_imageID (varchar) | logs 
Another DB - e.g, mongo DB - would be more suitable to store logs from the security container analysis tool instead of json.
<br />
job_id -> id to retrieve the job. <br />
job_status -> success / fail - according to the analysis from Snyk or if any error like container already exists. <br />
performances -> performance inside the volume. <br />
docker_imageID -> associated docker_image ID. <br />
logs -> output from the Snyk analysis.


## Tests
The service being designed as a standalone - without any interactions after submitting the file.
I didn't find out test to performs outside of ORM check tests - adding a job, retrieving a job.


## DB / Table  - postgreSQL
I provided an export of the PostgreSQL table.
Everything is mapped in the 'config.json' so you can configure your own


## Postman
I provided JSON postman curls to test the different endpoints


## Limits of the code
The volume being staticaly defined -> 'data' by default but some may argue it should be passed as a var in the dockerfile <br />
Security shell script -> executing shell in python program doesn't seem relevant at all and allows for some inconsistency depending on the system where the code is deployed. <br />
Roots inside the 'app.py' creates a strong dependency on this file. A solution can be to create a 'Ressource' file where all the @route are mapped and then use 'add.ressource' to the correct ressource. This is allowed by 'flask-restful' framework for exemple.


## What could be improved
Make the app run inside a container so it can access the volume 'data' and read the perf from it. <br />
Make it easier for you to check the work -> config.json to help -> The best way would be a docker compose to run with the app in 1 container and the postgreSQL db in the other, and you just have to endpoints the container' addresses to check everything without any installation.
