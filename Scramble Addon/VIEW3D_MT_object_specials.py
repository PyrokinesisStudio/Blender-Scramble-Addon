import bpy
import re

##############
# その他関数 #
##############

################
# オペレーター #
################

class CopyObjectName(bpy.types.Operator):
	bl_idname = "object.copy_object_name"
	bl_label = "オブジェクト名をクリップボードにコピー"
	bl_description = "アクティブなオブジェクトの名前をクリップボードにコピーします"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		context.window_manager.clipboard = context.active_object.name
		return {'FINISHED'}

class RenameObjectRegularExpression(bpy.types.Operator):
	bl_idname = "object.rename_object_regular_expression"
	bl_label = "オブジェクト名を正規表現で置換"
	bl_description = "選択中のオブジェクトの名前を正規表現で置換します"
	bl_options = {'REGISTER', 'UNDO'}
	
	pattern = bpy.props.StringProperty(name="置換前(正規表現)", default="")
	repl = bpy.props.StringProperty(name="置換後", default="")
	
	def execute(self, context):
		for obj in context.selected_objects:
			obj.name = re.sub(self.pattern, self.repl, obj.name)
		return {'FINISHED'}

class EqualizeObjectNameAndDataName(bpy.types.Operator):
	bl_idname = "object.equalize_objectname_and_dataname"
	bl_label = "オブジェクト名とデータ名を同じにする"
	bl_description = "選択中のオブジェクトのオブジェクト名とデータ名を同じにします"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		for obj in context.selected_objects:
			if (obj and obj.data):
				obj.data.name = obj.name
		return {'FINISHED'}

class AddVertexColorSelectedObject(bpy.types.Operator):
	bl_idname = "object.add_vertex_color_selected_object"
	bl_label = "頂点カラーを一括追加"
	bl_description = "選択中のメッシュオブジェクト全てに色と名前を指定して頂点カラーを追加します"
	bl_options = {'REGISTER', 'UNDO'}
	
	name = bpy.props.StringProperty(name="頂点カラー名", default="Col")
	color = bpy.props.FloatVectorProperty(name="頂点カラー", default=(0.0, 0.0, 0.0), min=0, max=1, soft_min=0, soft_max=1, step=10, precision=3, subtype='COLOR')
	
	def execute(self, context):
		for obj in context.selected_objects:
			if (obj.type == "MESH"):
				me = obj.data
				try:
					col = me.vertex_colors[self.name]
				except KeyError:
					col = me.vertex_colors.new(self.name)
				for data in col.data:
					data.color = self.color
		return {'FINISHED'}

class CreateRopeMesh(bpy.types.Operator):
	bl_idname = "object.create_rope_mesh"
	bl_label = "カーブからロープ状のメッシュを作成"
	bl_description = "アクティブなカーブオブジェクトに沿ったロープや蛇のようなメッシュを新規作成します"
	bl_options = {'REGISTER', 'UNDO'}
	
	vertices = bpy.props.IntProperty(name="頂点数", default=32, min=3, soft_min=3, step=1)
	radius = bpy.props.FloatProperty(name="半径", default=0.1, step=1, precision=3)
	number_cuts = bpy.props.IntProperty(name="分割数", default=32, min=1, soft_min=1, step=1)
	resolution_u = bpy.props.IntProperty(name="カーブの解像度", default=64, min=1, soft_min=1, step=1)
	
	def execute(self, context):
		activeObj = context.active_object
		pre_use_stretch = activeObj.data.use_stretch
		pre_use_deform_bounds = activeObj.data.use_deform_bounds
		
		bpy.ops.mesh.primitive_cylinder_add(vertices=self.vertices, radius=self.radius, depth=1, end_fill_type='NOTHING', view_align=False, enter_editmode=True, location=(0, 0, 0), rotation=(0, 1.5708, 0))
		bpy.ops.mesh.select_all(action='DESELECT')
		context.tool_settings.mesh_select_mode = [False, True, False]
		bpy.ops.mesh.select_non_manifold()
		bpy.ops.mesh.select_all(action='INVERT')
		bpy.ops.mesh.subdivide(number_cuts=self.number_cuts, smoothness=0)
		bpy.ops.object.mode_set(mode='OBJECT')
		
		meshObj = context.active_object
		modi = meshObj.modifiers.new("temp", 'CURVE')
		modi.object = activeObj
		activeObj.data.use_stretch = True
		activeObj.data.use_deform_bounds = True
		activeObj.data.resolution_u = self.resolution_u
		bpy.ops.object.modifier_apply(apply_as='DATA', modifier=modi.name)
		
		activeObj.data.use_stretch = pre_use_stretch
		activeObj.data.use_deform_bounds = pre_use_deform_bounds
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(CopyObjectName.bl_idname, icon="PLUGIN")
	self.layout.operator(RenameObjectRegularExpression.bl_idname, icon="PLUGIN")
	self.layout.operator(EqualizeObjectNameAndDataName.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.operator(AddVertexColorSelectedObject.bl_idname, icon="PLUGIN")
	if (context.active_object):
		if (context.active_object.type == "CURVE"):
			self.layout.separator()
			self.layout.operator(CreateRopeMesh.bl_idname, icon="PLUGIN")
