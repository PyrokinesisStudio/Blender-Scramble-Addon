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

class SelectMoveSymmetryNameBones(bpy.types.Operator):
	bl_idname = "pose.select_move_symmetry_name_bones"
	bl_label = "対称のボーンへ選択を移動"
	bl_description = "X.Rを選択中ならX.Lへ選択を変更、X.LならX.Rへ"
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
		pre_selected_pose_bones = context.selected_pose_bones[:]
		for bone in pre_selected_pose_bones[:]:
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
		for bone in pre_selected_pose_bones[:]:
			arm.bones[bone.name].select = False
		try:
			arm.bones.active = arm.bones[GetMirrorBoneName(arm.bones.active.name)]
		except KeyError:
			arm.bones.active = arm.bones[context.selected_pose_bones[0].name]
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
	bl_label = "名前が対称のボーンを追加選択"
	bl_description = "X.Rを選択中ならX.Lも追加選択、X.LならX.Rも選択"
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

class SelectChildrenEnd(bpy.types.Operator):
	bl_idname = "pose.select_children_end"
	bl_label = "ボーンの末端まで選択"
	bl_description = "選択ボーンの子 → 子ボーンの子...と最後まで選択していきます"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		obj = context.active_object
		if (not obj):
			self.report(type={'ERROR'}, message="アクティブオブジェクトがありません")
			return {'CANCELLED'}
		if (obj.type != 'ARMATURE'):
			self.report(type={'ERROR'}, message="アーマチュアオブジェクトで実行して下さい")
			return {'CANCELLED'}
		arm = obj.data
		selected_bones = context.selected_pose_bones[:]
		for bone in selected_bones:
			bone_children = []
			for b in arm.bones[bone.name].children[:]:
				bone_children.append(b)
			bone_queue = bone_children[:]
			while (0 < len(bone_queue)):
				removed_bone = bone_queue.pop(0)
				for b in removed_bone.children[:]:
					bone_queue.append(b)
					bone_children.append(b)
			for b in bone_children:
				b.select = True
		return {'FINISHED'}

class SelectParentEnd(bpy.types.Operator):
	bl_idname = "pose.select_parent_end"
	bl_label = "ボーンの根本まで選択"
	bl_description = "選択ボーンの親 → 親ボーンの親...と最後まで選択していきます"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		obj = context.active_object
		if (not obj):
			self.report(type={'ERROR'}, message="アクティブオブジェクトがありません")
			return {'CANCELLED'}
		if (obj.type != 'ARMATURE'):
			self.report(type={'ERROR'}, message="アーマチュアオブジェクトで実行して下さい")
			return {'CANCELLED'}
		arm = obj.data
		selected_bones = context.selected_pose_bones[:]
		for bone in selected_bones:
			target_bone = arm.bones[bone.name]
			while target_bone.parent:
				target_bone = target_bone.parent
				target_bone.select = True
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
		self.layout.operator(SelectParentEnd.bl_idname, icon="PLUGIN")
		self.layout.operator(SelectChildrenEnd.bl_idname, icon="PLUGIN")
		self.layout.separator()
		self.layout.operator(SelectSerialNumberNameBone.bl_idname, icon="PLUGIN")
		self.layout.operator(SelectMoveSymmetryNameBones.bl_idname, icon="PLUGIN")
		self.layout.separator()
		self.layout.menu(SelectGroupedMenu.bl_idname, icon="PLUGIN")
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.separator()
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
