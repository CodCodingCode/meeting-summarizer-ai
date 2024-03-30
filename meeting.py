import pyaudio
import selenium
import requests

zoom_api_key = "1PjcVtavRH2pBd_SNshqKA"
zoom_api_secret = "D7229G56zB2g8NcGKRQVoFLPXW6qkGvn"
recording_id = "819 4504 5515"
play_passcode = ""

url = f"https://api.zoom.us/v2/meetings/{recording_id}/recordings"
headers = {"Authorization": f"Bearer {zoom_api_key}.{zoom_api_secret}"}
response = requests.get(url, headers=headers)
recording = response.json()["recording_files"][0]
                            
download_link = f"{recording["download_url"]}?access_token={recording["recording_access_token"]}&playback_access_token={play_passcode}"


with open("my_recording.mp4", "wb") as f:
    response = requests.get(download_link)
    f.write(response.content)

#if __name__ == "__main__":
    #main()