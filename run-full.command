#!/bin/bash

TARGET_USER=target_user
USER=user
PASS=pass
YEAR=2018
NUM_ENTRIES=9

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"

cd $DIR

instagram-scraper $TARGET_USER -u $USER -p $PASS -t none --media-metadata
python instaparser.py -- $TARGET_USER/$TARGET_USER.json $YEAR $NUM_ENTRIES > $TARGET_USER.html
