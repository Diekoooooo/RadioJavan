import re, json, requests
from urllib.request import urlretrieve as download_file

def download_rj(music_url):
    try:
        if re.match("^https://rj\.app/m/(.*?)$", music_url, re.IGNORECASE):
            response = requests.get(music_url)
            music_url = response.url
        
        if re.match("^https://www\.radiojavan\.com/mp3s/mp3/(.*?)(\?(.*)|\/(.*)|)$", music_url, re.IGNORECASE):
            match = re.match("^https://www\.radiojavan\.com/mp3s/mp3/(.*?)(\?(.*)|\/(.*)|)$", music_url, re.IGNORECASE)
            music_name = match.group(1)
            
            response = requests.get(f"https://www.radiojavan.com/mp3s/mp3_host/?id={music_name}")
            base_url = json.loads(response.text)
                
            return download_file(f"{base_url['host']}/media/mp3/{music_name}.mp3", f"{music_name}.mp3")
    except:
        pass
    
    return False
print(3*'@python3_channel\n')
media_link = input("Enter music url: ")

download_music = download_rj(media_link)
if download_music:
    print("Download is successfully, Music was downloaded:", download_music[0])
else:
    print("Couldn't download music!")
