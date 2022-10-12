# LOIC Attack

1. Clone the repository from [LOIC GitHub](https://github.com/NewEraCracker/LOIC)

2. Add the Mono (C# runtime implementation) repository to the system
```shell
$ sudo apt install apt-transport-https dirmngr
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
$ echo "deb https://download.mono-project.com/repo/ubuntu vs-bionic main" | sudo tee /etc/apt/sources.list.d/mono-official-vs.list
$ sudo apt update
```

3. Install monodevelop
```shell
$ sudo apt-get install monodevelop
```

4. cd to the LOIC directory and install LOIC
```shell
$ bash ./loic.sh install
```

5. Run LOIC
```shell
$ bash ./loic.sh run
```

6. Set the target IP address and port
7. Set the attack type to UDP (suggested by GH Copilot; to be changed later)
8. Set the attack rate to 1000 (suggested by GH Copilot; to be changed later)
9. Start the attack
