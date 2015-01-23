import bpy

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

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(DeleteBySelectMode.bl_idname, icon="PLUGIN")
