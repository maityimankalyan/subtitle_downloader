from argparse import ArgumentParser
import os
import subprocess
import subliminal
import shlex

# supported video extensions
VIDEO_EXTENSIONS = ('.3g2', '.3gp', '.3gp2', '.3gpp', '.60d', '.ajp', '.asf', '.asx', '.avchd', '.avi', '.bik',
                    '.bix', '.box', '.cam', '.dat', '.divx', '.dmf', '.dv', '.dvr-ms', '.evo', '.flc', '.fli',
                    '.flic', '.flv', '.flx', '.gvi', '.gvp', '.h264', '.m1v', '.m2p', '.m2ts', '.m2v', '.m4e',
                    '.m4v', '.mjp', '.mjpeg', '.mjpg', '.mkv', '.moov', '.mov', '.movhd', '.movie', '.movx', '.mp4',
                    '.mpe', '.mpeg', '.mpg', '.mpv', '.mpv2', '.mxf', '.nsv', '.nut', '.ogg', '.ogm' '.ogv', '.omf',
                    '.ps', '.qt', '.ram', '.rm', '.rmvb', '.swf', '.ts', '.vfw', '.vid', '.video', '.viv', '.vivo',
                    '.vob', '.vro', '.wm', '.wmv', '.wmx', '.wrap', '.wvx', '.wx', '.x264', '.xvid')

SUBTITLE_EXT = ('.sub', '.smi', '.txt', '.ssa', '.ass', '.mpl')


def download_subtitles(args):
    """Function to process supported video files and download subtitles for them
    Parameters:
        args (ArgumentParser object): contains all the command line args
    Returns:
        1 (int): for success
    """
    print("[User] checking files in - {}".format(args.directory))
    all_files = [os.path.join(args.directory, each_file) for each_file in os.listdir(args.directory)]
    all_video_files = []
    for each_ext in VIDEO_EXTENSIONS:
        temp_video_files = [each_file for each_file in all_files if each_file.endswith(each_ext)]
        all_video_files += temp_video_files
    print("[User] all video files are: {}".format('\n'.join(all_video_files)))
    for each_video in all_video_files:
        cmd = 'subliminal download -l {} "{}"'.format(args.language, each_video)
        print("[User] Downloading subtitles for: {}".format(each_video))
        p = subprocess.Popen(cmd, shell=True)
    for file in os.listdir( ):
        for ext in SUBTITLE_EXT:
            lan_ext = '.{}{}'.format(args.language, ext)
            if file.endswith(lan_ext):
                os.rename(file , file.replace(lan_ext , ext))
    return 1


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-d", "--directory", dest="directory",
                        help='example: -d <directory path>. default is current directory', type=str, default=os.getcwd())
    parser.add_argument("-l", "--language", dest="language",
                        help="example: -l <en|fr>. default is English", type=str, default='en')
    args = parser.parse_args()
    download_subtitles(args)
