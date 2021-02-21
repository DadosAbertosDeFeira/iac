import os
 
import testinfra.utils.ansible_runner

import pytest
 
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

repository_path = '/tmp/maria-quiteria'
app_name = 'mariaquiteria.gomex.me'

def run_inside_repository_decorator(original):
    def decorated(command, *args, **kwargs):
        new_command = f'cd {repository_path} && ' + command
        return original(new_command, *args, **kwargs)
    return decorated

@pytest.fixture()
def host_with_repository(host, monkeypatch):
    host.run_test('ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa -q')
    host.run_test('ssh-keyscan -t rsa localhost > ~/.ssh/known_hosts')
    host.run_test('dokku ssh-keys:add test-key ~/.ssh/id_rsa.pub')
    host.run_test(f'git clone https://github.com/DadosAbertosDeFeira/maria-quiteria.git {repository_path}')
    with monkeypatch.context() as m:
        m.setattr(host, 'run', run_inside_repository_decorator(host.run))
        host.run(f'git remote add dokku dokku@localhost:{app_name}')
        yield host
    host.run_test('dokku ssh-keys:remove test-key')
    host.run_test(f'rm -rf ~/.ssh {repository_path}')

def test_deploy_is_successfull(host_with_repository):
    host = host_with_repository

    cmd = host.run('git push dokku main:master')

    print(cmd.stdout)
    print(cmd.stderr)
    assert cmd.rc == 0