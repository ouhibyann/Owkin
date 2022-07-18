
import docker
import json


f = open('config.json')
dict = json.load(f)
f.close()
CONTAINER_LIMIT = dict['CONTAINER_LIMIT']

docker_client = docker.from_env()


def build_image(Dockerfile_path, image_tag='latest'):
    """
    This method build a docker image from a submited dockerfile

    :params     docker image
                image_tag
    :return     docker.image object type 
    """
    # Might be useful to check if image already exists and load it instead of rebuild
    image = docker_client.images.build(path=Dockerfile_path, container_limits=CONTAINER_LIMIT, tag=image_tag)
    return image
    # get_ContainerID()


def get_Image(image):
    return docker_client.images.get(image)


def build_container(docker_image, container_name):
    return docker_client.containers.create(docker_image, name=container_name)


def run_container(docker_image, container_name='Owkin', volume=['data:/data']):

    """
    This method run a docker container from a previously built image

    :params     docker image
    :return     False if error in container run - means error in Dockerfile 
    """
    try:
        docker_client.containers.run(docker_image, name=container_name, volumes=volume)
    except (docker.errors.ContainerError, docker.errors.APIError):
        return False



def create_volume(volume_name):
    # As we need to create a volume on /data directory
    # The optional 'volumes' param is provided by default
    docker_client.volumes.create(name=volume_name, driver='local')


def get_volume(volume_name):
    return docker_client.volumes.get(volume_name)

