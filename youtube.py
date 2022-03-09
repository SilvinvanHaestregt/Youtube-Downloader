from pytube import YouTube
count = 0

choice = str(input("Kies je optie: \n1.Losse video\n2.Lijst met video's\n"))

if (choice == "1"):
    yt = YouTube(input("Voer een link in: "))
    yt.streams.filter(res="720p").first().download(output_path = f"../Video's/YouTube/{yt.video_id}/", filename = "video.mp4")
    infoFile = open(f"../Video's/YouTube/{yt.video_id}/info.txt", "w", encoding="utf-8")
    infoFile.write("Title: " + str(yt.title) + "\nViews: " + str(yt.views) + "\nDescription: " + str(yt.description))
    infoFile.close()
if (choice == "2"):
    listFile = open("listfile.txt", "r", encoding="utf-8")
    for line in listFile:
        print(line)
        for i in line:
            count += 1
        if (count < 40):
            yt = YouTube(line)
            yt.streams.filter(res="720p").first().download(output_path = f"../Video's/YouTube/{yt.video_id}/", filename = "video.mp4")
            infoFile = open(f"../Video's/YouTube/{yt.video_id}/info.txt", "w", encoding="utf-8")
            infoFile.write("Title: " + str(yt.title) + "\nViews: " + str(yt.views) + "\nDescription: " + str(yt.description))
            infoFile.close()
            line = listFile.readline()
        else:
            print("Error! Je hebt waarschijnlijk 2 links naast elkaar staan! Check dit en run het programma daarna opnieuw.")
    listFile.close()
# Idee om to maken dat het programma door een lijst van linkjes gaat en elke download

print("Succesvol de video gedownload!")