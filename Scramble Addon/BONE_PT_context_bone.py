# 「プロパティ」エリア > 「ボーン」タブ

import bpy

################
# オペレーター #
################

class CopyBoneName(bpy.types.Operator):
	bl_idname = "object.copy_bone_name"
	bl_label = "Copy to Clipboard bone name"
	bl_description = "To the Clipboard copies the bone name"
	bl_options = {'REGISTER'}
	
	@classmethod
	def poll(cls, context):
		if (context.active_bone):
			if (context.window_manager.clipboard != context.active_bone.name):
				return True
		if (context.active_pose_bone):
			if (context.window_manager.clipboard != context.active_pose_bone.name):
				return True
		return False
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
			self.layout.operator(CopyBoneName.bl_idname, icon='COPYDOWN', text="Copy the name to the Clipboard")
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
