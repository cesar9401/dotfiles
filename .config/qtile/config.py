# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# my imports
from settings.theme import load_theme
# my imports

import os

mod = "mod4"
mod1 = "mod1"
# terminal = guess_terminal()
terminal = "kitty"

theme = load_theme()

# ------------------ function base
def base(fg="text", bg="dark"):
	return {
		"foreground": theme[fg],
		"background": theme[bg]
	}
# ------------------ function base

# ------------------ function separator
def separator():
	return widget.Sep(**base(), linewidth=0, padding=5)
# ------------------ function separator

# ------------------ function powerline
def powerline(fg="light", bg="dark"):
	return widget.TextBox(**base(fg, bg), text=" ", fontsize=40, padding=-13)
# ------------------ function powerline

# --------------------- BAR
def getBar():
	return bar.Bar(
        [
            # widget.CurrentScreen(active_color=color, inactive_color="#B3B6B7"),
			widget.TextBox(text="", foreground="#1793d1", background=theme["dark"], fontsize=20, padding=5),
            widget.CurrentLayout(**base(fg="light")),
			separator(),
            widget.GroupBox(
				**base(fg="light"),
				# font='FiraCode Nerd Font Mono',
				fontsize=28,
				borderwidth = 1,
                active = theme["active"],
                inactive = theme["inactive"],
				highlight_method="block",
				rounded=False,
				urgent_alert_method='block',
				urgent_border=theme["urgent"],
                this_current_screen_border = theme["focus"],
                this_screen_border = theme["grey"],
                other_current_screen_border = theme["dark"],
                other_screen_border = theme["dark"],
				disable_drag=True
            ),
            # widget.Prompt(), # se quita por usar dmenu
            # widget.WindowName(foreground=color),
			separator(),
            widget.TaskList(visible_on=["treetab"], max_title_width=130, border=theme["active"], **base(fg="light")),
			powerline("color4", "dark"),
			icon(fg="dark", bg="color4", text=""),
			widget.KeyboardLayout(background=theme["color4"], configured_keyboards=["us -variant altgr-intl", "us", "latam"], update_interval=1),
			powerline("color3", "color4"),
			icon(fg="dark", bg="color3", text="墳"),
			widget.PulseVolume(**base(bg="color3"), scroll_delay=1),
			powerline("color2", "color3"),
			widget.Systray(**base(bg="color2")),
			powerline("color1", "color2"),
			icon(fg="dark", bg="color1", text=""),
			widget.Clock(format='%Y-%m-%d %a %I:%M %p', **base(bg="color1")),
			powerline("dark", "color1"),
			icon(fg="active", bg="dark", text=""),
			widget.QuickExit(**base(fg="light")),
        ],
        28,
        # background=colors[0],
        opacity=1,
        margin=1
    )
# --------------------- BAR

# --------------------- ICONS
def icon(fg="text", bg="dark", fontsize=17, padding=0, text="?"):
	return widget.TextBox(**base(fg, bg), fontsize=fontsize, padding=padding, text=text)
# --------------------- ICONS

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.run_extension(extension.DmenuRun(
            background="#222222",
            selected_background=theme["active"],
            foreground=theme["active"],
            selected_foreground="#ffffff"
        )),
        desc="Spawn a command using a prompt widget"),

    # Switch keyboard layout
    Key(["shift", "control"], "u", lazy.spawn("setxkbmap us"), desc="keyboard layout to english"),
    Key(["shift", "control"], "i", lazy.spawn("setxkbmap -layout us -variant altgr-intl"), desc="keybaord layout to english international"),
    Key(["shift", "control"], "l", lazy.spawn("setxkbmap latam"), desc="keybaord layout to latam"),

    # Volume
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q sset Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q sset Master 5%+")),

    # Music Player
    Key([], "XF86AudioPlay", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause")),
    Key([], "XF86AudioNext", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next")),
    Key([], "XF86AudioPrev", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous")),

    # Stop - just with extra keyboard
    Key([], "XF86AudioStop", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Stop")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # Menu
    # Key([mod], "m", lazy.spawn("rofi -show drun")),
    Key([mod], "m", lazy.spawn("launcher_colorful")),

    # menu_powermenu
    # win + alt + f4
    # Key([mod], "F4", lazy.spawn("menu_powermenu")),

    # window nav
    # Key([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser - google-chrome
    Key([mod], "b", lazy.spawn("brave")),

    # File Explorer
    Key([mod], "f", lazy.spawn("pcmanfm")),

    # File Explorer on ~/Downloads
    Key([mod], "d", lazy.spawn("pcmanfm -n Downloads")),

    # gnome-control-center
    Key([mod], "g", lazy.spawn("gnome-control-center")),

    # pavucontrol - audio
    Key([mod], "p", lazy.spawn("pavucontrol")),
]

groups = [Group(i) for i in [
    "", "", "", "", "", "", "", "", "",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

# groups = [Group(i) for i in "1234567890"]

# for i in groups:
#     keys.extend([
#         # mod1 + letter of group = switch to group
#         Key([mod], i.name, lazy.group[i.name].toscreen(),
#             desc="Switch to group {}".format(i.name)),

#         # mod1 + shift + letter of group = switch to & move focused window to group
#         Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
#             desc="Switch to & move focused window to group {}".format(i.name)),
#         # Or, use below if you prefer not to switch to that group.
#         # # mod1 + shift + letter of group = move focused window to group
#         # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#         #     desc="move focused window to group {}".format(i.name)),
#     ])

layouts = [
    # layout.Floating(),
    layout.Max(
        margin=1,
        border_width=1,
        border_focus=theme["active"]
    ),
    layout.Columns(
        border_focus=theme["active"],
        border_focus_stack=theme["active"],
        border_normal=theme["dark"],
        border_normal_stack=theme["dark"],
        margin=1,
        border_width=3,
        insert_position=0,
        split=False
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(
        # num_stacks=1,
        # border_width=1,
        # single_border_width=1,
        # border_focus=theme["active"],
        # margin=1,
        # border_normal="#222222"
    # ),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        border_width=3,
        border_focus=theme["active"],
        single_border_width=1,
        margin=1,
        border_normal=theme["dark"],
        change_size=10
    ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(
    #    active_bg=theme["active"],
    #    active_fg=theme["grey"],
    #    bg_color=theme["dark"],
    #    border_width=3,
    #    inactive_bg=theme["inactive"],
    #    inactive_fg=theme["light"],
    #    section_fg=theme["text"],
    #    font="Ubuntu Nerd Font Bold",
    #    panel_width=200,
    #    fontsize=15,
    #    previous_on_rm=True,
    #    urgent_bg=theme["urgent"],
    #    urgent_fg=theme["light"]
    # ),
    # layout.VerticalTile(),
    # layout.Zoomy(columnwidth=200, margin=1),
]

widget_defaults = dict(
	# font='Roboto',
    font="Ubuntu Nerd Font Bold",
    # font='FiraCode Nerd Font Mono',
    fontsize=17,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=getBar(),
    ),
    Screen(
        top=getBar(),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# my config
autostart = [
    # samsung left, laptop right
    # "xrandr --output eDP1 --primary --mode 1366x768 --pos 1920x156 --rotate normal --output DP1 --mode 1920x1080 --pos 0x0 --rotate normal --output HDMI1 --off --output VIRTUAL1 --off",
    # samsung(primary) up, laptop down
    # "xrandr --output eDP1 --mode 1366x768 --pos 277x1080 --rotate normal --output DP1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output HDMI1 --off --output VIRTUAL1 --off",
    # samsung(primary) right, laptop left
    "xrandr --output eDP1 --mode 1366x768 --pos 0x156 --rotate normal --output DP1 --primary --mode 1920x1080 --pos 1366x0 --rotate normal --output HDMI1 --off --output VIRTUAL1 --off",
    # "setxkbmap us",
    "setxkbmap -layout us -variant altgr-intl",
    # "setxkbmap latam",
    "feh --bg-fill ~/Pictures/wallhaven/wallhaven-5wl3z8.png",
    "picom &",
    "nm-applet &",
    # "blueman-applet &",
    "touchpad-indicator &",
	"screencloud &",
    # "udiskie -t &",
    # "volumeicon &",
    # "cbatticon &",
]

for x in autostart:
    os.system(x)
