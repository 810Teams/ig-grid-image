"""
    Settings
"""


# ---------------------------------------------------------------------------
# Output canvas settings
# ---------------------------------------------------------------------------

# Output resolution in pixels (width, height).
OUTPUT_WIDTH: int = 2160
OUTPUT_HEIGHT: int = 2160

# Background color of the canvas (R, G, B).
CANVAS_COLOR: tuple[int, int, int] = (255, 255, 255)

# Padding as a fraction of the canvas size, applied to each side of the
# image's long axis.  For example, 0.015 means 1.5% of the canvas dimension.
PADDING_RATIO: float = 0.015

# ---------------------------------------------------------------------------
# Export settings
# ---------------------------------------------------------------------------

# JPEG quality (1–100, where 100 is maximum quality).
JPEG_QUALITY: int = 100

# Prefix prepended to every exported file name.
EXPORT_PREFIX: str = "exported_"
