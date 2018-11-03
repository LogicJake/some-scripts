## bandwagon-bandwidth-monitor
A python script which can check bandwagon server bandwidth and send email notification every day. It gets information from kiwivm website, so you should provide ip and password to login.
### HOW TO USE
There is a file named 'config.example.json'. You should copy this file to a file called 'config.json' in which you should fill in the information. The 'login' information is used to login. The 'mail' information is used to send email.  
***tip***  
The default SMTP server is qq, so if you want to use other mail, you should change SMTP server accordingly. It is located in line 16 in 'monitor.py'.
#### arguments
There are two arguments you can set:
```sh
usage: monitor [-h] [--test [TEST]] --hour [HOUR]

report your SS usage.

optional arguments:
  -h, --help     show this help message and exit
  --test [TEST]  whether to send an email immediately to test if the system
                 works well
  --hour [HOUR]  the time(hour between 0 and 23) the system sent the report
```
* hour  
A number of hours ranging from 0 to 23, the script will send a report at that time. Default value is 9.
* test    
A bool value which decides whether to send an email immediately to test if the system works well. Default value is False.

#### start
I have packaged the script into executable files in Ubuntu. But i don't know whether it works in other linux platform. If not, you can use 'main.py', but it need Python3 environmnet. Next, Let's give examples of executable file 'monitor'.
```sh
$ ./monitor --hour 9 --test true
```
Using this command, the script will send a test email immediately to test if all ok. Of course, in most cases, we want the script to run in the background. So we can use following command.
```sh
$ nohup ./monitor --hour 9 --test true &
```
