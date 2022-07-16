# Owkin

## Thoughts - This is how my work went
1/ Flask - as I'm more used to it - and upload a file. Was pretty straightforward, implemented POST first but will do the get later. <br />
2/ Docker implementation via Python into the service. docker-py library. <br />
3/ security checks -> hard to implement, will work on later <br />
4/ Process of storing job perfs into data/perf.json and mount volume.

Realised the Dockerfile provided is one supposed to fail! As the data dir is not mkdir before.


## Container security
I'd use an external security tool to analyse docker image before running it - Snyk.
In this project, I tried to run a 'docker scan image' commande in shell trough a python script - security.py


## Jobs storage 
I would have a table in PostgreSQL storing log from the analysis of the 'job'.
You can find and exemple in the models.job file that represent the model of the DB.
The table would be structured as follow:
    job_id (int) | job_status (varchar) | performances (float) | docker_imageID (varchar) | logs 


job_id -> id to retrieve the job
job_status -> success / fail - according to the analysis from Snyk.
performances -> performance echoed by the container
docker_imageID -> associated docker_image ID
logs -> output from the Snyk analysis


## What could be improved

All the global variables 'CONTAINER_LIMIT', 'ALLOWED_FILES', 'UPLOAD_FOLDER' could be put in a json file and retrieve through the code.