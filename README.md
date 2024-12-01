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
export PYTHONPATH=$PYTHONPATH:/home/richard/IdeaProjects/aoc2024
export AOC_SESSION=<session>
python3 dayx/python/main.py

# z80
cd dayx/z80
pasmo --tapbas main.asm main.tap
fuse main.tap
```

## Personal rules

- Having fun with python to get the scores z80 is just a bonus
- For z80 data can be preprocessed in python and then copied to the z80 code, this is a must tbh for it to happen

