'''
    This file handles the Docker build & analysis part

'''

import docker


# Set the container:
    # memory
    # total memory
    # CPU shares
    # CPU to be used
CONTAINER_LIMIT = {'memory': 1*10**9, 'memswap': -1, 'cpushares': 1, 'cpusetcpus': 2 }

docker_client = docker.from_env()


def build(Dockerfile_path):

    # Might be useful to check if image already exists and load it instead of rebuild
    docker_client.images.build(path=Dockerfile_path, container_limits=CONTAINER_LIMIT)


def create_volume(volume_name):
    docker_client.volumes.create(name=volume_name, driver='local')

  
def get_volume(volume_name):
    return docker_client.volumes.get(volume_name)