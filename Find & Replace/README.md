# Find & Replace <img src="icon.png" alt="image" width="30"/>

Window pops up that allows you to enter a character/string to find, and a character/string to replace.

- Supports javascript regex (flags are `gm`)

<img width="400px" src="https://i.imgur.com/nt28AaI.png">


## Requirements:

This should run with no dependencies on apple silicon, but if on intel, you just compile the binary yourself.

1. Install latest version of [V](https://vlang.io/).
```shell
# install
brew install vlang
# update
v up
```
2. Install latest version of [ui](https://github.com/vlang/ui)
```shell
v install ui
```
3. Set `Find & Replace` folder as current directory.
```shell
# example
cd "Downloads/Find & Replace"
```
4. Compile binary.
```shell
v -prod ./action.v
```
5. Now install the popclip extension like usual.