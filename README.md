#### This is a fork of the project EDOPro-HD-Card-Downloader



### Disclaimer

You are responsible for all use of this script. I am not responsible for any consequences that come as a result of using this software I did not create most of it and this is simply a fork. Please contact and hold the original project creators accountable for any issues you occur although they may have a disclaimer making them void of responsibility similar to this one.

This application is meant and designed for seamless use on Windows 10 and 11 if you are using another operating system it is not an issue that there is no seamless process for you. These are the main 2 supported operating systems for this Project Fork.

Always think twice about whether that GitHub release was actually built with the same code downloadable and viewable from the github page that is "safe". Is it a reproducible build? Is the person reputable? Can you easily build this program yourself using something like pyinstaller and the makefile the project had included? (what i did here),

### How to Use

Please checkout the folder "custom tools by tilas01" as its where most of my custom additions to this project with this fork can be used and are stored.

I didn't entirely trust the project and it seems weird that they offer a Windows release with build instructions for other OS's and I cant find anything malicicious in their code but their executable is flagged for actions mine isnt that are malicious in sandboxes so i believe there is possibly malware inside that release alledgedly of course. I think the safest way to use this tool on windows with python is to build it yourself and cleanup easily and remove exif/extra data from the pics (this script is provided by me with the help of chatgpt) to reduce file size without ever reducing image size, it is a completely lossless process and simply makes the images file content only its visual pixels.

This program only supports windows 10 and 11 mainly.

Instead of using the release they have compiled for you this fork uses the latest version of all requirements and the latest version of python to automatically build and run the software yourself using pyinstaller without any technical knowledge simply visit the custom tools folder by tilas01 and read my guide by tilas01

Once all cards are downloaded if you would like to clear them of all exif (your pics data will be backed up before continuing)

and other extra unneccassary data that is stored in them that could be malicious, unneeded and wasting storage etc.

This basically "sanitises" the images to just be the raw image data and the exact same file name and replaces it so it contains no extra data.

### Important Note about Exif Tool - Please Read
Although at this time I would recommmend NOT using the exif feature as it recompresses all card images into a 10+ gb file and does not do the field images or look for them so it needs some work first ive found. From reviewing the code it simply downloads all the card pictures and names and sorts them from a yugioh card database website.

You dont need to do this but you can and it will show you exactly what your file size was before and after and what files had exif data and i believe what that exif data was it should be printed on screen or found in the logs that will be everything you saw on screen and more data about the proccess after. You must be patient for both these tools as they are using python a quite unoptimised interpreter to download and remove all extra data from these images.



To build run the script that says it will build and run the program

To delete the build directory and working directory of the build run the batch file that says it will do so (THIS WILL ALSO DELETE YOUR DOWNLOADED PICS AND TRACKING IF THEY ARE STORED IN THERE)

### To-Do
Add a part that also goes into the fields folder if they downloaded hd fields also and does the same thing and places it inside pics_out as just fields since its already in the out directory.

### License

This project is licensed under the MIT License
