# ansible-automation
ansible-automation

## Getting started

Clone repositary, activate env (if you want), install ansible and run playbook:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
git clone https://github.com/bbossankimster/ansible-automation.git
cd ansible-automation/
# If venv is used
# python3 -m venv env
# source env/bin/activate
pip3 install ansible
export ANSIBLE_LIBRARY=./library

To run playbook:
ansible-playbook playbook.yml -i inventory.ini
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

