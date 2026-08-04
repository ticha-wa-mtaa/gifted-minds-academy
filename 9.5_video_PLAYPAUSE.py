from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.video import Video
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

#IN THIS VIDEO I HAVE CREATED ONE PLAY AND PAUSE BUTTON
#In this video i have used floatlayout
class VideoApp(App):
    def build(self):
        
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
                play_pause_btn.text="play"
            else:
                self.thumbnail.opacity=0    #hide thumbnail whenstarting
                self.thumbnail.disabled=True
                self.math.state="play"
                play_pause_btn.text="pause"

        play_pause_btn.bind(on_press=play_pause)
                
        return main_layout

VideoApp().run()
