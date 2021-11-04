window (new|open): app.window_open()
window next: app.window_next()
window last: app.window_previous()
window close: app.window_close()
focus <user.running_applications> [<phrase>]$:
    user.switcher_focus(running_applications)
    sleep(200ms)
    user.parse_phrase(phrase or "")
running list: user.switcher_toggle_running()
launch <user.launch_applications>: user.switcher_launch(launch_applications)

snap <user.window_snap_position>: user.snap_window(window_snap_position)
snap next [screen]: user.move_window_next_screen()
snap last [screen]: user.move_window_previous_screen()
snap screen <number>: user.move_window_to_screen(number)
snap <user.running_applications> <user.window_snap_position>:
    user.snap_app(running_applications, window_snap_position)
snap <user.running_applications> [screen] <number>:
    user.move_app_to_screen(running_applications, number)
portal [<phrase>]$:
    user.switcher_focus("Google Chrome")
    sleep(200ms)
    user.parse_phrase(phrase or "")
coder [<phrase>]$:
    user.switcher_focus("Code")
    sleep(200ms)
    user.parse_phrase(phrase or "")
change set up [<phrase>]$:
    user.switcher_focus("Code")
    user.vscode("workbench.action.openRecent")
    sleep(50ms)
    insert("pokey-talon")
    key(enter)
    sleep(250ms)
    user.parse_phrase(phrase or "")
slacker [<phrase>]$:
    user.switcher_focus("Slack")
    sleep(200ms)
    user.parse_phrase(phrase or "")
folk things [<phrase>]$:
    user.switcher_focus("Things")
    sleep(200ms)
    user.parse_phrase(phrase or "")
folk sim [<phrase>]$:
    user.switcher_focus("Simulator")
    sleep(200ms)
    user.parse_phrase(phrase or "")