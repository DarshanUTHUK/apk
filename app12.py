import os
import re
import subprocess
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class MyApp(App):
    def build(self):
        # Create a BoxLayout to arrange the background and the button
        layout = BoxLayout(orientation='vertical')

        # Create the background frame
        background = Label(
            text='My Application Background',
            font_size=24,
            color=(1, 1, 1, 1),  # white color
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        background.background_color = (0, 0, 0, 1)  # black color
        layout.add_widget(background)

        # Create the button
        button = Button(
            text='Open',
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            on_press=self.open
        )
        layout.add_widget(button)

        # Create the close button
        close_button = Button(
            text='Close',
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            on_press=self.close
        )
        layout.add_widget(close_button)

        # Create the close button
        open_recent_button = Button(
            text='Login recent app',
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            on_press=self.open_recent
        )
        layout.add_widget(open_recent_button)

        # Create the close button
        call_button = Button(
            text='Call',
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.01},
            on_press=self.call
        )
        layout.add_widget(call_button)

        return layout

    def open(self, instance):
        # Change the current working directory
        os.chdir('C:\\platform-tools_r34.0.5-windows\\platform-tools')
        # com.whatsapp/.Main
        subprocess.Popen(["adb", "shell", "am", "start", "-n", "com.android.dialer/.BBKTwelveKeyDialer"])
        # Wait for the WhatsApp window to be activated
        time.sleep(0.5)

    def open_recent(self, instance):
        # Change the current working directory
        os.chdir('C:\\platform-tools_r34.0.5-windows\\platform-tools')
        time.sleep(0.5)
        result = subprocess.run(["adb", "shell", "dumpsys", "activity", "recents"], capture_output=True, text=True)
        lines = result.stdout.strip().split("\n")
        for line in lines:
            match = re.search(r"realActivity=\{([^}]+)\}", line)
            if match:
                task = match.group()
                task = task.replace("realActivity={", "").replace("}", "")
                subprocess.Popen(["adb", "shell", "am", "start", "-n", task])
                break
        else:
            print("Not found any activies")
            return

    def close(self, instance):
        # Change the current working directory
        os.chdir('C:\\platform-tools_r34.0.5-windows\\platform-tools')
        # time.sleep(0.5)
        result = subprocess.run(["adb", "shell", "dumpsys", "activity", "recents"], capture_output=True, text=True)
        lines = result.stdout.strip().split("\n")
        task = None
        for line in lines:
            match = re.search(r"baseActivity=\{([^}]+)\}", line)
            if match:
                task = match.group()
                task = task.replace("baseActivity={", "").replace("}", "").replace(" ",'')
                print(task)
                task = task.split("/")[0]
                subprocess.run(["adb", "shell", "am", "force-stop", task])
                break
        else:
            print("Not found any activies")
            return
        print(task)

    import time

    def call(self, instance):
        os.chdir('C:\\platform-tools_r34.0.5-windows\\platform-tools')
        # Open the dialer app
        subprocess.Popen(["adb" ,"shell", "am" ,"start" ,'-a' ,'android.intent.action.CALL' ,'-d' ,'tel:+919535431916'])

        time.sleep(30)

        # Hang up the call
        subprocess.Popen(["adb", "shell", "input", "keyevent", '6'])

        print('end')

if __name__ == '__main__':
    MyApp().run()