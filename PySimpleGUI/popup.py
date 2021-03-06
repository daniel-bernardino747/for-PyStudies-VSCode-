import PySimpleGUI as sg

"""sg.popup_ok('popup_ok')  # Shows OK button
sg.popup('popup')  # Shows OK button
sg.popup_yes_no('popup_yes_no')  # Shows Yes and No buttons
sg.popup_cancel('popup_cancel')  # Shows Cancelled button
sg.popup_ok_cancel('popup_ok_cancel')  # Shows OK and Cancel buttons
sg.popup_error('popup_error')  # Shows red error button
sg.popup_timed('popup_timed')  # Automatically closes
sg.popup_auto_close('popup_auto_close')  # Same as PopupTimed
sg.popup_scrolled('oi\n\n\n\noi')"""

password = sg.popup_get_text(
    'Digite sua senha abaixo:', 
    title='Login', 
    password_char='*'
    )

sg.popup(
    'O que foi digitado na tela anterior: ', 
    password, 
    title='Senha'
    )
