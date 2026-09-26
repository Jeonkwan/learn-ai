#!/usr/bin/env bash
set -euo pipefail

SOURCE_DIR="/Users/jeonkwan/projects/learn_ai"
DEST_DIR="/Users/jeonkwan/Library/Mobile Documents/com~apple~CloudDocs/learn_ai"

mkdir -p "$DEST_DIR"
rsync -av --delete --exclude '.git' "$SOURCE_DIR/" "$DEST_DIR/"
echo "Sync to iCloud completed successfully at $(date)."
