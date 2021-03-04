import lvgl as lv
from gui.screens.screen import Screen
from gui.common import add_label, add_button_pair
from gui.decorators import on_release, cb_with_args




class DiceRollScreen(Screen):
    def __init__(
        self, title, message, note=None
    ):
        super().__init__()
        self.title = add_label(title, scr=self, style="title")
        obj = self.title
        if note is not None:
            self.note = add_label(note, scr=self, style="hint")
            self.note.align(self.title, lv.ALIGN.OUT_BOTTOM_MID, 0, 5)
            obj = self.note
        self.page = lv.page(self)
        self.page.set_size(480, 600)
        self.message = add_label(message, scr=self.page)
        self.page.align(obj, lv.ALIGN.OUT_BOTTOM_MID, 0, 0)

        (self.close_button, self.again_button) = add_button_pair(
            lv.SYMBOL.LEFT + " Back",
            on_release(cb_with_args(self.set_value, False)),
            "Roll again",
            on_release(cb_with_args(self.set_value, True)),
            scr=self,
        )
