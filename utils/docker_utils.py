
import docker
import json

from config import CONTAINER_LIMIT


docker_client = docker.from_env()


def build_image(Dockerfile_path, image_tag='latest'):
    """
    This method build a docker image from a submited path where dockerfile lays

    :params     docker image
                image_tag
    :return     docker.image object type 
    """
    # The docker-py .build method check auto if the image already exists and doesn't rebuild it if Dockerfile from which it's built is exactly the same
    image = docker_client.images.build(path=Dockerfile_path, container_limits=CONTAINER_LIMIT, tag=image_tag)
    return image


def get_Image(image):
    return docker_client.images.get(image)


def build_container(docker_image, container_name):
    return docker_client.containers.create(docker_image, name=container_name)


def run_container(docker_image, container_name='Owkin', volume=['data:/data']):

    """
    This method run a docker container from a previously built image
    We handle the case of Container Error when being built
    Also the case of any API built in from docker-py error


    :params     docker image
    :return     False, error - if any   
    :rtypes     boolean, json
    """
    try:
        docker_client.containers.run(docker_image, name=container_name, volumes=volume)

    # Errors are stored into the logs
    except docker.errors.ContainerError as e:

        return False, json.dumps(str(e)) 

    except docker.errors.APIError as e:

        return False, json.dumps(str(e))



def create_volume(volume_name):
    # As we need to create a volume on /data directory
    # The optional 'volumes' param is provided by default
    docker_client.volumes.create(name=volume_name, driver='local')


def get_volume(volume_name):
    return docker_client.volumes.get(volume_name)

