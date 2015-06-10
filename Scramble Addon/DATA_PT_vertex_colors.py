# プロパティ > "メッシュデータ"タブ > "頂点色"パネル

import bpy

################
# オペレーター #
################

class MoveActiveVertexColor(bpy.types.Operator):
	bl_idname = "object.move_active_vertex_color"
	bl_label = "頂点色を移動"
	bl_description = "アクティブなオブジェクトの頂点色を移動して並び替えます"
	bl_options = {'REGISTER', 'UNDO'}
	
	items = [
		('UP', "上へ", "", 1),
		('DOWN', "下へ", "", 2),
		]
	mode = bpy.props.EnumProperty(items=items, name="方向", default="UP")
	
	def execute(self, context):
		obj = context.active_object
		if (not obj):
			self.report(type={'ERROR'}, message="アクティブオブジェクトがありません")
			return {'CANCELLED'}
		if (obj.type != 'MESH'):
			self.report(type={'ERROR'}, message="これはメッシュオブジェクトではありません")
			return {'CANCELLED'}
		me = obj.data
		if (len(me.vertex_colors) <= 1):
			self.report(type={'ERROR'}, message="頂点色数が1つ以下です")
			return {'CANCELLED'}
		if (self.mode == 'UP'):
			if (me.vertex_colors.active_index <= 0):
				return {'CANCELLED'}
			target_index = me.vertex_colors.active_index - 1
		elif (self.mode == 'DOWN'):
			target_index = me.vertex_colors.active_index + 1
			if (len(me.vertex_colors) <= target_index):
				return {'CANCELLED'}
		pre_mode = obj.mode
		bpy.ops.object.mode_set(mode='OBJECT')
		vertex_color = me.vertex_colors.active
		vertex_color_target = me.vertex_colors[target_index]
		for data_name in dir(vertex_color):
			if (data_name[0] != '_' and data_name != 'bl_rna' and data_name != 'rna_type' and data_name != 'data'):
				temp = vertex_color.__getattribute__(data_name)
				temp_target = vertex_color_target.__getattribute__(data_name)
				vertex_color.__setattr__(data_name, temp_target)
				vertex_color_target.__setattr__(data_name, temp)
				vertex_color.__setattr__(data_name, temp_target)
				vertex_color_target.__setattr__(data_name, temp)
		for i in range(len(vertex_color.data)):
			temp = vertex_color.data[i].color[:]
			vertex_color.data[i].color = vertex_color_target.data[i].color[:]
			vertex_color_target.data[i].color = temp[:]
		me.vertex_colors.active_index = target_index
		bpy.ops.object.mode_set(mode=pre_mode)
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	row = self.layout.row()
	sub = row.row(align=True)
	sub.operator(MoveActiveVertexColor.bl_idname, icon='TRIA_UP', text="").mode = 'UP'
	sub.operator(MoveActiveVertexColor.bl_idname, icon='TRIA_DOWN', text="").mode = 'DOWN'
