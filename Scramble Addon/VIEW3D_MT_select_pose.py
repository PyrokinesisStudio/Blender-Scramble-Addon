# 3Dビュー > ポーズモード > 「選択」メニュー

import bpy

################
# オペレーター #
################

class SelectSameConstraintBone(bpy.types.Operator):
	bl_idname = "pose.select_same_constraint_bone"
	bl_label = "同じコンストレイントのボーンを選択"
	bl_description = "アクティブボーンと同じ種類のコンストレイントを持ったボーンを追加選択します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		active = context.active_pose_bone
		activeConstraints = []
		for const in active.constraints:
			activeConstraints.append(const.type)
		for bone in context.visible_pose_bones:
			constraints = []
			for const in bone.constraints:
				constraints.append(const.type)
			if (len(activeConstraints) == len(constraints)):
				for i in range(len(constraints)):
					if (activeConstraints[i] != constraints[i]):
						break
				else:
					context.active_object.data.bones[bone.name].select = True
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(SelectSameConstraintBone.bl_idname, icon="PLUGIN")
