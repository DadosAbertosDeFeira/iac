import os
 
import testinfra.utils.ansible_runner
 
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')
 
 
def test_is_http_listening(host):
    socket_http = host.socket("tcp://0.0.0.0:80")
 
    assert socket_http.is_listening 

def test_is_https_listening(host):
    socket_https = host.socket("tcp://0.0.0.0:443")
 
    assert socket_https.is_listening 