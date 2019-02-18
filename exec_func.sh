#!/bin/bash

# Get datetime
CURR_TIME=$(date | sed 's/[ ]/_/g' | sed 's/:/-/g')

# Remove file
if [ -f $PWD/last_image.jpg ]; then
  echo "Good frame."
  # Uncomment line to keep images
  # cp last_image.jpg "images/$CURR_TIME.jpg"
else
  echo "Bad frame."
  #sudo reboot
fi

# Log image
echo $CURR_TIME >> capture.log
