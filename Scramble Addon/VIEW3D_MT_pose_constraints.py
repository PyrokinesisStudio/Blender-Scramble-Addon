# 3Dビュー > ポーズモード > 「ポーズ」メニュー > 「コンストレイント」メニュー

import bpy

################
# オペレーター #
################

class ConstraintIKToLimitRotation(bpy.types.Operator):
	bl_idname = "pose.constraint_ik_to_limit_rotation"
	bl_label = "IK回転制限をコンストレイント化"
	bl_description = "IKの回転制限設定をコンストレイントの回転制限設定にコピー"
	bl_options = {'REGISTER', 'UNDO'}
	
	isAdd = bpy.props.BoolProperty(name="無い場合コンストレイントを追加", default=True)
	isLocal = bpy.props.BoolProperty(name="ローカル空間", default=True)
	
	def execute(self, context):
		for bone in context.selected_pose_bones:
			if (self.isAdd):
				for const in bone.constraints:
					if (const.type == "LIMIT_ROTATION"):
						break
				else:
					bone.constraints.new("LIMIT_ROTATION")
			for const in bone.constraints:
				if (const.type == "LIMIT_ROTATION"):
					const.use_limit_x = bone.use_ik_limit_x
					const.use_limit_y = bone.use_ik_limit_y
					const.use_limit_z = bone.use_ik_limit_z
					const.min_x = bone.ik_min_x
					const.min_y = bone.ik_min_y
					const.min_z = bone.ik_min_z
					const.max_x = bone.ik_max_x
					const.max_y = bone.ik_max_y
					const.max_z = bone.ik_max_z
					if (self.isLocal):
						const.owner_space = "LOCAL"
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
		self.layout.operator(ConstraintIKToLimitRotation.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
