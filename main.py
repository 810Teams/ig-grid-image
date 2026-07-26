"""
    Main
"""


import os
import sys

from src.scanner import scan_images
from src.canvas import create_canvas_image
from src.exporter import export_image
from settings import (
    OUTPUT_WIDTH,
    OUTPUT_HEIGHT,
    CANVAS_COLOR,
    PADDING_RATIO,
    JPEG_QUALITY,
    EXPORT_PREFIX,
)


def main() -> None:
    """ Main function """

    # -----------------------------------------------------------------------
    # Resolve paths
    # -----------------------------------------------------------------------
    input_directory: str = os.getcwd()
    output_directory: str = input_directory

    # -----------------------------------------------------------------------
    # Scan for images
    # -----------------------------------------------------------------------
    image_paths: list[str] = scan_images(input_directory)

    print()
    print('Directory : "{}"'.format(input_directory))
    print('Canvas    : {}x{} px'.format(OUTPUT_WIDTH, OUTPUT_HEIGHT))
    print('Padding   : {}% each side'.format(PADDING_RATIO * 100))
    print('Quality   : {}'.format(JPEG_QUALITY))
    print('Prefix    : "{}"'.format(EXPORT_PREFIX))
    print()

    if not image_paths:
        print('No JPEG or PNG files found.')
        sys.exit(0)

    print('Found {} image{}.'.format(len(image_paths), 's' * (len(image_paths) > 1)))
    print()

    # -----------------------------------------------------------------------
    # Process each image
    # -----------------------------------------------------------------------
    exported_count: int = 0

    for image_path in image_paths:
        base_name: str = os.path.basename(image_path)

        canvas, icc_profile = create_canvas_image(
            source_path=image_path,
            output_width=OUTPUT_WIDTH,
            output_height=OUTPUT_HEIGHT,
            canvas_color=CANVAS_COLOR,
            padding_ratio=PADDING_RATIO,
        )

        export_path: str = export_image(
            image=canvas,
            original_path=image_path,
            output_directory=output_directory,
            export_prefix=EXPORT_PREFIX,
            jpeg_quality=JPEG_QUALITY,
            icc_profile=icc_profile,
        )

        print('  - Exported "{}" -> "{}"'.format(base_name, os.path.basename(export_path)))
        exported_count += 1

    # -----------------------------------------------------------------------
    # Summary
    # -----------------------------------------------------------------------
    print()
    print('Total of {} file{} exported.'.format(exported_count, 's' * (exported_count > 1)))


main()
