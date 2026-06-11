from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

from jnius import autoclass

PythonActivity = autoclass('org.kivy.android.PythonActivity')
Context = autoclass('android.content.Context')
IntentFilter = autoclass('android.content.IntentFilter')
BatteryManager = autoclass('android.os.BatteryManager')


class BatteryLayout(BoxLayout):

    def update_battery(self, *args):
        activity = PythonActivity.mActivity
        intent = activity.registerReceiver(
            None,
            IntentFilter("android.intent.action.BATTERY_CHANGED")
        )

        level = intent.getIntExtra(BatteryManager.EXTRA_LEVEL, -1)
        temp = intent.getIntExtra(BatteryManager.EXTRA_TEMPERATURE, 0) / 10.0
        voltage = intent.getIntExtra(BatteryManager.EXTRA_VOLTAGE, 0)

        self.ids.level_label.text = f"Niveau : {level}%"
        self.ids.temp_label.text = f"Température : {temp} °C"
        self.ids.voltage_label.text = f"Voltage : {voltage} mV"

        if level >= 80:
            conseil = "Batterie excellente"
        elif level >= 50:
            conseil = "Batterie normale"
        elif level >= 20:
            conseil = "Activer économie batterie"
        else:
            conseil = "Recharge urgente"

        self.ids.conseil_label.text = conseil


class BatteryAIApp(App):
def build(self):
layout = BatteryLayout()

    self.title = "Battery AI"

    layout.ids.level_label.text = "Niveau : Test"
    layout.ids.temp_label.text = "Température : Test"
    layout.ids.voltage_label.text = "Voltage : Test"
    layout.ids.conseil_label.text = "Application Kivy OK"

    return layout


if __name__ == "__main__":
    BatteryAIApp().run()
