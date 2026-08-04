from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.video import Video
from kivy.uix.image import Image

class SplashScreen(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        layout=FloatLayout()

        title=Label(
            text="Welcome to Gifted Minds Academy",
            size_hint=(None,None), size=(300,50),
            pos_hint={"center_x":0.5,"center_y":0.9},
            font_size=30
            )
        video=Button(
            text="Watch KCSE Past Papers",
            size_hint=(0.5,0.1),
            pos_hint={"center_x":0.5,"center_y":0.5}
            )
        video.bind(on_press=self.go_to_video)

        layout.add_widget(title)
        layout.add_widget(video)

        self.add_widget(layout)

    def go_to_video(self,instance):
            self.manager.current="VideoScreen"
   

class LoginScreen(Screen):
    pass

class Registration(Screen):
    pass

class HomeScreen(Screen):
    pass

class SubjectScreen(Screen):

    pass

class VideoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

#IN THIS VIDEO I HAVE CREATED ONE PLAY AND PAUSE BUTTON
#In this video i have used floatlayout
#In this video i have used floatlayout
class VideoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout=BoxLayout(orientation="vertical")
        # this for video
        main_layout=FloatLayout()
        self.thumbnail=Image (source="kcse.jpg",
                         allow_stretch=True) 
        self.math=Video(source="KCSE-2025-QUESTION 1.mp4",
                   state="stop",
                   size_hint=(1,1))

        # The buttons
        button_layout=FloatLayout(size_hint=(1,0.12))
            
        play_pause_btn=Button(text=("PLAY"),
            size_hint=(0.18,0.5),
            pos_hint={"x":0.05,"center_y":0.5}
        )
        
        pause_btn=Button(text=("NEXT QUESTION"),
            size_hint=(0.18,0.5),
            pos_hint={"x":0.3,"center_y":0.5}
        )

        button3=Button(text=("SEARCH FOR PAST KCSE QUESTION"),
            size_hint=(0.20,0.5),
            pos_hint={"x":0.52,"center_y":0.5}
        )

        button4=Button(text=("HOME"),
            size_hint=(0.18,0.5),
            pos_hint={"x":0.77,"center_y":0.5}
        )

        button_layout.add_widget(play_pause_btn)
        button_layout.add_widget(pause_btn)
        button_layout.add_widget(button3)
        button_layout.add_widget(button4)
        main_layout.add_widget(self.math)
        main_layout.add_widget(self.thumbnail)
        main_layout.add_widget(button_layout)
        

        def play_pause(instance):
            if self.math.state=="play":
                self.math.state= "pause"
                play_pause_btn.text="Play"
            else:
                self.thumbnail.opacity=0    #hide thumbnail whenstarting
                self.thumbnail.disabled=True
                self.math.state="play"
                play_pause_btn.text="Pause"

        play_pause_btn.bind(on_press=play_pause)
                
        self.add_widget(main_layout)
        

class QuizScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class SettingScreen(Screen):
    pass

class GiftedMindsApp(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(SplashScreen(name="splash"))
        sm.add_widget(VideoScreen(name="VideoScreen"))
        return sm
GiftedMindsApp().run()



