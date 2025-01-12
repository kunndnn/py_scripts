import yt_dlp

def download_video_with_audio(url):
    ydl_opts = {
        "format": "best",   # Downloads the best available combined stream (video + audio)
        "noplaylist": True, # Ensure only a single video is downloaded
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading: {url}")
            ydl.download([url])
            print("Download complete!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video_with_audio(video_url)
