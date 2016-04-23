#!/bin/sh
rsync -a /home/username/Music/Top10Music /home/username/Music
rmdir Top10Music
mkdir Top10Music
cd Top10Music
python ./parsing.py
python ./ownsearch.py
cd ..
