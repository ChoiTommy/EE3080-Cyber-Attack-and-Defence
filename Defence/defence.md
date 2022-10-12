# Defence

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


## 1. Defending the DoS attack
