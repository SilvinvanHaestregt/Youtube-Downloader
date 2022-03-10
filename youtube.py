from pytube import YouTube
from pytube import Channel
from pytube import Search
from pytube import Playlist
import os
os.system("cls")
count = 0

isRunning = True

def continueEnter():
    choice = input("Druk op enter om door te gaan.")
    os.system("cls")

while (isRunning):
    
    #First option menu
    firstChoice = str(input("1. Video's\n2. YouTube kanaal\n3. Playlist - Deze doet het nog niet\n4. Search engine - Deze doet het nog niet\nZ. Sluit het programma\nKies je optie: "))

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
            elif (choice == "2"):
                print("Video wordt gedownload...")
                yt.streams.get_highest_resolution().download(output_path = f"YouTube/Video's/{yt.video_id}/", filename = "video.mp4")
                print("De video is succesvol gedownload in het mapje " + f"YouTube/Video's/{yt.video_id}/video.mp4")
                infoFile = open(f"YouTube/Video's/{yt.video_id}/info.txt", "w", encoding="utf-8")
                infoFile.write("Title: " + str(yt.title) + "\nViews: " + str(yt.views) + "\nDescription: " + str(yt.description) + "\nKeywords: " + str(yt.keywords) + "\nLength: " + str(yt.length) + "\nMetadata: " + str(yt.metadata) + "\nRating: " + str(yt.rating) + "\nVideo info " + str(yt.vid_info))
            infoFile.close()
            continueEnter()
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
                            if not os.path.exists(f"YouTube/Channels/{channel.channel_name}/"):
                                os.makedirs(f"YouTube/Channels/{channel.channel_name}/")
                            urlFile = open(f"YouTube/Channels/{channel.channel_name}/url.txt", "w", encoding="utf-8")
                            for video in channel.video_urls:
                                urlFile.write(video + "\n")
                            urlFile.close()
                        os.system("cls")
                        continueEnter()
                        break
                    elif (choice == "3"):
                        if not os.path.exists(f"YouTube/Channels/{channel.channel_name}/"):
                            os.makedirs(f"YouTube/Channels/{channel.channel_name}/")
                        infoFile = open(f"YouTube/Channels/{channel.channel_name}/channel.txt", "w", encoding="utf-8")
                        infoFile.write("Name: " + str(channel.channel_name) + "\nId: " + str(channel.channel_id))
                        infoFile.close()
                        print("Succesvol alle kanaal data opgehaald!")
                        continueEnter()
        elif (choice == "2"):
            choice = str(input("1. Alle video's downloaden\n2. Url van alle video's\n3. Kanaal informatie\nKies je optie: "))
            os.system("cls")
            channelList = open("channel.txt", "r", encoding="utf-8")
            for line in channelList:
                print(line)
                try:
                    channel = Channel(line)
                except:
                    print("Het programma wordt gestopt omdat er een ongeldige link in het tekst bestand zit.")
                    break
                else:
                    if (choice == "1"):
                        for video in channel.videos:
                            video.streams.get_highest_resolution().download(output_path= f"YouTube/Channels/{channel.channel_name}/{video.video_id}", filename = "video.mp4")

            continueEnter()
    elif (firstChoice == "3"):
        print("Dit werkt nog niet dit komt later pas!")
        continueEnter()
        continue
        choice = str(input("1. Playlist downloaden\nKies je optie: "))
        os.system("cls")
    elif (firstChoice == "4"):
        print("Dit werkt nog niet dit komt later pas!")
        continueEnter()
        continue
        search = str(input("Wat wil je opzoeken: "))
        while True:
            try:
                search = Search(search)
                break
            except:
                print("Dit is geen geldige zoek term")
    elif (firstChoice == "Z" or "z"):
        isRunning = False