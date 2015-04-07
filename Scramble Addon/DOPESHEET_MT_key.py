# ドープシート > 「キー」メニュー

import bpy

################
# オペレーター #
################

class DeleteUnmessage(bpy.types.Operator):
	bl_idname = "action.delete_unmessage"
	bl_label = "キーフレームを削除 (確認しない)"
	bl_description = "選択した全てのキーフレームを確認せずに削除します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		bpy.ops.action.delete()
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューのオン/オフの判定
def IsMenuEnable(self_id):
	for string in bpy.context.user_preferences.addons["Scramble Addon"].preferences.is_enables.split(','):
		splited = string.split(':')
		if (len(splited) != 2):
			continue
		id = splited[0]
		value = splited[1]
		if (id == self_id):
			if (value == "0"):
				return False
			else:
				return True
	return True

# メニューを登録する関数
def menu(self, context):
	if (IsMenuEnable(__name__.split('.')[-1])):
		self.layout.separator()
		self.layout.operator(DeleteUnmessage.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
