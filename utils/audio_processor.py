import os
import re
import yt_dlp
from pydub import AudioSegment

# FFmpeg paths for your system
AudioSegment.ffmpeg = r"C:\ffmpeg\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\ffmpeg\bin\ffprobe.exe"

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def safe_filename(name):
    """
    Remove characters Windows doesn't allow in filenames.
    """
    return re.sub(r'[<>:"/\\|?*]', '_', name)


def download_youtube_audio(url: str) -> str:
    """
    Download YouTube audio and convert to WAV.
    """

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s"),
        "restrictfilenames": True,
        "ffmpeg_location": r"C:\ffmpeg\bin",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
            }
        ],
        "quiet": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

        downloaded_file = ydl.prepare_filename(info)

        wav_path = os.path.splitext(downloaded_file)[0] + ".wav"

        # Backup search in case yt-dlp renamed differently
        if not os.path.exists(wav_path):

            title = safe_filename(info["title"])

            for file in os.listdir(DOWNLOAD_DIR):
                if file.endswith(".wav"):
                    if title.lower().split("_")[0] in file.lower():
                        wav_path = os.path.join(DOWNLOAD_DIR, file)
                        break

    print("WAV file:", wav_path)

    if not os.path.exists(wav_path):
        raise FileNotFoundError(f"WAV file not found: {wav_path}")

    return wav_path


def convert_to_wav(input_path: str) -> str:
    """
    Convert local audio/video file to 16kHz mono WAV.
    """

    output_path = os.path.splitext(input_path)[0] + "_converted.wav"

    audio = AudioSegment.from_file(input_path)

    audio = audio.set_channels(1)
    audio = audio.set_frame_rate(16000)

    audio.export(output_path, format="wav")

    return output_path


def chunk_audio(wav_path: str, chunk_minutes: int = 10) -> list:
    """
    Split WAV into chunks.
    """

    if not os.path.exists(wav_path):
        raise FileNotFoundError(f"File not found: {wav_path}")

    audio = AudioSegment.from_wav(wav_path)

    chunk_ms = chunk_minutes * 60 * 1000

    chunks = []

    base_name = os.path.splitext(wav_path)[0]

    for i, start in enumerate(range(0, len(audio), chunk_ms)):
        chunk = audio[start:start + chunk_ms]

        chunk_path = f"{base_name}_chunk_{i}.wav"

        chunk.export(chunk_path, format="wav")

        chunks.append(chunk_path)

    return chunks


def process_input(source: str) -> list:

    if source.startswith(("http://", "https://")):
        print("Detected YouTube URL. Downloading audio...")
        wav_path = download_youtube_audio(source)

    else:
        print("Detected local file. Converting to WAV...")
        wav_path = convert_to_wav(source)

    print("Chunking audio...")
    chunks = chunk_audio(wav_path)

    print(f"Audio ready — {len(chunks)} chunk(s) created.")

    return chunks
