import PySimpleGUI as sg

from . import txt

sg.theme('DarkBlue1')

def MAIN_VIEW() -> sg.Window:
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
        [sg.Text(txt.HEADING, font=txt.F14B)],
        [sg.VPush()],
        [modes_frame],
        [sg.VPush()],
        [single_frame],
        [batch_frame]
    ]
    return sg.Window(txt.APP_TITLE, layout, font=txt.F10B, icon=_LOGO(), finalize=True)


def PROGRESS(curr_val: int, max_val: int) -> sg.OneLineProgressMeter:
    return sg.OneLineProgressMeter(
        title='',
        current_value=curr_val + 1,
        max_value=max_val,
        key='-METER-',
        no_titlebar=True,
        orientation='h'
    )

def MSG_POPUP(msg: str) -> sg.Popup:
    return sg.popup(f'\n{msg}\n', font=txt.F12B, no_titlebar=True)

def _LOGO() -> bytes:
    return b'iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAC4jAAAuIwF4pT92AAAIiGlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNy4xLWMwMDAgNzkuYjBmOGJlOSwgMjAyMS8xMi8wOC0xOToxMToyMiAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdEV2dD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlRXZlbnQjIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyMy4yIChXaW5kb3dzKSIgeG1wOkNyZWF0ZURhdGU9IjIwMjItMDYtMDZUMjA6MjM6MzktMDM6MDAiIHhtcDpNZXRhZGF0YURhdGU9IjIwMjItMDYtMDZUMjA6MzI6NTktMDM6MDAiIHhtcDpNb2RpZnlEYXRlPSIyMDIyLTA2LTA2VDIwOjMyOjU5LTAzOjAwIiBkYzpmb3JtYXQ9ImltYWdlL3BuZyIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpiZjFmM2U0NS1kZTYwLWZhNDUtYjQwMS04ZjJkYzc1YTcyYTMiIHhtcE1NOkRvY3VtZW50SUQ9ImFkb2JlOmRvY2lkOnBob3Rvc2hvcDo5ODQ2NGRkMC1mYjYxLTNhNDctYjYwZi1lYzliMDNhZjQzMzEiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDo5NjczYzQ2Zi1hM2JlLWRjNDAtYTViNy0xM2Q2N2M2YTI0ZDEiIHBob3Rvc2hvcDpDb2xvck1vZGU9IjMiPiA8eG1wTU06SGlzdG9yeT4gPHJkZjpTZXE+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJjcmVhdGVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOjk2NzNjNDZmLWEzYmUtZGM0MC1hNWI3LTEzZDY3YzZhMjRkMSIgc3RFdnQ6d2hlbj0iMjAyMi0wNi0wNlQyMDoyMzozOS0wMzowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIDIzLjIgKFdpbmRvd3MpIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDo5MTUyMjdiMi03MWJjLTQ5NDMtOWEzMC0xMTdkNWFhZGEyN2MiIHN0RXZ0OndoZW49IjIwMjItMDYtMDZUMjA6MzI6NTktMDM6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCAyMy4yIChXaW5kb3dzKSIgc3RFdnQ6Y2hhbmdlZD0iLyIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0iY29udmVydGVkIiBzdEV2dDpwYXJhbWV0ZXJzPSJmcm9tIGFwcGxpY2F0aW9uL3ZuZC5hZG9iZS5waG90b3Nob3AgdG8gaW1hZ2UvcG5nIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJkZXJpdmVkIiBzdEV2dDpwYXJhbWV0ZXJzPSJjb252ZXJ0ZWQgZnJvbSBhcHBsaWNhdGlvbi92bmQuYWRvYmUucGhvdG9zaG9wIHRvIGltYWdlL3BuZyIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6YmYxZjNlNDUtZGU2MC1m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'
