sudo apt-get update
sudo apt-get install -y build-essential cmake wget pkg-config clang \
    libclang-dev llvm-dev libudev-dev libfreetype6-dev libexpat1-dev
git clone https://github.com/darkrenaissance/darkfi
cd darkfi
make
sudo make install
mkdir -p ~/.config/darkfi
cp -f /usr/local/share/doc/darkfi/*.toml ~/.config/darkfi
