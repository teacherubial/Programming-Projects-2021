# Image Magic
# Load an image and manipulate the pixels

from PIL import Image


def to_greyscale(pixel: tuple) -> tuple:
    """Convert a pixel to greyscale.

    Args:
        pixel: a 3-tuple of ints from
            0-255, e.g. (140, 120, 255)
            represents (red, green, blue)

    Returns:
        a 3-tuple pixel (r, g, b) in
        greyscale
    """
    # grab r, g, b
    red, green, blue = pixel

    # calculate the average
    average = int((red + green + blue) / 3)

    return average, average, average


def to_greyscale_luma(pixel: tuple) -> tuple:
    """Convert to greyscale using luma algorithm

    Args:
        pixel: a 3-tuple of ints from
            0-255, e.g. (140, 120, 255)
            represents (red, green, blue)

    Returns:
        a 3-tuple pixel (r, g, b) in
        greyscale
    """
    red, green, blue = pixel

    grey = int(red * 0.3 + green * 0.59 + blue * 0.11)

    return grey, grey, grey


# Load the image (pumpkin)
# Open an output image that's the same size
image = Image.open('./halloween-unsplash.jpg')
output_image = Image.open('./halloween-unsplash.jpg')

# Grab pixel information
a_pixel = image.getpixel((0, 0))  # grab pixel (0, 0) top-left

print(a_pixel)

# Iterate over EVERY PIXEL
# Get dimensions (size) of the image
image_width = image.width
image_height = image.height

# Modify the image to convert it from colour to grayscale
# ( r, g, b ) --> ( ?, ?, ? )
# take the r g b, add them up and divide by 3
# replace r, g, b with that AVERAGE value

# Top to bottom
for y in range(image_height):
    # Left to right
    for x in range(image_width):
        # Grab pixel information for THIS pixel
        pixel = image.getpixel((x, y))

        grey_pixel = to_greyscale_luma(pixel)

        # put that in the new image
        output_image.putpixel((x, y), grey_pixel)

output_image.save('grayscale_luma.jpg')
