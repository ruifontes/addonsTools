# -*- coding: utf-8 -*-
# Copyright (C) 2022 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Copyright (C) 2023-2024 Rui Fontes <rui.fontes@tiflotecnia.com>
# This file is covered by the GNU General Public License.

# Import the necessary modules
import globalPluginHandler
import addonHandler
import globalVars
import gui
import ui
import core
from scriptHandler import script
import wx
from threading import Thread
import os
import sys
from . import configs
from . import main
from .kill import kill_process_by_name

# Start the translation process
addonHandler.initTranslation()

def disableInSecureMode(decoratedCls):
	if globalVars.appArgs.secure:
		return globalPluginHandler.GlobalPlugin
	return decoratedCls

@disableInSecureMode
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()

		if hasattr(globalVars, "addonPackager"):
			self.postStartupHandler()
		core.postNvdaStartup.register(self.postStartupHandler)
		globalVars.addonPackager = None

	def postStartupHandler(self):
		self.toolsMenu = gui.mainFrame.sysTrayIcon.toolsMenu
		self.menuItem = self.toolsMenu.Append(wx.ID_ANY, _("&Add-ons tools"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.menuApp, self.menuItem)

	def terminate(self):
		try:
			self.toolsMenu.Remove(self.menuItem)
		except Exception:
			pass

		try:
			core.postNvdaStartup.unregister(self.postStartupHandler)
		except (AttributeError, RuntimeError):
			pass
		super().terminate()

	def runMsgRestart(self):
		message = wx.MessageDialog(None, 
			_("An action is pending a NVDA restart.")+"\n"+
			_("By security reasons, the add-on only can be used after restarting NVDA")+"\n"+
			_("Do you want to restart NVDA now?"),
			_("Question"), wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
		ret = message.ShowModal()
		if ret == wx.ID_YES:
			message.Destroy
			core.restart()
		else:
			message.Destroy
			configs.IS_WinON = False
			return

	@script(
		gesture=None,
		description= _("Shows Add-ons tools main window"),
		category= _("Add-ons tools"))
	def script_menuApp(self, event, menu=False):
		if configs.IS_WinON == False:
			if configs.restart == False:
				AddonFlow(self, 1).start()
			else:
				configs.IS_WinON = True
				wx.CallAfter(self.runMsgRestart)
		else:
				if menu:
					gui.messageBox(_("Already exist an instance of Add-ons Tools open."), _("Information"), wx.ICON_INFORMATION)
				else:
					ui.message(_("Already exist an instance of Add-ons Tools open."))

	def menuApp(self, event):
		wx.CallAfter(self.script_menuApp, None, True)

	@script(
		gesture=None,
		description= _("Close NVDA when it gets blocked"),
		category= _("Add-ons tools"))
	def script_kill(self, event):
		AddonFlow(None, 2).start()

class AddonFlow(Thread):
	def __init__(self, frame, opcion):
		super(AddonFlow, self).__init__()
		self.frame = frame
		self.opcion = opcion
		self.daemon = True

	def run(self):
		def appLauncherMain():
			self._main = main.MainWindow(gui.mainFrame, self.frame)
			gui.mainFrame.prePopup()
			self._main.Show()

		def killNVDA():
			kill_process_by_name("nvda.exe")

		if self.opcion == 1:
			wx.CallAfter(appLauncherMain)
		elif self.opcion == 2:
			wx.CallAfter(killNVDA)

