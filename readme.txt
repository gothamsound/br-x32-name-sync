---------------------------
Boom Recorder/X32 Name Sync
v1.1
---------------------------


------------
Description:
------------

This Applescript continually synchronizes track names from Boom Recorder to a networked Behringer X32 mixer. Editing a track name in Boom Recorder should be reflected in real-time on the X32.


------
Usage:
------

To use, you will initially need to make some edits to the .plist file: 


- The IP address field should be overwritten with the IP of your X32. 

- The Track Count field represents the amount of tracks (starting from the first one, going sequentially) you want to sync from Boom Recorder. This will likely be the same as your track count in Boom Recorder.

- The Directory address only needs to be changed if you extract the br-x32 folder to anywhere other than the desktop. This value is crucial to directing the Python script to the proper folder, so it can then read the IP address from the .plist file.


Additionally, the Python script that handles OSC commands requires a library not installed on OSX by default. This library can be installed manually (search for "pyOSC") or automated using the "install_libraries" Applescript included.


------
Fixes:
------

	v1.1
	- Improved character handling. Bad characters are defined in the script and replaced with an underscore.


-----------
Known Bugs:
-----------


--------
Credits:
--------
Open SoundControl for Python
Copyright (C) 2002 Daniel Holth, Clinton McChesney


Will Colding
Gotham Sound and Communications
willc@gothamsound.com
2/18/16