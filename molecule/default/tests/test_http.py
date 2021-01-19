import os
 
import testinfra.utils.ansible_runner
 
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')
 
 
def test_is_http_listening(host):
    socket_http = host.socket("tcp://0.0.0.0:80")
 
    assert socket_http.is_listening 