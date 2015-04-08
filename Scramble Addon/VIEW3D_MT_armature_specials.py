# 3Dビュー > アーマチュア編集モード > 「W」キー

import bpy
import re

################
# オペレーター #
################

class CreateMirror(bpy.types.Operator):
	bl_idname = "armature.create_mirror"
	bl_label = "選択ボーンをミラーリング"
	bl_description = "選択中のボーンを任意の軸でミラーリングします"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		obj = context.active_object
		if (obj.type == "ARMATURE"):
			if (obj.mode == "EDIT"):
				preCursorCo = context.space_data.cursor_location[:]
				prePivotPoint = context.space_data.pivot_point
				preUseMirror = context.object.data.use_mirror_x
				
				context.space_data.cursor_location = (0, 0, 0)
				context.space_data.pivot_point = 'CURSOR'
				context.object.data.use_mirror_x = True
				
				selectedBones = context.selected_bones[:]
				bpy.ops.armature.autoside_names(type='XAXIS')
				bpy.ops.armature.duplicate()
				axis = (True, False, False)
				bpy.ops.transform.mirror(constraint_axis=axis)
				bpy.ops.armature.flip_names()
				newBones = []
				for bone in context.selected_bones:
					for pre in selectedBones:
						if (bone.name == pre.name):
							break
					else:
						newBones.append(bone)
				bpy.ops.armature.select_all(action='DESELECT')
				for bone in selectedBones:
					bone.select = True
					bone.select_head = True
					bone.select_tail = True
				bpy.ops.transform.transform(mode='BONE_ROLL', value=(0, 0, 0, 0))
				bpy.ops.armature.select_all(action='DESELECT')
				for bone in newBones:
					bone.select = True
					bone.select_head = True
					bone.select_tail = True
				
				context.space_data.cursor_location = preCursorCo[:]
				context.space_data.pivot_point = prePivotPoint
				context.object.data.use_mirror_x = preUseMirror
			else:
				self.report(type={"ERROR"}, message="エディトモードで実行してください")
		else:
			self.report(type={"ERROR"}, message="アーマチュアオブジェクトではありません")
		return {'FINISHED'}

class CopyBoneName(bpy.types.Operator):
	bl_idname = "armature.copy_bone_name"
	bl_label = "ボーン名をクリップボードにコピー"
	bl_description = "アクティブボーンの名前をクリップボードにコピーします"
	bl_options = {'REGISTER', 'UNDO'}
	
	isObject = bpy.props.BoolProperty(name="オブジェクト名も", default=False)
	
	def execute(self, context):
		if (self.isObject):
			context.window_manager.clipboard = context.active_object.name + ":" + context.active_bone.name
		else:
			context.window_manager.clipboard = context.active_bone.name
		return {'FINISHED'}

class RenameBoneRegularExpression(bpy.types.Operator):
	bl_idname = "armature.rename_bone_regular_expression"
	bl_label = "ボーン名を正規表現で置換"
	bl_description = "(選択中の)ボーン名を正規表現に一致する部分で置換します"
	bl_options = {'REGISTER', 'UNDO'}
	
	isAll = bpy.props.BoolProperty(name="非選択も含め全て", default=False)
	pattern = bpy.props.StringProperty(name="置換前(正規表現)", default="^")
	repl = bpy.props.StringProperty(name="置換後", default="@")
	
	def execute(self, context):
		obj = context.active_object
		if (obj.type == "ARMATURE"):
			if (obj.mode == "EDIT"):
				bones = context.selected_bones
				if (self.isAll):
					bones = obj.data.bones
				for bone in bones:
					bone.name = re.sub(self.pattern, self.repl, bone.name)
			else:
				self.report(type={"ERROR"}, message="エディトモードで実行してください")
		else:
			self.report(type={"ERROR"}, message="アーマチュアオブジェクトではありません")
		return {'FINISHED'}

class RenameOppositeBone(bpy.types.Operator):
	bl_idname = "armature.rename_opposite_bone"
	bl_label = "反対位置にあるボーンをリネーム"
	bl_description = "選択中ボーンのX軸反対側の位置にあるボーンを「○.R ○.L」のように対にします"
	bl_options = {'REGISTER', 'UNDO'}
	
	threshold = bpy.props.FloatProperty(name="位置のしきい値", default=0.00001, min=0, soft_min=0, step=0.001, precision=5)
	
	def execute(self, context):
		obj = context.active_object
		if (obj.type == "ARMATURE"):
			if (obj.mode == "EDIT"):
				arm = obj.data
				bpy.ops.armature.autoside_names(type='XAXIS')
				selectedBones = context.selected_bones[:]
				bpy.ops.armature.select_all(action='DESELECT')
				bpy.ops.object.mode_set(mode='OBJECT')
				threshold = self.threshold
				for bone in selectedBones:
					bone = arm.bones[bone.name]
					head = (-bone.head_local[0], bone.head_local[1], bone.head_local[2])
					tail = (-bone.tail_local[0], bone.tail_local[1], bone.tail_local[2])
					for b in arm.bones:
						if ( (head[0]-threshold) <= b.head_local[0] <= (head[0]+threshold)):
							if ( (head[1]-threshold) <= b.head_local[1] <= (head[1]+threshold)):
								if ( (head[2]-threshold) <= b.head_local[2] <= (head[2]+threshold)):
									if ( (tail[0]-threshold) <= b.tail_local[0] <= (tail[0]+threshold)):
										if ( (tail[1]-threshold) <= b.tail_local[1] <= (tail[1]+threshold)):
											if ( (tail[2]-threshold) <= b.tail_local[2] <= (tail[2]+threshold)):
												b.name = bone.name
												b.select = True
												b.select_head = True
												b.select_tail = True
												break
				bpy.ops.object.mode_set(mode='EDIT')
				bpy.ops.armature.flip_names()
			else:
				self.report(type={"ERROR"}, message="エディトモードで実行してください")
		else:
			self.report(type={"ERROR"}, message="アーマチュアオブジェクトではありません")
		return {'FINISHED'}
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
		self.layout.prop(context.object.data, "use_mirror_x", icon="PLUGIN", text="X軸ミラー編集")
		self.layout.operator(CreateMirror.bl_idname, icon="PLUGIN")
		self.layout.operator(RenameOppositeBone.bl_idname, icon="PLUGIN")
		self.layout.separator()
		self.layout.operator(CopyBoneName.bl_idname, icon="PLUGIN")
		self.layout.operator(RenameBoneRegularExpression.bl_idname, icon="PLUGIN")
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.separator()
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
