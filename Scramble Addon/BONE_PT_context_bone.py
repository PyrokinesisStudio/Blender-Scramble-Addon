# 「プロパティ」エリア > 「ボーン」タブ

import bpy

################
# オペレーター #
################

class CopyBoneName(bpy.types.Operator):
	bl_idname = "object.copy_bone_name"
	bl_label = "ボーン名をクリップボードにコピー"
	bl_description = "ボーン名をクリップボードにコピーします"
	bl_options = {'REGISTER'}
	
	@classmethod
	def poll(cls, context):
		if (not context.active_bone and not context.active_pose_bone):
			return False
		if (context.window_manager.clipboard == context.active_bone.name):
			return False
		if (context.window_manager.clipboard == context.active_pose_bone.name):
			return False
		return True
	def execute(self, context):
		if (context.active_bone):
			context.window_manager.clipboard = context.active_bone.name
			self.report(type={'INFO'}, message=context.active_bone.name)
		elif (context.active_pose_bone):
			context.window_manager.clipboard = context.active_pose_bone.name
			self.report(type={'INFO'}, message=context.active_pose_bone.name)
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
		if (context.edit_bone or context.bone):
			self.layout.operator(CopyBoneName.bl_idname, icon='COPYDOWN', text="名前をクリップボードにコピー")
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
