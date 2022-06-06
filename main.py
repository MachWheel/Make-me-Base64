import PySimpleGUI as sg
import os

import _txt
import _view
import _app


def main():
    view = _view.VIEW()
    view['-BATCH_FRAME-'].hide_row()
    while True:
        event, values = view.read(timeout=10)

        if event == sg.WIN_CLOSED:
            return

        validate_input(view, values)

        if event == '-BATCH_MODE-':
            enable_batch(view)

        if event == '-SINGLE_MODE-':
            enable_single(view)

        if event == '-SINGLE_START-':
            run_single(view, values)

        if event == '-BATCH_START-':
            view.hide()
            folder, images = read_folder(view, values)
            if not images:
                continue
            run_batch(folder, images)
            view.un_hide()

def validate_input(view, values):
    file_selected = os.path.isfile(values['-FILE_IN-'])
    folder_selected = os.path.isdir(values['-FOLDER_IN-'])
    view['-SINGLE_START-'].update(disabled=not file_selected)
    view['-BATCH_START-'].update(disabled=not folder_selected)

def enable_batch(view):
    view['-SINGLE_FRAME-'].hide_row()
    view['-BATCH_FRAME-'].unhide_row()

def enable_single(view):
    view['-BATCH_FRAME-'].hide_row()
    view['-SINGLE_FRAME-'].unhide_row()

def read_folder(view, values):
    folder = values['-FOLDER_IN-']
    images = _app.read_images(folder)
    if not images:
        _view.MESSAGE(_txt.NO_IMGS)
        view.un_hide()
        return None, None
    return folder, images

def run_single(view, values):
    view.hide()
    file = values['-FILE_IN-']
    encoded = _app.get_base64(file)
    sg.clipboard_set(encoded)
    _view.MESSAGE(_txt.COPIED)
    view.un_hide()

def run_batch(folder, images):
    contents = []
    loaded = len(images)
    for n, img in enumerate(images):
        encoded = _app.get_base64(img, folder)
        name = _app.clean_file_name(img)
        line = f'{name} = {encoded}\n\n'
        contents.append(line)
        _view.PROGRESS(n, loaded)
    _app.write_contents(folder, contents)
    _view.MESSAGE(_txt.GENERATED % len(images))
    os.startfile(folder)

if __name__ == '__main__':
    sg.theme('DarkBlue1')
    main()
