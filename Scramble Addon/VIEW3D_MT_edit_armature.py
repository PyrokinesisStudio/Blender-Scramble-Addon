import bpy

##############
# その他関数 #
##############

################
# オペレーター #
################

class Move3DCursor(bpy.types.Operator):
	bl_idname = "armature.move_3d_cursor"
	bl_label = "ボーンをそのまま3Dカーソルの位置へ"
	bl_description = "相対的なボーンの尾(根本でも可)の位置をそのままに、ボーンを3Dカーソルの位置へ移動させます"
	bl_options = {'REGISTER', 'UNDO'}
	
	isTail = bpy.props.BoolProperty(name="尾を移動", default=False)
	
	def execute(self, context):
		for bone in context.selected_bones:
			if (not self.isTail):
				co = bone.tail - bone.head
				bone.head = context.space_data.cursor_location
				bone.tail = context.space_data.cursor_location + co
			else:
				co = bone.head - bone.tail
				bone.head = context.space_data.cursor_location + co
				bone.tail = context.space_data.cursor_location
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(Move3DCursor.bl_idname, icon="PLUGIN")