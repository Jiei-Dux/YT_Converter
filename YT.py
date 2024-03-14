#! /bin/env python3

import os
import yt_dlp


# ===== ===== ===== ===== ===== # ===== ===== ===== ===== ===== #


def clear_terminal():
    if os.name == 'nt':
        os.system('cls')

    if os.name == 'posix':
        os.system('clear')


def menu():
    clear_terminal()
    print("Choose:\n 1:SFX\n 2:Music\n Q: Quit\n")
    choice = input(">> ")

    if choice == "1":
        SFX()

    if choice == "2":
        Music()

    if choice == "q" or "Q":
        quit


# ===== ===== ===== ===== ===== # ===== ===== ===== ===== ===== #


def mp3_convert(link, file_path):
    ytdlp_settings = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(file_path, '%(title)s.%(ext)s'),
    }


    with yt_dlp.YoutubeDL(ytdlp_settings) as YT_DLP:
        video = YT_DLP.extract_info(link, download=False)
        video_title = video.get('title', None)
        YT_DLP.download([link])

    return os.path.join(file_path, f"{video_title}.mp3")


def ogg_convert(link, file_path):
    ytdlp_settings = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'ogg',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(file_path, '%(title)s.%(ext)s'),
    }


    with yt_dlp.YoutubeDL(ytdlp_settings) as YT_DLP:
        video = YT_DLP.extract_info(link, download=False)
        video_title = video.get('title', None)
        YT_DLP.download([link])

    return os.path.join(file_path, f"{video_title}.mp3")


# ===== ===== ===== ===== ===== # ===== ===== ===== ===== ===== #


def Music():
    link = input("Enter link: ")

    file_path = "~/Music"
    file_name = mp3_convert(link, file_path)

    print("Video Conversion Success! File Path: {}" .format(file_name))


def SFX():
    link = input("Enter link: ")

    file_path = "~/Music/SFX"
    file_name = ogg_convert(link, file_path)

    print("Video Conversion Success! File Path: {}" .format(file_name))


# ===== ===== ===== ===== ===== # ===== ===== ===== ===== ===== #


if __name__ == "__menu__":
    menu()
