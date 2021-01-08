# IaC

Esse repositório por hora servirá de espaço para organização do time de infra para o projeto Dados Abertos De Feira.

Aqui teremos a lista de tarefas e qualquer documento necessário pra ajudar pessoas a começarem a ajudar.

## Desenvolvimento

### Requisitos

 - Python 3 [installed](https://www.python.org/downloads/)
 - Molecule [installed](https://molecule.readthedocs.io/en/latest/installation.html):

    ```
    $ python3 -m venv .venv
    $ source .venv/bin/activate
    $ pip install "molecule[docker,lint]"
    ```

 - Testando as roles

    ```
    cd /roles/setting-server
    molecule create
    molecule converge
    ```
