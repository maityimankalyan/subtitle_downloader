"""Copyright (C) 2019 Iman Kalyan Maity - All Rights Reserved
You may use, distribute and modify this code under the
terms of the open source license, which unfortunately won't be
written for another century.

You should have received a copy of the open source license with
this file. If not,
please write to: maityimankalyan@gmail.com.
"""
# importing necessary libraries
from argparse import ArgumentParser
import os
import subprocess
import subliminal
from babelfish import Language
import shlex
import subliminal_process
# supported video extensions
VIDEO_EXTENSIONS = ('.3g2', '.3gp', '.3gp2', '.3gpp', '.60d', '.ajp', '.asf', '.asx', '.avchd', '.avi', '.bik',
                    '.bix', '.box', '.cam', '.dat', '.divx', '.dmf', '.dv', '.dvr-ms', '.evo', '.flc', '.fli',
                    '.flic', '.flv', '.flx', '.gvi', '.gvp', '.h264', '.m1v', '.m2p', '.m2ts', '.m2v', '.m4e',
                    '.m4v', '.mjp', '.mjpeg', '.mjpg', '.mkv', '.moov', '.mov', '.movhd', '.movie', '.movx', '.mp4',
                    '.mpe', '.mpeg', '.mpg', '.mpv', '.mpv2', '.mxf', '.nsv', '.nut', '.ogg', '.ogm' '.ogv', '.omf',
                    '.ps', '.qt', '.ram', '.rm', '.rmvb', '.swf', '.ts', '.vfw', '.vid', '.video', '.viv', '.vivo',
                    '.vob', '.vro', '.wm', '.wmv', '.wmx', '.wrap', '.wvx', '.wx', '.x264', '.xvid')

# supported output subtitle extensions
SUBTITLE_EXT = ('.sub', '.smi', '.txt', '.ssa', '.ass', '.mpl')


def download_subtitles(args):
    """Function to process supported video files and download subtitles for them
    Parameters:
        args (ArgumentParser object): contains all the command line args
    Returns:
        1 (int): for success
    """

    # collecting all the video file names in the targeted directory
    language_dict = {}
    path = ' '.join(args.directory)
    print("[User] checking files in {} ...".format(path))
    videos = subliminal.scan_videos(path)  #TODO: download new video's subtitles , age=timedelta(weeks=2)
    if args.languages == 'en':
        language_dict ={Language('en')}
    elif args.language == 'fr':
        language_dict ={Language('fr')}
    else:
        language_dict = {Language('eng'), Language('fra')}
    subtitles = subliminal.download_best_subtitles(videos, language_dict)
    for v in videos:
        subliminal.save_subtitles(v, subtitles[v])

    # TODO: removing en/fr from the subtitle name
    for file in os.listdir( ):
        for ext in SUBTITLE_EXT:
            lan_ext = '.{}{}'.format(, ext)
            if file.endswith(lan_ext):
                os.rename(file , file.replace(lan_ext , ext))
    return 1


if __name__ == "__main__":
    # command line argument persing
    parser = ArgumentParser()
    parser.add_argument("-d", "--directory", dest="directory", nargs='+',
                        help='example: -d <directory path>. default is current directory', type=str, default=os.getcwd())
    parser.add_argument("-l", "--language", dest="language",
                        help="example: -l <en_fr or fr>. default is English only", type=str, default='en')
    args = parser.parse_args()
    download_subtitles(args)
