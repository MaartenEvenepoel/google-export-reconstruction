from PIL import Image
from datetime import datetime

TIME_TAKEN_TAG_JPG = 36867

class ImageUtils:

    @staticmethod
    def get_image_filename(image: Image) -> str:
        return image.filename.split('/')[-1]

    @staticmethod
    def get_datetime_taken(image: Image) -> datetime:
        """
        For a jpg image at the given file path, return the time the picture was taken
        function returns a datetime object

        Functions raises an exception if the creation time of the image is not present in the 
        image's metadata.
        """
        try:
            datetime_taken = image._getexif()[TIME_TAKEN_TAG_JPG]
            return datetime.strptime(datetime_taken, "%Y:%m:%d %H:%M:%S")
        except:
            raise

    @staticmethod
    def print_info(image: Image):
        """
        Print some basic info for image at the given path
        """
        info_dict = {
            "Filename": image.filename,
            "Image Size": image.size,
            "Image Height": image.height,
            "Image Width": image.width,
            "Image Format": image.format,
            "Image Mode": image.mode,
            "Image is Animated": getattr(image, "is_animated", False),
            "Frames in Image": getattr(image, "n_frames", True)
        }

        for label, value in info_dict.items():
            print(f"{label:25}: {value}")
