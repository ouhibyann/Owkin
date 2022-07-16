import subprocess
import os


def container_scan(docker_image, output='output.log'):
    """
    Executing 'docker scan' command trough shell
    A better use of external service can be find in the architecture diag
    """
    os.makedirs('tmp', exist_ok=True)

    with open('tmp/'+output, "w") as output:
        docker_scan = str('docker scan '  + docker_image)
        subprocess.run(docker_scan + ';' + 'Y', shell=True, stdout=output, stderr=output)
        # You need to be connected to use the scan feature
        # docker credentials needed for that part

