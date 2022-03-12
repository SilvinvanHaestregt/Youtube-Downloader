# Table of contents
* [Technologies](#technologies)
* [General info](#general-info)
* [Setup](#setup)
* [How to add your own google API key](#How-to-add-your-own-google-API-key)


## Technologies

Project is created with:
* Python 3.10.2
* Visual studio code
* pytube
* Google API

# General info

With this program it is possible to download one or more youtube videos. You can choose to download 1 video, but you can also choose to download a whole list of youtube videos by simply copying the link of the video in video.txt. This file can be found in the Lists folder.

It is also possible to download all videos from a specified youtube channel. The option is also present to have a list of youtube channels, from which all videos are downloaded. Note that this can take up a lot of space on your PC so pay attention to this.

You can also get information about a certain youtube channel. The total number of views, subscribers and the total number of videos that the channel has. To be able to use this you need a google API key.

Below is explained how you can get it.

It is also possible to support me by subscribing to my patreon where you will get exclusive content and tutorials.

## Setup
```
$ cd Youtube-Downloader
$ pip3 install requirements.txt
$ python3 youtube_en.py or python3 youtube_nl.py
```


# How to add your own google API key

Go to the https://cloud.google.com/apis/ link and click the Console button in the top right corner.

(If you don't see this button, please log in with your google account first)

![First Image](/images/firstimage.png)

Then click on the button where the red arrow is. For me it says My First Project which is because I have already created a project before.

![Second Image](/images/secondimage.png)

Once you have done that, you will get the window below.

Then click on New Project.

![Third Image](/images/thirdimage.png)

Then give your project a name. For example: "YouTube API" (without the quotes) because we are going to work with the youtube api.

Now open your project by pressing the same button that will give you the window where you created your project. Click on the name of your project and then open at the bottom right.

Now click on the button "ENABLE APIS AND SERVICES".

![Fourth Image](/images/fourthimage.png)

Now search for the word YouTube.

Click "YouTube Data API v3". Now you are redirected to another page where you can enable the API. Click the "ENABLE" button.

![Fifth Image](/images/fifthimage.png)

You will now be sent back to your project where you then click on the "CREATE CREDENTIALS" button.

![Sixth Image](/images/sixthimage.png)

Now you need to select which API you are going to use. Click on the drop-down menu and press the "y" on your keyboard. After that, click on the option "YouTube Data API v3.

Now you get the 2 options namely: User data and Public data. Click on Public data and then on NEXT.

![Seventh Image](/images/seventhimage.png)

Now you will see your API Key.

# ATTENTION! Never share your API key if you haven't set any limits on it!

Copy and paste your API key to the api.json file. Now you can start your program!

Good luck!