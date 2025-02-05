import yt_dlp

def download_video_without_ffmpeg(url: str):
    # Instead of 'bestvideo+bestaudio', choose a single combined format
    # that includes both audio & video.
    ydl_opts = {
        'format': 'best',  # This instructs yt-dlp to download the best *combined* format
        # No postprocessing needed if we never merge.
        'postprocessors': [],  # Ensure we don't try to run FFmpeg at all
        'outtmpl': '%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    video_url = "URL"
    download_video_without_ffmpeg(video_url)
    print("Download completed!")
