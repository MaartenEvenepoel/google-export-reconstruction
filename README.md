# Google Export Reconstruction
Script that reconstructs a more time-accurate directory structure based for large Google Photos exports

The script takes a source directory as input, recursively searches for all jpg and mp4 images in that source directory or any subdirectories. The discovered jpg and mp4 images are then written to a new output directory structure, with subdirectories for different years. Images are placed in these directories according to the time they were taken.

Videos are just moved to a seperate video subdirectories in the output directory.

## Running the script

`$ python src/main.py /path/to/google-export-directory /path/to/destination-directory`

