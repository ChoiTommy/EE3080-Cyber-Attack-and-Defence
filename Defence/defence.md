# Defence

## Quick links
[Setup](#setup) | [DoS Attack](#defending-dos-attack) | [Reverse-shell Attack](#countering-reverse-shell-attack)

---

## Setup
1. Install SNORT on the VMs

2. Install the gedit command to operate snort properly, go to terminal, then
    ```shell
    $ sudo apt-get clean 
    $ sudo apt-get install gedit
    ```

3. Enter snort configuration file: 
    ```shell
    $ cd /etc/snort > ls -l
    ```

4. Create a backup of configuration file (optional)
    ```shell
    $ sudo cp snort.conf snort.conf.back > ls -l
    ```

5. Create a copy of the configuration file(optional): 
    ```shell
    $ sudo cp snort.conf test_snort.conf > ls -l
    ```

6. Edit configuration file in txt file: 
    ```shell
    $ sudo gedit /etc/snort/snort.conf
    ``` 
    or if the test file is there already (based on 3) then 
    ```shell
    $ sudo gedit test_snort.conf
    ```
    - Within the `.conf` file, key in IP address that is of interest: `ipvar HOME_NET any`, e.g. `ipvar HOME_NET 10.0.2.0/24` (last digit always 0 so that the range it covers is from 0-256)
    - Make sure that command code: `include $RULE_PATH/local.rules` is enabled/included within your configuration file so that custom local files that's written later

7. Check snort configuration file in command prompt: 
    ```shell
    $ sudo snort -T -i enp0s3 -c /etc/snort/test_snort.conf
    ``` 
    
8. Accessing snort rules, directly add/remove local files (open new command prompt): 
    ```shell
    $ cd etc/snort/rules/
    $ ls -l 
    $ sudo nano local.rules
    ```


## Defending DoS attack

1. Download the `dos.rules` file from [GitHub](https://github.com/maj0rmil4d/snort-ddos-mitigation/blob/main/dos.rules). Save it in `etc/snort/rules/` directory.

2. Modify the `snort.conf` file to include the `dos.rules` file. Add the following line to the `snort.conf` file:
    ```
    include $RULE_PATH/dos.rules
    ```

3. Run either of the following commands:
    ```shell
    $ sudo snort -q -l /var/log/snort/ -i eth0 -A console -c /etc/snort/snort.conf
    ```
    ```shell
    $ sudo snort -c /etc/snort/snort.conf -q -Q --daq afpacket -i eth0:eth1 -A full
    ``` 
    Either execution will store the output logging data to IPEAR Log file.


## Countering Reverse Shell attack

We assume the attackers use port ‘70’ for their attacks.

1. Run Snort in IDS mode to detect all activities
    ```shell
    $ sudo snort -dev -l
    ```

2. Let the attacks happen for a while with IDS mode activated. Press `ctrl + z` to end the IDS mode on snort. Type `ls` to view the log files.

3. To view the log file, type in the following command: 
    ```shell
    $ sudo snort -r snort.log.1664875421
    ```
    Notice the IP address of the attacker attempting the reverse shell attack via TCP 70 connection is logged in this packet log file. The attackers' IP address is revealed on the RHS and victims' IP address is on the LHS.

4. Filter out only inbound traffic to focus on what is truly relevant. Note down the ports with most amount of traffic, e.g. in this case, assuming that we noticed port 70 to be suspicious, type 
    ```shell 
    $ sudo snort -r snort.log.1664880824 'port 70'
    ```

5. To prevent further attacking attempts on port 70, implement a rule with ‘drop’ function in snort local rules. Add the following line into the `local.rules` file:
    ```
    drop tcp any 70 <> any any (msg: "Suspicious Activity Detected"; sid: 10000005; rev: 1;)
    ```
    This rule will drop all TCP traffic on port 70.

    Next, type in
    ```shell
    $ sudo snort -c /etc/snort/snort.conf -q -Q --daq afpacket -i eth0:eth1 -A full
    ```
    to run the snort configuration file. Now the attacker is unable to connect to victims' PC via port 70.

    Furthermore, any packet exchanges that occur at port 70 will be stored in a text file called `alert`.

6. To prevent cluttering, the directory which the log files related to  “suspicious activities” are to be saved into a local folder called “IPEAR_Snort_Log_Files”. Modify the `snort.conf` file and add the following line:
    ```
    config logdir /home/kali/Desktop/IPEAR_Snort_Log_Files
    ```
