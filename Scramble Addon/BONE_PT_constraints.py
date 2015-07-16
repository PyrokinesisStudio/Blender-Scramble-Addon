# 「プロパティ」エリア > 「ボーンコンストレイント」タブ
# "Propaties" Area > "Bone Constraints" Tab

import bpy

################
# オペレーター #
################

class quick_child_constraint(bpy.types.Operator):
	bl_idname = "constraint.quick_child_constraint"
	bl_label = "Quick-child constraints"
	bl_description = "Quickly add child constraint"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		if 'selected_pose_bones' in dir(context):
			if 2 <= len(context.selected_pose_bones):
				return True
		return False
	
	def execute(self, context):
		active_ob = context.active_object
		active_bone = context.active_pose_bone
		for target_bone in context.selected_pose_bones:
			if active_bone.name != target_bone.name:
				break
		const = active_bone.constraints.new('CHILD_OF')
		const.target = active_ob
		const.subtarget = target_bone.name
		override = context.copy()
		override = {'constraint':const}
		bpy.ops.constraint.childof_clear_inverse(override, constraint=const.name, owner='BONE')
		bpy.ops.constraint.childof_set_inverse(override, constraint=const.name, owner='BONE')
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
		self.layout.operator(quick_child_constraint.bl_idname, icon='CONSTRAINT_BONE')
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
