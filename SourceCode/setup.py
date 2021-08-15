from cx_Freeze import setup, Executable

base = None    

executables = [Executable("YouTubeDownloader.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "VidGet",
    options = options,
    version = "1",
    description = 'Sime program to download the videos from YouTube', 
    executables = executables
)
