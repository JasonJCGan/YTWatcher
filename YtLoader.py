import json
import time
import urllib.request
import webbrowser


def check_new_video():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    api_key = '' # Google API Key
    channel_id = '' # SAM THE COOKING GUY channel (UCbRj3Tcy1Zoz3rcf83nW5kw)

    base_yt_url = 'https://www.youtube.com/watch?v='
    base_url = 'https://www.googleapis.com/youtube/v3/search?' # Google API base url

    # Url used for request
    url = base_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=1'.format(api_key, channel_id)
    
    # Response of most recent video
    s = urllib.request.urlopen(url)
    resp = json.load(s)

    # Extract the videoID from the response
    vidID = resp['items'][0]['id']['videoId']

    video_exists = False
    # Check if the videoID is that of last cached
    with open('videoid.json','r') as json_file:
        data = json.load(json_file)
        if data['videoId'] != vidID:
            webbrowser.get(chrome_path).open(base_yt_url + vidID)
            video_exists = True
    
    # Update the latest video seen
    if video_exists:
        with open('videoid.json', 'w') as json_file:
            print("We found a new video. Enjoy!")
            data = {'videoId' : vidID}
            json.dump(data, json_file)
    else:
        print("No new videos were uploaded, we'll keep an eye out.")

try:
    while True:
        check_new_video()
        time.sleep(1000)
except KeyboardInterrupt:
    print('stopping')