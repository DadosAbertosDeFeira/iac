# IaC

Esse repositório por hora servirá de espaço para organização do time de infra para o projeto Dados Abertos De Feira.

Aqui teremos a lista de tarefas e qualquer documento necessário pra ajudar pessoas a começarem a ajudar.

# Como executar

## Requisitos:
Instale o Python 3

Instale o ansible usando venv:

```
python3 -m venv .venv
source .venv/bin/activate
pip install ansible
```

Primeiro é necessário instalar as roles necessárias com o comando:

```
ansible-galaxy install -r requirements.yml
```

Depois, crie um inventário para a máquina de teste. No repositório há um inventário de exemplo em *hosts.example*. Recomenda-se utilizar uma máquina com Ubuntu 18.04.
