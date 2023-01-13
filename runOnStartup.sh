
screen -dmS pythonUpdater bash -c 'python3 /BeavDNS/update.py'

iptables -P OUTPUT DROP
iptables -P INPUT DROP

iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

iptables -I INPUT 1 -i lo -j ACCEPT
iptables -A OUTPUT -p udp --dport 53 -j ACCEPT
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

iptables -A OUTPUT -j LOG

bash ipAllowances.sh
