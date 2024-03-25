# -*- coding: utf-8 -*-
# Copyright (C) 2022 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Copyright (C) 2023-2024 Rui Fontes <rui.fontes@tiflotecnia.com>
# This file is covered by the GNU General Public License.

# Import the necessary modules
import addonHandler
import addonAPIVersion
import globalVars
import wx
import os
import zipfile
from threading import Thread
import re
import fnmatch
import string
import random
import shutil
import json
from . import configs

# Start the translation process
addonHandler.initTranslation()

ADDON_API_VERSION_REGEX = re.compile(r"^(0|\d{4})\.(\d)(?:\.(\d))?$")

def getAPIVersionTupleFromString(version):
	# Converts a string containing an NVDA version to a tuple of the form (versionYear, versionMajor, versionMinor)
	match = ADDON_API_VERSION_REGEX.match(version)
	if not match:
		raise ValueError(version)
	return tuple(int(i) if i is not None else 0 for i in match.groups())

def hasAddonGotRequiredSupport(addonMin, currentAPIVersion=addonAPIVersion.CURRENT):
	# True if NVDA provides the add-on with an API version high enough to meet the add-on's minimum requirements
	return addonMin <= currentAPIVersion

def isAddonTested(addonMax, backwardsCompatToVersion=addonAPIVersion.BACK_COMPAT_TO):
	# True if this add-on is tested for the given API version.
	# By default, the current version of NVDA is evaluated.
	return addonMax >= backwardsCompatToVersion

def isAddonCompatible(
		addonMin,
		addonMax,
		currentAPIVersion=addonAPIVersion.CURRENT,
		backwardsCompatToVersion=addonAPIVersion.BACK_COMPAT_TO
):
	"""
	Tests if the addon is compatible.
	The compatibility is defined by having the required features in NVDA, and by having been tested / built against
	an API version that is still supported by this version of NVDA.
	"""
	return hasAddonGotRequiredSupport(addonMin, currentAPIVersion) and isAddonTested(addonMax, backwardsCompatToVersion)

def GetAddons(directory, extension):
	return [f for f in os.listdir(directory) if f.endswith(extension)]

def placeCommentary(archive, commentary):
	with zipfile.ZipFile(archive, 'a') as zip:
		zip.comment = commentary.encode("utf-8")

def readCommentary(archive):
	with zipfile.ZipFile(archive, 'r') as zip:
		commentary = zip.comment.decode("utf-8")
	return commentary

def extractZIP(archive, target, ZIPFile):
	try:
		with zipfile.ZipFile(ZIPFile) as archive:
			for file in archive.namelist():
				if file.startswith(archive):
					archive.extract(file, target)
		return True
	except:
		return False

def addToZIP(archive, ZIPFile):
	try:
		with zipfile.ZipFile(ZIPFile, 'a') as zipf:
			zipf.write(archive, os.path.basename(archive))
		return True
	except:
		return False

def zipfolder(foldername, target_dir, addon=True, progressBar=False, frame=None):
	if addon:
		zipobj = zipfile.ZipFile(foldername + '.nvda-addon', 'w', zipfile.ZIP_DEFLATED)
	else:
		zipobj = zipfile.ZipFile(foldername, 'w', zipfile.ZIP_DEFLATED)
	total = 0
	rootlen = len(target_dir) + 1
	for base, dirs, files in os.walk(target_dir):
		if addon:
			if '__pycache__' in dirs:
				dirs.remove('__pycache__')
		for fname in files:
			path = os.path.join(base, fname)
			total += os.path.getsize(path)

	current = 0
	for base, dirs, files in os.walk(target_dir):
		if addon:
			if '__pycache__' in dirs:
				dirs.remove('__pycache__')
		for fname in files:
			path = os.path.join(base, fname)
			fn = os.path.join(base, fname)
			percent = 100 * current / total + 1
			if progressBar:
				wx.CallAfter(frame.onProgress, int(percent))
			zipobj.write(fn, fn[rootlen:])
			current += os.path.getsize(path)
	zipobj.close()

def uncompressZIP(frame, archive, targetFolder, Progress=True):
	try:
		zf = zipfile.ZipFile(archive)
		uncompress_size = sum((file.file_size for file in zf.infolist()))
		extracted_size = 0
		for file in zf.infolist():
			extracted_size += file.file_size
			if Progress:
				progress = (lambda x, y: (int(x), int(x*y) % y/y))((extracted_size * 100/uncompress_size), 1e0)
				wx.CallAfter(frame.onProgress, progress[0])
			zf.extract(file, targetFolder)
		return True
	except Exception as e:
		return False

def findReplace(directory, find, replace, filePattern):
	for path, dirs, files in os.walk(os.path.abspath(directory)):
		for filename in fnmatch.filter(files, filePattern):
			filepath = os.path.join(path, filename)
			with open(filepath, 'r', errors="ignore") as file:
				fileContent = file.readlines()
			for lineIndex in range(len(fileContent)):
				if (find in fileContent[lineIndex]):
					fileContent[lineIndex] = replace
					with open(filepath, 'w', errors="ignore") as tableFile:
						tableFile.writelines(fileContent)
					break

def id_generator(size=6, composition=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation):
	return ''.join(random.choice(composition) for _ in range(size))

def tempGenFolder():
	return os.path.join(globalVars.appArgs.configPath, id_generator(15, string.ascii_uppercase + string.ascii_lowercase + string.digits))

class compressIndividualAddons(Thread):
	def __init__(self, frame, selection, directory):
		super(compressIndividualAddons, self).__init__()

		self.frame = frame
		self.selection = selection
		self.directory = directory
		self.daemon = True
		self.start()

	def run(self):
		try:
			for i in self.selection:
				addonSave = os.path.join(self.directory, self.frame.listAddons[i].manifest["name"] + "_" + self.frame.listAddons[i].manifest["version"].replace(":", "_") + "_Gen")
				wx.CallAfter(self.frame.onStatusText, _("Creating the add-on: {} {}").format(self.frame.listAddons[i].manifest["name"], self.frame.listAddons[i].manifest["version"]))
				zipfolder(addonSave, self.frame.listAddons[i].path)
				wx.CallAfter(self.frame.onProgress, i+1)
			msg = (
				_("All add-ons were generated correctly.") + "\n" +
				_("Press 'Accept' to continue.")
			)
			wx.CallAfter(self.frame.onCorrect, msg)
		except Exception as e:
			msg = (
				_("Occurred an unexpected error.") + "\n" +
				_("Error: {}").format(e) + "\n" +
					_("Please try again."))
			wx.CallAfter(self.frame.onError, msg)


class InstallAddons(Thread):
	def __init__(self, frame, selection):
		super(InstallAddons, self).__init__()

		self.frame = frame
		self.selection = selection
		self.daemon = True
		self.start()

	def run(self):
		lstError = []
		num = 0
		numRestart = 0
		try:
			for i in self.selection:
				num += 1
				wx.CallAfter(self.frame.onStatusText, _("Installing the add-on: {}").format(self.frame.installTempList[1][i]))
				wx.CallAfter(self.frame.onProgress, num)
				bundle = addonHandler.AddonBundle(self.frame.installTempList[0][i])
				if not addonHandler.addonVersionCheck.hasAddonGotRequiredSupport(bundle):
					pass #We can create an error check here for plug-ins that cannot be installed due to incompatibility and then give a message
				else:
					if addonHandler.addonVersionCheck.isAddonTested(bundle):
						bundleName = bundle.manifest['name']
						isDisabled = False
						for addon in addonHandler.getAvailableAddons():
							if bundleName == addon.manifest['name']:
								if addon.isDisabled:
									isDisabled = True
								if not addon.isPendingRemove:
									addon.requestRemove()
								break
						addonHandler.installAddonBundle(bundle)
						numRestart += 1
					else:
						lstError.append(i)
			if len(lstError) == 0:
				self.frame.restart = True
				msg = (
					_("Instalation correctly completed.") + "\n" +
					_("NVDA needs to restart to make changes available.") + "\n" +
					_("Press 'Accept' to restart.")
				)
				wx.CallAfter(self.frame.onCorrect, msg)
			else:
				if len(lstError) == len(self.frame.selectionInstall):
					self.frame.restart = False
					msg = (
						_("Was not possible to install the add-on.") + "\n" +
						_("Compatibility error.") + "\n" +
						_("Search for a compatible add-on")
					)
					wx.CallAfter(self.frame.onError, msg)
				else:
					temp = []
					for i in lstError:
						temp.append(self.frame.installTempList[1][i])
					msg = (
						_("Instalation completed correctly.") + "\n" +
						_("However some add-ons were not possible to be installed.") + "\n" +
							_("The following add-ons are incompatibles, search for a compatible version:\n{}").format("\n".join(str(x) for x in temp)) + "\n" +
							_("NVDA needs to restart to make changes available.") + "\n" +
						_("Press 'Accept' to restart.")
					)
					self.frame.restart = True
					wx.CallAfter(self.frame.onCorrect, msg)
		except Exception as e:
			if numRestart == 0:
				msg = (
					_("Occurred an unexpected error.") + "\n" +
					_("Error: {}").format(e) + "\n" +
					_("Please try again.")
				)
				self.frame.restart = False
				wx.CallAfter(self.frame.onError, msg)
			else:
				msg = (
					_("Occurred an unexpected error.") + "\n" +
					_("Error: {}").format(e) + "\n" +
					_("However some add-ons were installed.") + "\n" +
					_("NVDA needs to restart to make changes available.") + "\n" +
					_("Press 'Accept' to restart.")
				)
				self.frame.restart = True
				wx.CallAfter(self.frame.onCorrect, msg)


class folderWithAddons(Thread):
	def __init__(self, frame, directory, List):
		super(folderWithAddons, self).__init__()

		self.frame = frame
		self.directory = directory
		self.List = List
		self.daemon = True
		self.start()

	def run(self):
		files = [] # List with files name
		names = [] # List add-ons name
		version = [] # List add-ons version
		filesNotCompatible = [] # List files not compatibles with API
		fileError = [] # List failed when loading manifest.
		flagNotCompatible = False # Compatible flag
		flagNotFile = False # Flag errors
		num = 0
		for i in self.List:
			num += 1
			try:
				bundle = addonHandler.AddonBundle(os.path.join(self.directory, i))
				t1 = i
				t2 = bundle.manifest['summary']
				t3 = bundle.manifest['version']
				t4 = bundle.manifest['minimumNVDAVersion']
				t5 = bundle.manifest['lastTestedNVDAVersion']
				if isAddonCompatible(t4, t5):
					files.append(os.path.join(self.directory, t1))
					names.append(t2)
					version.append(t3)
				else:
					flagNotCompatible = True
					filesNotCompatible.append(i)
			except Exception as e:
				flagNotFile = True
				fileError.append(i)
			wx.CallAfter(self.frame.onStatusText, _("Searching add-ons in {}...").format(self.directory))
			wx.CallAfter(self.frame.onProgress, num)
		Results = [files, names, version, filesNotCompatible, fileError, "installer"]
		if len(Results[0]) == 0:
			wx.CallAfter(self.frame.onError, _("No compatible add-ons on directory."), ["installer"])
		else:
			if flagNotCompatible or flagNotFile:
				msg = (
					_("Add-on information extraction completed successfully.") + "\n" +
					_("However, the folder contains incompatible add-ons.") + "\n" +
					_("* Add-ons with errors in manifest: {}'\n'{}").format(len(fileError), "\n".join(fileError)) + "\n" +
					_("* Add-ons not compatible with current API: {}.'\n'{}").format(len(filesNotCompatible), "\n".join(filesNotCompatible)) + "\n" +
					_("Press 'Accept' to continue."))
				wx.CallAfter(self.frame.onCorrect, msg, Results)
			else:
				msg = (
					_("Add-on information extraction completed successfully.") + "\n" +
					_("Press 'Accept' to continue."))
				wx.CallAfter(self.frame.onCorrect, msg, Results)

class CreateBackup(Thread):
	def __init__(self, frame, backupFile, commentary):
		super(CreateBackup, self).__init__()

		self.frame = frame
		self.backupFile = backupFile
		self.commentary = commentary
		self.daemon = True
		self.start()

	def run(self):
		error = []
		try:
			zipobj = zipfile.ZipFile(self.backupFile, 'w', zipfile.ZIP_DEFLATED)
			zipobj.close()
			placeCommentary(self.backupFile, json.dumps(self.commentary))
			for i in self.commentary:
				id = i
				archive = self.commentary.get(id)
				if id == 0: # Dictionary
					wx.CallAfter(self.frame.onStatusText, _("Adding dictionaries folder..."))
					zipfolder(os.path.join(configs.dirConfig, archive), configs.dict_directories.get(id), False, False)
					p = addToZIP(os.path.join(configs.dirConfig, archive), self.backupFile)
					if p:
						os.remove(os.path.join(configs.dirConfig, archive))
					else:
						error.append(_("Was not possible to add dictionaries folder to the backup file."))
				if id == 1: # Profiles
					wx.CallAfter(self.frame.onStatusText, _("Adding profiles folder..."))
					zipfolder(os.path.join(configs.dirConfig, archive), configs.dict_directories.get(id), False, False)
					p = addToZIP(os.path.join(configs.dirConfig, archive), self.backupFile)
					if p:
						os.remove(os.path.join(configs.dirConfig, archive))
					else:
						error.append(_("Was not possible to add profiles folder to the backup file."))
				if id == 2: # Scratchpad
					wx.CallAfter(self.frame.onStatusText, _("Adding Scratchpad folder..."))
					zipfolder(os.path.join(configs.dirConfig, archive), configs.dict_directories.get(id), False, False)
					p = addToZIP(os.path.join(configs.dirConfig, archive), self.backupFile)
					if p:
						os.remove(os.path.join(configs.dirConfig, archive))
					else:
						error.append(_("Was not possible to add Scratchpad folder to the backup file."))

				if id == 3: # Profiles triggers file
					wx.CallAfter(self.frame.onStatusText, _("Adding profiles triggers file..."))
					p = addToZIP(configs.dict_directories.get(id), os.path.join(configs.dirConfig, archive))
					if p:
						z = addToZIP(os.path.join(configs.dirConfig, archive), self.backupFile)
						if z:
							os.remove(os.path.join(configs.dirConfig, archive))
						else:
							error.append(_("Was not possible to add profiles triggers file to the backup file."))
					else:
						error.append(_("Was not possible to add profiles triggers file to the backup file."))
				if id == 4: # File gestures.ini
					wx.CallAfter(self.frame.onStatusText, _("Adding gestures file..."))
					p = addToZIP(configs.dict_directories.get(id), os.path.join(configs.dirConfig, archive))
					if p:
						z = addToZIP(os.path.join(configs.dirConfig, archive), self.backupFile)
						if z:
							os.remove(os.path.join(configs.dirConfig, archive))
						else:
							error.append(_("Was not possible to add gestures file to the backup file.."))
					else:
						error.append(_("Was not possible to add gestures file to the backup file.."))
				if id == 5: # NVDA configuration file
					wx.CallAfter(self.frame.onStatusText, _("Adding NVDA configuration file..."))
					p = addToZIP(configs.dict_directories.get(id), os.path.join(configs.dirConfig, archive))
					if p:
						z = addToZIP(os.path.join(configs.dirConfig, archive), self.backupFile)
						if z:
							os.remove(os.path.join(configs.dirConfig, archive))
						else:
							error.append(_("Was not possible to add NVDA configuration file to the backup file.."))
					else:
						error.append(_("Was not possible to add NVDA configuration file to the backup file.."))

				try:
					os.remove(os.path.join(configs.dirConfig, archive))
				except:
					pass
				wx.CallAfter(self.frame.onProgress, i+1)

		except Exception as e:
			error.append(e)

		if len(error) == 0:
			msg = (
				_("Correctly created backup file at:\n{}").format(self.backupFile) + "\n" +
				_("Press 'Accept' to continue."))
			wx.CallAfter(self.frame.onCorrect, msg, ["Backup"])
		else:
			try:
				os.remove(self.backupFile)
			except:
				pass
			if len(error) == 1:
				msg = (
					_("The following error have Occurred:\n{}").format(error[0]) + "\n" +
					_("Was not possible to create the backup file") + "\n" +
					_("Press 'Accept' to continue."))
				wx.CallAfter(self.frame.onError, msg, ["Backup"])
			else:
				msg = (
					_("The following errors have Occurred:\n{}").format("\n".join(error)) + "\n" +
					_("Was not possible to create the backup file") + "\n" +
					_("Press 'Accept' to continue."))
				wx.CallAfter(self.frame.onError, msg, ["Backup"])

class RestoreBackup(Thread):
	def __init__(self, frame, backupFile, commentary):
		super(RestoreBackup, self).__init__()

		self.frame = frame
		self.backupFile = backupFile
		self.commentary = commentary
		self.archiveNVDA = False
		self.daemon = True
		self.start()

	def run(self):
		error = []
		try:
			for i in self.commentary:
				id = i
				archive = self.commentary.get(id)
				if id == 0: # Dictionary
					wx.CallAfter(self.frame.onStatusText, _("Restoring dictionary folder..."))
					p = extractZIP(archive, configs.dirConfig, self.backupFile)
					if p:
						z = uncompressZIP(self.frame, os.path.join(configs.dirConfig, archive), configs.dirDictionary, False)
						if z:
							os.remove(os.path.join(configs.dirConfig, archive))
							self.archiveNVDA = True
						else:
							os.remove(os.path.join(configs.dirConfig, archive))
							error.append(_("Was not possible to restore the dictionaries folder."))
					else:
						error.append(_("Was not possible to restore the dictionaries folder."))
				if id == 1: # Profiles
					wx.CallAfter(self.frame.onStatusText, _("Restoring profiles folder..."))
					p = extractZIP(archive, configs.dirConfig, self.backupFile)
					if p:
						z = uncompressZIP(self.frame, os.path.join(configs.dirConfig, archive), configs.dirProfile, False)
						if z:
							os.remove(os.path.join(configs.dirConfig, archive))
							self.archiveNVDA = True
						else:
							os.remove(os.path.join(configs.dirConfig, archive))
							error.append(_("Was not possible to restore the profiles folder."))
					else:
						error.append(_("Was not possible to restore the profiles folder."))
				if id == 2: # Scratchpad
					wx.CallAfter(self.frame.onStatusText, _("Restoring Scratchpad folder..."))
					p = extractZIP(archive, configs.dirConfig, self.backupFile)
					if p:
						z = uncompressZIP(self.frame, os.path.join(configs.dirConfig, archive), configs.dirScratchpad, False)
						if z:
							os.remove(os.path.join(configs.dirConfig, archive))
							self.archiveNVDA = True
						else:
							os.remove(os.path.join(configs.dirConfig, archive))
							error.append(_("Was not possible to restore the Scratchpad folder."))
					else:
						error.append(_("Was not possible to restore the Scratchpad folder."))
				if id == 3: # profiles triggers file
					wx.CallAfter(self.frame.onStatusText, _("Restoring profiles triggers file..."))
					p = extractZIP(archive, configs.dirConfig, self.backupFile)
					if p:
						try:
							try:
								os.remove(os.path.join(configs.dirConfig, "profileTriggers.ini"))
							except:
								pass
							z = uncompressZIP(self.frame, os.path.join(configs.dirConfig, archive), configs.dirConfig, False)
							if z:
								os.remove(os.path.join(configs.dirConfig, archive))
								self.archiveNVDA = True
							else:
								os.remove(os.path.join(configs.dirConfig, archive))
								error.append(_("Was not possible to restore the profiles triggers file."))
						except Exception as e:
							error.append(_("Was not possible to restore the profiles triggers file."))
					else:
						error.append(_("Was not possible to restore the profiles triggers file."))
				if id == 4: # File gestures.ini
					wx.CallAfter(self.frame.onStatusText, _("Restoring gestures file..."))
					p = extractZIP(archive, configs.dirConfig, self.backupFile)
					if p:
						try:
							try:
								os.remove(os.path.join(configs.dirConfig, "gestures.ini"))
							except:
								pass
							z = uncompressZIP(self.frame, os.path.join(configs.dirConfig, archive), configs.dirConfig, False)
							if z:
								os.remove(os.path.join(configs.dirConfig, archive))
								self.archiveNVDA = True
							else:
								os.remove(os.path.join(configs.dirConfig, archive))
								error.append(_("Was not possible to restore the gestures file."))
						except Exception as e:
							error.append(_("Was not possible to restore the gestures file."))
					else:
						error.append(_("Was not possible to restore the gestures file."))
				if id == 5: # NVDA configuration file
					wx.CallAfter(self.frame.onStatusText, _("Restoring NVDA configuration file..."))
					p = extractZIP(archive, configs.dirConfig, self.backupFile)
					if p:
						try:
							try:
								os.remove(os.path.join(configs.dirConfig, "nvda.ini"))
							except:
								pass
							z = uncompressZIP(self.frame, os.path.join(configs.dirConfig, archive), configs.dirConfig, False)
							if z:
								os.remove(os.path.join(configs.dirConfig, archive))
								self.archiveNVDA = True
							else:
								os.remove(os.path.join(configs.dirConfig, archive))
								error.append(_("Was not possible to restore the NVDA configuration file."))
						except Exception as e:
							error.append(_("Was not possible to restore the NVDA configuration file."))
					else:
						error.append(_("Was not possible to restore the NVDA configuration file."))
				wx.CallAfter(self.frame.onProgress, i+1)
		except Exception as e:
			error.append(e)
		if len(error) == 0:
			if self.archiveNVDA:
				msg = (
					_("The restore process was completed successfully.") + "\n" +
					_("NVDA needs to restart to make changes available.") + "\n" +
				_("Press 'Accept' to restart."))
				wx.CallAfter(self.frame.onCorrect, msg, [_("restart")])
		else:
			if len(error) == 1:
				if self.archiveNVDA:
					msg = (
						_("The following error have Occurred:\n{}").format(error[0]) + "\n" +
						_("Was not possible to restore all the backup") + "\n" +
						_("However some elements were restored") + "\n" +
						_("NVDA needs to restart to make changes available.") + "\n" +
						_("Press 'Accept' to restart."))
					wx.CallAfter(self.frame.onError, msg, [_("restart")])
				else:
					msg = (
						_("The following error have Occurred:\n{}").format(error[0]) + "\n" +
						_("Was not possible to restore NVDA") + "\n" +
						_("Press 'Accept' or 'Close' to continue."))
					wx.CallAfter(self.frame.onError, msg, ["Backup"])
			else:
				if self.archiveNVDA:
					msg = (
						_("The following errors have Occurred:\n{}").format("\n".join(error)) + "\n" +
						_("Was not possible to restore all the backup") + "\n" +
						_("However some elements were restored") + "\n" +
						_("NVDA needs to restart to make changes available.") + "\n" +
						_("Press 'Accept' to restart."))
					wx.CallAfter(self.frame.onError, msg, [_("restart")])
				else:
					msg = (
						_("The following errors have Occurred:\n{}").format("\n".join(error)) + "\n" +
						_("Was not possible to restore NVDA") + "\n" +
						_("Press 'Accept' or 'Close' to continue."))
					wx.CallAfter(self.frame.onError, msg, ["Backup"])
