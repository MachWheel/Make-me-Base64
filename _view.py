import PySimpleGUI as sg

import _txt


def VIEW():
    modes_layout = [
        [sg.Radio(
            'Single file to clipboard', '_',
            default=True,
            key='-SINGLE_MODE-',
            enable_events=True
        ), sg.Radio(
            'Whole folder to "_output.py"', '_',
            default=False,
            key='-BATCH_MODE-',
            enable_events=True
        )]
    ]
    single_layout = [
        [sg.In(key='-FILE_IN-'), sg.FileBrowse()],
        [sg.Button('Copy to Clipboard', key='-SINGLE_START-')],
        [sg.VPush()]
    ]
    batch_layout = [
        [sg.In(key='-FOLDER_IN-'), sg.FolderBrowse()],
        [sg.Button('Export File', key='-BATCH_START-')],
        [sg.VPush()]
    ]
    modes_frame = sg.Frame(
        'Conversion mode',
        modes_layout, 
        relief=sg.RELIEF_RAISED
    )
    single_frame = sg.Frame(
        'Select a file',
        single_layout,
        key='-SINGLE_FRAME-', 
        element_justification='center', 
        relief=sg.RELIEF_RAISED
    )
    batch_frame = sg.Frame(
        'Select a folder',
        batch_layout,
        key='-BATCH_FRAME-',
        element_justification='center', 
        relief=sg.RELIEF_RAISED
    )
    layout = [
        [sg.Text(_txt.HEADING, font=_txt.F14B)],
        [sg.VPush()],
        [modes_frame],
        [sg.VPush()],
        [single_frame],
        [batch_frame]
    ]
    return sg.Window(_txt.APP_TITLE, layout, font=_txt.F10B, finalize=True)


def PROGRESS(curr_val, max_val):
    return sg.OneLineProgressMeter(
        title='',
        current_value=curr_val + 1,
        max_value=max_val,
        key='-METER-',
        no_titlebar=True,
        orientation='h'
    )


def MESSAGE(msg):
    return sg.popup(f'\n{msg}\n', font=_txt.F12B, no_titlebar=True)
