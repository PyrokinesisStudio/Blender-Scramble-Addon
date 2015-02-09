# 情報 > 「ヘルプ」メニュー

import bpy
import zipfile, urllib.request, os

################
# オペレーター #
################

class UpdateScrambleAddon(bpy.types.Operator):
	bl_idname = "script.update_scramble_addon"
	bl_label = "Blender-Scramble-Addonを更新"
	bl_description = "Blender-Scramble-Addonをダウンロード・更新を済ませます"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		response = urllib.request.urlopen("https://github.com/saidenka/Blender-Scramble-Addon/archive/master.zip")
		tempDir = bpy.app.tempdir
		zipPath = tempDir + r"\Blender-Scramble-Addon-master.zip"
		addonDir = os.path.dirname(__file__)
		f = open(zipPath, "wb")
		f.write(response.read())
		f.close()
		zf = zipfile.ZipFile(zipPath, "r")
		for f in zf.namelist():
			if not os.path.basename(f):
				pass
			else:
				if (".py" in f):
					uzf = open(addonDir +"\\"+ os.path.basename(f), 'wb')
					uzf.write(zf.read(f))
					uzf.close()
		zf.close()
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(UpdateScrambleAddon.bl_idname, icon="PLUGIN")
