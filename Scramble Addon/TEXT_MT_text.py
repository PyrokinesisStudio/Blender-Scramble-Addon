# テキストエディター > 「テキスト」メニュー

import bpy
import os, subprocess

################
# オペレーター #
################

class ExternalEdit(bpy.types.Operator):
	bl_idname = "text.external_edit"
	bl_label = "外部エディターで編集"
	bl_description = "ユーザー設定のファイルタブで設定した外部エディターでテキストを開きます"
	bl_options = {'REGISTER', 'UNDO'}
	
	index = bpy.props.IntProperty(name="使用する番号", default=1, min=1, max=3, soft_min=1, soft_max=3)
	
	@classmethod
	def poll(cls, context):
		if (not context.edit_text):
			return False
		if (context.edit_text.filepath == ""):
			return False
		return True
	def execute(self, context):
		path = bpy.path.abspath(context.edit_text.filepath)
		if (self.index == 1):
			editor_path = context.user_preferences.addons["Scramble Addon"].preferences.text_editor_path_1
		elif (self.index == 2):
			editor_path = context.user_preferences.addons["Scramble Addon"].preferences.text_editor_path_2
		elif (self.index == 3):
			editor_path = context.user_preferences.addons["Scramble Addon"].preferences.text_editor_path_3
		subprocess.Popen([editor_path, path])
		return {'FINISHED'}

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
		if (context.user_preferences.addons["Scramble Addon"].preferences.text_editor_path_1):
			path = os.path.basename(context.user_preferences.addons["Scramble Addon"].preferences.text_editor_path_1)
			name, ext = os.path.splitext(path)
			self.layout.operator(ExternalEdit.bl_idname, icon="PLUGIN", text=name+" で開く").index = 1
		if (context.user_preferences.addons["Scramble Addon"].preferences.text_editor_path_2):
			path = os.path.basename(context.user_preferences.addons["Scramble Addon"].preferences.text_editor_path_2)
			name, ext = os.path.splitext(path)
			self.layout.operator(ExternalEdit.bl_idname, icon="PLUGIN", text=name+" で開く").index = 2
		if (context.user_preferences.addons["Scramble Addon"].preferences.text_editor_path_3):
			path = os.path.basename(context.user_preferences.addons["Scramble Addon"].preferences.text_editor_path_3)
			name, ext = os.path.splitext(path)
			self.layout.operator(ExternalEdit.bl_idname, icon="PLUGIN", text=name+" で開く").index = 3
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.separator()
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
