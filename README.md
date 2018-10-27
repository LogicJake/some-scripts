## bing-wallpaper
A python script which can download bing's beautiful images and set the image to your computer wallpaper. This script can also change wallpaper every once in a while. It is tested and works well on ubuntu.   
### HOW TO USE
#### arguments
There are three arguments you can set:
```
usage: main.py [-h] [--interval [INTERVAL]] [--num [NUM]] [--path [PATH]]

timely replacement wallpaper from bing.

optional arguments:
  -h, --help            show this help message and exit
  --interval [INTERVAL]
                        time interval for scripts to change wallpapers. By
                        minutes.
  --num [NUM]           number of images saved in local folder at most
  --path [PATH]         path to save images
```
* interval  
Time interval for scripts to change wallpapers. The unit of this argument is minute and default value is **60 minutes**. 
* num  
Number of images saved in local folder at most. Script will only keep **num** latest bing's images, and the expired will be deleted. Script will choose one image as wallpaper randomly. Default value is **7**.
* path  
Path to save wallpaper. If the current user does not have permission to write to or create the path, you may need administrator privileges. Default value is **'/home/user/wallpapers'**.
#### start
you have two choices to use it:
* in your terminator
``` sh
$ cd bing-wallpaper
$ python3 main.py
``` 
This is the simplest command and three arguments are set to the default value. You can customize your commands like this:
```
python3 main.py --interval 0.5 --num 5 --path /home/bing/test/
```
* If you don not have python3 environment, you can just double click packed executable file 'wallpaper'. If you want use provided arguments, you can use it in terminator too.
``` sh
$ cd bing-wallpaper
$ ./wallpaper --interval 0.5 --num 5 --path /home/bing/test/
``` 
