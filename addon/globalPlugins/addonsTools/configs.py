# -*- coding: utf-8 -*-
# Copyright (C) 2022 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Copyright (C) 2023-2024 Rui Fontes <rui.fontes@tiflotecnia.com>
# This file is covered by the GNU General Public License.

# Import the necessary modules
import globalVars
import os

dirConfig = globalVars.appArgs.configPath
dirDictionary = os.path.join(dirConfig, "speechDicts")
dirProfile = os.path.join(dirConfig, "profiles")
dirScratchpad = os.path.join(dirConfig, "scratchpad")
fileTrigger = os.path.join(dirConfig, "profileTriggers.ini")
fileGestures = os.path.join(dirConfig, "gestures.ini")
fileNVDA = os.path.join(dirConfig, "nvda.ini")
fileNVDABAK = os.path.join(dirConfig, "nvda.iniBAK")
listTempBackupID = []
dict_directories = {
	0: dirDictionary,
	1: dirProfile,
	2: dirScratchpad,
	3: fileTrigger,
	4: fileGestures,
	5: fileNVDA,
}
IS_WinON = False
restart = False
dictionaryMajor = {0:"2021", 1:"2022", 2:"2023", 3:"2024", 4:"2025", 5:"2026", 6:"2027", 7:"2028", 8:"2029", 9:"2030"}
major = ["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"]
dictionaryMinor = {0:"1", 1:"2", 2:"3", 3:"4"}
minor = ["1", "2", "3", "4"] 
revision = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
