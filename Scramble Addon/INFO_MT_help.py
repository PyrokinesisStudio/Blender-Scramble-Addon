# 情報 > 「ヘルプ」メニュー

import bpy
import zipfile, urllib.request, os, sys
import csv

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
				if ("Blender-Scramble-Addon-master/Scramble Addon/" in f):
					uzf = open(addonDir +"\\"+ os.path.basename(f), 'wb')
					uzf.write(zf.read(f))
					uzf.close()
		zf.close()
		self.report(type={"INFO"}, message="アドオンを更新しました、Blenderを再起動して下さい")
		return {'FINISHED'}

class ShowShortcutHtml(bpy.types.Operator):
	bl_idname = "system.show_shortcut_html"
	bl_label = "ショートカット一覧をブラウザで閲覧"
	bl_description = "Blenderの全てのショートカットをブラウザで確認出来ます"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		addonDir = os.path.dirname(__file__)
		keyDatas = {}
		with open(addonDir + "\\ShortcutHtmlKeysData.csv", 'r') as f:
			reader = csv.reader(f)
			for row in reader:
				name = row[1]
				keyDatas[name] = {}
				keyDatas[name]["key_name"] = row[0]
				keyDatas[name]["key_code"] = row[1]
				keyDatas[name]["shape"] = row[2]
				keyDatas[name]["coords"] = row[3]
				keyDatas[name]["configs"] = {}
		for kc in context.window_manager.keyconfigs:
			for km in kc.keymaps:
				for kmi in km.keymap_items:
					if (kmi.type in keyDatas):
						if (not kmi.name):
							continue
						if (km.name in keyDatas[kmi.type]["configs"]):
							keyDatas[kmi.type]["configs"][km.name].append(kmi)
						else:
							keyDatas[kmi.type]["configs"][km.name] = [kmi]
		areaStrings = ""
		for name, data in keyDatas.items():
			title = "<b>【 " +data["key_name"]+ " 】</b><br><br>"
			for mapName, cfgs in data["configs"].items():
				title = title + "<b>[" + mapName + "]</b><br>"
				for cfg in cfgs:
					cfgStr = ""
					if (cfg.shift):
						cfgStr = cfgStr + " Shift"
					if (cfg.ctrl):
						cfgStr = cfgStr + " Ctrl"
					if (cfg.alt):
						cfgStr = cfgStr + " Alt"
					if (cfg.oskey):
						cfgStr = cfgStr + " OS"
					if (cfg.key_modifier != 'NONE'):
						cfgStr = cfgStr + " " + cfg.key_modifier
					if (cfgStr):
						cfgStr = "(+" + cfgStr[1:] + ")　"
					if (cfg.any):
						cfgStr = "(常に)　"
					if (cfg.name):
						if (cfg.idname == "wm.call_menu"):
							cfgStr = cfgStr + "メニュー「" + cfg.properties.name + "」の呼び出し"
						elif (cfg.idname == "wm.context_set_enum"):
							cfgStr = cfgStr + "「" + cfg.properties.data_path + "」を「" + cfg.properties.value + "」に変更"
						elif (cfg.idname == "wm.context_toggle"):
							cfgStr = cfgStr + "「" + cfg.properties.data_path + "」の切り替え"
						elif (cfg.idname == "wm.context_toggle_enum"):
							cfgStr = cfgStr + "「" + cfg.properties.data_path + "」を「" + cfg.properties.value_1 + "」と「" + cfg.properties.value_2 + "」に切り替え"
						else:
							cfgStr = cfgStr + cfg.name
					else:
						cfgStr = cfgStr + cfg.propvalue
					if (not cfg.active):
						cfgStr = "<s>" + cfgStr + "</s>"
					title = title + "　" + cfgStr + "<br>"
				#title = title + "<br>"
			areaStrings = areaStrings+'<area href="#" title="' +title+ '" shape="' +data["shape"]+ '" coords="' +data["coords"]+ '">\n'
			print(areaStrings)
		file = open(addonDir + "\\ShortcutHtmlTemplate.html", "r")
		template = file.read()
		file.close()
		template = template.replace("<!-- [AREAS] -->", areaStrings)
		file = open(addonDir + "\\ShortcutHtmlTemp.html", "w")
		file.write(template)
		file.close()
		os.system('"' + addonDir + '\\ShortcutHtmlTemp.html"')
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(ShowShortcutHtml.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.operator(UpdateScrambleAddon.bl_idname, icon="PLUGIN")
