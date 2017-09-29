from bs4 import BeautifulSoup
import requests, sys
import youtube_dl

prefix = "https://www.youtube.com";
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


print("Enter link to playlist(including http://)");
destination = input();

r = requests.get(destination)
data = r.text
soup = BeautifulSoup(data, "html.parser");

res=soup.find_all('a',{'class':'pl-video-title-link'})
for k in res:
    dl_link = prefix + k.get('href');
    print("Downloading: " + k.text)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([dl_link]);
