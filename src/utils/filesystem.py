import os

class FilesystemUtils:

    @staticmethod
    def get_file_paths(root_dir: str):
        """
        For a given directory, return all file paths of jpg and mp4 files that are direct or indirect children of the dir
        """
        images = []
        videos = []

        for root, _, files in os.walk(root_dir):
            for f in files:
                extension = f.split(".")[-1]
                if extension == "jpg":
                    images.append(os.path.join(root, f))
                elif extension == "mp4":
                    videos.append(os.path.join(root, f))
        
        return images, videos

    @staticmethod
    def create_if_not_exists(path: str):
        """
        Check if the given directory exists. If it doesn't, create it. This function behaves recursively by default
        """
        if not os.path.exists(path):
            os.makedirs(path)
