'''
Execute the following:

    # Build the docker image
    # Scan for vulnerabilities with docker scan
    # Status:
        # Fail -> if any vulnerabilites
        # Succes + perf from the echo 
    # Job Id associated to the image

'''

from  utils.docker_utils import build, run, get_Container


def process(container):
    

    build(container)
    output = run('owkin')
    if output == False:
        return {'container_name': get_Container('owkin'), 'job_status': 'failed'}
    

