### Python script that automatically updates [hosts file](https://en.wikipedia.org/wiki/Hosts_(file)) from [StevenBlack/hosts](https://github.com/StevenBlack/hosts), exclude addresses from the blacklist.
#### Supported systems:
* Linux
* Windows
* macOS


#### Installation & Usage:
##### Linux or macOS
```zsh
# clone the repo
$ git clone https://github.com/alcortazzo/update-hosts-file.git

# change the working directory to update-hosts-file
$ cd update-hosts-file

# install python3 and python3-pip if they are not installed

# install the requirements
$ python3 -m pip install -r requirements.txt

# run script as root user 
$ sudo python3 main.py
```
##### Windows
```zsh
# OPEN POWERSHELL AS ADMIN!

# clone the repo
$ git clone https://github.com/alcortazzo/update-hosts-file.git

# change the working directory to update-hosts-file
$ cd update-hosts-file

# install python3 and python3-pip if they are not installed

# install the requirements
$ python3 -m pip install -r requirements.txt

# run script as root user 
$ python main.py
```
