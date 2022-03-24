import json
import googleapiclient.discovery
import os
from pytube import YouTube
import psutil

class Video:

    def downloadVideo(yt):
        print("Video is being downloaded...")
        yt.streams.get_highest_resolution().download(output_path = f"YouTube/Video's/{yt.video_id}/", filename = "video.mp4")
        print("The video is succesfully installed to " + f"YouTube/Video's/{yt.video_id}/video.mp4")
        infoFile = open(f"YouTube/Video's/{yt.video_id}/info.txt", "w", encoding="utf-8")
        infoFile.write("Title: " + str(yt.title) + "\nViews: " + str(yt.views) + "\nDescription: " + str(yt.description) + "\nKeywords: " + str(yt.keywords) + "\nLength: " + str(yt.length) + "\nMetadata: " + str(yt.metadata) + "\nRating: " + str(yt.rating) + "\nVideo info " + str(yt.vid_info))

    def commentsVideo(api_service_name, api_version, api_key, yt):
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
        commentsFile = open(f"YouTube/Video's/{yt.video_id}/statistics.json", "w", encoding="utf-8")
        commentsFile.write(json_data + "\n")
        commentsFile.close()

    def downloadVideoList(yt):
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


class Audio:

    def downloadAudio(yt):
        print("The sound is being downloaded")
        yt.streams.get_audio_only().download(output_path = f"YouTube/Audio/{yt.video_id}/", filename = "audio.mp3")
        print("The audio is succesfully installed to " + f"YouTube/Audio/{yt.video_id}/audio.mp3")
        infoFile = open(f"YouTube/Audio/{yt.video_id}/info.txt", "w", encoding="utf-8")
        infoFile.write("Title: " + str(yt.title) + "\nViews: " + str(yt.views) + "\nDescription: " + str(yt.description) + "\nKeywords: " + str(yt.keywords) + "\nLength: " + str(yt.length) + "\nMetadata: " + str(yt.metadata) + "\nRating: " + str(yt.rating) + "\nVideo info " + str(yt.vid_info))

class Channel:

    def downloadVideos(channel):
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
                    break
    
    def videoUrls(channel):
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

    def ownerInformation(api_service_name, api_version, api_key, channel):
        if not os.path.exists(f"YouTube/Channels/{channel.channel_name}/Information"):
            os.makedirs(f"YouTube/Channels/{channel.channel_name}/Information")
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey = api_key)

        # First request statistics
        request = youtube.channels().list(part="statistics", id= channel.channel_id)
        response = request.execute()
        print(f"Channel name: {channel.channel_name}\nChannel id: {response['items'][0]['id']}\nAmount of views: {response['items'][0]['statistics']['viewCount']}\nAmount of subcribers: {response['items'][0]['statistics']['subscriberCount']}\nAmount of video's: {response['items'][0]['statistics']['videoCount']}")
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

    def channelInformationList(api_service_name, api_version, api_key, channel):
        channelList = open("Lists/channel.txt", "r", encoding="utf-8")
        for line in channelList:
            try:
                channel = Channel(line)
            except:
                print("The program is going to stop because there is an invalid link in the file.")
                break
            else: 
                if not os.path.exists(f"YouTube/Channels/{channel.channel_name}/Info"):
                    os.makedirs(f"YouTube/Channels/{channel.channel_name}/Info")
                youtube = googleapiclient.discovery.build(
                    api_service_name, api_version, developerKey = api_key)
                request = youtube.channels().list(part="statistics", id=channel.channel_id)
                response = request.execute()
                print(f"Channel name: {channel.channel_name}\nChannel id: {response['items'][0]['id']}\nAmount of views: {response['items'][0]['statistics']['viewCount']}\nAmount of subcribers: {response['items'][0]['statistics']['subscriberCount']}\nAmount of video's: {response['items'][0]['statistics']['videoCount']}")
                json_data = json.dumps(response, indent = 4)
                infoFile = open(f"YouTube/Channels/{channel.channel_name}/Information/channel.json", "w", encoding="utf-8")
                infoFile.write(json_data)
                infoFile.close()
class searchEngine:

    def searchEngine(api_service_name, api_version, api_key, searchQuery, amountOfResults):
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey = api_key
        )

        request = youtube.search().list(
            part="snippet",
            maxResults=amountOfResults,
            q=searchQuery
        )

        response = request.execute()

        json_data = json.dumps(response, indent=4)
        print(json_data)
        if not os.path.exists("Search"):
            os.makedirs("Search")
        jsonFile = open(f"Search/{searchQuery}.json", "w", encoding="utf-8")
        jsonFile.write(json_data)
        jsonFile.close()

        amountOfItems = {
            "numberOfItems" : amountOfResults 
        }
        json_data = json.dumps(amountOfItems, indent = 4)
        jsonFileAmount = open(f"Search/{searchQuery}.amount.json", "w", encoding="utf-8")
        jsonFileAmount.write("\n" + json_data)
        jsonFileAmount.close()

    def searchEngineFile(file):
        isFile = os.path.isfile(f"Search/{file}.json")
        isFileAmount = os.path.isfile(f"Search/{file}.amount.json")
        if (isFile == True):
            if (isFileAmount == True):
                jsonFile = open(f"Search/{file}.json", "r")
                jsonFileAmount = open(f"Search/{file}.amount.json", "r")
                jsonData = json.load(jsonFile)
                jsonDataAmount = json.load(jsonFileAmount)
                amount = jsonDataAmount['numberOfItems']
                for i in range(0, amount):
                    print(f"Link: https://www.youtube.com/watch?v={jsonData['items'][i]['id']['videoId']}")
                    print(f"Published at: {jsonData['items'][i]['snippet']['publishedAt']}")
                    print(f"Title: {jsonData['items'][i]['snippet']['title']}")
                    print(f"Channel title: {jsonData['items'][i]['snippet']['channelTitle']}")
                    print("\n")
        jsonFile.close()
        jsonFileAmount.close()