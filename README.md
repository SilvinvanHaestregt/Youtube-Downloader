# Table of contents
* [Technologies](#technologies)
* [General info](#general-info)
* [Setup](#setup)
* [How to add your own google API key](#api)


## Technologies

Project is created with:
* Python 3.10.2
* Visual studio code
* pytube
* Google API

# General info

With this program it is possible to download one or more youtube videos. You can choose to download 1 video, but you can also choose to download a whole list of youtube videos by simply copying the link of the video in video.txt. This file can be found in the Lists folder.

It is also possible to download all videos from a specified youtube channel. The option is also present to have a list of youtube channels, from which all videos are downloaded. Note that this can take up a lot of space on your PC so pay attention to this.

You can also get information about a certain youtube channel. The total number of views, subscribers and the total number of videos that the channel has. To be able to use this you need a google API key.

Below is explained how you can get it.

It is also possible to support me by subscribing to my patreon where you will get exclusive content and tutorials.

## Setup
```
$ cd Youtube-Downloader
$ pip3 install requirements.txt
$ python3 youtube_en.py or python3 youtube_nl.py
```


# How to add your own google API key

Go to the https://cloud.google.com/apis/ link and click the Console button in the top right corner.

(If you don't see this button, please log in with your google account first)

![First Image](/images/firstimage.png)

Then click on the button where the red arrow is. For me it says My First Project which is because I have already created a project before.

![Second Image](/images/secondimage.png)

Once you have done that, you will get the window below.

Then click on New Project.

![Third Image](/images/thirdimage.png)

Then give your project a name. For example: "YouTube API" (without the quotes) because we are going to work with the youtube api.

Now open your project by pressing the same button that will give you the window where you created your project. Click on the name of your project and then open at the bottom right.

Now click on the button "ENABLE APIS AND SERVICES".

![Fourth Image](/images/fourthimage.png)

Now search for the word YouTube.

Click "YouTube Data API v3". Now you are redirected to another page where you can enable the API. Click the "ENABLE" button.

![Fifth Image](/images/fifthimage.png)

You will now be sent back to your project where you then click on the "CREATE CREDENTIALS" button.

![Sixth Image](/images/sixthimage.png)

Now you need to select which API you are going to use. Click on the drop-down menu and press the "y" on your keyboard. After that, click on the option "YouTube Data API v3.

Now you get the 2 options namely: User data and Public data. Click on Public data and then on NEXT.

![Seventh Image](/images/seventhimage.png)

Now you will see your API Key.

# ATTENTION! Never share your API key if you haven't set any limits on it!

Copy and paste your API key to the api.json file. Now you can start your program!

Good luck!


# Table of contents
* [Wat doet dit programma?](#about)
* [Hoe voeg je je eigen google API key toe?](#api)
 
# Wat doet dit programma?

Met dit programma is het mogelijk om eeen of meerdere youtube video's te downloaden. Je kunt kiezen om 1 video te downloaden, maar je kunt er ook voor kiezen om een hele lijst aan youtube video's te downloaden door simpel weg de link van de video in video.txt te kopiëren. Dit bestand is te vinden in de map Lists.

Het is ook mogelijk om alle video's van een opgegeven youtube kanaal te downloaden. Hierbij is de optie ook aanwezig om een lijst van youtube kanalen te hebben, waarvan dan alle video's worden gedownload. Let wel op dat dit heel veel ruimte in kan nemen op je pc let hier dus goed op.

Je kan ook informatie krijgen over een bepaald youtube kanaal. Het totaal aantal views, subscribers en het totaal aantal video's dat het kanaal heeft. Om dit te kunnen gebruiken heb je we een google API key nodig.

Hieronder wordt uitgelegd hoe je die kan bemachtigen.

Het is ook mogelijk om mij te supporten via patreon waar je exlusieve content en tutorials kan krijgen.

# Hoe voeg je je eigen google API key toe?

Ga naar de link https://cloud.google.com/apis/ en klik rechts boven in op de knop Console.

(Als je deze knop niet te zien krijgt, log dan eerst in met je google account)

![First Image](/images/firstimage.png)

Klik vervolgens op de knop waar de rode pijl heen staat. Bij mij staat er My First Project dat komt omdat ik al eens eerder een project heb aangemaakt.

![Second Image](/images/secondimage.png)

Als je dat hebt gedaan dan krijg je het onderstaande venster.

Klik dan nu op New Project.

![Third Image](/images/thirdimage.png)

Geef je project vervolgens een naam. Bijvoorbeeld: "YouTube-API" (zonder de quotes) omdat we met de youtube api gaan werken.

Open nu je project door op de zelfde knop te drukken waarmee je het venster krijg waar je je project hebt aangemaakt. Klik op de naam van je project en dan rechts onder op open.

Klik nu op de knopt "ENABLE APIS AND SERVICES".

![Fourth Image](/images/fourthimage.png)

Zoek nu op het woord YouTube.

Klik op "YouTube Data API v3". Nu woord je doorgestuurd naar een andere pagina waar je de API kan inschakelen. Klik op de knop "ENABLE".

![Fifth Image](/images/fifthimage.png)

Je wordt nu terug gestuurd naar je project waarbij je vervolgens op de knop "CREATE CREDENTIALS" klikt.

![Sixth Image](/images/sixthimage.png)

Nu moet je selecteren welke API je gaat gebruiken. Klik op het dropdown menu en druk op je toetsenbord de "y" in. Klik daarna op de optie "YouTube Data API v3.

Nu krijg je de 2 opties namelijk: User data en Public data. Klik op Public data en daarna op NEXT.

![Seventh Image](/images/seventhimage.png)

Nu krijg je je API Key te zien.

# LET OP! Deel nooit je API key als je er geen grenzen op hebt gezet!

Kopieer en plak je API key nu naar de api.json file. Nu kan je je programma starten!

Veel succes!