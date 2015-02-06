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

class ApplySolidify(bpy.types.Operator):
	bl_idname = "mesh.apply_solidify"
	bl_label = "選択部分に厚みを付ける"
	bl_description = "選択中の面に厚みを付けます"
	bl_options = {'REGISTER', 'UNDO'}
	
	thickness = bpy.props.FloatProperty(name="厚み", default=0.01, min=-10, soft_min=-10, step=0.1, precision=4)
	offset = bpy.props.FloatProperty(name="オフセット", default=-1, min=-1, max=1, soft_min=-1, soft_max=1, step=10, precision=4)
	
	def execute(self, context):
		activeObj = context.active_object
		me = activeObj.data
		bpy.ops.mesh.separate(type='SELECTED')
		bpy.ops.object.mode_set(mode='OBJECT')
		for obj in context.selected_objects:
			if (activeObj.name != obj.name):
				tempObj = obj
		modi = tempObj.modifiers.new("temp", 'SOLIDIFY')
		modi.thickness = self.thickness
		modi.offset = self.offset
		context.scene.objects.active = tempObj
		bpy.ops.object.mode_set(mode='EDIT')
		bpy.ops.mesh.select_all(action='SELECT')
		bpy.ops.object.mode_set(mode='OBJECT')
		bpy.ops.object.modifier_apply(apply_as='DATA', modifier=modi.name)
		bpy.ops.object.select_all(action='DESELECT')
		activeObj.select = True
		tempObj.select = True
		context.scene.objects.active = activeObj
		bpy.ops.object.join()
		bpy.ops.object.mode_set(mode='EDIT')
		return {'FINISHED'}

class SelectTopShape(bpy.types.Operator):
	bl_idname = "mesh.select_top_shape"
	bl_label = "一番上のシェイプを選択"
	bl_description = "リストの一番上にあるシェイプキーを選択します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		context.active_object.active_shape_key_index = 0
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.operator(SelectTopShape.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.prop(context.object.data, "use_mirror_x", icon="PLUGIN", text="X軸ミラー編集")
	self.layout.separator()
	self.layout.operator(PaintSelectedVertexColor.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.operator(ApplySolidify.bl_idname, icon="PLUGIN")
