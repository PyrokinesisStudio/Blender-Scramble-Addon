# 3Dビュー > ポーズモード > 「選択」メニュー

import bpy
import re

################
# オペレーター #
################

class SelectSerialNumberNameBone(bpy.types.Operator):
	bl_idname = "pose.select_serial_number_name_bone"
	bl_label = "連番の付いたボーンを選択"
	bl_description = "X.001 のように番号の付いた名前のボーンを選択します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		obj = context.active_object
		if (obj.type != 'ARMATURE'):
			self.report(type={"ERROR"}, message="アーマチュアオブジェクトで実行して下さい")
			return {"CANCELLED"}
		arm = obj.data
		for bone in context.visible_pose_bones[:]:
			if (re.search(r'\.\d+$', bone.name)):
				arm.bones[bone.name].select = True
		return {'FINISHED'}

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

class SelectSameNameBones(bpy.types.Operator):
	bl_idname = "pose.select_same_name_bones"
	bl_label = "同じ名前のボーンを選択"
	bl_description = "X X.001 X.002 などのボーン名を同じ名前とみなして選択します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		obj = context.active_object
		if (obj.type != 'ARMATURE'):
			self.report(type={"ERROR"}, message="アーマチュアオブジェクトで実行して下さい")
			return {"CANCELLED"}
		arm = obj.data
		name_base = context.active_pose_bone.name
		if (re.search(r'\.\d+$', name_base)):
			name_base = re.search(r'^(.*)\.\d+$', name_base).groups()[0]
		for bone in context.visible_pose_bones[:]:
			if (re.search('^'+name_base+r'\.\d+$', bone.name) or name_base == bone.name):
				arm.bones[bone.name].select = True
		return {'FINISHED'}

class SelectSymmetryNameBones(bpy.types.Operator):
	bl_idname = "pose.select_symmetry_name_bones"
	bl_label = "名前が対のボーンを選択"
	bl_description = "X.Rを選択中ならX.Lも選択、X.LならX.Rも選択"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		def GetMirrorBoneName(name):
			new_name = re.sub(r'([\._])L$', r"\1R", name)
			if (new_name != name): return new_name
			new_name = re.sub(r'([\._])l$', r"\1r", name)
			if (new_name != name): return new_name
			new_name = re.sub(r'([\._])R$', r"\1L", name)
			if (new_name != name): return new_name
			new_name = re.sub(r'([\._])r$', r"\1l", name)
			if (new_name != name): return new_name
			new_name = re.sub(r'([\._])L([\._]\d+)$', r"\1R\2", name)
			if (new_name != name): return new_name
			new_name = re.sub(r'([\._])l([\._]\d+)$', r"\1r\2", name)
			if (new_name != name): return new_name
			new_name = re.sub(r'([\._])R([\._]\d+)$', r"\1L\2", name)
			if (new_name != name): return new_name
			new_name = re.sub(r'([\._])r([\._]\d+)$', r"\1l\2", name)
			if (new_name != name): return new_name
			return name
		obj = context.active_object
		if (obj.type != 'ARMATURE'):
			self.report(type={"ERROR"}, message="アーマチュアオブジェクトで実行して下さい")
			return {"CANCELLED"}
		arm = obj.data
		for bone in context.selected_pose_bones[:]:
			mirror_name = GetMirrorBoneName(bone.name)
			if (mirror_name == bone.name):
				self.report(type={"WARNING"}, message=bone.name+"はミラーに対応した名前ではありません、無視します")
				continue
			try:
				arm.bones[mirror_name]
			except KeyError:
				self.report(type={"WARNING"}, message=bone.name+"の対になるボーンが存在しないので無視します")
				continue
			arm.bones[mirror_name].select = True
		return {'FINISHED'}

################
# サブメニュー #
################

class SelectGroupedMenu(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_select_pose_grouped"
	bl_label = "関係で選択 (拡張)"
	bl_description = "同じプロパティでまとめた可視ボーンをすべて選択する機能のメニューです"
	
	def draw(self, context):
		self.layout.operator('pose.select_grouped', text="レイヤー", icon="PLUGIN").type = 'LAYER'
		self.layout.operator('pose.select_grouped', text="グループ", icon="PLUGIN").type = 'GROUP'
		self.layout.operator('pose.select_grouped', text="キーイングセット", icon="PLUGIN").type = 'KEYINGSET'
		self.layout.separator()
		self.layout.operator(SelectSameNameBones.bl_idname, text="ボーン名", icon="PLUGIN")
		self.layout.operator(SelectSymmetryNameBones.bl_idname, text="名前が対称", icon="PLUGIN")
		self.layout.operator(SelectSameConstraintBone.bl_idname, text="コンストレイント", icon="PLUGIN")

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(SelectSerialNumberNameBone.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.menu(SelectGroupedMenu.bl_idname, icon="PLUGIN")
