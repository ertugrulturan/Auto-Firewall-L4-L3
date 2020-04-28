# [PYTHON] L4/L3 Auto Firewall Rule/Soft
Run/Install,

> sudo su

> wget https://raw.githubusercontent.com/obirninja/Auto-Firewall-L4-L3/master/autofirewall.py

> chmod +x autofirewall.py

> python autofirewall.py

Iptables Port Connection Limit(FIN,SYN,RST,ACK,SYN),
```
iptables -A INPUT -p tcp -m tcp --dport [PORT] --tcp-flags FIN,SYN,RST,ACK SYN -m connlimit --connlimit-above [cNumber] --connlimit-mask 32 -j REJECT --reject-with tcp-reset
```
