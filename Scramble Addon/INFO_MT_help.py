# 情報 > 「ヘルプ」メニュー

import bpy
import zipfile, urllib.request, os, sys, re
import csv, codecs
import collections
import subprocess
import webbrowser
try:
	import winreg
except:
	pass

################
# オペレーター #
################

class RegisterBlendFile(bpy.types.Operator):
	bl_idname = "system.register_blend_file"
	bl_label = ".blendファイルをこのバージョンに関連付け"
	bl_description = ".blendファイルをこのBlender実行ファイルに関連付けます (WindowsOSのみ)"
	bl_options = {'REGISTER'}
	
	def execute(self, context):
		winreg.SetValue(winreg.HKEY_CURRENT_USER, r"Software\Classes\.blend", winreg.REG_SZ, 'blend_auto_file')
		winreg.SetValue(winreg.HKEY_CURRENT_USER, r"Software\Classes\blend_auto_file\shell\open\command", winreg.REG_SZ, '"'+sys.argv[0]+'" "%1"')
		self.report(type={"INFO"}, message=".blendファイルをこの実行ファイルに関連付けました")
		return {'FINISHED'}

class RegisterBlendBackupFiles(bpy.types.Operator):
	bl_idname = "system.register_blend_backup_files"
	bl_label = "バックアップをこのバージョンに関連付け"
	bl_description = ".blend1 .blend2 などのバックアップファイルをこのBlender実行ファイルに関連付けます (WindowsOSのみ)"
	bl_options = {'REGISTER'}
	
	max = bpy.props.IntProperty(name=".blend1～.blendN まで", default=10, min=1, max=1000, soft_min=1, soft_max=1000)
	
	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self)
	def execute(self, context):
		winreg.SetValue(winreg.HKEY_CURRENT_USER, r"Software\Classes\blend1_auto_file\shell\open\command", winreg.REG_SZ, '"'+sys.argv[0]+'" "%1"')
		for i in range(self.max):
			i += 1
			winreg.SetValue(winreg.HKEY_CURRENT_USER, r"Software\Classes\.blend"+str(i), winreg.REG_SZ, 'blend1_auto_file')
		self.report(type={"INFO"}, message="バックアップファイルをこの実行ファイルに関連付けました")
		return {'FINISHED'}

class UpdateScrambleAddon(bpy.types.Operator):
	bl_idname = "script.update_scramble_addon"
	bl_label = "Blender-Scramble-Addonを更新"
	bl_description = "Blender-Scramble-Addonをダウンロード・更新を済ませます"
	bl_options = {'REGISTER'}
	
	def execute(self, context):
		response = urllib.request.urlopen("https://github.com/saidenka/Blender-Scramble-Addon/archive/master.zip")
		tempDir = bpy.app.tempdir
		zipPath = os.path.join(tempDir, "Blender-Scramble-Addon-master.zip")
		addonDir = os.path.dirname(__file__)
		f = open(zipPath, "wb")
		f.write(response.read())
		f.close()
		zf = zipfile.ZipFile(zipPath, "r")
		for f in zf.namelist():
			if not os.path.basename(f):
				pass
			else:
				if ("Scramble Addon" in f):
					uzf = open(os.path.join(addonDir, os.path.basename(f)), 'wb')
					uzf.write(zf.read(f))
					uzf.close()
		zf.close()
		self.report(type={"INFO"}, message="アドオンを更新しました、Blenderを再起動して下さい")
		return {'FINISHED'}

class ToggleDisabledMenu(bpy.types.Operator):
	bl_idname = "wm.toggle_disabled_menu"
	bl_label = "「追加項目のオン/オフ」の表示切り替え"
	bl_description = "ScrambleAddonによるメニューの末尾の「追加項目のオン/オフ」ボタンの表示/非表示を切り替えます"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu = not context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu
		return {'FINISHED'}

################
# サブメニュー #
################

class AssociateMenu(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_help_associate"
	bl_label = "関連付け関係"
	bl_description = "関連付け関係のメニューです (WindowsOSのみ)"
	
	def draw(self, context):
		column = self.layout.column()
		column.operator(RegisterBlendFile.bl_idname, icon="PLUGIN")
		column.operator(RegisterBlendBackupFiles.bl_idname, icon="PLUGIN")

################
# メニュー追加 #
################

# メニューのオン/オフの判定
def IsMenuEnable(self_id):
	for id in bpy.context.user_preferences.addons["Scramble Addon"].preferences.disabled_menu.split(','):
		if (id == self_id):
			return False
	else:
		return True

# メニューを登録する関数
def menu(self, context):
	if (IsMenuEnable(__name__.split('.')[-1])):
		self.layout.separator()
		self.layout.menu(AssociateMenu.bl_idname, icon="PLUGIN")
		self.layout.separator()
		self.layout.operator(UpdateScrambleAddon.bl_idname, icon="PLUGIN")
	self.layout.separator()
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
	self.layout.operator(ToggleDisabledMenu.bl_idname, icon='CANCEL')
