#!/bin/bash
# Running latency trials for different graphics cases

# 001: no video, no preview, no captures
tegrastats --interval 1000 --logfile 001d_hwusage.txt &
python3 001_capture.py
pkill tegrastats


# 002: video, no preview, no captures
tegrastats --inverval 1000 --logfile 002d_hwusage.txt &
python3 002_capture.py
pkill tegrastats

# 003: video, preview, no captures
tegrastats --inverval 1000 --logfile 003d_hwusage.txt &
python3 003_capture.py
pkill tegrastats


# 004: video, preview, captures
tegrastats --inverval 1000 --logfile 004d_hwusage.txt &
python3 004_capture.py
pkill tegrastats

# plot trials
mv 00*.txt data/
cd analysis/
python3 plotgraphics.py
