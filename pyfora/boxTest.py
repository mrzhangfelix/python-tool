from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


# 布局类
class BoxLayoutWidget(BoxLayout):
    # 初始化
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BoxApp(App):
    # 实现App类的build()方法（继承自App类）
    def build(self):
        # 返回根控件
        return BoxLayoutWidget()


if __name__ == '__main__':
    # 启动程序
    BoxApp().run()
