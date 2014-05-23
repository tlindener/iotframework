#!/bin/bash

SCRIPTPATH=$( cd "$(dirname "$0")" ; pwd -P )
cd $SCRIPTPATH

docker build --rm -t tlindener/mqttclient mqttclient
docker build --rm -t tlindener/mqttserver mqttserver
apt-get install openvswitch-switch -y

ovs=$(docker run -d -i -t davetucker/docker-ovs:2.1.2 /bin/supervisord -n)
ovspid=$(docker inspect --format='{{ .State.Pid }}' $ovs)
echo $ovs
echo $ovspid
mkdir -p /var/run/netns
rm -f /var/run/netns/$ovspid
ln -s /proc/$ovspid/ns/net /var/run/netns/$ovspid
ip netns exec $ovspid /etc/init.d/openvswitch-switch status

mqttserver=$(docker run -d -P tlindener/mqttserver)
mqttserverpid=$(docker inspect --format='{{ .State.Pid }}' $mqttserver)
echo $mqttserver
echo $mqttserverpid
rm -f /var/run/netns/$mqttserverpid
ln -s /proc/$mqttserverpid/ns/net /var/run/netns/$mqttserverpid

ip netns exec $ovspid ovs-vsctl add-br br0
ip netns exec $ovspid ovs-vsctl set bridge br0 datapath_type=netdev

switchcounter=1
ethovs="eth$ovspid"
ethmqtt="eth$mqttserverpid"
ip link add name $ethovs type veth peer name $ethmqtt
ip link set $ethovs netns $ovspid
ip link set $ethmqtt netns $mqttserverpid
ip netns exec $mqttserverpid ip link set $ethmqtt name eth1
ip netns exec $ovspid ip link set $ethovs name eth$switchcounter
ip netns exec $ovspid ovs-vsctl add-port br0 eth$switchcounter
ip netns exec $mqttserverpid ifconfig eth1 192.168.5.5/24 up
ip netns exec $ovspid ip link set eth$switchcounter up
switchcounter=$(($switchcounter+1))

for i in {6..10}
do
        mqttclient=$(sudo docker run -d -P tlindener/mqttclient)
        dockerpid=$(docker inspect --format='{{ .State.Pid }}' $mqttclient)
        rm -f /var/run/netns/$dockerpid
        ln -s /proc/$dockerpid/ns/net /var/run/netns/$dockerpid
        ethclient="eth$dockerpid"
        ip link add name $ethclient type veth peer name local-veth1
        ip link set $ethclient netns $ovspid
        ip link set local-veth1 netns $dockerpid
        ip netns exec $dockerpid ip link set local-veth1 name eth1
        ip netns exec $ovspid ip link set $ethclient name eth$switchcounter
        ip netns exec $ovspid ovs-vsctl add-port br0 eth$switchcounter
        ip netns exec $dockerpid ifconfig eth1 192.168.5.$i/24 up
        ip netns exec $ovspid ip link set eth$switchcounter up
        switchcounter=$(($switchcounter+1))
done





