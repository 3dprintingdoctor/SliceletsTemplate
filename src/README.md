# Windows: put slicer path in the path enviroment
* run by: 
  * command line: slicer --no-main-window --python-script path/to/template.py
  * double click: 
    * copy template.bat and template.py to a folder.
    * right click SEEG.bat, select 'send to', 'desktop'
    * go to desktop, right click 'template.bat - Shortcut', 'properties', change run to 'minimized'

# Mac: put slicer path(/Applications/Slicer.app/Contents/MacOS) in the PATH enviroment
* run by:
  * command line: Slicer --no-main-window --python-script path/to/template.py
  * double click: 
    * copy template.sh and template.py to a folder.
    * In finder, right click SEEG.sh, select "Open with" and then "Other...", select 'Terminal'. 
       (To be able to select terminal you need to switch from "Recommended Applications" to "All Applications".)
    * create an alias of template.sh, and drag it to the desktop.
