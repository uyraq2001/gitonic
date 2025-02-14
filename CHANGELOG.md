 
# Changelog


## version v0.0.16 - ???

- support for multiple repo workspaces
  - on `settings` tab the `workspaces` entry field accepts a 
    list of paths separated by `;`
  - use `~` for user-home path 
  - blanks between `;` separated paths are ignored
  - when using double or single quotes around paths make sure the `;` exists to separate paths
  - blanks at the start or end of paths are not supported
- added `$PYTHON` to context menu variables
- added clear message after commit select box
- added keyboard interrupt cntrl+c handler
- added `workdir` key for context menu handlers
- 


## version v0.0.15 - 20240812

- fix: blank in path will show file as deleted
- fix: rename file with git
- 


## version v0.0.14 - 20240518

- improved formatter 
  - support for multiple file extension for single config entry 
  - support for path expansion for formatter config
  - added sample for uncrustify (c, c++)
- on "changes" tab
  - added context menu to open file system explorer
  - added support for custom context menu with `~/.gitonic/context.json`
- calling merge-tool with more then more file selected on change tab will 
 not block the user-interface anymore since starting independent from main process
  - **important** add `--newtab` to `meld` configuration in `.gitconfig` 
   to re-use an already running instance of `meld`
- context menu handler expands user path (`~`)
- 


## version v0.0.13 - 20231125

- show all untracked files on changes tab (not only the folder)
- 


## version v0.0.12 - 20231111

- support for more code formatters (included in standard installation as extras)
  - install with `pip install gitonic[PEP08]`
    - pycodestyle
    - autopep8
    - black
    - yapf 
- support for meld (included in standard installation as extra)
  - install with `pip install gitonic[MELD]`
- installation script (linux) for using within a virtual environment 
- added more installation options
- 


## version v0.0.11 - 20230710

- fixed logging
- fix no branch crash when no branch is set up 
- added fetch buttons
- double ESC will exit gitonic
- new hotkey Alt-c to go directly to commit tab
- added F5, F6 hotkeys for changing the active tabs
- custom formatter support
  - defined under settings `formatter.json`
-


## version v0.0.10 - 20230225

- sort files in changes tab
- 


## version v0.0.9 - 20221008

- git current branch in changes tab
- support for black
- 


## version v0.0.8 - 20220802

- bug fix, due to corrupted local env
- double click in changes view will stage/ unstage a file
- 


## version v0.0.7 - 20220729

- changes view height
- bug fix, due to corrupted local env
- bug fix, removed control-x hotkey
- 


## version v0.0.6 - 20220729

- fix save settings 
- set focus on commit entry after clearing fields
- expert (dev-mode) logging tab
- calling diff-tool will not switch to log tab
- icon support with 
  [`fontawesome`](https://github.com/FortAwesome/Font-Awesome)
  and 
  [`pytkfaicons`](https://github.com/kr-g/pytkfaicons)
- added tooltips
- added hotkeys
- BUG fix: search only in first level of workspace folder for git folder
- 


## version v0.0.5 - 20220515

- rework ui layout
- use subprocess popen to capture stdout, and stderr
- added "commit + push" button 
- 


## version v0.0.4 - 20211107

- fix find git repo in workspace (with similar starting letters)
- hopefully all childhood diseases are gone for now
- 


## version v0.0.3 - 20211107

- thonny-gitonic plugin support
- 


## pre version v0.0.2 - 20211106

- config parameter in config file
- workspace not fixed anymore to ~/repo
- refactored 
- commit history
- documentation in readme
- 


## pre version v0.0.1 - 20211106

- first version 
  - no yet released official 
  - 
-
