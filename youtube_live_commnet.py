import requests
import json

YOUTUBE_API_KEY = 'AIzaSyBILnGxrgm2IoKKPXe2Pe1PRdkV-ljt84s'
LIVE_URL = 'https://www.youtube.com/watch?v=sbSKv5U0tAc'

def get_live_chat_id(live_url):
    video_id = live_url.replace('https://www.youtube.com/watch?v=','')
    print('video_id: ', video_id)
    
    url = 'https://www.googleapis.com/youtube/v3/videos'
    params = {'key': YOUTUBE_API_KEY, 'id': video_id, 'part': 'liveStreamingDetails'}
    data = requests.get(url, params=params).json()
    
    live_streaming_details = data['items'][0]['liveStreamingDetails']
    if 'activeLiveChatId' in live_streaming_details:
        live_chat_id = live_streaming_details['activeLiveChatId']
        print('live chat id: ', live_chat_id)
        
    return live_chat_id

def get_chat(live_chat_id, pageToken, log_file):
    url = 'https://www.googleapis.com/youtube/v3/liveChat/messages'
    params = {'key': YOUTUBE_API_KEY, 'liveChatId': live_chat_id, 'part': 'id,snippet,authorDetails'}
    if type(pageToken) == str:
        params['pageToken'] = pageToken
        
    data = requests.get(url, params=params).json()
    
    for item in data['items']:
        msg = item['snippet']['displayMessage']
        print(msg)
        print(data['nextPageToken'])

if __name__ == '__main__':
    live_chat_id = get_live_chat_id(LIVE_URL)
    get_chat(live_chat_id, None, '')