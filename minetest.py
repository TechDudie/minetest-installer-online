#!/usr/bin/python3
print("Checking OS...")
import platform
if not platform.release() == "Debian":
    print("Incompatible OS, aborting...")
    exit()
import os
print("Initilizing Install Process...")
dependencies = [
    'g++',
    'make',
    'libc6-dev', 
    'libirrlicht-dev',
    'cmake',
    'libbz2-dev',
    'libpng-dev',
    'libjpeg-dev',
    'libxxf86vm-dev',
    'libgl1-mesa-dev',
    'libsqlite3-dev',
    'libogg-dev',
    'libvorbis-dev',
    'libopenal-dev',
    'libcurl4-gnutls-dev',
    'libfreetype6-dev', 
    'zlib1g-dev',
    'libgmp-dev',
    'libjsoncpp-dev',
    'git'
]
print('Installing Dependencies...')
for install in dependencies:
    print(f"Installing {install}")
    os.system(f"sudo apt install {install} -y")


print('Collecting Source Minetest...')
os.system('git clone --depth 1 https://github.com/minetest/minetest.git')
os.chdir('minetest')
os.system('git clone --depth 1 https://github.com/minetest/minetest_game.git games/minetest_game')
print('Compiling Source....')
os.system('cmake . -DRUN_IN_PLACE=TRUE && make -j$(nproc)')
print("Adding Desktop Shortcut...")
with open('/usr/share/applications/minetest.desktop', 'w') as desktop:
     desktop.write("""[Desktop Entry]
	Name=Minetest 
	Comment=A voxel game engine
	GenericName=game
	X-GNOME-FullName=minetest
	Exec=/home/pc/minetest/bin/minetest
	Terminal=false
	X-MultipleArgs=false
	Type=Application
	Icon=/home/pc/minetest/textures/base/pack/logo.png
	Categories=Network;Games;
	StartupWMClass=Minetest
	StartupNotify=true""")
print("Done.")
