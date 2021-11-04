VERSION = "v0.0.1-a"

import os
import time

from tile import *

import tkinter
from tkinter import Tk

from file import FileStat
from gitutil import GitWorkspace, git_diff, git_difftool

#

frepo = FileStat("~/repo")

tk_root = Tk()

mainframe = Tile(tk_root=tk_root, idn="mainframe")


main = TileTab(
    idn="maintabs",
    source=[
        (
            "settings",
            TileRows(
                source=[
                    TileLabel(caption=""),
                    TileDirectorySelect(
                        caption="select workspace",
                        commandtext="...",
                        idn="workspace",
                        path=frepo.name,
                    ),
                ]
            ),
        ),
        (
            "tracked git's",
            TileRows(
                source=[
                    TileLabel(caption=""),
                    TileEntryListbox(
                        caption="",
                        idn="gits",
                        max_show=15,
                        width=40,
                        select_many=True,
                        map_value=lambda x: os.path.basename(x),
                        on_sel=lambda x: set_tracked_gits(),
                    ),
                    TileCols(
                        source=[
                            TileLabelButton(
                                caption="workspace",
                                commandtext="refresh",
                                command=lambda: set_workspace(),
                            ),
                            TileLabelButton(
                                caption="all",
                                commandtext="select",
                                command=lambda: on_sel_all_gits(),
                            ),
                            TileLabelButton(
                                caption="",
                                commandtext="un-select",
                                command=lambda: on_unsel_all_gits(),
                            ),
                        ]
                    ),
                    TileCols(
                        source=[
                            TileLabelButton(
                                caption="pull",
                                commandtext="selected",
                                idn="pull_selected_workspace",
                            ),
                            TileLabelButton(
                                caption="", commandtext="all", idn="pull_all_workspace"
                            ),
                        ]
                    ),
                ]
            ),
        ),
        (
            "changes",
            TileRows(
                source=[
                    TileLabel(caption=""),
                    TileTreeView(
                        caption="",
                        idn="changes",
                        header=[
                            ("git", None),
                            ("file", None),
                            ("state", None),
                            ("type", None),
                        ],
                    ),
                    TileLabelButton(
                        caption="",
                        commandtext="refresh",
                        command=lambda: set_changes(),
                    ),
                    TileCols(
                        source=[
                            TileLabelButton(
                                caption="selected",
                                commandtext="add",
                            ),
                            TileLabelButton(
                                caption="",
                                commandtext="unstage",
                            ),
                            TileLabelButton(
                                caption="",
                                commandtext="diff",
                                command=lambda: on_diff(),
                            ),
                            TileLabelButton(
                                caption="",
                                commandtext="difftool",
                                command=lambda: on_difftool(),
                            ),
                            TileLabelButton(
                                caption="all",
                                commandtext="select",
                                command=lambda: gt("changes").set_selection(-1),
                            ),
                            TileLabelButton(
                                caption="",
                                commandtext="unselect",
                                command=lambda: gt("changes").clr_selection(),
                            ),
                        ]
                    ),
                ]
            ),
        ),
        (
            "commit",
            TileRows(
                source=[
                    TileLabel(caption=""),
                    TileEntry(caption="", idn="commit_short", width=40),
                    TileEntryText(caption="", idn="commit_long", height=10),
                    TileLabelButton(
                        caption="",
                        commandtext="commit",
                        idn="commit_workspace",
                    ),
                ]
            ),
        ),
        (
            "tag",
            TileRows(
                source=[
                    TileLabel(caption=""),
                    TileEntryButton(
                        caption="new tag name",
                        commandtext="tag",
                        idn="tag_workspace",
                    ),
                ]
            ),
        ),
        (
            "log",
            TileRows(
                source=[
                    TileLabel(caption=""),
                    TileEntryText(
                        caption="", idn="log", height=20, width=80, readonly=True
                    ),
                    TileCols(
                        source=[
                            TileLabelButton(
                                caption="",
                                commandtext="clear",
                                command=lambda: on_log_clr(),
                            ),
                            TileCheckbutton(caption="follow log", idn="follow"),
                        ]
                    ),
                ]
            ),
        ),
    ],
)


def quit_all(frame):
    def quit():
        print("quit_all")
        # removes all, including threads
        # sys.exit()
        # soft, state remains
        # download_stop()
        frame.quit()

    return quit


def minimize():
    print("minimize")
    tk_root.iconify()


url_homepage = "https://github.com/kr-g/pygitonic"


def open_homepage():
    import webbrowser

    webbrowser.get().open(url_homepage, new=0)


main_content = TileRows(
    source=[
        TileCols(
            source=[
                TileLabelButton(
                    caption="close app", commandtext="bye", command=quit_all(mainframe)
                ),
                TileLabelButton(caption="", commandtext="minimize", command=minimize),
            ]
        ),
        main,
        TileCols(
            source=[
                TileLabelClick(
                    caption=f"gitonic - {url_homepage}",
                    on_click=open_homepage,
                ),
                TileLabel(
                    caption=f"version: {VERSION}",
                ),
            ]
        ),
    ]
)

mainframe.tk.protocol("WM_DELETE_WINDOW", quit_all(mainframe))
mainframe.tk.bind("<Escape>", lambda e: minimize())

mainframe.title("gitonic")
mainframe.resize_grip()

mainframe.add(main_content)
mainframe.layout()

# gui handling


def on_sel_all_gits():
    print("on_sel_all_gits")
    gt("gits").set_selection(-1)
    set_tracked_gits()


def on_unsel_all_gits():
    print("on_sel_all_gits")
    gt("gits").clr_selection()
    set_tracked_gits()


def on_diff():
    print("on_diff")
    sel = gt("changes").get_selection_values()
    for rec in sel:
        if rec["type"] == "file":
            pg = FileStat(gws.base_repo_dir.name).join([rec["git"]]).name
            git = gws.find(pg)[0]
            rc = git_diff(git.path, rec["file"])
            print(f"--- {git}")
            [print(x) for x in rc]
            do_log_time("on_diff")
            do_logs(rc)


def on_difftool():
    print("on_difftool")
    sel = gt("changes").get_selection_values()
    for rec in sel:
        if rec["type"] == "file":
            pg = FileStat(gws.base_repo_dir.name).join([rec["git"]]).name
            git = gws.find(pg)[0]
            rc = git_difftool(git.path, rec["file"])
            print(f"--- {git}")
            [print(x) for x in rc]
            do_log_time("on_difftool")
            do_logs(rc)


def on_log_clr():
    print("on_log_clr")
    gt("log").clr()


def on_follow_log():
    if int(gt("follow").get_val()) > 0:
        gt("log").gotoline()


def do_log_time(x):
    print("do_log_time", x)
    log = gt("log")
    ts = time.asctime(time.localtime(time.time()))
    log.append(f"\n\n\n--- {x} --- {ts}")
    on_follow_log()


def do_log(x):
    print("do_log", x)
    gt("log").append(x)
    on_follow_log()


def do_logs(x):
    print("do_logs", x)
    gt("log").extend(x)
    on_follow_log()


# init


def set_workspace(update=True):
    print("refresh_workspace")
    global gws
    gws = GitWorkspace(frepo.name)
    gws.refresh()
    gt("gits").set_values(sorted(gws.gits.keys()))
    print("gws", gws)
    # gws.refresh_status()
    if update:
        set_tracked_gits()


def set_tracked_gits(update=True):
    print("set_tracked_gits")
    global tracked_gits
    tracked_gits = gt("gits").get_selection_values()
    tracked_gits = list(map(lambda x: x[1], tracked_gits))
    print("tracked_gits", tracked_gits)
    if update:
        set_changes()


set_workspace(False)
set_tracked_gits(False)


def set_changes():
    print("set_changes")
    global changes
    changes = []

    gits = list(map(lambda x: (x, gws.find(x)[0]), tracked_gits))
    print(gits)

    for path, git in gits:
        rnam = FileStat(path).basename()
        git.refresh_status()
        if len(git.status) > 0:
            for stat in git.status:
                fs = git.stat(stat)
                gst = {
                    "git": rnam,
                    "file": stat.file,
                    "state": stat.mode,
                    "type": ("file" if fs.is_file() else "dir"),
                }
                changes.append(gst)
    gt("changes").set_values(changes)


set_changes()
if len(changes) > 0:
    gt("maintabs").select("tab_changes")

gt("follow").set_val(1)

# end-of init

print(tk_root.geometry())
print(tk_root.winfo_reqwidth(), tk_root.winfo_reqheight())

mainframe.mainloop()
