# -*- coding: utf-8 -*-
# Copyright (C) 2022 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Copyright (C) 2023-2024 Rui Fontes <rui.fontes@tiflotecnia.com>
# This file is covered by the GNU General Public License.

# Import the necessary modules
import addonHandler
import globalVars
import config
import gui
from gui.nvdaControls import CustomCheckListBox
import core
import winsound
import wx
import string
import os
import json
from . import utilities
from . import configs

# Start the translation process
addonHandler.initTranslation()

class MainWindow(wx.Dialog):
	def __init__(self, parent, frame):
		super(MainWindow, self).__init__(parent, -1)

		self.frame = frame

		configs.IS_WinON = True
		self.SetSize((1000, 800))
		self.SetTitle(_("Add-ons tools"))

		self.listAddons = list(addonHandler.getAvailableAddons())
		self.IS_Active = False
		self.restart = False
		self.installTempList = []
		self.enabledAddonsList = []
		self.disabledAddonsList = []
		self.dirDocumentation = []

		self.mainPanel = wx.Panel(self, wx.ID_ANY)

		sizer_main = wx.BoxSizer(wx.VERTICAL)

		# Translators: StaticText with instructions for the user:
		label_0 = wx.StaticText(self.mainPanel, wx.ID_ANY, _("Choose an tool and press Tab to access the options."))
		sizer_main.Add(label_0, 1, wx.EXPAND, 0)

		self.list = wx.Listbook(self.mainPanel, wx.ID_ANY)
		sizer_main.Add(self.list, 1, wx.EXPAND, 0)

		self.packager_panel = wx.Panel(self.list, wx.ID_ANY)
		self.list.AddPage(self.packager_panel, _("Add-ons packager"))

		sizerPackager = wx.BoxSizer(wx.VERTICAL)

		label_1 = wx.StaticText(self.packager_panel, wx.ID_ANY, _("&Add-ons list:"))
		sizerPackager.Add(label_1, 0, wx.EXPAND, 0)

		self.packager_listbox = CustomCheckListBox(self.packager_panel, wx.ID_ANY)
		sizerPackager.Add(self.packager_listbox, 1, wx.EXPAND, 0)

		sizerPackagerButtons = wx.BoxSizer(wx.HORIZONTAL)
		sizerPackager.Add(sizerPackagerButtons, 0, wx.EXPAND, 0)

		self.packageSelectionBTN = wx.Button(self.packager_panel, 101, _("&Selection"))
		sizerPackagerButtons.Add(self.packageSelectionBTN, 2, wx.CENTRE, 0)

		self.generatePackageBTN = wx.Button(self.packager_panel, 102, _("&Generate"))
		sizerPackagerButtons.Add(self.generatePackageBTN, 2, wx.CENTRE, 0)

		self.installer_panel = wx.Panel(self.list, wx.ID_ANY)
		self.list.AddPage(self.installer_panel, _("Multiple installer"))

		sizerInstaller = wx.BoxSizer(wx.VERTICAL)

		self.installersFolderBTN = wx.Button(self.installer_panel, 103, _("&Select a folder with add-ons to install..."))
		sizerInstaller.Add(self.installersFolderBTN, 0, wx.EXPAND, 0)

		label_3 = wx.StaticText(self.installer_panel, wx.ID_ANY, _("&Add-ons list:"))
		sizerInstaller.Add(label_3, 0, wx.EXPAND, 0)

		self.installers_listbox = CustomCheckListBox(self.installer_panel, wx.ID_ANY)
		sizerInstaller.Add(self.installers_listbox, 1, wx.EXPAND, 0)

		sizerInstallersButtons = wx.BoxSizer(wx.HORIZONTAL)
		sizerInstaller.Add(sizerInstallersButtons, 0, wx.EXPAND, 0)

		self.selectionInstallerBTN = wx.Button(self.installer_panel, 104, _("&Selection"))
		sizerInstallersButtons.Add(self.selectionInstallerBTN, 2, wx.CENTRE, 0)

		self.installBTN = wx.Button(self.installer_panel, 105, _("&Install"))
		sizerInstallersButtons.Add(self.installBTN, 2, wx.CENTRE, 0)

		self.panel_Backup = wx.Panel(self.list, wx.ID_ANY)
		self.list.AddPage(self.panel_Backup, _("Make/restore Backups"))

		sizerBackup = wx.BoxSizer(wx.VERTICAL)

		label_12 = wx.StaticText(self.panel_Backup, wx.ID_ANY, _("&Backup elements:"))
		sizerBackup.Add(label_12, 0, wx.EXPAND, 0)

		self.makeBackup_listbox = CustomCheckListBox(self.panel_Backup, wx.ID_ANY)
		sizerBackup.Add(self.makeBackup_listbox, 2, wx.EXPAND, 0)

		sizerBackupButtons = wx.BoxSizer(wx.HORIZONTAL)
		sizerBackup.Add(sizerBackupButtons, 0, wx.EXPAND, 0)

		self.makeBackupBTN = wx.Button(self.panel_Backup, 113, _("&Create a backup"))
		sizerBackupButtons.Add(self.makeBackupBTN, 2, wx.CENTRE, 0)

		self.restoreBackupBTN = wx.Button(self.panel_Backup, 114, _("&Restore backup"))
		sizerBackupButtons.Add(self.restoreBackupBTN, 2, wx.CENTRE, 0)

		self.panel_documentation = wx.Panel(self.list, wx.ID_ANY)
		self.list.AddPage(self.panel_documentation, _("Add-ons documentation"))

		sizerDocumentation = wx.BoxSizer(wx.VERTICAL)

		label_11 = wx.StaticText(self.panel_documentation, wx.ID_ANY, _("&Add-ons list:"))
		sizerDocumentation.Add(label_11, 0, wx.EXPAND, 0)

		self.listbox_documentation = wx.ListBox(self.panel_documentation, wx.ID_ANY)
		sizerDocumentation.Add(self.listbox_documentation, 1, wx.EXPAND, 0)

		self.seeDocumentationBTN = wx.Button(self.panel_documentation, 112, _("&Open add-on documentation"))
		sizerDocumentation.Add(self.seeDocumentationBTN, 0, wx.EXPAND, 0)

		sizer_status = wx.BoxSizer(wx.VERTICAL)
		sizer_main.Add(sizer_status, 0, wx.EXPAND, 0)

		label_2 = wx.StaticText(self.mainPanel, wx.ID_ANY, _("&Status:"))
		sizer_status.Add(label_2, 0, wx.EXPAND, 0)

		self.statusText = wx.TextCtrl(self.mainPanel, wx.ID_ANY, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
		sizer_status.Add(self.statusText, 1, wx.EXPAND, 0)

		self.progress = wx.Gauge(self.mainPanel, wx.ID_ANY, 10)
		sizer_status.Add(self.progress, 0, wx.EXPAND, 0)

		sizer_Status_Buttons = wx.BoxSizer(wx.HORIZONTAL)
		sizer_status.Add(sizer_Status_Buttons, 0, wx.EXPAND, 0)

		self.acceptBTN = wx.Button(self.mainPanel, 197, _("&Accept"))
		sizer_Status_Buttons.Add(self.acceptBTN, 2, wx.CENTRE, 0)

		self.cancelBTN = wx.Button(self.mainPanel, 198, _("&Cancel"))
		sizer_Status_Buttons.Add(self.cancelBTN, 2, wx.CENTRE, 0)

		self.closeBTN = wx.Button(self.mainPanel, 199, _("Close"))
		sizer_Status_Buttons.Add(self.closeBTN, 0, 2, wx.CENTRE, 0)

		self.panel_documentation.SetSizer(sizerDocumentation)
		self.panel_Backup.SetSizer(sizerBackup)
		self.installer_panel.SetSizer(sizerInstaller)
		self.packager_panel.SetSizer(sizerPackager)
		self.mainPanel.SetSizer(sizer_main)

		self.Layout()
		self.CenterOnScreen()
		self.events()

	def events(self):
		self.Bind(wx.EVT_CHECKLISTBOX, self.OnSelection, self.packager_listbox)
		self.Bind(wx.EVT_CHECKLISTBOX, self.OnSelection, self.installers_listbox)
		self.statusText.Bind(wx.EVT_CONTEXT_MENU, self.onPass)
		self.Bind(wx.EVT_BUTTON,self.onButton)
		self.Bind(wx.EVT_CHAR_HOOK, self.onKeyPress)
		self.Bind(wx.EVT_CLOSE, self.onExit)
		self.onStatus()
		self.start()

	def onStatus(self):
		self.installers_listbox.Disable()
		self.selectionInstallerBTN.Disable()
		self.installBTN.Disable()
		self.statusText.Disable()
		self.acceptBTN.Disable()
		self.cancelBTN.Disable()

	def start(self):
		for i in self.listAddons:
			self.packager_listbox.Append(i.manifest["summary"])
			if addonHandler.Addon(i.path).getDocFilePath():
				self.listbox_documentation.Append(i.manifest["summary"])
				self.dirDocumentation.append(addonHandler.Addon(i.path).getDocFilePath())

		self.packager_listbox.SetSelection(0)
		self.listbox_documentation.SetSelection(0)

		# Start backup
		if os.path.isdir(configs.dirDictionary):
			if os.listdir(configs.dirDictionary):
				self.makeBackup_listbox.Append(_("Dictionaries folder"))
				configs.listTempBackupID.append(0)
		if os.path.isdir(configs.dirProfile):
			if os.listdir(configs.dirProfile):
				self.makeBackup_listbox.Append(_("Profiles folder"))
				configs.listTempBackupID.append(1)
		if os.path.isdir(configs.dirScratchpad):
			if os.listdir(configs.dirScratchpad):
				self.makeBackup_listbox.Append(_("Scratchpad folder"))
				configs.listTempBackupID.append(2)
		if os.path.isfile(configs.fileTrigger):
			self.makeBackup_listbox.Append(_("Profiles triggers file"))
			configs.listTempBackupID.append(3)
		if os.path.isfile(configs.fileGestures):
			self.makeBackup_listbox.Append(_("Gestures file"))
			configs.listTempBackupID.append(4)
		if os.path.isfile(configs.fileNVDA):
			self.makeBackup_listbox.Append(_("NVDA configurations file"))
			configs.listTempBackupID.append(5)
		self.makeBackup_listbox.SetSelection(0)

	def onPass(self, event):
		return

	def OnSelection(self, event):
		pass

	def onProgress(self, event):
		self.progress.SetValue(event)

	def onStatusText(self, event):
		self.statusText.Clear()
		self.statusText.AppendText(event)

	def onCorrect(self, event, List=None):
		self.installTempList = List
		print(str(List))
		self.progress.SetValue(0)
		winsound.MessageBeep(0)
		self.IS_Active = False
		self.statusText.Clear()
		self.statusText.AppendText(event)
		self.statusText.SetInsertionPoint(0) 
		self.acceptBTN.Enable()
		self.closeBTN.Enable()

	def onError(self, event, List=None):
		self.installTempList = List
		self.progress.SetValue(0)
		winsound.MessageBeep(16)
		self.IS_Active = False
		self.statusText.Clear()
		self.statusText.AppendText(event)
		self.statusText.SetInsertionPoint(0) 
		self.cancelBTN.Enable()
		self.closeBTN.Enable()

	def onButton(self, event):
		id = event.GetId()
		if id == 101: # Button selection packager.
			self.menu = wx.Menu()
			item1 = self.menu.Append(1, _("&Select all"))
			item2 = self.menu.Append(2, _("&Unselect all"))
			self.menu.Bind(wx.EVT_MENU, self.onSelect)
			self.packageSelectionBTN.PopupMenu(self.menu)
		elif id == 102: # Button generate packager.
			self.selection = [i for i in range(self.packager_listbox.GetCount()) if self.packager_listbox.IsChecked(i)]
			if len(self.selection) == 0:
				gui.messageBox(_("You need to select at least one add-on to continue."), _("Error"), wx.ICON_ERROR)
				self.packager_listbox.SetFocus()
			else:
				dlg = wx.DirDialog(self, _("Select a folder:"), style=wx.DD_DEFAULT_STYLE)
				if dlg.ShowModal() == wx.ID_OK:
					self.directoryToSave =dlg.GetPath()
					dlg.Destroy()
					self.IS_Active = True
					self.progress.SetRange(len(self.selection))
					self.list.Disable()
					self.closeBTN.Disable()
					self.statusText.Enable()
					self.statusText.SetFocus()
					utilities.compressIndividualAddons(self, self.selection, self.directoryToSave)
				else:
					dlg.Destroy()
		elif id == 103: # Button select folder with add-ons to install.
			dlg = wx.DirDialog(self, _("Select a folder:"), style=wx.DD_DEFAULT_STYLE)
			if dlg.ShowModal() == wx.ID_OK:
				self.dirInstaller = dlg.GetPath()
				dlg.Destroy()
				x = utilities.GetAddons(self.dirInstaller, ".nvda-addon")
				if len(x) == 0:
					gui.messageBox(_("No add-ons found on selected folder."), _("Information"), wx.ICON_INFORMATION)
					self.installersFolderBTN.SetFocus()
				else:
					self.installTempList = None
					self.IS_Active = True
					self.progress.SetRange(len(x))
					self.list.Disable()
					self.closeBTN.Disable()
					self.statusText.Enable()
					self.statusText.SetFocus()
					utilities.folderWithAddons(self, self.dirInstaller, x)
			else:
				dlg.Destroy()
		elif id == 104: # Botón selection installer. 
			self.menu = wx.Menu()
			item1 = self.menu.Append(3, _("&Select all"))
			item2 = self.menu.Append(4, _("&Unselect all"))
			self.menu.Bind(wx.EVT_MENU, self.onSelect)
			self.selectionInstallerBTN.PopupMenu(self.menu)
		elif id == 105: # Button install installer. 
			self.selectionInstall = [i for i in range(self.installers_listbox.GetCount()) if self.installers_listbox.IsChecked(i)]
			if len(self.selectionInstall) == 0:
				gui.messageBox(_("You need to select at least one add-on to continue."), _("Error"), wx.ICON_ERROR)
				self.installers_listbox.SetFocus()
			else:
				self.IS_Active = True
				self.progress.SetRange(len(self.selectionInstall))
				self.list.Disable()
				self.closeBTN.Disable()
				self.statusText.Enable()
				self.statusText.SetFocus()
				utilities.InstallAddons(self, self.selectionInstall)
		elif id == 112: # boton see documentation
			wx.LaunchDefaultBrowser('file://' + self.dirDocumentation[self.listbox_documentation.GetSelection()], flags=0)
		elif id == 113: # Button make backup
			self.selectedCopy = [i for i in range(self.makeBackup_listbox.GetCount()) if self.makeBackup_listbox.IsChecked(i)]
			if len(self.selectedCopy) == 0:
				gui.messageBox(_("You need to select at least one backup element from the list to continue."), _("Error"), wx.ICON_ERROR)
				self.makeBackup_listbox.SetFocus()
			else:
				dict_commentary = {}
				for i in self.selectedCopy:
					dict_commentary[configs.listTempBackupID[i]] = utilities.id_generator(15, string.ascii_uppercase + string.ascii_lowercase + string.digits)
				wildcard = _("NVDA backup file (*.nvda-backup)|*.nvda-backup")
				dlg = wx.FileDialog(None, message=_("Save backup in..."), defaultDir=os.getcwd(), defaultFile="", wildcard=wildcard, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
				if dlg.ShowModal() == wx.ID_OK:
					backupFile = dlg.GetPath()
					dlg.Destroy()
					self.IS_Active = True
					self.progress.SetRange(len(self.selectedCopy))
					self.list.Disable()
					self.closeBTN.Disable()
					self.statusText.Enable()
					self.statusText.SetFocus()
					utilities.CreateBackup(self, backupFile, dict_commentary)
				else:
					dlg.Destroy()
					self.makeBackup_listbox.SetFocus()
		elif id == 114: # Button restore backup
			wildcard = _("NVDA backup file (*.nvda-backup)|*.nvda-backup")
			dlg = wx.FileDialog(None, message=_("Select a NVDA backup file"), defaultDir=os.getcwd(), defaultFile="", wildcard=wildcard, style=wx.FD_OPEN | wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST | wx.FD_PREVIEW)
			if dlg.ShowModal() == wx.ID_OK:
				archive = dlg.GetPath()
				dlg.Destroy()
				dlg = RestoreBackupDialog(archive)
				result = dlg.ShowModal()
				if result == 0: # Restore
					dlg.Destroy()
					backupFile = dlg.backupFile
					Dictionary = dlg.Dictionary
					selection = dlg.selectedCopy
					dictionaryFinal = {}
					temp = [int(i) for i in Dictionary.keys()]
					for i in selection:
						dictionaryFinal[temp[i]] = Dictionary.get(str(temp[i]))
					self.IS_Active = True
					self.progress.SetRange(len(seleccion))
					self.list.Disable()
					self.closeBTN.Disable()
					self.statusText.Enable()
					self.statusText.SetFocus()
					utilities.RestoreBackup(self, backupFile, dictionaryFinal)

				else:  # Cancel
					dlg.Destroy()
					self.makeBackup_listbox.SetFocus()
			else:
				dlg.Destroy()
				self.makeBackup_listbox.SetFocus()

		elif id== 197: # General button accept.
			if self.restart:
				core.restart()
			else:
				self.onStatus()
				self.list.Enable()
				self.list.SetFocus()
				if self.installTempList == None:
					return
				elif self.installTempList[-1] == "installer":
					self.installers_listbox.Enable()
					self.selectionInstallerBTN.Enable()
					self.installBTN.Enable()
					self.installers_listbox.Clear()
					for i in range(0, len(self.installTempList[1])):
						self.installers_listbox.Append("{} {}".format(self.installTempList[1][i], self.installTempList[2][i]))
					self.installers_listbox.SetSelection(0)
					self.installers_listbox.SetFocus()
				elif self.installTempList[-1] == "Backup":
					self.makeBackup_listbox.Clear()
					if os.path.isdir(configs.dirDictionary):
						if os.listdir(configs.dirDictionary):
							self.makeBackup_listbox.Append(_("Dictionaries folder"))
							configs.listTempBackupID.append(0)
					if os.path.isdir(configs.dirProfile):
						if os.listdir(configs.dirProfile):
							self.makeBackup_listbox.Append(_("Profiles folder"))
							configs.listTempBackupID.append(1)
					if os.path.isdir(configs.dirScratchpad):
						if os.listdir(configs.dirScratchpad):
							self.makeBackup_listbox.Append(_("Scratchpad folder"))
							configs.listTempBackupID.append(2)
					if os.path.isfile(configs.fileTrigger):
						self.makeBackup_listbox.Append(_("Profiles triggers file"))
						configs.listTempBackupID.append(3)
					if os.path.isfile(configs.fileGestures):
						self.makeBackup_listbox.Append(_("Gestures file"))
						configs.listTempBackupID.append(4)
					if os.path.isfile(configs.fileNVDA):
						self.makeBackup_listbox.Append(_("NVDA configurations file"))
						configs.listTempBackupID.append(5)
					self.makeBackup_listbox.SetSelection(0)
					self.makeBackup_listbox.SetFocus()
				elif self.installTempList[-1] == _("restart"):
					try:
						config.conf.profiles[0]["general"]["saveConfigurationOnExit"] = False
					except:
						config.conf["general"]["saveConfigurationOnExit"] = False
					core.restart()

		elif id == 198: # Button general cancel.
			if self.restart:
				pass
			else:
				self.onStatus()
				self.list.Enable()
				self.list.SetFocus()
				if self.installTempList == None:
					return
				elif self.installTempList[-1] == "installer":
					self.installersFolderBTN.SetFocus()
				elif self.installTempList[-1] == "Backup":
					self.makeBackup_listbox.Clear()
					if os.path.isdir(configs.dirDictionary):
						if os.listdir(configs.dirDictionary):
							self.makeBackup_listbox.Append(_("Dictionaries folder"))
							configs.listTempBackupID.append(0)
					if os.path.isdir(configs.dirProfile):
						if os.listdir(configs.dirProfile):
							self.makeBackup_listbox.Append(_("Profiles folder"))
							configs.listTempBackupID.append(1)
					if os.path.isdir(configs.dirScratchpad):
						if os.listdir(configs.dirScratchpad):
							self.makeBackup_listbox.Append(_("Scratchpad folder"))
							configs.listTempBackupID.append(2)
					if os.path.isfile(configs.fileTrigger):
						self.makeBackup_listbox.Append(_("Profiles triggers file"))
						configs.listTempBackupID.append(3)
					if os.path.isfile(configs.fileGestures):
						self.makeBackup_listbox.Append(_("Gestures file"))
						configs.listTempBackupID.append(4)
					if os.path.isfile(configs.fileNVDA):
						self.makeBackup_listbox.Append(_("NVDA configurations file"))
						configs.listTempBackupID.append(5)
					self.makeBackup_listbox.SetSelection(0)
					self.makeBackup_listbox.SetFocus()

				elif self.installTempList[-1] == _("restart"):
					try:
						config.conf.profiles[0]["general"]["saveConfigurationOnExit"] = False
					except:
						config.conf["general"]["saveConfigurationOnExit"] = False
					core.restart()

		elif id == 199: # Botón general close.
			try:
				if self.installTempList[-1] == _("restart"):
					try:
						config.conf.profiles[0]["general"]["saveConfigurationOnExit"] = False
					except:
						config.conf["general"]["saveConfigurationOnExit"] = False
					core.restart()
				else:
					self.onExit(None)
			except:
				self.onExit(None)

	def onSelect(self, event):
		id = event.GetId()
		if id == 1: # Packager select all.
			num = self.packager_listbox.GetCount()
			for i in range(num):
				self.packager_listbox.Check(	i, True)
			self.packager_listbox.SetSelection(0)
			self.packager_listbox.SetFocus()
		elif id == 2: # Packager unselect all.
			self.packager_listbox.Clear()
			for i in self.listAddons:
				self.packager_listbox.Append(i.manifest["summary"])
			self.packager_listbox.SetSelection(0)
			self.packager_listbox.SetFocus()
		elif id == 3: # Installer select all.
			num = self.installers_listbox.GetCount()
			for i in range(num):
				self.installers_listbox.Check(	i, True)
			self.installers_listbox.SetSelection(0)
			self.installers_listbox.SetFocus()
		elif id == 4: # Installer unselect all.
			self.installers_listbox.Clear()
			for i in range(0, len(self.installTempList[1])):
				self.installers_listbox.Append("{} {}".format(self.installTempList[1][i], self.installTempList[2][i]))
			self.installers_listbox.SetSelection(0)
			self.installers_listbox.SetFocus()

	def onKeyPress(self, event):
		if event.GetKeyCode() == 27: # Pressing Escape close the window
			try:
				if self.installTempList[-1] == _("restart"):
					try:
						config.conf.profiles[0]["general"]["saveConfigurationOnExit"] = False
					except:
						config.conf["general"]["saveConfigurationOnExit"] = False
					core.restart()
				else:
					self.onExit(None)
			except:
				self.onExit(None)
		else:
			event.Skip()

	def onExit(self, event):
		try:
			if self.installTempList[-1] == _("restart"):
				try:
					config.conf.profiles[0]["general"]["saveConfigurationOnExit"] = False
				except:
					config.conf["general"]["saveConfigurationOnExit"] = False
				core.restart()
		except:
			pass
		if self.IS_Active:
			return
		else:
			if self.restart:
				configs.restart = True
			configs.IS_WinON = False
			self.Destroy()
			gui.mainFrame.postPopup()

class RestoreBackupDialog(wx.Dialog):
	def __init__(self, archive):
		super(RestoreBackupDialog, self).__init__(None, -1)

		self.backupFile = archive
		self.dictionary = None
		self.selectedCopy = []

		self.SetSize((640, 480))
		self.SetTitle(_("Restore NVDA backup"))

		self.mainPanel = wx.Panel(self, wx.ID_ANY)

		sizer_main = wx.BoxSizer(wx.VERTICAL)

		label_1 = wx.StaticText(self.mainPanel, wx.ID_ANY, _("Backup &content:"))
		sizer_main.Add(label_1, 0, wx.EXPAND, 0)

		self.listbox_RestoreBackup = CustomCheckListBox(self.mainPanel, wx.ID_ANY)
		sizer_main.Add(self.listbox_RestoreBackup, 1, wx.EXPAND, 0)

		sizer_buttons = wx.BoxSizer(wx.HORIZONTAL)
		sizer_main.Add(sizer_buttons, 0, wx.EXPAND, 0)

		self.restoreBTN = wx.Button(self.mainPanel, wx.ID_ANY, _("&Restore"))
		sizer_buttons.Add(self.restoreBTN, 2, wx.EXPAND, 0)

		self.closeBTN = wx.Button(self.mainPanel, wx.ID_ANY, _("&Close"))
		sizer_buttons.Add(self.closeBTN, 2, wx.EXPAND, 0)

		self.mainPanel.SetSizer(sizer_main)

		self.Layout()
		self.CenterOnScreen()
		self.loadEvents()
		self.start()

	def loadEvents(self):
		self.restoreBTN.Bind(wx.EVT_BUTTON,self.onRestore)
		self.closeBTN.Bind(wx.EVT_BUTTON, self.onClose)
		self.Bind(wx.EVT_CLOSE, self.onClose)
		self.Bind(wx.EVT_CHAR_HOOK, self.onKeyPress)

	def start(self):
		self.dictionary = json.loads(utilities.readCommentary(self.backupFile))
		for i in self.dictionary:
			id = int(i)
			if id == 0:
				self.listbox_RestoreBackup.Append(_("Dictionaries folder"))
			if id == 1:
				self.listbox_RestoreBackup.Append(_("Profiles folder"))
			if id == 2:
				self.listbox_RestoreBackup.Append(_("Scratchpad folder"))
			if id == 3:
				self.listbox_RestoreBackup.Append(_("Profiles triggers file"))
			if id == 4:
				self.listbox_RestoreBackup.Append(_("Gestures file"))
			if id == 5:
				self.listbox_RestoreBackup.Append(_("NVDA configurations file"))
		self.listbox_RestoreBackup.SetSelection(0)
		self.listbox_RestoreBackup.SetFocus()

	def onRestore(self, event):
		self.selectedCopy = [i for i in range(self.listbox_RestoreBackup.GetCount()) if self.listbox_RestoreBackup.IsChecked(i)]
		if len(self.selectedCopy) == 0:
			gui.messageBox(_("You need to select at least one backup element from the list to continue."), _("Error"), wx.ICON_ERROR)
			self.listbox_RestoreBackup.SetFocus()
		else:
			self.EndModal(0)

	def onKeyPress(self, event):
		if event.GetKeyCode() == 27: # Press Escape to close the window
			self.EndModal(1)
		else:
			event.Skip()

	def onClose(self, event):
		self.EndModal(1)
