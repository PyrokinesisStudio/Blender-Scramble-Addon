# 3Dビュー > オブジェクトモード > 「選択」メニュー

import bpy

################
# オペレーター #
################

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
		self.layout.operator(SelectGroupedMaterial.bl_idname, text="マテリアル", icon="PLUGIN")

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.menu(SelectGroupedEX.bl_idname, icon="PLUGIN")
