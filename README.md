# POC

## Required tools set:
- Virtualbox
- Vagrant
- Ansible

## Provision:
- Install virtual box, vagrant and ansible
- git clone https://github.com/glhftech/sky_poc.git
- cd sky_poc
- vagrant up

## Output:
Vagrant will provision 1 app node and 1 db node.
Also, it will use ansible to config the 2 nodes.
App node will have a HTTP endpoint http://192.168.10.10:8080/app, which will insert current timestamp to db once received a POST request.
Db node is a Cassandra DB, which will persist the timestamp into the keyspace "test", table "test", column "ts".

## Checking:
- Insert timestamp: 
  - curl -X POST http://127.0.0.1:8080/app
- Check db table: 
  - vagrant ssh db 
  - cqlsh -e "select * from test.test;"

## Cleanup:
- vagrant destroy

## Files:
- Vagrantfile
  - vagrant file
- app.py
  - python flask app
- app-playbook.yaml
  - ansible playbook to config app node
- db-playbook.yaml
  - ansible playbook to config db node
