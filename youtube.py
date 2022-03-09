from pytube import YouTube
from pytube import Channel
from time import sleep
import os
os.system("cls")
count = 0

isRunning = True

def continueEnter():
    choice = input("Druk op enter om door te gaan.")
    os.system("cls")

while (isRunning):
    
    #First option menu
    firstChoice = str(input("1. Video's\n2. YouTube kanaal\nKies je optie: "))

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
            while True:
                print("Video wordt gedownload...")
                yt.streams.get_highest_resolution().download(output_path = f"YouTube/Video's/{yt.video_id}/", filename = "video.mp4")
                infoFile = open(f"YouTube/Video's/{yt.video_id}/info.txt", "w", encoding="utf-8")
                infoFile.write("Title: " + str(yt.title) + "\nViews: " + str(yt.views) + "\nDescription: " + str(yt.description) + "\nKeywords: " + str(yt.keywords) + "\nLength: " + str(yt.length) + "\nMetadata: " + str(yt.metadata) + "\nRating: " + str(yt.rating) + "\nVideo info " + str(yt.vid_info))
                infoFile.close()
                continueEnter()
                break
        elif (choice == "2"):
            listFile = open("listfile.txt", "r", encoding="utf-8")
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
        choice = str(input("1. Een kanaal\n2. Lijst met kanalen\n3. Kanaal informatie\nKies je optie: "))
        os.system("cls")
        if (choice == "1"):
            # Try to convert de input string into a Channel if this doesn't work it gives an error message and you can try again
            while True:
                c = input("Voer een link in: ")
                try:
                    Channel(c)
                    break
                except:
                    print("Dit is geen kanaal link!")
                os.system("cls")
            choice = str(input("1. Alle video's downloaden\n2. Url van alle video's\nKies je optie: "))
            os.system("cls")
            if (choice == "1"):
                videos = 0
                for video in c.videos:
                    videos += 1
                for video in c.video:
                    video.streams.first().download(output_path = f"YouTube/Channels/{c.channel_name}/{video.video_id}/", filename = "video.mp4")
                    infoFile = open(f"YouTube/Channels/{c.channel_name}/{video.video_id}/info.txt", "w", encoding="utf-8")
                    infoFile.write("Title: " + str(video.title) + "\nViews: " + str(video.views) + "\nDescription: " + str(video.description) + "\nKeywords: " + str(video.keywords) + "\nLength: " + str(video.length) + "\nMetadata: " + str(video.metadata) + "\nRating: " + str(video.rating) + "\nVideo info " + str(video.vid_info))
                    infoFile.close()
                    videos -= 1
                    if (videos > 0):
                        print(f"Succesvol gedownload! Nog {videos} video's te gaan.")
                    else:
                        print("Alle video's zijn succesvol gedownload!")
                continueEnter()
            elif (choice == "2"):
                # This doesn't work yet it gives an error: AttributeError: 'str' object has no attribute 'video_url'
                for url in c.video_url:
                    print(url)
            elif (choice == "3"):
                if not os.path.exists(f"YouTube/Channels/{c.channel_name}/"):
                    os.makedirs(f"YouTube/Channels/{c.channel_name}/")
                infoFile = open(f"YouTube/Channels/{c.channel_name}/channel.txt", "w", encoding="utf-8")
                infoFile.write("Name: " + str(c.channel_name) + "\nId: " + str(c.channel_id))
                infoFile.close()
                print("Succesvol alle kanaal data opgehaald!")
                continueEnter()

