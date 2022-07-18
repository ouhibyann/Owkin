"""
Execute the following:

    # Build the docker image
    # Scan for vulnerabilities with docker scan
    # Status:
        # Fail -> if any vulnerabilites
        # Succes + perf from the volume 
    # Job Id associated to the image
"""

# from security import container_scan
from  utils.docker_utils import build_image, run_container, get_Image, create_volume



def process(Dockerfile):

    create_volume(volume_name='data') # Should be specified in Dockerfile but can be created here
    image = build_image(Dockerfile)
    # The return from build is a tuple of 2 objects:
    # First element is the one we want -> a docker image type. 2dn one is memory address
    r = get_Image(image[0].id)

    # Here, we should call for the security analytic tool before any action as a container - Snyk for exemple
    # container_scan(image, output='output.log')
    # If successful in the analysis, we continue. Else, we end the process

    output = run_container(r)

    return output
