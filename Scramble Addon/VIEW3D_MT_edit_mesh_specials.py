import bpy

################
# オペレーター #
################

class PaintSelectedVertexColor(bpy.types.Operator):
	bl_idname = "mesh.paint_selected_vertex_color"
	bl_label = "選択頂点の頂点カラーを塗り潰す"
	bl_description = "選択中の頂点のアクティブ頂点カラーを指定色で塗り潰します"
	bl_options = {'REGISTER', 'UNDO'}
	
	color = bpy.props.FloatVectorProperty(name="色", default=(1, 1, 1), step=1, precision=3, subtype='COLOR', min=0, max=1, soft_min=0, soft_max=1)
	
	def execute(self, context):
		activeObj = context.active_object
		me = activeObj.data
		bpy.ops.object.mode_set(mode='OBJECT')
		i = 0
		for poly in me.polygons:
			for vert in poly.vertices:
				if (me.vertices[vert].select):
					me.vertex_colors.active.data[i].color = self.color
				i += 1
		bpy.ops.object.mode_set(mode='EDIT')
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.prop(context.object.data, "use_mirror_x", icon="PLUGIN", text="X軸ミラー編集")
	self.layout.separator()
	self.layout.operator(PaintSelectedVertexColor.bl_idname, icon="PLUGIN")
