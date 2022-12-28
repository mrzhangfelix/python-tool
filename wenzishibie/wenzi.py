import pytesseract
from PIL import Image
def main():
    # 读取图片
    im = Image.open('medal.png')
    # 识别文字
    string = pytesseract.image_to_string(im)
    print(string)


if __name__ == '__main__':
    main()