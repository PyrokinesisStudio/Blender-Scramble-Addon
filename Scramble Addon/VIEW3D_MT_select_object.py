# 3Dビュー > オブジェクトモード > 「選択」メニュー

import bpy
import re

################
# オペレーター #
################

class SelectGroupedName(bpy.types.Operator):
	bl_idname = "object.select_grouped_name"
	bl_label = "同じ名前のオブジェクトを選択"
	bl_description = "アクティブなオブジェクトと同じ名前 (X X.001 X.002など) の可視オブジェクトを選択します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		name_base = context.active_object.name
		if (re.search(r'\.\d+$', name_base)):
			name_base = re.search(r'^(.*)\.\d+$', name_base).groups()[0]
		for obj in context.selectable_objects:
			if (re.search('^'+name_base+r'\.\d+$', obj.name) or name_base == obj.name):
				obj.select = True
		return {'FINISHED'}

class SelectGroupedMaterial(bpy.types.Operator):
	bl_idname = "object.select_grouped_material"
	bl_label = "同じマテリアル構造のオブジェクトを選択"
	bl_description = "アクティブなオブジェクトのマテリアル構造と同じ可視オブジェクトを選択します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		def GetMaterialList(slots):
			list = []
			for slot in slots:
				if (slot.material):
					list.append(slot.material.name)
			return list
		activeMats = GetMaterialList(context.active_object.material_slots)
		if (0 < len(activeMats)):
			for obj in context.selectable_objects:
				if (activeMats == GetMaterialList(obj.material_slots)):
					obj.select = True
		return {'FINISHED'}

class SelectGroupedModifiers(bpy.types.Operator):
	bl_idname = "object.select_grouped_modifiers"
	bl_label = "同じモディファイア構造のオブジェクトを選択"
	bl_description = "アクティブなオブジェクトのモディファイア構造が同じ可視オブジェクトを選択します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		def GetModifiersString(obj):
			str = ""
			for mod in obj.modifiers:
				str = str + mod.type
			return str
		active_modifiers = GetModifiersString(context.active_object)
		active_type = context.active_object.type
		for obj in context.selectable_objects:
			if (GetModifiersString(obj) == active_modifiers and active_type == obj.type):
				obj.select= True
		return {'FINISHED'}

class SelectGroupedSubsurfLevel(bpy.types.Operator):
	bl_idname = "object.select_grouped_subsurf_level"
	bl_label = "同じサブサーフレベルのオブジェクトを選択"
	bl_description = "アクティブなオブジェクトのサブサーフレベルが同じ可視オブジェクトを選択します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		def GetSubsurfLevel(obj):
			level = 0
			for mod in obj.modifiers:
				if (mod.type == 'SUBSURF'):
					level += mod.levels
			return level
		active_subsurf_level = GetSubsurfLevel(context.active_object)
		active_type = context.active_object.type
		for obj in context.selectable_objects:
			if (GetSubsurfLevel(obj) == active_subsurf_level and active_type == obj.type):
				obj.select= True
		return {'FINISHED'}

class SelectGroupedArmatureTarget(bpy.types.Operator):
	bl_idname = "object.select_grouped_armature_target"
	bl_label = "同じアーマチュアで変形しているオブジェクトを選択"
	bl_description = "アクティブなオブジェクトと同じアーマチュアで変形している可視オブジェクトを選択します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		def GetArmatureTarget(obj):
			target = []
			for mod in obj.modifiers:
				if (mod.type == 'ARMATURE'):
					if (mod.object):
						target.append(mod.object.name)
					else:
						target.append("")
			return set(target)
		active_armature_targets = GetArmatureTarget(context.active_object)
		if (len(active_armature_targets) == 0):
			self.report(type={"ERROR"}, message="アクティブオブジェクトにアーマチュアモディファイアがありません")
			return {"CANCELLED"}
		active_type = context.active_object.type
		for obj in context.selectable_objects:
			if (len(GetArmatureTarget(obj).intersection(active_armature_targets)) == len(active_armature_targets) and active_type == obj.type):
				obj.select= True
		return {'FINISHED'}

################
# サブメニュー #
################

class SelectGroupedEX(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_select_object_grouped_ex"
	bl_label = "関係で選択 (拡張)"
	bl_description = "プロパティによってグループ化されたすべての可視オブジェクトを選択します"
	
	def draw(self, context):
		self.layout.operator("object.select_grouped", text="子").type = 'CHILDREN_RECURSIVE'
		self.layout.operator("object.select_grouped", text="直接の子").type = 'CHILDREN'
		self.layout.operator("object.select_grouped", text="親").type = 'PARENT'
		self.layout.operator("object.select_grouped", text="兄弟").type = 'SIBLINGS'
		self.layout.operator("object.select_grouped", text="タイプ").type = 'TYPE'
		self.layout.operator("object.select_grouped", text="レイヤー").type = 'LAYER'
		self.layout.operator("object.select_grouped", text="グループ").type = 'GROUP'
		self.layout.operator("object.select_grouped", text="パス").type = 'PASS'
		self.layout.operator("object.select_grouped", text="カラー").type = 'COLOR'
		self.layout.operator("object.select_grouped", text="プロパティ").type = 'PROPERTIES'
		self.layout.operator("object.select_grouped", text="キーイングセット").type = 'KEYINGSET'
		self.layout.operator("object.select_grouped", text="ランプタイプ").type = 'LAMP_TYPE'
		self.layout.separator()
		self.layout.operator(SelectGroupedName.bl_idname, text="オブジェクト名", icon="PLUGIN")
		self.layout.operator(SelectGroupedMaterial.bl_idname, text="マテリアル", icon="PLUGIN")
		self.layout.operator(SelectGroupedModifiers.bl_idname, text="モディファイア", icon="PLUGIN")
		self.layout.operator(SelectGroupedSubsurfLevel.bl_idname, text="サブサーフレベル", icon="PLUGIN")
		self.layout.operator(SelectGroupedArmatureTarget.bl_idname, text="同アーマチュア変形", icon="PLUGIN")

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.menu(SelectGroupedEX.bl_idname, icon="PLUGIN")
