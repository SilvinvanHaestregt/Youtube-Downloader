from pytube import YouTube
from pytube import Channel
from time import sleep
import json
import os
import YouTubeLibrary as youtube
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
        choice = input("Do you want to continue without an API key?\n1. Yes\n2. No\nYour choice: ")
        if (choice == "1"):
            print("The app will continue without an API key!")
            sleep(2)
            os.system("cls")
        elif (choice == "2"):
            print("You need to add your api key in api.json")
            sleep(2)
            os.system("cls")
            quit()
        elif (choice != "1", "2"):
            quit()
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
    firstChoice = str(input("1. Video's\n2. YouTube channels\n3. Search Engine\nZ. Quit the app\nYour choice: "))

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
            choice = str(input("1. Only sound\n2. image and sound\n3. Comments\nYour choice: "))
            os.system("cls")
            if (choice == "1"):

                youtube.Audio.downloadAudio(yt)

            elif (choice == "2"):

                youtube.Video.downloadVideo(yt)

            elif (choice == "3"):

                youtube.Video.commentsVideo(api_service_name, api_version, api_key, yt)

            continueEnter()
        elif (choice == "2"):

            youtube.Video.downloadVideoList(yt)

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

                        youtube.Channel.downloadVideos(channel)

                        continueEnter()
                        break
                    elif (choice == "2"):

                        youtube.Channel.videoUrls(channel)

                        continueEnter()
                        break
                    elif (choice == "3"):

                        youtube.Channel.ownerInformation(api_service_name, api_version, api_key, channel)

                        continueEnter()
                        break
        elif (choice == "2"): 
            choice = str(input("1. Download all the video's\n2. Youtube video url's\n3. Channel information\nYour choice: "))
            os.system("cls")
            if (choice == "1"):
                youtube.Channel.channelInformationList(api_service_name, api_version, api_key, channel)
                print("Succesfully gather all of the data from all the channels!")
            continueEnter()
    elif (firstChoice == "3"):
        choice = str(input("1. Show data from specific file\n2. Run a search query\nYour choice: "))
        os.system("cls")
        if (choice == "1"):
            file = str(input("File name: "))
            os.system("cls")
            youtube.searchEngine.searchEngineFile(file)
        elif (choice == "2"):
            searchQuery = str(input("What do you want to search: ")) 
            os.system("cls")

            while True:
                amountOfResults = int(input("How many results do you want: "))
                if (amountOfResults < 1001):
                    os.system("cls")
                    break
                else:
                    print("This number is to big!")
            youtube.searchEngine.searchEngine(api_service_name, api_version, api_key, searchQuery, amountOfResults)
        continueEnter()
    elif (firstChoice == "Z" or "z"):
        print("Thanks for using my program!")
        isRunning = False