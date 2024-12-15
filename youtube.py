import yt_dlp


def download_video(url):
    ydl_opts = {
        "format": "bestvideo[height<=1080]",
        "noplaylist": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    video_url = input("Enter video url to download: ")
    print("\nDownloading...")
    try:
        download_video(video_url)
    except Exception as e:
        print(f"\nError: {e}")
