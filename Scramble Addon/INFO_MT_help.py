# 情報 > 「ヘルプ」メニュー

import bpy
import zipfile, urllib.request, os, sys, re
import csv
import collections
import winreg

################
# オペレーター #
################

class RegisterBlendFile(bpy.types.Operator):
	bl_idname = "system.register_blend_file"
	bl_label = ".blendファイルをこのバージョンに関連付け"
	bl_description = ".blendファイルをこのBlender実行ファイルに関連付けます (WindowsOSのみ)"
	bl_options = {'REGISTER'}
	
	def execute(self, context):
		winreg.SetValue(winreg.HKEY_CURRENT_USER, r"Software\Classes\blend_auto_file\shell\open\command", winreg.REG_SZ, '"'+sys.argv[0]+'" "%1"')
		self.report(type={"INFO"}, message=".blendファイルをこの実行ファイルに関連付けました")
		return {'FINISHED'}

class UpdateScrambleAddon(bpy.types.Operator):
	bl_idname = "script.update_scramble_addon"
	bl_label = "Blender-Scramble-Addonを更新"
	bl_description = "Blender-Scramble-Addonをダウンロード・更新を済ませます"
	bl_options = {'REGISTER'}
	
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
		keyDatas = collections.OrderedDict()
		with open(addonDir + "\\ShortcutHtmlKeysData.csv", 'r') as f:
			reader = csv.reader(f)
			for row in reader:
				name = row[1]
				keyDatas[name] = {}
				keyDatas[name]["key_name"] = row[0]
				keyDatas[name]["key_code"] = row[1]
				keyDatas[name]["shape"] = row[2]
				keyDatas[name]["coords"] = row[3]
				keyDatas[name]["configs"] = collections.OrderedDict()
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
				cfgsData = []
				for cfg in cfgs:
					cfgStr = ""
					color = ["0", "0", "0"]
					if (cfg.shift):
						cfgStr = cfgStr + " Shift"
						color[2] = "6"
					if (cfg.ctrl):
						cfgStr = cfgStr + " Ctrl"
						color[1] = "6"
					if (cfg.alt):
						cfgStr = cfgStr + " Alt"
						color[0] = "6"
					if (cfg.oskey):
						cfgStr = cfgStr + " OS"
					if (cfg.key_modifier != 'NONE'):
						cfgStr = cfgStr + " " + cfg.key_modifier
					if (cfgStr):
						cfgStr = "(+" + cfgStr[1:] + ")　"
					if (cfg.any):
						cfgStr = "(常に)　"
					modifierKeyStr = cfgStr
					if (cfg.name):
						if (cfg.idname == "wm.call_menu"):
							cfgStr = cfgStr + "「" + cfg.properties.name + "」メニューの呼び出し"
						elif (cfg.idname == "wm.context_set_enum"):
							cfgStr = cfgStr + "「" + cfg.properties.data_path + "」を「" + cfg.properties.value + "」に変更"
						elif (cfg.idname == "wm.context_toggle"):
							cfgStr = cfgStr + "「" + cfg.properties.data_path + "」の切り替え"
						elif (cfg.idname == "wm.context_toggle_enum"):
							cfgStr = cfgStr + "「" + cfg.properties.data_path + "」を「" + cfg.properties.value_1 + "」と「" + cfg.properties.value_2 + "」に切り替え"
						elif (cfg.idname == "wm.context_menu_enum"):
							cfgStr = cfgStr + "「" + cfg.properties.data_path + "」メニューの呼び出し"
						else:
							cfgStr = cfgStr + cfg.name
					else:
						cfgStr = cfgStr + cfg.propvalue
					if (not cfg.active):
						cfgStr = "<s>" + cfgStr + "</s>"
					cfgStr = "　<font size='2' color='#" +color[0]+color[1]+color[2]+ "'>" + cfgStr + "</font><br>"
					cfgsData.append([cfgStr, modifierKeyStr])
				cfgsData = sorted(cfgsData, key=lambda i: len(i[1]))
				alreadys = []
				for i in cfgsData:
					if (i[0] not in alreadys):
						title = title + i[0]
						alreadys.append(i[0])
			areaStrings = areaStrings+ '<area href="#" title="' +title+ '" shape="' +data["shape"]+ '" coords="' +data["coords"]+ '">\n'
		file = open(addonDir + "\\ShortcutHtmlTemplate.html", "r")
		template = file.read()
		file.close()
		template = template.replace("<!-- [AREAS] -->", areaStrings)
		file = open(addonDir + "\\ShortcutHtmlTemp.html", "w")
		file.write(template)
		file.close()
		os.system('"' + addonDir + '\\ShortcutHtmlTemp.html"')
		return {'FINISHED'}

class RegisterLastCommandKeyconfig(bpy.types.Operator):
	bl_idname = "wm.register_last_command_keyconfig"
	bl_label = "最後のコマンドをショートカットに登録"
	bl_description = "最後に実行したコマンドをショートカットに登録します"
	bl_options = {'REGISTER'}
	
	command = bpy.props.StringProperty(name="登録コマンド(変更不可)")
	sub_command = bpy.props.StringProperty(name="サブコマンド(変更不可)")
	items = [
		('Window', "Window", "", 1),
		('Screen', "Screen", "", 2),
		('Screen Editing', "Screen Editing", "", 3),
		('View2D', "View2D", "", 4),
		('Frames', "Frames", "", 5),
		('Header', "Header", "", 6),
		('View2D Buttons List', "View2D Buttons List", "", 7),
		('Property Editor', "Property Editor", "", 8),
		('3D View Generic', "3D View Generic", "", 9),
		('Grease Pencil', "Grease Pencil", "", 10),
		('Grease Pencil Stroke Edit Mode', "Grease Pencil Stroke Edit Mode", "", 11),
		('Face Mask', "Face Mask", "", 12),
		('Weight Paint Vertex Selection', "Weight Paint Vertex Selection", "", 13),
		('Pose', "Pose", "", 14),
		('Object Mode', "Object Mode", "", 15),
		('Paint Curve', "Paint Curve", "", 16),
		('Curve', "Curve", "", 17),
		('Image Paint', "Image Paint", "", 18),
		('Vertex Paint', "Vertex Paint", "", 19),
		('Weight Paint', "Weight Paint", "", 20),
		('Sculpt', "Sculpt", "", 21),
		('Mesh', "Mesh", "", 22),
		('Armature', "Armature", "", 23),
		('Metaball', "Metaball", "", 24),
		('Lattice', "Lattice", "", 25),
		('Particle', "Particle", "", 26),
		('Font', "Font", "", 27),
		('Object Non-modal', "Object Non-modal", "", 28),
		('3D View', "3D View", "", 29),
		('Outliner', "Outliner", "", 30),
		('Info', "Info", "", 31),
		('View3D Gesture Circle', "View3D Gesture Circle", "", 32),
		('Gesture Border', "Gesture Border", "", 33),
		('Gesture Zoom Border', "Gesture Zoom Border", "", 34),
		('Gesture Straight Line', "Gesture Straight Line", "", 35),
		('Standard Modal Map', "Standard Modal Map", "", 36),
		('Animation', "Animation", "", 37),
		('Animation Channels', "Animation Channels", "", 38),
		('Knife Tool Modal Map', "Knife Tool Modal Map", "", 39),
		('UV Editor', "UV Editor", "", 40),
		('Transform Modal Map', "Transform Modal Map", "", 41),
		('UV Sculpt', "UV Sculpt", "", 42),
		('Paint Stroke Modal', "Paint Stroke Modal", "", 43),
		('Mask Editing', "Mask Editing", "", 44),
		('Markers', "Markers", "", 45),
		('Timeline', "Timeline", "", 46),
		('View3D Fly Modal', "View3D Fly Modal", "", 47),
		('View3D Walk Modal', "View3D Walk Modal", "", 48),
		('View3D Rotate Modal', "View3D Rotate Modal", "", 49),
		('View3D Move Modal', "View3D Move Modal", "", 50),
		('View3D Zoom Modal', "View3D Zoom Modal", "", 51),
		('View3D Dolly Modal', "View3D Dolly Modal", "", 52),
		('Graph Editor Generic', "Graph Editor Generic", "", 53),
		('Graph Editor', "Graph Editor", "", 54),
		('Image Generic', "Image Generic", "", 55),
		('Image', "Image", "", 56),
		('Node Generic', "Node Generic", "", 57),
		('Node Editor', "Node Editor", "", 58),
		('File Browser', "File Browser", "", 59),
		('File Browser Main', "File Browser Main", "", 60),
		('File Browser Buttons', "File Browser Buttons", "", 61),
		('Dopesheet', "Dopesheet", "", 62),
		('NLA Generic', "NLA Generic", "", 63),
		('NLA Channels', "NLA Channels", "", 64),
		('NLA Editor', "NLA Editor", "", 65),
		('Text Generic', "Text Generic", "", 66),
		('Text', "Text", "", 67),
		('SequencerCommon', "SequencerCommon", "", 68),
		('Sequencer', "Sequencer", "", 69),
		('SequencerPreview', "SequencerPreview", "", 70),
		('Logic Editor', "Logic Editor", "", 71),
		('Console', "Console", "", 72),
		('Clip', "Clip", "", 73),
		('Clip Editor', "Clip Editor", "", 74),
		('Clip Graph Editor', "Clip Graph Editor", "", 75),
		('Clip Dopesheet Editor', "Clip Dopesheet Editor", "", 76),
		]
	key_map = bpy.props.EnumProperty(items=items, name="有効エリア")
	items = [
		('LEFTMOUSE', "左クリック", "", 1),
		('MIDDLEMOUSE', "ホイールクリック", "", 2),
		('RIGHTMOUSE', "右クリック", "", 3),
		('BUTTON4MOUSE', "マウス4ボタン", "", 4),
		('BUTTON5MOUSE', "マウス5ボタン", "", 5),
		('BUTTON6MOUSE', "マウス6ボタン", "", 6),
		('BUTTON7MOUSE', "マウス7ボタン", "", 7),
		('MOUSEMOVE', "マウス移動", "", 8),
		('INBETWEEN_MOUSEMOVE', "境界のマウス移動", "", 9),
		('WHEELUPMOUSE', "ホイールアップ", "", 10),
		('WHEELDOWNMOUSE', "ホイールダウン", "", 11),
		('A', "Aキー", "", 12),
		('B', "Bキー", "", 13),
		('C', "Cキー", "", 14),
		('D', "Dキー", "", 15),
		('E', "Eキー", "", 16),
		('F', "Fキー", "", 17),
		('G', "Gキー", "", 18),
		('H', "Hキー", "", 19),
		('I', "Iキー", "", 20),
		('J', "Jキー", "", 21),
		('K', "Kキー", "", 22),
		('L', "Lキー", "", 23),
		('M', "Mキー", "", 24),
		('N', "Nキー", "", 25),
		('O', "Oキー", "", 26),
		('P', "Pキー", "", 27),
		('Q', "Qキー", "", 28),
		('R', "Rキー", "", 29),
		('S', "Sキー", "", 30),
		('T', "Tキー", "", 31),
		('U', "Uキー", "", 32),
		('V', "Vキー", "", 33),
		('W', "Wキー", "", 34),
		('X', "Xキー", "", 35),
		('Y', "Yキー", "", 36),
		('Z', "Zキー", "", 37),
		('ZERO', "0", "", 38),
		('ONE', "1", "", 39),
		('TWO', "2", "", 40),
		('THREE', "3", "", 41),
		('FOUR', "4", "", 42),
		('FIVE', "5", "", 43),
		('SIX', "6", "", 44),
		('SEVEN', "7", "", 45),
		('EIGHT', "8", "", 46),
		('NINE', "9", "", 47),
		('LEFT_CTRL', "左CTRL", "", 48),
		('LEFT_ALT', "左ALT", "", 49),
		('LEFT_SHIFT', "左SHIFT", "", 50),
		('RIGHT_ALT', "右ALT", "", 51),
		('RIGHT_CTRL', "右CTRL", "", 52),
		('RIGHT_SHIFT', "右SHIFT", "", 53),
		('OSKEY', "OSキー", "", 54),
		('GRLESS', "\\", "", 55),
		('ESC', "Escキー", "", 56),
		('TAB', "Tabキー", "", 57),
		('RET', "Retキー", "", 58),
		('SPACE', "Spaceキー", "", 59),
		('BACK_SPACE', "BackSpaceキー", "", 60),
		('DEL', "Deleteキー", "", 61),
		('SEMI_COLON', ":", "", 62),
		('PERIOD', ".(ピリオド)", "", 63),
		('COMMA', ",(コンマ)", "", 64),
		('QUOTE', "^", "", 65),
		('ACCENT_GRAVE', "@", "", 66),
		('MINUS', "-", "", 67),
		('SLASH', "/", "", 68),
		('BACK_SLASH', "\\(バックスラッシュ)", "", 69),
		('EQUAL', ";", "", 70),
		('LEFT_BRACKET', "[", "", 71),
		('RIGHT_BRACKET', "]", "", 72),
		('LEFT_ARROW', "←", "", 73),
		('DOWN_ARROW', "↓", "", 74),
		('RIGHT_ARROW', "→", "", 75),
		('UP_ARROW', "↑", "", 76),
		('NUMPAD_2', "テンキー2", "", 77),
		('NUMPAD_4', "テンキー4", "", 78),
		('NUMPAD_6', "テンキー6", "", 79),
		('NUMPAD_8', "テンキー8", "", 80),
		('NUMPAD_1', "テンキー1", "", 81),
		('NUMPAD_3', "テンキー3", "", 82),
		('NUMPAD_5', "テンキー5", "", 83),
		('NUMPAD_7', "テンキー7", "", 84),
		('NUMPAD_9', "テンキー9", "", 85),
		('NUMPAD_PERIOD', "テンキーピリオド", "", 86),
		('NUMPAD_SLASH', "テンキースラッシュ", "", 87),
		('NUMPAD_ASTERIX', "テンキー＊", "", 88),
		('NUMPAD_0', "テンキー0", "", 89),
		('NUMPAD_MINUS', "テンキーマイナス", "", 90),
		('NUMPAD_ENTER', "テンキーエンター", "", 91),
		('NUMPAD_PLUS', "テンキー＋", "", 92),
		('F1', "F1", "", 93),
		('F2', "F2", "", 94),
		('F3', "F3", "", 95),
		('F4', "F4", "", 96),
		('F5', "F5", "", 97),
		('F6', "F6", "", 98),
		('F7', "F7", "", 99),
		('F8', "F8", "", 100),
		('F9', "F9", "", 101),
		('F10', "F10", "", 102),
		('F11', "F11", "", 103),
		('F12', "F12", "", 104),
		('F13', "F13", "", 105),
		('F14', "F14", "", 106),
		('F15', "F15", "", 107),
		('F16', "F16", "", 108),
		('F17', "F17", "", 109),
		('F18', "F18", "", 110),
		('F19', "F19", "", 111),
		('PAUSE', "Pauseキー", "", 112),
		('INSERT', "Insertキー", "", 113),
		('HOME', "Homeキー", "", 114),
		('PAGE_UP', "PageUpキー", "", 115),
		('PAGE_DOWN', "PageDownキー", "", 116),
		('END', "Endキー", "", 117),
		]
	type = bpy.props.EnumProperty(items=items, name="入力キー")
	shift = bpy.props.BoolProperty(name="Shiftを修飾キーに", default=False)
	ctrl = bpy.props.BoolProperty(name="Ctrlを修飾キーに", default=False)
	alt = bpy.props.BoolProperty(name="Altを修飾キーに", default=False)
	
	def execute(self, context):
		keymap_item = context.window_manager.keyconfigs.default.keymaps[self.key_map].keymap_items.new(self.command, self.type, 'PRESS', False, self.shift, self.ctrl, self.alt)
		for command in self.sub_command.split(","):
			name, value = command.split(":")
			keymap_item.properties[name] = value
		self.report(type={"INFO"}, message="ショートカットを登録しました、必要であれば「ユーザー設定の保存」をしてください")
		return {'FINISHED'}
	def invoke(self, context, event):
		bpy.ops.info.reports_display_update()
		pre_clipboard = context.window_manager.clipboard
		for i in range(10):
			bpy.ops.info.select_all_toggle()
			bpy.ops.info.report_copy()
			if (context.window_manager.clipboard != ""):
				break
		bpy.ops.info.select_all_toggle()
		commands = context.window_manager.clipboard.split("\n")
		context.window_manager.clipboard = pre_clipboard
		if (commands[-1] == ''):
			commands = commands[:-1]
		if (len(commands) <= 0):
			self.report(type={'ERROR'}, message="最後に実行したコマンドが見つかりません")
			return {'CANCELLED'}
		commands.reverse()
		for command in commands:
			if (re.search(r"^bpy\.ops\.", command)):
				self.command = re.search(r"^bpy\.ops\.([^\(]+)", command).groups()[0]
				#options = re.search(r"\((.*)\)$", command).groups()[0]
				#properties = options.split(",")
				break
			elif (re.search(r"^bpy\.context\.", command)):
				if (re.search(r"True$", command) or re.search(r"False$", command)):
					self.command = 'wm.context_toggle'
					self.sub_command = 'data_path:'+re.search(r"^bpy\.context\.([^ ]+)", command).groups()[0]
		return context.window_manager.invoke_props_dialog(self)


################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(RegisterLastCommandKeyconfig.bl_idname, icon="PLUGIN")
	self.layout.operator(ShowShortcutHtml.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.operator(RegisterBlendFile.bl_idname, icon="PLUGIN")
	self.layout.operator(UpdateScrambleAddon.bl_idname, icon="PLUGIN")
