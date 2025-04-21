#### This is a fork of the project EDOPro-HD-Card-Downloader



### Disclaimer

You are responsible for all use of this script. I am not responsible for any consequences that come as a result of using this software I did not create most of it and this is simply a fork. Please contact and hold the original project creators accountable for any issues you occur although they may have a disclaimer making them void of responsibility similar to this one.

This application is meant and designed for seamless use on Windows 10 and 11 if you are using another operating system it is not an issue that there is no seamless process for you. These are the main 2 supported operating systems for this Project Fork.

Always think twice about whether that GitHub release was actually built with the same code downloadable and viewable from the github page that is "safe". Is it a reproducible build? Is the person reputable? Can you easily build this program yourself using something like pyinstaller and the makefile the project had included? (what i did here),

### How to Use

##### You are required to download Python 3 to build or run this repository so I recommend:
##### I recommend running from source using Python 3 on Windows and simply typing `python main.py` into the command prompt inside the repository directory for a faster experience after installing all requirements with `pip install -r requirements.txt` in the directory of the requirements.txt file.

or

##### Build it quickly and easily with my script if you wish to share it and run again in the future the exact same way as it did (working) as well as the exif removal tool which I will include a build tool for but you could probably work it out using the quick build batch script for the main project at the moment. All tools built with pyinstaller may be slower such as this main project at the exchange of convenience.


Please checkout the folder "custom tools by tilas01" as its where most of my custom additions to this project with this fork can be used and are stored.

I didn't entirely trust the project and it seems weird that they offer a Windows release with build instructions for other OS's and I cant find anything malicicious in their code but their executable is flagged for actions mine isnt that are malicious in sandboxes so i believe there is possibly malware inside that release alledgedly of course. I think the safest way to use this tool on windows with python is to build it yourself and cleanup easily and remove exif/extra data from the pics (this script is provided by me with the help of chatgpt) to reduce file size without ever reducing image size, it is a completely lossless process and simply makes the images file content only its visual pixels.

This program only supports windows 10 and 11 mainly.

Instead of using the release they have compiled for you this fork uses the latest version of all requirements and the latest version of python to automatically build and run the software yourself using pyinstaller without any technical knowledge simply visit the custom tools folder by tilas01 and read my guide by tilas01

Once all cards are downloaded if you would like to clear them of all exif (your pics data will be backed up before continuing)

and other extra unneccassary data that is stored in them that could be malicious, unneeded and wasting storage etc.

This basically "sanitises" the images to just be the raw image data and the exact same file name and replaces it so it contains no extra data.

To build run the script that says it will build and run the program

To delete the build directory and working directory of the build run the batch file that says it will do so (THIS WILL ALSO DELETE YOUR DOWNLOADED PICS AND TRACKING IF THEY ARE STORED IN THERE)

### To-Do
Add a part that also goes into the fields folder if they downloaded hd fields also and does the same thing and places it inside pics_out as just fields since its already in the out directory.

### License

This project is licensed under the MIT License
