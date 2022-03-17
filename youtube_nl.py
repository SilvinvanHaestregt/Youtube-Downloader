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
        choice = input("Wil je doorgaan zonder API key?\n1. Ja\n2. Nee\nKies je optie: ")
        if (choice == "1"):
            print("Het programma gaat door zonder API key!")
            sleep(2)
            os.system("cls")
        elif (choice == "2"):
            print("Je moet nog je API key toevoegen in api.json!")
            sleep(2)
            os.system("cls")
            quit()
        elif (choice != "1", "2"):
            quit()
# Set api_service_name to the api name in api.json
api_service_name = jsonList['api_service_name']
# Check if the name of the api is 'youtube'
if (api_service_name != "youtube"):
    print("Het lijkt erop dat je de naam hebt veranderd in api.json. Controleer of de naam 'youtube' is, als dit niet het geval is veranderd het dan naar 'youtube'.")
    quit()

# Set api_version to the api version in api.json
api_version = jsonList['api_version']
# Check if the api version is v3
if (api_version != "v3"):
    print("Het lijkt erop dat je de versie hebt veranderd in api.json. Controleer of de versie v3 is, als dit niet jet geval is veranderd het dan naar v3.")
    quit()

def continueEnter():
    choice = input("Druk op enter om door te gaan.")
    os.system("cls")

while (isRunning):
    
    #First option menu
    firstChoice = str(input("1. Video's\n2. YouTube kanaal\n3. Playlist - Deze doet het nog niet\n4. Search engine - Deze doet het nog niet\n5. Upload video naar youtube - Deze doet het nog niet\nZ. Sluit het programma\nKies je optie: "))

    # Clear the screen
    os.system("cls")
    # First Choice
    if (firstChoice == "1"):
        choice = str(input("1. Een video\n2. Lijst met video's\nKies je optie: "))
        os.system("cls")
        if (choice == "1"):
            while True:
                yt = str(input("Voer een link in: "))
                try:
                    yt = YouTube(yt)
                    break
                except:
                    print("Dit is geen youtube video link!")
            os.system("cls")
            choice = str(input("1. Alleen geluid\n2. Beeld en geluid\nKies je optie: "))
            os.system("cls")
            if (choice == "1"):
                print("Audio wordt gedownload")
                yt.streams.get_audio_only().download(output_path = f"YouTube/Audio/{yt.video_id}/", filename = "audio.mp3")
                print("Audio is succesvol gedownload in het mapje " + f"YouTube/Audio/{yt.video_id}/audio.mp3")
                infoFile = open(f"YouTube/Audio/{yt.video_id}/info.txt", "w", encoding="utf-8")
                infoFile.write("Title: " + str(yt.title) + "\nViews: " + str(yt.views) + "\nDescription: " + str(yt.description) + "\nKeywords: " + str(yt.keywords) + "\nLength: " + str(yt.length) + "\nMetadata: " + str(yt.metadata) + "\nRating: " + str(yt.rating) + "\nVideo info " + str(yt.vid_info))
                infoFile.close()
            elif (choice == "2"):
                print("Video wordt gedownload...")
                yt.streams.get_highest_resolution().download(output_path = f"YouTube/Video's/{yt.video_id}/", filename = "video.mp4")
                print("De video is succesvol gedownload in het mapje " + f"YouTube/Video's/{yt.video_id}/video.mp4")
                infoFile = open(f"YouTube/Video's/{yt.video_id}/info.txt", "w", encoding="utf-8")
                infoFile.write("Title: " + str(yt.title) + "\nViews: " + str(yt.views) + "\nDescription: " + str(yt.description) + "\nKeywords: " + str(yt.keywords) + "\nLength: " + str(yt.length) + "\nMetadata: " + str(yt.metadata) + "\nRating: " + str(yt.rating) + "\nVideo info " + str(yt.vid_info))
                infoFile.close()
            elif (choice == "3"):
                youtube = googleapiclient.discovery.build(
                    api_service_name, api_version, developerKey = api_key)

                request = youtube.commentThreads().list(
                    part="id, snippet, replies",
                    maxResults=100,
                    order="time",
                    videoId=yt.video_id
                )

                response = request.execute()

                json_data = json.dumps(response, indent = 4)
                if not os.path.exists(f"YouTube/Video's/{yt.video_id}/"):
                    os.makedirs(f"YouTube/Video's/{yt.video_id}/")
                commentsFile = open(f"YouTube/Video's/{yt.video_id}/comments.json", "w", encoding="utf-8")
                commentsFile.write(json_data + "\n")
                commentsFile.close()
                print("De comments van de video zijn succesvol gedownload!")
            continueEnter()
        elif (choice == "2"):
            listFile = open("Lists/video.txt", "r", encoding="utf-8")
            for line in listFile:
                print(line)
                try:
                    yt = YouTube(line)
                except:
                    print("Het programma wordt gestopt omdat er een ongeldige link in het text bestand zit.")
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
        choice = str(input("1. Een kanaal\n2. Lijst met kanalen\nKies je optie: "))
        os.system("cls")
        if (choice == "1"):
            # Try to convert de input string into a Channel if this doesn't work it gives an error message and you can try again
            while True:
                channel = str(input("Voer een link in: "))
                try:
                    channel = Channel(channel)
                except:
                    print("Dit is geen kanaal link!")
                else:
                    os.system("cls")
                    choice = str(input("1. Alle video's downloaden\n2. Url van alle video's\n3. Kanaal informatie\nKies je optie: "))
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
                                print("Je hebt niet genoeg ruimte meer op je systeem!")
                                break
                            else:
                                video.streams.first().download(output_path = f"YouTube/Channels/{channel.channel_name}/{video.video_id}/", filename = "video.mp4")
                                infoFile = open(f"YouTube/Channels/{channel.channel_name}/{video.video_id}/info.txt", "w", encoding="utf-8")
                                infoFile.write("Title: " + str(video.title) + "\nViews: " + str(video.views) + "\nDescription: " + str(video.description) + "\nKeywords: " + str(video.keywords) + "\nLength: " + str(video.length) + "\nMetadata: " + str(video.metadata) + "\nRating: " + str(video.rating) + "\nVideo info " + str(video.vid_info))
                                infoFile.close()
                                videos -= 1
                                if (videos > 0):
                                    print(f"Succesvol gedownload! Nog {videos} video's te gaan.")
                                else:
                                    print("Alle video's zijn succesvol gedownload!")
                        continueEnter()
                        break
                    elif (choice == "2"):
                        for video in channel.video_urls:
                            print(video)
                        choice = input("1. Schrijf alle urls naar een bestand\n2. Contiune\nKies je optie: ")
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

                        # First request statistics
                        request = youtube.channels().list(part="statistics", id= channel.channel_id)
                        response = request.execute()
                        print(f"Kanaal naam: {channel.channel_name}\nKanaal id: {response['items'][0]['id']}\nAantal views: {response['items'][0]['statistics']['viewCount']}\nAantal abonnees: {response['items'][0]['statistics']['subscriberCount']}\nAantal video's: {response['items'][0]['statistics']['videoCount']}")
                        json_data = json.dumps(response, indent = 4)
                        statisticsFile = open(f"YouTube/Channels/{channel.channel_name}/Information/statistics.json", "w", encoding="utf-8")
                        statisticsFile.write(json_data + "\n")
                        statisticsFile.close()

                        # Second request branding
                        request = youtube.channels().list(part="brandingSettings", id= channel.channel_id)
                        response = request.execute()
                        json_data = json.dumps(response, indent = 4)
                        brandingFile = open(f"YouTube/Channels/{channel.channel_name}/Information/branding.json", "w", encoding="utf-8")
                        brandingFile.write(json_data + "\n")
                        brandingFile.close()

                        # Third request contentOwnerDetails
                        request = youtube.channels().list(part="contentOwnerDetails", id = channel.channel_id)
                        response = request.execute()
                        json_data = json.dumps(response, indent = 4)
                        contentOwnerFile = open(f"YouTube/Channels/{channel.channel_name}/Information/branding.json", "w", encoding="utf-8")
                        contentOwnerFile.write(json_data)
                        contentOwnerFile.close()

                        print("Succesvol alle kanaal data opgehaald!")
                        continueEnter()
                        break
        elif (choice == "2"):
            choice = str(input("1. Alle video's downloaden\n2. Url van alle video's\n3. Kanaal informatie\nKies je optie: "))
            os.system("cls")
            channelList = open("Lists/channel.txt", "r", encoding="utf-8")
            videos = 0
            for line in channelList:
                try:
                    channel = Channel(line)
                except:
                    print("Het programma wordt gestopt omdat er een ongeldige link in het tekst bestand zit.")
                    break
                else:
                    if (choice == "1"):
                        for video in channel.videos:
                            videos += 1
                        print(f"Het downloaden van de video's van {channel.channel_name} gaat beginnen.")
                        for video in channel.videos:
                            fileSizeBytes = video.streams.get_highest_resolution().filesize
                            fileSizeGB = fileSizeBytes / 1073741824
                            # Get the free diskspace
                            objDisk = psutil.disk_usage("/")
                            diskFreeSpace = objDisk.free / 1024.0 ** 3 - 20
                            if not (fileSizeGB < diskFreeSpace):
                                print("Je hebt niet genoeg ruimte meer op je systeem!")
                                break
                            else:
                                video.streams.get_highest_resolution().download(output_path= f"YouTube/Channels/{channel.channel_name}/Video's/{video.video_id}", filename = "video.mp4")
                                videos -= 1
                                if (videos == 0):
                                    print(f"Succesvol gedownload! Nog {videos} video's te gaan.")
                                else:
                                    print("Alle video's zijn succesvol gedownload!")
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
                        print(f"Kanaal naam: {channel.channel_name}\nKanaal id: {response['items'][0]['id']}\nAantal views: {response['items'][0]['statistics']['viewCount']}\nAantal abonnees: {response['items'][0]['statistics']['subscriberCount']}\nAantal video's: {response['items'][0]['statistics']['videoCount']}")
                        json_data = json.dumps(response, indent = 4)
                        infoFile = open(f"YouTube/Channels/{channel.channel_name}/Info/channel.json", "w", encoding="utf-8")
                        infoFile.write(json_data)
                        infoFile.close()
            if (choice == "1"):
                print("Alle video's zijn succesvol gedownload!")
            elif (choice == "2"):
                print("Alle video links zijn succesvol naar een bestand toegeschreven!")
            elif (choice == "3"):
                print("Succesvol alle data van alle kanalen opgehaald!")
            continueEnter()
    elif (firstChoice == "3"):
        continueEnter()
    elif (firstChoice == "4"):
        continueEnter()
    elif (firstChoice == "5"):
        continueEnter()
    elif (firstChoice == "Z" or "z"):
        print("Bedankt voor het gebruiken van mijn programma, we gaan het nu sluiten!")
        isRunning = False