from PIL import Image, ImageFilter, ImageEnhance

def open_image(path):
    return Image.open(path)

def save_image(image, path):
    image.save(path)

def crop_image(image, box):
    return image.crop(box)

def apply_filter(image, filter_type):
    filters = {
        'BLUR': ImageFilter.BLUR,
        'CONTOUR': ImageFilter.CONTOUR,
        'DETAIL': ImageFilter.DETAIL
    }
    return image.filter(filters.get(filter_type, ImageFilter.BLUR))

def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def main():
    image = open_image('input.jpg')
    cropped_image = crop_image(image, (100, 100, 400, 400))
    filtered_image = apply_filter(cropped_image, 'DETAIL')
    bright_image = adjust_brightness(filtered_image, 1.5)
    save_image(bright_image, 'output.jpg')

if __name__ == "__main__":
    main()
