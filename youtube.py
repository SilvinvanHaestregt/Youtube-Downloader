from pytube import YouTube
from pytube import Channel
from time import sleep
import os
os.system("cls")
count = 0

firstChoice = str(input("1. Video's\n2. Livestream's\n3. YouTube kanaal\nKies je optie: "))
os.system("cls")

def downloadVideo(resolution, audio_only):
    yt.streams.filter(res=resolution, only_audio=audio_only).download(output_path = f"YouTube/Video's/{yt.video_id}/", filename = "video.mp3")

if (firstChoice == "1"):
    choice = str(input("1. Een video\n2. Lijst met video's\nKies je optie: "))
    os.system("cls")
    if (choice == "1"):
        while True:
            yt = input("Voer een link in: ")
            try:
                yt = YouTube(yt)
                break
            except:
                print("Dit is geen youtube video link!")
        while True:
            choice = input("1. Alleen audio\n2. Met beeld\nKies je optie: ")
            if (choice == "1"):
                audio_only = True
            try:
                print("Proberen om video te downloaden in 1080p")
                downloadVideo("1080p", audio_only)
                break
            except:
                print("Het is niet gelukt om de video in 1080p te downloaden we proberen nu 720p")
            try:
                downloadVideo("720p", audio_only)
                print("Succesvol de video gedownload in 720p")
                break
            except:
                print("Het is niet gelukt om de video in 720p te downloaden we proberen nu 480p")
            try:
                downloadVideo("480p", audio_only)
                print("Succesvol de video gedownload in 480p")
                break
            except:
                print("Het is niet gelukt om de video in 480p te downloaden we proberen nu 360p")
            try:
                downloadVideo("380p", audio_only)
                print("Succesvol de video gedownload in 360p")
                break
            except:
                print("Het is niet gelukt om de video in 360p we stoppen nu het programma.")
                break
        if not os.path.exists(f"YouTube/Video's/{yt.video_id}/info.txt"):
            os.makedirs(f"YouTube/Video's/{yt.video_id}/info.txt")
        infoFile = open(f"YouTube/Video's/{yt.video_id}/info.txt", "w", encoding="utf-8")
        infoFile.write("Title: " + str(yt.title) + "\nViews: " + str(yt.views) + "\nDescription: " + str(yt.description) + "\nKeywords: " + str(yt.keywords) + "\nLength: " + str(yt.length) + "\nMetadata: " + str(yt.metadata) + "\nRating: " + str(yt.rating) + "\nVideo info " + str(yt.vid_info))
        infoFile.close()
    if (choice == "2"):
        listFile = open("listfile.txt", "r", encoding="utf-8")
        for line in listFile:
            for i in line:
                count += 1
            if (count < 40):
                try:
                    yt = YouTube(line)
                except:
                    print("Dit is geen youtube video link!")
                else:
                    yt.streams.filter(res="720p").first().download(output_path = f"YouTube/Video's/{yt.video_id}/", filename = "video.mp4")
                    infoFile = open(f"YouTube/Video's/{yt.video_id}/info.txt", "w", encoding="utf-8")
                    infoFile.write("Title: " + str(yt.title) + "\nViews: " + str(yt.views) + "\nDescription: " + str(yt.description) + "\nKeywords: " + str(yt.keywords) + "\nLength: " + str(yt.length) + "\nMetadata: " + str(yt.metadata) + "\nRating: " + str(yt.rating) + "\nVideo info " + str(yt.vid_info))
                    infoFile.close()
                    line = listFile.readline()
                    print("Succesvol de video gedownload!")
            else:
                print("Error! Je hebt waarschijnlijk 2 links naast elkaar staan! Check dit en run het programma daarna opnieuw.")
        listFile.close()
elif (firstChoice == "2"):
    choice = str(input("1. Een livestream\n2. Lijst met livestream's\nKies je optie: "))
elif (firstChoice == "3"):
    choice = str(input("1. Een kanaal\n2. Lijst met kanalen\n3. Kanaal informatie\nKies je optie: "))
    if (choice == "1"):
        c = input("Voer een link in: ")
        try:
            Channel(c)
        except:
            print("Dit is geen kanaal link!")
        else:
            os.system("cls")
            choice = input("1. Alle video's downloaden\n2. Url van alle video's\nKies je optie: ")
            if (choice == "1"):
                videos = 0
                for video in c.videos:
                    videos += 1
                for video in c.videos:
                    video.streams.first().download(output_path = f"YouTube/Channels/{c.channel_name}/{video.video_id}/", filename = "video.mp4")
                    infoFile = open(f"YouTube/Channels/{c.channel_name}/{video.video_id}/info.txt", "w", encoding="utf-8")
                    infoFile.write("Title: " + str(video.title) + "\nViews: " + str(video.views) + "\nDescription: " + str(video.description) + "\nKeywords: " + str(video.keywords) + "\nLength: " + str(video.length) + "\nMetadata: " + str(video.metadata) + "\nRating: " + str(video.rating) + "\nVideo info " + str(video.vid_info))
                    infoFile.close()
                    videos -= 1
                    if (videos > 0):
                        print(f"Succesvol gedownload! Nog {videos} video's te gaan.")
                    else:
                        print("Alle video's zijn succesvol gedownload!")
            elif (choice == "2"):
                for url in c.video_urls:
                    print(url)
            elif (choice == "3"):
                if not os.path.exists(f"YouTube/Channels/{c.channel_name}/"):
                    os.makedirs(f"YouTube/Channels/{c.channel_name}/")
                infoFile = open(f"YouTube/Channels/{c.channel_name}/channel.txt", "w", encoding="utf-8")
                infoFile.write("Name: " + str(c.channel_name) + "\nId: " + str(c.channel_id))
                infoFile.close()
                print("Succesvol alle kanaal data opgehaald!")

