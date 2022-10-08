from PIL import Image
import shutil
from typing import Dict
from utils.image import ImageUtils
from utils.filesystem import FilesystemUtils
from datetime import datetime
from tqdm import tqdm
import argparse

# input_dir = "/Users/maartenevenepoel/Documents/google-photos"
# output_dir = "/Users/maartenevenepoel/Documents/google-photos-reconstructed"

def process_images(images, output_dir):
    years_seen = []
    for image_path in tqdm(images):
        image = Image.open(image_path)
        try:
            datetime_taken = ImageUtils.get_datetime_taken(image)
            storage_path = f"{output_dir}/images/{datetime_taken.year}"

            if not datetime_taken.year in years_seen:
                FilesystemUtils.create_if_not_exists(storage_path)
                years_seen.append(datetime_taken.year)

            image.save(f"{storage_path}/{ImageUtils.get_image_filename(image)}")
        except:
            storage_path = f"{output_dir}/images/other"
            FilesystemUtils.create_if_not_exists(storage_path)
            image.save(f"{storage_path}/{ImageUtils.get_image_filename(image)}")


def process_videos(videos, output_dir):
    video_storage_directory = f"{output_dir}/videos"
    FilesystemUtils.create_if_not_exists(video_storage_directory)
    for video_path in tqdm(videos):
        video_name = video_path.split("/")[-1]
        shutil.copy(video_path, f"{video_storage_directory}/{video_name}")


def main():
    parser = argparse.ArgumentParser(description='Reconstruct google export')
    parser.add_argument('source_dir', type=str, help='Directory containing the Google export')
    parser.add_argument('output_dir', type=str, help='the reconstructed directory')
    args = parser.parse_args()

    images, videos = FilesystemUtils.get_file_paths(args.source_dir)

    print(f"Found {len(images)} images")
    print(f"Found {len(videos)} videos") 

    process_images(images, args.output_dir)
    process_videos(videos, args.output_dir)

    print("Done")
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Stopping process")
