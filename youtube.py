from pytube import YouTube
from pytube import Channel
from time import sleep
import os
count = 0

firstChoice = str(input("1. Video's\n2. Livestream's\n3. YouTube kanaal\nKies je optie: "))
os.system("cls")

if (firstChoice == "1"):
    choice = str(input("\n1. Een video\n2. Lijst met video's\nKies je optie: "))
    os.system("cls")
    if (choice == "1"):
        yt = YouTube(input("Voer een link in: "))
        try:
            print("Proberen om video te downloaden in 720p")
            yt.streams.filter(res="720p").first().download(output_path = f"../Video's/YouTube/{yt.video_id}/", filename = "video.mp4")
            print("Succesvol de video gedownload in 720p")
        except:
            print("Het is niet gelukt om de video in 720p te downloaden we proberen nu 480p")
            yt.streams.filter(res="480p").first().download(output_path = f"../Video's/YouTube/{yt.video_id}/", filename = "video.mp4")
            print("Succesvol de video gedownload in 480p")
        infoFile = open(f"../Video's/YouTube/{yt.video_id}/info.txt", "w", encoding="utf-8")
        infoFile.write("Title: " + str(yt.title) + "\nViews: " + str(yt.views) + "\nDescription: " + str(yt.description))
        infoFile.close()
    if (choice == "2"):
        listFile = open("listfile.txt", "r", encoding="utf-8")
        for line in listFile:
            for i in line:
                count += 1
            if (count < 40):
                yt = YouTube(line)
                yt.streams.filter(res="720p").first().download(output_path = f"../Video's/YouTube/{yt.video_id}/", filename = "video.mp4")
                infoFile = open(f"../Video's/YouTube/{yt.video_id}/info.txt", "w", encoding="utf-8")
                infoFile.write("Title: " + str(yt.title) + "\nViews: " + str(yt.views) + "\nDescription: " + str(yt.description))
                infoFile.close()
                line = listFile.readline()
                print("Succesvol de video gedownload!")
            else:
                print("Error! Je hebt waarschijnlijk 2 links naast elkaar staan! Check dit en run het programma daarna opnieuw.")
        listFile.close()
elif (firstChoice == "2"):
    choice = str(input("1. Een livestream\n2. Lijst met livestream's\nKies je optie: "))
elif (firstChoice == "3"):
    choice = str(input("1. Een kanaal\n2. Lijst met kanalen\nKies je optie: "))
    if (choice == "1"):
        c = Channel(input("Voer een link in: "))
        os.system("cls")
        choice = input("1. Alle video's downloaden\n2. Url van alle video's\nKies je optie: ")
        if (choice == "1"):
            for video in c.videos:
                # Zet hier het download path neer zie line 33
                video.streams.first().download()
        elif (choice == "2"):
            for url in c.video_urls:
                print(url)