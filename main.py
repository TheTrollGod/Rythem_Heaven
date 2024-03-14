import os
from dotenv import load_dotenv
from discord.ext import commands
from discord_interactions import InteractionsClient
import youtube_dl
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Load environment variables from the .env file
dotenv_path = "./creds.env"
load_dotenv()

# Set up Discord bot with interactions
bot = InteractionsClient()

# Set up YouTube downloader
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# Initialize Spotipy client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

# Command to play a YouTube video
@bot.command(name="youtube", description="Play a YouTube video")
async def play(ctx, query: str):
    youtube_api_key = os.getenv('YOUTUBE_API_KEY')
    voice_channel = ctx.author.voice.channel
    voice_client = await voice_channel.connect()

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f'ytsearch:{query}', download=False)
        url = info['entries'][0]['formats'][0]['url']

    voice_client.play(discord.FFmpegPCMAudio(url))
    voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
    voice_client.source.volume = 0.5

# Command to play a Spotify track
@bot.command(name="spotify", description="Play a Spotify track")
async def spotify(ctx, track_uri: str):
    voice_channel = ctx.author.voice.channel
    voice_client = await voice_channel.connect()

    track_info = sp.track(track_uri)
    track_preview_url = track_info['preview_url']

    voice_client.play(discord.FFmpegPCMAudio(track_preview_url))
    voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
    voice_client.source.volume = 0.5

# Run the bot with the Discord token loaded from the .env file
bot.run(os.getenv('DISCORD_TOKEN'))
