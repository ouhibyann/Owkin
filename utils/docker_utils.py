
import docker


# Set the container:
    # memory
    # total memory
    # CPU shares
    # CPU to be used
CONTAINER_LIMIT = {'memory': 1*10**9, 'memswap': -1, 'cpushares': 1, 'cpusetcpus': 2 }

docker_client = docker.from_env()


def build(Dockerfile_path, image_tag='latest'):
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


def run(image):

    """
    This method run a docker container from a previously built image

    :params     docker image
    :return     False if error in container run - means error in Dockerfile 
    """
    try:
        docker_client.containers.run(image)
    except docker.errors.ContainerError:
        return False


def create_volume(volume_name):
    docker_client.volumes.create(name=volume_name, driver='local')
    
  
def get_volume(volume_name):
    return docker_client.volumes.get(volume_name)


def get_Image(image):
    return docker_client.images.get(image)

