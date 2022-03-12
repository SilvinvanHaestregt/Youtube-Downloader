from pytube import YouTube
from pytube import Channel
from time import sleep
import googleapiclient.discovery
import json
import os
import psutil
os.system("cls")
count = 0

isRunning = True

# Load the .json file
jsonFile = open("api.json", "r")
jsonContent = jsonFile.read()
jsonList = json.loads(jsonContent)

# Set api_key to the api key in api.json
api_key = jsonList['api_key']
# The import is for purposes only don't worry if you don't have the key file.
if (api_key == "YOUR_API_KEY"):
    try:
        from key import api_key
    except:
        print("You need to add your api key in api.json")
# Set api_service_name to the api name in api.json
api_service_name = jsonList['api_service_name']
# Check if the name of the api is 'youtube'
if (api_service_name != "youtube"):
    print("It looks like you changed the name in api.json. Check if the name is 'youtube', if this is not the case you need to change it to 'youtube'.")
    quit()

# Set api_version to the api version in api.json
api_version = jsonList['api_version']
# Check if the api version is v3
if (api_version != "v3"):
    print("It looks like you changed the version in api.json. Check if the version is 'v3', if this is not the case change it to 'v3'.")
    quit()

def continueEnter():
    choice = input("Press enter to continue.")
    os.system("cls")

while (isRunning):
    
    #First option menu
    firstChoice = str(input("1. Video's\n2. YouTube channels\n3. Playlist - This one is not available\n4. Search engine - This one is not available\n5. Upload a video to YouTube - This one is not available\nZ. Quit the app\nYour choice: "))

    # Clear the screen
    os.system("cls")
    # First Choice
    if (firstChoice == "1"):
        choice = str(input("1. A video\n2. List of video's\nYour choice: "))
        os.system("cls")
        if (choice == "1"):
            while True:
                yt = str(input("Enter a youtube video link: "))
                try:
                    yt = YouTube(yt)
                    break
                except:
                    print("This is not a youtube video link!")
            os.system("cls")
            choice = str(input("1. Only sound\n2. image and sound\nYour choice: "))
            os.system("cls")
            if (choice == "1"):
                print("The sound is being downloaded")
                yt.streams.get_audio_only().download(output_path = f"YouTube/Audio/{yt.video_id}/", filename = "audio.mp3")
                print("The audio is succesfully installed to " + f"YouTube/Audio/{yt.video_id}/audio.mp3")
                infoFile = open(f"YouTube/Audio/{yt.video_id}/info.txt", "w", encoding="utf-8")
                infoFile.write("Title: " + str(yt.title) + "\nViews: " + str(yt.views) + "\nDescription: " + str(yt.description) + "\nKeywords: " + str(yt.keywords) + "\nLength: " + str(yt.length) + "\nMetadata: " + str(yt.metadata) + "\nRating: " + str(yt.rating) + "\nVideo info " + str(yt.vid_info))
            elif (choice == "2"):
                print("Video is being downloaded...")
                yt.streams.get_highest_resolution().download(output_path = f"YouTube/Video's/{yt.video_id}/", filename = "video.mp4")
                print("The video is succesfully installed to " + f"YouTube/Video's/{yt.video_id}/video.mp4")
                infoFile = open(f"YouTube/Video's/{yt.video_id}/info.txt", "w", encoding="utf-8")
                infoFile.write("Title: " + str(yt.title) + "\nViews: " + str(yt.views) + "\nDescription: " + str(yt.description) + "\nKeywords: " + str(yt.keywords) + "\nLength: " + str(yt.length) + "\nMetadata: " + str(yt.metadata) + "\nRating: " + str(yt.rating) + "\nVideo info " + str(yt.vid_info))
            infoFile.close()
            continueEnter()
        elif (choice == "2"):
            listFile = open("Lists/video.txt", "r", encoding="utf-8")
            for line in listFile:
                print(line)
                try:
                    yt = YouTube(line)
                except:
                    print("The program is being stopped because there is an invalid link in the text file.")
                    break
                else:
                    yt.streams.get_highest_resolution().download(output_path = f"YouTube/Video's/List/{yt.video_id}/", filename = "video.mp4")
                    infoFile = open(f"YouTube/Video's/List/{yt.video_id}/info.txt", "w", encoding="utf-8")
                    infoFile.write("Title: " + str(yt.title) + "\nViews: " + str(yt.views) + "\nDescription: " + str(yt.description))
                    infoFile.close()
            listFile.close()
            continueEnter()
    # Second Choice
    elif (firstChoice == "2"):
        choice = str(input("1. A channel\n2. List of channels\nYour choice: "))
        os.system("cls")
        if (choice == "1"):
            # Try to convert de input string into a Channel if this doesn't work it gives an error message and you can try again
            while True:
                channel = str(input("Enter a youtube channel link: "))
                try:
                    channel = Channel(channel)
                except:
                    print("This is not a youtube channel link!")
                else:
                    os.system("cls")
                    choice = str(input("1. Download all video's\n2. Video url's\n3. Channel information\nYour choice: "))
                    os.system("cls")
                    if (choice == "1"):
                        videos = 0
                        for video in channel.videos:
                            videos += 1
                        for video in channel.videos:
                            # Get file size of the video
                            fileSizeBytes = video.streams.get_highest_resolution().filesize
                            fileSizeGB = fileSizeBytes / 1073741824
                            # Get the free diskspace
                            objDisk = psutil.disk_usage("/")
                            diskFreeSpace = objDisk.free / 1024.0 ** 3 - 20
                            print(diskFreeSpace)
                            if not (fileSizeGB < diskFreeSpace):
                                print("You don't have enough storage on your system left!")
                                break
                            else:
                                video.streams.first().download(output_path = f"YouTube/Channels/{channel.channel_name}/{video.video_id}/", filename = "video.mp4")
                                infoFile = open(f"YouTube/Channels/{channel.channel_name}/{video.video_id}/info.txt", "w", encoding="utf-8")
                                infoFile.write("Title: " + str(video.title) + "\nViews: " + str(video.views) + "\nDescription: " + str(video.description) + "\nKeywords: " + str(video.keywords) + "\nLength: " + str(video.length) + "\nMetadata: " + str(video.metadata) + "\nRating: " + str(video.rating) + "\nVideo info " + str(video.vid_info))
                                infoFile.close()
                                videos -= 1
                                if (videos > 0):
                                    print(f"Succesfully installed! {videos} video's still left to download.")
                                else:
                                    print("All of the video's are succesfully installed!")
                        continueEnter()
                        break
                    elif (choice == "2"):
                        for video in channel.video_urls:
                            print(video)
                        choice = input("1. Write all the urls to a file\n2. Continue\nYour choice: ")
                        if (choice == "1"):
                            if not os.path.exists(f"YouTube/Channels/{channel.channel_name}/url/"):
                                os.makedirs(f"YouTube/Channels/{channel.channel_name}/url/")
                            urlFile = open(f"YouTube/Channels/{channel.channel_name}/url/url.txt", "w", encoding="utf-8")
                            for video in channel.video_urls:
                                urlFile.write(video + "\n")
                            urlFile.close()
                        os.system("cls")
                        continueEnter()
                        break
                    elif (choice == "3"):
                        if not os.path.exists(f"YouTube/Channels/{channel.channel_name}/Info"):
                            os.makedirs(f"YouTube/Channels/{channel.channel_name}/Info")
                        youtube = googleapiclient.discovery.build(
                            api_service_name, api_version, developerKey = api_key)
                        request = youtube.channels().list(part="statistics", id=channel.channel_id)
                        response = request.execute()
                        print(f"Channel name: {channel.channel_name}\nChannel id: {response['items'][0]['id']}\nAmount of views: {response['items'][0]['statistics']['viewCount']}\nAmount of subcribers: {response['items'][0]['statistics']['subscriberCount']}\nAmount of video's: {response['items'][0]['statistics']['videoCount']}")
                        json_data = json.dumps(response, indent = 4)
                        infoFile = open(f"YouTube/Channels/{channel.channel_name}/Info/channel.json", "w", encoding="utf-8")
                        infoFile.write(json_data)
                        infoFile.close()
                        print("Succesvol alle kanaal data opgehaald!")
                        continueEnter()
                        break
        elif (choice == "2"):
            choice = str(input("1. Download all the video's\n2. Youtube video url's\n3. Channel information\nYour choice: "))
            os.system("cls")
            channelList = open("Lists/channel.txt", "r", encoding="utf-8")
            videos = 0
            for line in channelList:
                try:
                    channel = Channel(line)
                except:
                    print("The program is going to stop because there is an invalid link in the file.")
                    break
                else:
                    if (choice == "1"):
                        for video in channel.videos:
                            videos += 1
                        print(f"The installation of the video's from {channel.channel_name} is going to start.")
                        for video in channel.videos:
                            fileSizeBytes = video.streams.get_highest_resolution().filesize
                            fileSizeGB = fileSizeBytes / 1073741824
                            # Get the free diskspace
                            objDisk = psutil.disk_usage("/")
                            diskFreeSpace = objDisk.free / 1024.0 ** 3 - 20
                            if not (fileSizeGB < diskFreeSpace):
                                print("You don't have enough storage on your system left!")
                                break
                            else:
                                video.streams.get_highest_resolution().download(output_path= f"YouTube/Channels/{channel.channel_name}/Video's/{video.video_id}", filename = "video.mp4")
                                videos -= 1
                                if (videos == 0):
                                    print(f"Succesfully installed! {videos} video's still left to download")
                                else:
                                    print("All of the video's have been downloaded succesfully")
                                    break     
                    elif (choice == "2"):
                        for video in channel.video_urls:
                            print(video)
                        if not os.path.exists(f"YouTube/Channels/{channel.channel_name}/url/"):
                            os.makedirs(f"YouTube/Channels/{channel.channel_name}/url/")
                        urlFile = open(f"YouTube/Channels/{channel.channel_name}/url/url.txt", "w", encoding="utf-8")
                        for video in channel.video_urls:
                            urlFile.write(video + "\n")
                        urlFile.close()
                    elif (choice == "3"):
                        if not os.path.exists(f"YouTube/Channels/{channel.channel_name}/Info"):
                            os.makedirs(f"YouTube/Channels/{channel.channel_name}/Info")
                        youtube = googleapiclient.discovery.build(
                            api_service_name, api_version, developerKey = api_key)
                        request = youtube.channels().list(part="statistics", id=channel.channel_id)
                        response = request.execute()
                        print(f"Channel name: {channel.channel_name}\nChannel id: {response['items'][0]['id']}\nAmount of views: {response['items'][0]['statistics']['viewCount']}\nAmount of subcribers: {response['items'][0]['statistics']['subscriberCount']}\nAmount of video's: {response['items'][0]['statistics']['videoCount']}")
                        json_data = json.dumps(response, indent = 4)
                        infoFile = open(f"YouTube/Channels/{channel.channel_name}/Info/channel.json", "w", encoding="utf-8")
                        infoFile.write(json_data)
                        infoFile.close()
            if (choice == "1"):
                print("All of the video's are have been downloaded succesfully")
            elif (choice == "2"):
                print("All of the url's have been succesfully written to a file!")
            elif (choice == "3"):
                print("Succesfully gather all of the data from all the channels!")
            continueEnter()
    elif (firstChoice == "3"):
        continueEnter()
    elif (firstChoice == "4"):
        continueEnter()
    elif (firstChoice == "5"):
        continueEnter()
    elif (firstChoice == "Z" or "z"):
        print("Thanks for using my program!")
        isRunning = False