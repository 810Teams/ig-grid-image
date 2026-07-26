"""
    Scanner utility — discovers JPEG and PNG files in a directory.
"""


import os


# Extensions considered valid image files (case-insensitive comparison).
_VALID_EXTENSIONS: set[str] = {'.jpg', '.jpeg', '.png'}


def scan_images(directory: str) -> list[str]:
    """Return a sorted list of absolute paths to JPEG/PNG files in *directory*.

    Only files directly inside *directory* are returned (no recursion).
    """
    image_paths: list[str] = []

    for entry in os.listdir(directory):
        full_path: str = os.path.join(directory, entry)
        if not os.path.isfile(full_path):
            continue
        _, ext = os.path.splitext(entry)
        if ext.lower() in _VALID_EXTENSIONS:
            image_paths.append(full_path)

    image_paths.sort()
    return image_paths
