# Google Export Reconstruction
Script that re-orders and structures image and video files into subdirectories based on their creation timestamp.

When you generate an export of photo and video data from your google account, chances are you can only download the exports in several unorderd zip files. This script takes these different exports and arranges them into a structured directory structure based on their creation timestamp.

The script takes a source directory as input, recursively searches for all jpg and mp4 images in that source directory or any subdirectories. The discovered jpg and mp4 images are then written to a new output directory structure, with subdirectories for different years. Images are placed in these directories according to the time they were taken.

Videos are just moved to a seperate video subdirectory in the output directory.

## Running the script

`$ python src/main.py /path/to/google-export-directory /path/to/destination-directory`

