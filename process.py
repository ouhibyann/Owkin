'''
    This file handles the Docker build & analysis part

'''

import docker


def build(dockerfile):
    client = docker.from_env()