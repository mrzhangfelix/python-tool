from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import pymysql

host="logs.lamp.run"
user="root"
password="mmit7750"
database="dev"
port=3306

def execute_sql(sql):
    conn = pymysql.connect(host=host,
                           user=user,
                           password=password,
                           database=database,
                           port=port)
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return result

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 4

        self.add_widget(Label(text='function'))
        self.add_widget(Label(text='duration'))
        self.add_widget(Label(text='count'))
        self.add_widget(Label(text='remark'))

        self.add_widget(Label(text='jiejie'))
        self.duration_jiejie = Label(text="")
        self.add_widget(self.duration_jiejie)
        self.count_jiejie = Label(text='')
        self.add_widget(self.count_jiejie)
        self.remark_jiejie = Label(text='',font_name='msyh.ttc')
        self.add_widget(self.remark_jiejie)

        self.add_widget(Label(text='tansuo'))
        self.duration_tansuo = Label(text='')
        self.add_widget(self.duration_tansuo)
        self.count_tansuo = Label(text='')
        self.add_widget(self.count_tansuo)
        self.remark_tansuo = Label(text='',font_name='msyh.ttc')
        self.add_widget(self.remark_tansuo)

        self.add_widget(Label(text='yaoqi'))
        self.duration_yaoqi = Label(text='')
        self.add_widget(self.duration_yaoqi)
        self.count_yaoqi = Label(text='')
        self.add_widget(self.count_yaoqi)
        self.remark_yaoqi = Label(text='',font_name='msyh.ttc')
        self.add_widget(self.remark_yaoqi)

        self.btn_1 = Button(text='refresh',on_press=self.dowork)

        self.add_widget(self.btn_1)

    def dowork(self,instance):
        result=execute_sql("select * from yyslog")
        self.duration_jiejie.text=str(result[0][3])
        self.count_jiejie.text=str(result[0][5])
        self.remark_jiejie.text=str(result[0][6])
        self.duration_tansuo.text=str(result[1][3])
        self.count_tansuo.text=str(result[1][5])
        self.remark_tansuo.text=str(result[1][6])
        self.duration_yaoqi.text=str(result[2][3])
        self.count_yaoqi.text=str(result[2][5])
        self.remark_yaoqi.text=str(result[2][6])
        print(result)


class MyApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
