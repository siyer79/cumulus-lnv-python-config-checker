#Vagrant.configure(2) do |config|
#  config.vm.box = "cumulus-vx-3.0.0" end

Vagrant.configure(2) do |config|

   config.vm.box = "cumulus-vx-3.0.0"

   
##### DEFINE VM for spine1 #####
   config.vm.define "spine1" do |device|
     device.vm.hostname = "spine1"

     # Internal network for swp* interfaces.
     device.vm.network "private_network", virtualbox__intnet: "swp1"
     device.vm.network "private_network", virtualbox__intnet: "swp2"
     device.vm.network "private_network", virtualbox__intnet: "swp3"
     device.vm.network "private_network", virtualbox__intnet: "swp4"

     device.vm.provider "virtualbox" do |v|
       v.name = "spine1"
       v.memory = 512
     end

   end

##### DEFINE VM for spine2 #####
   config.vm.define "spine2" do |device|
     device.vm.hostname = "spine2"

     # Internal network for swp* interfaces.
     device.vm.network "private_network", virtualbox__intnet: "swp1"
     device.vm.network "private_network", virtualbox__intnet: "swp2"
     device.vm.network "private_network", virtualbox__intnet: "swp3"
     device.vm.network "private_network", virtualbox__intnet: "swp4"

     device.vm.provider "virtualbox" do |v|
       v.name = "spine2"
       v.memory = 512
     end

   end

##### DEFINE VM for leaf1 #####
   config.vm.define "leaf1" do |device|
     device.vm.hostname = "leaf1"

     # Internal network for swp* interfaces.
     device.vm.network "private_network", virtualbox__intnet: "swp1"
     device.vm.network "private_network", virtualbox__intnet: "swp2"
     device.vm.network "private_network", virtualbox__intnet: "swp3"
     device.vm.network "private_network", virtualbox__intnet: "swp4"
     device.vm.network "private_network", virtualbox__intnet: "swp5"

     device.vm.provider "virtualbox" do |v|
       v.name = "leaf1"
       v.memory = 512
     end

   end

##### DEFINE VM for leaf2 #####
   config.vm.define "leaf2" do |device|
     device.vm.hostname = "leaf2"

     # Internal network for swp* interfaces.
     device.vm.network "private_network", virtualbox__intnet: "swp1"
     device.vm.network "private_network", virtualbox__intnet: "swp2"
     device.vm.network "private_network", virtualbox__intnet: "swp3"
     device.vm.network "private_network", virtualbox__intnet: "swp4"
     device.vm.network "private_network", virtualbox__intnet: "swp5"


     device.vm.provider "virtualbox" do |v|
       v.name = "leaf2"
       v.memory = 512
     end

   end


##### DEFINE VM for server1 #####
   config.vm.define "server1" do |device|
     device.vm.hostname = "server1"
     #device.vm.network "private_network", ip: "192.168.119.100/24"

     device.vm.provider "virtualbox" do |v|
       v.name = "server1"
       v.memory = 512
     end

   end

##### DEFINE VM for server2 #####
   config.vm.define "server2" do |device|
     device.vm.hostname = "server2"
     #device.vm.network "private_network", ip: "192.168.100/24"

     device.vm.provider "virtualbox" do |v|
       v.name = "server2"
       v.memory = 512
     end

   end

   config.vm.provision "ansible" do |ansible|
     ansible.verbose = "vvv"
     ansible.playbook = "lnv-playbook.yml"
   end

end



