# 3Dビュー > メッシュ編集モード > 「X」キー

import bpy
import bmesh

################
# オペレーター #
################

class DeleteBySelectMode(bpy.types.Operator):
	bl_idname = "mesh.delete_by_select_mode"
	bl_label = "選択モードと同じ要素を削除"
	bl_description = "現在のメッシュ選択モードと同じ要素(頂点・辺・面)を削除します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		mode = context.tool_settings.mesh_select_mode[:]
		if (mode[0]):
			bpy.ops.mesh.delete(type="VERT")
		elif (mode[1]):
			bpy.ops.mesh.delete(type="EDGE")
		elif (mode[2]):
			bpy.ops.mesh.delete(type="FACE")
		return {'FINISHED'}

class DeleteHideVertex(bpy.types.Operator):
	bl_idname = "mesh.delete_hide_vertex"
	bl_label = "隠している頂点を削除"
	bl_description = "隠している状態の頂点を全て削除します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		obj = context.active_object
		if (obj.type != 'MESH'):
			self.report(type={"ERROR"}, message="メッシュオブジェクトではありません")
			return {"CANCELLED"}
		me = obj.data
		bm = bmesh.from_edit_mesh(me)
		for vert in bm.verts[:]:
			if (vert.hide):
				bm.verts.remove(vert)
		bmesh.update_edit_mesh(me)
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(DeleteBySelectMode.bl_idname, icon="PLUGIN")
	self.layout.operator(DeleteHideVertex.bl_idname, icon="PLUGIN")
	self.layout.operator('mesh.dissolve_mode')
