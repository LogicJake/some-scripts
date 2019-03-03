[![pip](https://img.shields.io/pypi/dm/labssh.svg)](https://pypi.org/project/labssh/)
## ssh-for-lab  
A script which can directly login the lab's server without knowing the IP.  

The script works very simply. Check if the hostname is 'lab'. if so, find the newest IP address from the website, replace hostname with IP address, and then give the transformed command to 'os system'.    

[![gif with examples][examples-link]][examples-link]

### Installation
```bash
pip install labssh
```
### How To Use 
* just print IP
```bash
labssh 
```
* use 'lab' as hostname to login lab's server
```bash
labssh root@lab
```
* just use as ssh
```bash
labssh root@172.26.153.20 -p 220 
```
[examples-link]:   https://raw.githubusercontent.com/LogicJake/some-scripts/master/ssh-for-lab/example.gif
