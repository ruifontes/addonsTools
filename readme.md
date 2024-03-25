# Tools for managing add-ons


## Information
* Authors: Rui Fontes <rui.fontes@tiflotecnia.com>, Angelo Abrantes <ampa4374@gmail.com> and Abel Passos Jr. <abel.passos@gmail.com>"
* Download [stable version][1]
* Compatibility: NVDA version 2021.1 and beyond


## General info
This addon provides some tools to manage add-ons not present in the NVDA add-ons store.
To access the features open the main dialog of the add-on, through the NVDA/Tools menu or a command previously defined in "Input gestures" dialog.

In the main dialog you will find the list of tools:
* Add-on packager: To create a add-on backup file or to send a modified add-on to someone test or use;
* Multiple installer: Allows to select add-ons from a folder and install all at once;
* Make/restore Backups: Allow to backup and restore some NVDA preferences, such as configurations, profiles and dictionaries;
* Add-ons documentation: allow to open the documentation file.

To access the features of a tool press "Tab".
Follows a brief description of each tool.


### Add-on packager
In this section you will find a checkable list of all add-ons installed.
You can check the add-ons you want to package for backup or to send someone to test or use.
After checking the add-ons you want, press "Tab". You will find a "Selection" button allowing to select or unselect all.
When finished, press "Tab" to the "Generate" button and press "Enter".
You will be prompted to choose the folder where you want the add-on to be saved.
A dialog with the progress of the task is presented. When finished press "Accept" or "Close".


###Multiple installer
In this section you will find a "Select a folder with add-ons to install..." button.
Press it to select the folder where you have the add-on files wanting to install.
The folder is inspected to find all the possible add-ons to install. Incompatible add-ons, or with some error, are excluded of the list to install and shown in a message.
A list will be presented to choose the add-ons to install. After selection, press "Install".


### Make/restore Backups
Selecting this toll you will find a list of the possible elements to backup/restore.
Check the ones you want and select "Create a backup" or "Restore backup".
If you choose to create a backup you should say where it will be saved.
If you choose to restore, you must select the folder where it is saved and select the desired file.
After finishing the results of the operation are shown in a dialog.


### Add-ons documentation
Finally, here you will find the list of the installed add-ons with documentation.
Select the one you want to read the documentation and press the "Open add-on documentation" button.


## Commands
The two features available are opening the main dialog and kill the NVDA process in case of NVDA gets stuck.
Both do not have assigned commands.
You can assign/modify in the "Input gestures" dialog in the "Add-ons tools" section.

[1]: https://github.com/ruifontes/addonsTools/releases/download/2024.03.25/addonsTools-2024.03.25.nvda-addon
