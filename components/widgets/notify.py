from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.clock import Clock


class Notify(ModalView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Saved", color="green"))
        self.size_hint = (None, None)
        self.width = "100dp"
        self.height = "60dp"
        self.pos_hint = {'center_x': .5, 'center_y': .95}
        self.overlay_color = (0, 0, 0, 0)

        self.open()
        Clock.schedule_once(self._dismiss, 1)

    def _dismiss(self, args):
        self.dismiss()
