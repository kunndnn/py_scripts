from PIL import Image

 
def image_to_pdf(img_path, pdf_path):
    # open image file
    image = Image.open(img_path)

    # convert image to RGB mode if it's not
    if image.mode != "RGB":
        image = image.convert("RGB")

    # save image as a PDF
    image.save(pdf_path, "PDF", resolution=100.0)


# call function
image_to_pdf("icon.jpg", "output.pdf")
