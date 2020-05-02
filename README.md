# [PYTHON] L4/L3 Auto Firewall Rule/Soft
Run/Install,

> sudo su

> wget https://raw.githubusercontent.com/obirninja/Auto-Firewall-L4-L3/master/autofirewall.py

> chmod +x autofirewall.py

> python autofirewall.py

Iptables Port Connection Limit(FIN,SYN,RST,ACK,SYN)
All Rule,
```
iptables -A INPUT -p tcp -m tcp --dport [PORT] --tcp-flags FIN,SYN,RST,ACK SYN -m connlimit --connlimit-above [cNumber] --connlimit-mask 32 -j REJECT --reject-with tcp-reset

iptables -A FORWARD -p tcp --syn -m limit --limit 1/second -j ACCEPT

iptables -A FORWARD -p udp -m limit --limit 1/second -j ACCEPT

iptables -A FORWARD -p icmp --icmp-type echo-request -m limit --limit 1/second -j ACCEPT

iptables -A FORWARD -p tcp --tcp-flags SYN,ACK,FIN,RST RST -m limit --limit 1/s -j ACCEPT

iptables -A INPUT -p tcp -m tcp --tcp-flags RST RST -m limit --limit 2/second --limit-burst 2 -j ACCEPT
```
