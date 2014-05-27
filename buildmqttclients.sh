#!/bin/bash
cd /home/iot/iotframework/mqttclient
docker build --rm -t tlindener/mqttclient .
cd /home/iot/iotframework/mqttserver
docker build --rm -t tlindener/mqttserver .
cd /home/iot/iotframework/openvswitch
docker build --rm -t tlindener/docker-ovs .

ovs=$(docker run -p 6640:6640 -p 6633:6633 -p 6644:6644 --privileged=true -d -i -t tlindener/docker-ovs /bin/supervisord -n)
ovspid=$(docker inspect --format='{{ .State.Pid }}' $ovs)
echo $ovs
echo $ovspid
mkdir -p /var/run/netns
rm -f /var/run/netns/$ovspid
ln -s /proc/$ovspid/ns/net /var/run/netns/$ovspid

mqttserver=$(docker run -d -P tlindener/mqttserver)
mqttserverpid=$(docker inspect --format='{{ .State.Pid }}' $mqttserver)
rm -f /var/run/netns/$mqttserverpid
ln -s /proc/$mqttserverpid/ns/net /var/run/netns/$mqttserverpid
echo $mqttserver
echo $mqttserverpid 
apt-get install openvswitch-switch -y
ovs-vsctl --db=tcp:172.17.42.1:6640 add-br br0
ovs-vsctl --db=tcp:172.17.42.1:6640 set bridge br0 datapath_type=netdev

switchcounter=1
tmplinkname1="eth$ovspid"
tmplinkname2="eth$mqttserverpid"
ip link add name $tmplinkname1 type veth peer name $tmplinkname2
ip link set $tmplinkname1 netns $ovspid
ip link set $tmplinkname2 netns $mqttserverpid
ip netns exec $mqttserverpid ip link set $tmplinkname2 name eth1
ip netns exec $ovspid ip link set $tmplinkname1 name eth$switchcounter
ovs-vsctl --db=tcp:172.17.42.1:6640 add-port br0 eth$switchcounter 
ip netns exec $mqttserverpid ifconfig eth1 192.168.5.5/24 up
ip netns exec $ovspid ip link set eth$switchcounter up
switchcounter=$(($switchcounter+1))

for i in {6..10}
do
	mqttclient=$(sudo docker run -d -P tlindener/mqttclient)
	dockerpid=$(docker inspect --format='{{ .State.Pid }}' $mqttclient)
	
	rm -f /var/run/netns/$dockerpid
	ln -s /proc/$dockerpid/ns/net /var/run/netns/$dockerpid
	tmp="eth$dockerpid"
	ip link add name $tmp type veth peer name local-veth1
	ip link set $tmp netns $ovspid
	ip link set local-veth1 netns $dockerpid
	ip netns exec $dockerpid ip link set local-veth1 name eth1
	ip netns exec $ovspid ip link set $tmp name eth$switchcounter
	ovs-vsctl --db=tcp:172.17.42.1:6640 add-port br0 eth$switchcounter 
	ip netns exec $dockerpid ifconfig eth1 192.168.5.$i/24 up
	ip netns exec $ovspid ip link set eth$switchcounter up
	switchcounter=$(($switchcounter+1))
done





