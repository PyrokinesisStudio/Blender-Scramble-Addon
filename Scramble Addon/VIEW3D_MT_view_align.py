import bpy

################
# オペレーター #
################

class ViewSelectedEX(bpy.types.Operator):
	bl_idname = "view3d.view_selected_ex"
	bl_label = "選択部分を視点の中心に"
	bl_description = "選択中の物に3D視点の中心を合わせます(ズームはしません)"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		co = bpy.context.space_data.cursor_location[:]
		bpy.ops.view3d.snap_cursor_to_selected()
		bpy.ops.view3d.view_center_cursor()
		bpy.context.space_data.cursor_location = co
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(ViewSelectedEX.bl_idname, icon="PLUGIN")
