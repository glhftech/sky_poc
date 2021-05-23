Vagrant.configure("2") do |config|

 config.vm.box_check_update = "false"

 config.vm.provider "virtualbox" do |vb|
   vb.memory = "1024"
 end

 config.vm.define "app" do |app|
   app.vm.hostname = "app01"
   app.vm.box = "hashicorp/bionic64"
   app.vm.network :private_network, ip: "192.168.10.10"
   app.vm.network "forwarded_port", guest: "80", host: "8080"
   app.vm.provision "ansible" do |ansible|
     ansible.playbook="app-playbook.yaml"
   end
  end

 config.vm.define "db" do |db|
   db.vm.hostname = "db01"
   db.vm.box = "hashicorp/bionic64"
   db.vm.network :private_network, ip: "192.168.10.11"
   db.vm.provision "ansible" do |ansible|
     ansible.playbook="db-playbook.yaml"
   end
  end

end
