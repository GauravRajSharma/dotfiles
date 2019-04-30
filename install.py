from subprocess import call
from pathlib import Path

# Requirements
home_path = Path.home()
config_path = home_path / '.config'
scripts_path = home_path / '.scripts'

# Make Directories
# Check for .scripts and .config folders, if doesn't exist create them
if not config_path.exists():
    config_path.mkdir()
if not scripts_path.exists():
    scripts_path.mkdir()

# Utils
def clean_home(directory_path, home_path):
    for ff in get_files_folder(directory_path):
        call([f'pushd {home_path};rm -rf {ff};popd'], shell=True)


def get_files_folder(path):
    return map(lambda path_: path_.name, path.glob('*'))


# Remove exisiting Configs and Scripts
clean_home(Path('config'), config_path)
clean_home(Path('scripts'), scripts_path)
clean_home(Path('home'), home_path)


# Call Stow
call(['make all;make clean'], shell=True)
