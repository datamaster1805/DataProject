from PIL import Image, ImageFont, ImageDraw
from random import randint


# 验证码文件："verifycode.png"
# 验证码数据：num.code
class VerifyCode01(object):
    def __init__(self, width=100, height=40, size=4):
        self.width = width
        self.height = height
        self.size = size
        self.__code = None
        self.pen = None

    @property
    def code(self):
        return self.__code.lower()

    def show_pic(self):
        im1 = Image.new("RGB", (self.width, self.height), self.rand_color())
        self.__code = self.rand_string()
        self.pen = ImageDraw.Draw(im1)
        self.draw_string()
        self.draw_point()
        self.draw_line()

        im1.show()
        im1.save("verifycode.png", "PNG")   # 需要重新确定验证码存放的位置

    def draw_string(self):
        font1 = ImageFont.truetype("1.ttf", size=25, encoding="utf-8")
        width = (self.width / self.size) - 20
        for i in range(self.size):
            x = 15 + i * width * 4
            y = 2 + randint(0, width)
            self.pen.text((x, y), self.__code[i], fill="black", font=font1)

    def rand_string(self):
        str1 = "QWERTYUPASDFGHJKLMNBVCXqwertyupasdfghjklxcvbnm1234567890"
        str2 = ""
        for _ in range(self.size):
            str2 += str1[randint(0, len(str1) - 1)]

        return str2

    def rand_point(self):
        x = randint(0, self.width)
        y = randint(0, self.height)
        return x, y

    def rand_color(self):
        return randint(100, 255), randint(100, 255), randint(100, 255)

    def draw_point(self):
        for i in range(200):
            self.pen.point(self.rand_point(), self.rand_color())

    def draw_line(self):
        for i in range(10):
            self.pen.line([self.rand_point(), self.rand_point()], fill=self.rand_color(), width=1)


if __name__ == "__main__":
    num = VerifyCode01()
    num.show_pic()
    print(num.code)
