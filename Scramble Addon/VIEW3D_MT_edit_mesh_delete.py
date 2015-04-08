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

class DeleteHideMesh(bpy.types.Operator):
	bl_idname = "mesh.delete_hide_mesh"
	bl_label = "隠している部分を削除"
	bl_description = "隠している状態のメッシュを全て削除します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		obj = context.active_object
		if (obj.type != 'MESH'):
			self.report(type={"ERROR"}, message="メッシュオブジェクトではありません")
			return {"CANCELLED"}
		me = obj.data
		bm = bmesh.from_edit_mesh(me)
		for face in bm.faces[:]:
			if (face.hide):
				bm.faces.remove(face)
		for edge in bm.edges[:]:
			if (edge.hide):
				bm.edges.remove(edge)
		for vert in bm.verts[:]:
			if (vert.hide):
				bm.verts.remove(vert)
		bmesh.update_edit_mesh(me)
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
		self.layout.operator(DeleteBySelectMode.bl_idname, icon="PLUGIN")
		self.layout.operator(DeleteHideMesh.bl_idname, icon="PLUGIN")
		self.layout.operator('mesh.dissolve_mode')
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.separator()
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
