import bpy

##############
# その他関数 #
##############

################
# オペレーター #
################

class AddSphereOnlySquare(bpy.types.Operator):
	bl_idname = "mesh.add_sphere_only_square"
	bl_label = "四角ポリゴン球"
	bl_description = "四角ポリゴンのみで構成された球体メッシュを追加します"
	bl_options = {'REGISTER', 'UNDO'}
	
	level = bpy.props.IntProperty(name="分割数", default=2, step=1, min=1, max=6, soft_min=1, soft_max=6)
	radius = bpy.props.FloatProperty(name="半径(大体)", default=1.0, step=1, precision=3)
	view_align = bpy.props.BoolProperty(name="視点に揃える", default=False)
	location = bpy.props.FloatVectorProperty(name="位置", default=(0.0, 0.0, 0.0), step=1, precision=3)
	rotation = bpy.props.IntVectorProperty(name="回転", default=(0, 0, 0), step=1)
	enter_editmode = False
	
	def execute(self, context):
		bpy.ops.mesh.primitive_cube_add(radius=self.radius, view_align=self.view_align, location=self.location, rotation=self.rotation)
		bpy.ops.object.mode_set(mode="OBJECT")
		subsurf = context.active_object.modifiers.new("temp", "SUBSURF")
		subsurf.levels = self.level
		bpy.ops.object.modifier_apply(apply_as="DATA", modifier=subsurf.name)
		bpy.ops.object.mode_set(mode="EDIT")
		bpy.ops.mesh.select_all(action="SELECT")
		bpy.ops.transform.tosphere(value=1)
		if (not self.enter_editmode):
			bpy.ops.object.mode_set(mode="OBJECT")
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(AddSphereOnlySquare.bl_idname, icon="PLUGIN")
