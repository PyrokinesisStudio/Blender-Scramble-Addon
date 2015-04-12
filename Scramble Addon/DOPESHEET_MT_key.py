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

class CreanAndDelete(bpy.types.Operator):
	bl_idname = "action.crean_and_delete"
	bl_label = "キーフレームを掃除+削除"
	bl_description = "重複したキーフレームを削除、その上でキーフレームが1つしか無い場合はそれも削除します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		bpy.ops.action.clean()
		for action in bpy.data.actions[:]:
			for fcurve in action.fcurves[:]:
				if (len(fcurve.keyframe_points) <= 1):
					action.fcurves.remove(fcurve)
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
		self.layout.operator(DeleteUnmessage.bl_idname, icon="PLUGIN")
		self.layout.operator(CreanAndDelete.bl_idname, icon="PLUGIN")
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.separator()
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
