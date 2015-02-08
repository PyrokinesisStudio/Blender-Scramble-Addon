# 3Dビュー > オブジェクト/メッシュ編集モード > 「追加」メニュー > 「メッシュ」メニュー

import bpy

################
# オペレーター #
################

class AddSphereOnlySquare(bpy.types.Operator):
	bl_idname = "mesh.add_sphere_only_square"
	bl_label = "四角ポリゴン球"
	bl_description = "四角ポリゴンのみで構成された球体メッシュを追加します"
	bl_options = {'REGISTER', 'UNDO'}
	
	level = bpy.props.IntProperty(name="分割数", default=2, step=1, min=1, max=6, soft_min=1, soft_max=6)
	radius = bpy.props.FloatProperty(name="半径(大体)", default=1.0, step=10, precision=3)
	view_align = bpy.props.BoolProperty(name="視点に揃える", default=False)
	location = bpy.props.FloatVectorProperty(name="位置", default=(0.0, 0.0, 0.0), step=10, precision=3, subtype='XYZ')
	rotation = bpy.props.IntVectorProperty(name="回転", default=(0, 0, 0), step=1, subtype='ROTATION')
	enter_editmode = False
	
	def execute(self, context):
		isEdited = False
		if (context.mode == 'EDIT_MESH'):
			isEdited = True
			activeObj = context.active_object
		try:
			bpy.ops.object.mode_set(mode="OBJECT")
		except RuntimeError: pass
		if (self.view_align):
			bpy.ops.mesh.primitive_cube_add(radius=self.radius, view_align=True, location=self.location)
		else:
			bpy.ops.mesh.primitive_cube_add(radius=self.radius, location=self.location, rotation=self.rotation)
		context.active_object.name = "四角ポリゴン球"
		subsurf = context.active_object.modifiers.new("temp", "SUBSURF")
		subsurf.levels = self.level
		bpy.ops.object.modifier_apply(apply_as="DATA", modifier=subsurf.name)
		bpy.ops.object.mode_set(mode="EDIT")
		#bpy.ops.mesh.select_all(action="SELECT")
		bpy.ops.transform.tosphere(value=1)
		bpy.ops.object.mode_set(mode="OBJECT")
		if (isEdited and False):
			activeObj.select = True
			context.scene.objects.active = activeObj
			bpy.ops.object.join()
			bpy.ops.object.mode_set(mode="EDIT")
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(AddSphereOnlySquare.bl_idname, icon="PLUGIN").location = context.space_data.cursor_location
