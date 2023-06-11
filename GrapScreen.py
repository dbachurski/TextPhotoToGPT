from pynput import mouse
from pynput.mouse import Listener
import win32gui
import win32con
import threading
import pyscreenshot
import time


class GrapScreen:
    def __init__(self):
        self.start_pos = [0, 0]
        self.start_set = False
        self.XPOS = 0
        self.YPOS = 0
        self.mouse_button_pressed = False
        self.last_pos = []
        self.stop_thread = False
        self.ss_start_pos = []
        self.ss_end_pos = []
        self.file_name = 'ss.jpg'

    def take_screenshot(self, x1, y1, x2, y2):
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        pic = pyscreenshot.grab(bbox=(x1, y1, x2, y2))
        pic.save(self.file_name)

    def draw_rectangle(self, left, top, right, bottom):
        hdc = win32gui.GetDC(None)
        rect = (left, top, right, bottom)
        edge_style = win32con.BDR_RAISEDOUTER | win32con.BDR_SUNKENINNER
        flags = win32con.BF_RECT
        win32gui.DrawEdge(hdc, rect, edge_style, flags)
        win32gui.InvalidateRect(None, None, True)
        win32gui.ReleaseDC(None, hdc)

    def draw_rect_thread(self):
        while not self.stop_thread:
            if self.mouse_button_pressed:
                time.sleep(0.08)
                self.draw_rectangle(*self.start_pos, self.XPOS, self.YPOS)

    def on_move(self, x, y):
        self.XPOS = x
        self.YPOS = y
        if not self.start_set:
            self.start_pos = self.XPOS, self.YPOS
        if self.mouse_button_pressed:
            self.start_set = True

    def on_click(self, x, y, button, pressed):
        if pressed:
            if button == mouse.Button.right:
                self.stop_thread = True
                return False
            else:
                self.mouse_button_pressed = True
                self.ss_start_pos = [x, y]
        else:
            self.mouse_button_pressed = False
            self.ss_end_pos = [x, y]
            self.take_screenshot(*self.ss_start_pos, *self.ss_end_pos)
            self.stop_thread = True
            return False

    def start_listener(self):
        draw_thread = threading.Thread(target=self.draw_rect_thread, daemon=True)
        with Listener(on_move=self.on_move, on_click=self.on_click) as listener:
            draw_thread.start()
            listener.join()


grap = GrapScreen()

