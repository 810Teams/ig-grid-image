"""
    Exporter — saves a PIL Image as a JPEG file.
"""


import os

from PIL import Image


def export_image(
    image: Image.Image,
    original_path: str,
    output_directory: str,
    export_prefix: str,
    jpeg_quality: int,
    icc_profile: bytes | None = None,
) -> str:
    """Save *image* as a JPEG in *output_directory*.

    The exported file name is ``<export_prefix><original_basename>.jpg``.
    If the source file already had a ``.jpg`` or ``.jpeg`` extension it is
    replaced; PNG sources get ``.jpg`` appended in place of ``.png``.

    When *icc_profile* is provided, the ICC color profile is embedded in the
    output JPEG so that colour rendering matches the original file.

    Returns the absolute path of the written file.
    """
    base_name: str = os.path.basename(original_path)
    name, _ = os.path.splitext(base_name)
    export_name: str = '{}{}.jpg'.format(export_prefix, name)
    export_path: str = os.path.join(output_directory, export_name)

    os.makedirs(output_directory, exist_ok=True)

    save_kwargs: dict = {
        'format': 'JPEG',
        'quality': jpeg_quality,
        'subsampling': 0,
    }
    if icc_profile is not None:
        save_kwargs['icc_profile'] = icc_profile

    image.save(export_path, **save_kwargs)
    return export_path
