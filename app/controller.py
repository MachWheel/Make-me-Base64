import os

import PySimpleGUI as sg

from . import txt, views, worker


class Controller:
    def __init__(self, view: sg.Window):
        self.view = view
        self.view['-BATCH_FRAME-'].hide_row()

    def read_events(self) -> str | None:
        event, values = self.view.read(timeout=10)

        if event == sg.WIN_CLOSED:
            return 'done'

        if event == '-BATCH_MODE-':
            self.enable_batch()

        if event == '-SINGLE_MODE-':
            self.enable_single()

        if event == '-SINGLE_START-':
            self.run_single(values)

        if event == '-BATCH_START-':
            self.view.hide()
            folder, images = self.read_folder(values)
            if not images:
                return
            run_batch(folder, images)
            self.view.un_hide()

        self.check_inputs(values)

    def enable_single(self) -> None:
        self.view['-BATCH_FRAME-'].hide_row()
        self.view['-SINGLE_FRAME-'].unhide_row()

    def enable_batch(self) -> None:
        self.view['-SINGLE_FRAME-'].hide_row()
        self.view['-BATCH_FRAME-'].unhide_row()

    def check_inputs(self, values: dict) -> None:
        file_selected = os.path.isfile(values['-FILE_IN-'])
        folder_selected = os.path.isdir(values['-FOLDER_IN-'])
        self.view['-SINGLE_START-'].update(disabled=not file_selected)
        self.view['-BATCH_START-'].update(disabled=not folder_selected)

    def read_folder(self, values: dict) -> tuple[str, list] | tuple[None, None]:
        folder = values['-FOLDER_IN-']
        images = worker.read_images(folder)
        if not images:
            views.MESSAGE(txt.NO_IMGS)
            self.view.un_hide()
            return None, None
        return folder, images

    def run_single(self, values: dict) -> None:
        self.view.hide()
        file = values['-FILE_IN-']
        encoded = worker.get_base64(file)
        sg.clipboard_set(encoded)
        views.MESSAGE(txt.COPIED)
        self.view.un_hide()


def run_batch(folder: str, images: list) -> None:
    contents = []
    loaded = len(images)
    for n, img in enumerate(images):
        encoded = worker.get_base64(img, folder)
        name = worker.clean_file_name(img)
        line = f'{name} = {encoded}\n\n'
        contents.append(line)
        views.PROGRESS(n, loaded)
    worker.write_contents(folder, contents)
    views.MESSAGE(txt.GENERATED % len(images))
    os.startfile(folder)
