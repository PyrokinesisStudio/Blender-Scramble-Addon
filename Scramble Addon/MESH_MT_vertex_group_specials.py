# プロパティ > 「オブジェクトデータ」タブ > 頂点グループ一覧右の▼

import bpy
import re

################
# オペレーター #
################

class RemoveEmptyVertexGroups(bpy.types.Operator):
	bl_idname = "mesh.remove_empty_vertex_groups"
	bl_label = "空の頂点グループを削除"
	bl_description = "メッシュにウェイトが割り当てられていない頂点グループを削除します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		obj = context.active_object
		if (obj.type == "MESH"):
			for vg in obj.vertex_groups:
				for vert in obj.data.vertices:
					try:
						if (vg.weight(vert.index) > 0.0):
							break
					except RuntimeError:
						pass
				else:
					obj.vertex_groups.remove(vg)
		return {'FINISHED'}

class AddOppositeVertexGroups(bpy.types.Operator):
	bl_idname = "mesh.add_opposite_vertex_groups"
	bl_label = "ミラーの対になる空頂点グループを追加"
	bl_description = ".L .R などミラーの命令規則に従って付けられたボーンの対になる空の新規ボーンを追加します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		obj = context.active_object
		if (obj.type == "MESH"):
			vgs = obj.vertex_groups[:]
			for vg in vgs:
				oldName = vg.name
				newName = re.sub(r'([_\.-])L$', r'\1R', vg.name)
				if (oldName == newName):
					newName = re.sub(r'([_\.-])R$', r'\1L', vg.name)
					if (oldName == newName):
						newName = re.sub(r'([_\.-])l$', r'\1r', vg.name)
						if (oldName == newName):
							newName = re.sub(r'([_\.-])r$', r'\1l', vg.name)
							if (oldName == newName):
								newName = re.sub(r'[lL][eE][fF][tT]$', r'Right', vg.name)
								if (oldName == newName):
									newName = re.sub(r'[rR][iI][gG][hH][tT]$', r'Left', vg.name)
									if (oldName == newName):
										newName = re.sub(r'^[lL][eE][fF][tT]', r'Right', vg.name)
										if (oldName == newName):
											newName = re.sub(r'^[rR][iI][gG][hH][tT]', r'Left', vg.name)
				for v in vgs:
					if (newName.lower() == v.name.lower()):
						break
				else:
					obj.vertex_groups.new(newName)
		return {'FINISHED'}

class SelectVertexGroupsTop(bpy.types.Operator):
	bl_idname = "mesh.select_vertex_groups_top"
	bl_label = "一番上を選択"
	bl_description = "頂点グループの一番上の項目を選択します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		context.active_object.vertex_groups.active_index = 0
		return {'FINISHED'}
class SelectVertexGroupsBottom(bpy.types.Operator):
	bl_idname = "mesh.select_vertex_groups_bottom"
	bl_label = "一番下を選択"
	bl_description = "頂点グループの一番下の項目を選択します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		context.active_object.vertex_groups.active_index = len(context.active_object.vertex_groups) - 1
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(SelectVertexGroupsTop.bl_idname, icon="PLUGIN")
	self.layout.operator(SelectVertexGroupsBottom.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.operator(RemoveEmptyVertexGroups.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.operator(AddOppositeVertexGroups.bl_idname, icon="PLUGIN")
