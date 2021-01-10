import os
 
import testinfra.utils.ansible_runner
 
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')
 
 
def test_is_docker_installed(host):
    package_docker = host.package('docker-ce')
 
    assert package_docker.is_installed