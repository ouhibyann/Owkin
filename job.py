"""
Execute the following:

    # Build the docker image
    # Scan for vulnerabilities with docker scan
    # Status:
        # Fail -> if any vulnerabilites
        # Succes + perf from the echo 
    # Job Id associated to the image
"""

from  utils.docker_utils import build, run, get_Container


def process(Dockerfile):

    image = build(Dockerfile)
    # The return from build is a tuple of 2 objects:
    # First element is the one we want -> a docker image type. 2dn one is memory address
    get_Container(image[0].id)
    r = get_Container(image)

    output = run(r)

    if output != True:
        return {'job_id': 1, 'job_status': 'failed'}

    

