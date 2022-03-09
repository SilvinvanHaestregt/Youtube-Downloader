from pytube import YouTube
from time import sleep
count = 0

choice = str(input("Kies je optie: \n1.Losse video\n2.Lijst met video's\n"))

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