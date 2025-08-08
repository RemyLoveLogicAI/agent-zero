#!/bin/bash
set -e
SCRIPT_DIR=$(dirname "$0")
python3 "$SCRIPT_DIR/viral_video_experiment.py" "$@"
