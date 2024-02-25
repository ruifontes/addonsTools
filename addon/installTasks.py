#Install tasks for addonsTools addon
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2024 Rui Fontes <rui.fontes@tiflotecnia.com>

# Import the necessary modules
import addonHandler
import gui
import wx

# Start translation process
addonHandler.initTranslation()


def onInstall():
	for addon in addonHandler.getAvailableAddons():
		if addon.name == "addonPackager" and not addon.isDisabled:
			# Translators: Message asking user to remove an old add-on.
			gui.messageBox(				_("You have installed a version of the {} add-on.\nAs its functionalities are replaced by this add-on and by add-ons store, we strongly recommend you to remove or, at least, disable it!").format(addon.manifest["summary"]),
			# Translators: Label of a message asking user to remove an old add-on.
				_("Warning!"), style=wx.OK | wx.ICON_WARNING)
