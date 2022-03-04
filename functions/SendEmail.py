import pyautogui
import time


class SendEmail:

    @staticmethod
    def click_button_send(position_mouse_x, position_mouse_y):
        pyautogui.click(position_mouse_x, position_mouse_y)

    @staticmethod
    def send_email(address_email, title_email, body_email):
        time.sleep(2)
        typo_time = 0.05
        pyautogui.typewrite(address_email)
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.typewrite(title_email)
        pyautogui.press('tab')
        pyautogui.typewrite(body_email)
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'enter')
        time.sleep(1)
