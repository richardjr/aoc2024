# aoc2024

## Install

```bash
# Python
mkdir .venvs
python3 -m venv .venvs/
source .venvs/bin/activate
pip install -r requirements.txt

# z80
sudo apt-get install fuse-emulator-gtk spectrum-roms pasmo
```

## Run

```bash
# python
export AOC_SESSION=<session>
python3 dayx/python/main.py

# z80
cd dayx/z80
pasmo --tapbas main.asm main.tap
fuse main.tap
```

