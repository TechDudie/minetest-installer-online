import os
import multiprocessing

DEPENDENCIES = {
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
}

REDLIST_FILE = [
    'CMakeFiles',
    'src',
    '.github',
    'build',
    'util',
    'po',
    'doc',
    'cmake',
    'cmake_install.cmake',
    'CMakeCache.txt',
    'CPackConfig.cmake',
    'CMakeLists.txt',
    'install.log',
    'LICENSE.txt',
    'Makefile',
    '.clang-tidy',
    '.clang-format',
    '.mailmap',
    '.luacheckrc',
    '.gitlab-ci.yml',
    'README.md',
    'Dockerfile',
    'AppImageBuilder.yml',
    '.gitattributes',
    '.gitignore',
    'CPackSourceConfig.cmake',
    'lib',
]


class Main_file:
    def __init__(self):
        self.proc_in = [self.install_deps, self.getting_src]
        self.proc_out = []
        self.initialize()

    def initialize(self):
        if os.path.isdir('./minetest/bin/'):
            print(f'''Its seams minetest is already installed in this directory
          Press enter to Overwrite or q to exit:''')
            continue_input = input()
            if continue_input == "":
                os.system('rm -rf ./minetest')
                self.process_launcher()
                self.compiling_src()
            if continue_input == "q":
                exit()
        elif not os.path.isdir('./minetest/bin/'):
            self.process_launcher()
            self.compiling_src()

    @staticmethod
    def install_deps():
        print('Installing Dependencies...')
        for install in DEPENDENCIES:
            print(f"Installing {install}")
            os.system(f"sudo apt-get install {install} -y >> install.log")

    @staticmethod
    def getting_src():
        print('Collecting Source Minetest...')
        os.system('git clone --depth 1 https://github.com/minetest/minetest.git >> install.log')
        os.chdir('./minetest')
        os.system(
            'git clone --depth 1 https://github.com/minetest/minetest_game.git games/minetest_game >> install.log')

    @staticmethod
    def compiling_src():
        os.chdir('./minetest')
        print('Compiling Source....')
        os.system('cmake . -DRUN_IN_PLACE=TRUE >> install.log && make -j$(nproc) >> install.log')
        print('Finished Compiling')
        for file in REDLIST_FILE:
            os.system(f'rm -r {file}')


    def process_launcher(self):
        for name in self.proc_in:
            p = multiprocessing.Process(target=name)
            p.start()
            self.proc_out.append(p)

        for proc in self.proc_out:
            proc.join()



if __name__ == '__main__':
    start = Main_file()

