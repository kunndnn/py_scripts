import yt_dlp

def download_video_with_audio(url):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",  # Ensure best video and best audio are merged
        "merge_output_format": "mp4",  # Specify the output format after merging
        "noplaylist": True,  # Download a single video
        "postprocessors": [
            {
                "key": "FFmpegVideoConvertor",
                "preferedformat": "mp4",  # Convert to mp4 if necessary
            }
        ],
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
