"""
    Canvas processor — places an image onto a padded white canvas.
"""


from PIL import Image


def create_canvas_image(
    source_path: str,
    output_width: int,
    output_height: int,
    canvas_color: tuple[int, int, int],
    padding_ratio: float,
) -> tuple[Image.Image, bytes | None]:
    """Open *source_path* and centre it on a blank canvas.

    The image is scaled so that its long side fits within the canvas minus
    the padding on each end (``padding_ratio`` × canvas dimension on that
    axis, applied to both sides).

    Returns a tuple of (composed RGB image, ICC profile bytes or ``None``).
    """
    canvas: Image.Image = Image.new('RGB', (output_width, output_height), canvas_color)

    with Image.open(source_path) as src:
        # Preserve the ICC color profile before converting
        icc_profile: bytes | None = src.info.get('icc_profile')

        src_image: Image.Image = src.convert('RGB')
        src_w, src_h = src_image.size

        # Determine which axis is the long side
        if src_w >= src_h:
            # Horizontal (or square) image — pad left/right
            available_w: int = int(output_width * (1 - 2 * padding_ratio))
            scale: float = available_w / src_w
            new_w: int = available_w
            new_h: int = int(src_h * scale)
        else:
            # Vertical image — pad top/bottom
            available_h: int = int(output_height * (1 - 2 * padding_ratio))
            scale: float = available_h / src_h
            new_h: int = available_h
            new_w: int = int(src_w * scale)

        resized: Image.Image = src_image.resize((new_w, new_h), Image.LANCZOS)

        # Centre on the canvas
        paste_x: int = (output_width - new_w) // 2
        paste_y: int = (output_height - new_h) // 2
        canvas.paste(resized, (paste_x, paste_y))

    return canvas, icc_profile
