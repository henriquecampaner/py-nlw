import os

from barcode import Code128
from barcode.writer import ImageWriter


class BarcodeHandler:
    def create_barcode(self, product_code: str) -> str:
        tag = Code128(product_code, writer=ImageWriter())
        path_from_tag = f"{tag}"
        images_folder = "src/views/static/images"
        tag.save(os.path.join(images_folder, path_from_tag))

        return path_from_tag
