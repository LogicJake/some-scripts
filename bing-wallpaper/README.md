## bing-wallpaper
A python script which can download bing's beautiful images and set the image to your computer wallpaper. This script can also change wallpaper every once in a while. It is tested and works well on ubuntu.   
### Installation
```bash
pip3 install BingWallpaper
```
### HOW TO USE
#### arguments
There are three arguments you can set:
```
usage: wallpaper [-h] [--interval [INTERVAL]] [--num [NUM]] [--path [PATH]]
                 [stop]

timely replacement wallpaper from bing.

positional arguments:
  stop                  stop wallpaper

optional arguments:
  -h, --help            show this help message and exit
  --interval [INTERVAL]
                        time interval for scripts to change wallpapers. By
                        seconds.
  --num [NUM]           number of images saved in local folder at most
  --path [PATH]         path to save images
```
* stop
stop wallpaper
* interval  
Time interval for scripts to change wallpapers. The unit of this argument is second and default value is **3 seconds**. 
* num  
Number of images saved in local folder at most. Script will only keep **num** latest bing's images, and the expired will be deleted. Script will choose one image as wallpaper randomly. Default value is **7**.
* path  
Path to save wallpaper. If the current user does not have permission to write to or create the path, you may need administrator privileges. Default value is **'/home/user/wallpapers'**.  

#### example
```bash
wallpaper
``` 
This is the simplest command and three arguments are set to the default value. You can customize your commands like this:
```bash
wallpaper --interval 4 --num 5 --path /home/bing/test/
```
If you want to stop the script, you can run the following code.
```bash
wallpaper stop
```
