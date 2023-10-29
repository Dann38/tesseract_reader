import os

from utils.tesseract_reader.bbox.bbox import BBox
from utils.tesseract_reader.image_reader.image_reader import ImageReader
from typing import List
import numpy as np
from pytesseract import pytesseract


class TesseractReaderConfig:
    def __init__(self, lang="rus"):
        self.lang = lang
        pass

    def get_args_str(self) -> str:
        args_str = f"-l {self.lang}"
        return args_str


class TesseractReader:
    def __init__(self, conf: TesseractReaderConfig = None):
        self.config = conf

    def read(self, image: np.ndarray) -> List[BBox]:
        tesseract_bboxes = pytesseract.image_to_data(
            config=self.config.get_args_str(),
            image=image,
            output_type=pytesseract.Output.DICT)
        list_bbox = []
        for index_bbox, level in enumerate(tesseract_bboxes["level"]):
            if level == 5:
                x_top_left = tesseract_bboxes["left"][index_bbox]
                y_top_left = tesseract_bboxes["top"][index_bbox]
                width = tesseract_bboxes["width"][index_bbox]
                height = tesseract_bboxes["height"][index_bbox]
                print(tesseract_bboxes["text"][index_bbox])
                list_bbox.append(BBox(x_top_left, y_top_left, width, height))
        return list_bbox


if __name__ == '__main__':
    # Image path /example_img/img_1.jpeg
    path_project = os.path.abspath(os.path.join(os.getcwd(), ".."))
    path_img = os.path.join(path_project, 'example_img', "img_1.jpeg")

    # Objects
    image_reader = ImageReader()
    tesseract_config = TesseractReaderConfig()
    tesseract_reader = TesseractReader(tesseract_config)

    img = image_reader.read(path_img)
    tesseract_reader.read(img)


