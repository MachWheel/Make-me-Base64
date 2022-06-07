import importlib.util
import os

import PySimpleGUI as sg

import app


def close_splash() -> None:
    if '_PYIBoot_SPLASH' in os.environ:
        if not importlib.util.find_spec("pyi_splash"):
            return
        import pyi_splash
        pyi_splash.close()

def main(application: app.Controller) -> None:
    state = ''
    while state != 'done':
        state = application.read_events()
    return

if __name__ == '__main__':
    close_splash()
    sg.theme('DarkBlue1')
    view = app.MAIN_VIEW()
    controller = app.Controller(view)
    main(controller)
