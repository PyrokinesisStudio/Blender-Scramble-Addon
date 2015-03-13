# 3Dビュー > プロパティ > (拡張)トランスフォーム座標系

import bpy

################
# オペレーター #
################

class CreateOrientationTwoVertex(bpy.types.Operator):
	bl_idname = "mesh.create_orientation_two_vertex"
	bl_label = "2頂点の向きで新座標系を作成"
	bl_description = "選択中の2頂点の向きから新しい座標軸の向きを追加します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		obj = context.active_object
		if (obj.type != "MESH"):
			self.report(type={"ERROR"}, message="メッシュオブジェクトで実行して下さい")
		cursorCo = context.space_data.cursor_location[:]
		bpy.ops.object.mode_set(mode='OBJECT')
		me = obj.data
		verts = []
		for vert in me.vertices:
			if (vert.select):
				verts.append(vert.index)
		if (len(verts) != 2):
			bpy.ops.object.mode_set(mode='EDIT')
			self.report(type={"ERROR"}, message="2つのみ頂点を選択して実行して下さい")
			return {'CANCELLED'}
		me.vertices[verts[0]].select = False
		bpy.ops.object.mode_set(mode='EDIT')
		bpy.ops.view3d.snap_cursor_to_selected()
		bpy.ops.object.mode_set(mode='OBJECT')
		bpy.ops.object.empty_add()
		oneObj = context.active_object
		context.scene.objects.active = obj
		bpy.ops.object.mode_set(mode='EDIT')
		bpy.ops.mesh.select_all(action='DESELECT')
		bpy.ops.object.mode_set(mode='OBJECT')
		me.vertices[verts[0]].select = True
		bpy.ops.object.mode_set(mode='EDIT')
		bpy.ops.view3d.snap_cursor_to_selected()
		bpy.ops.object.mode_set(mode='OBJECT')
		bpy.ops.object.empty_add()
		twoObj = context.active_object
		const = twoObj.constraints.new("DAMPED_TRACK")
		const.target = oneObj
		bpy.ops.object.visual_transform_apply()
		twoObj.name = "2頂点の向き"
		bpy.ops.transform.create_orientation(use=True)
		bpy.ops.object.select_all(action='DESELECT')
		oneObj.select = True
		twoObj.select = True
		bpy.ops.object.delete()
		obj.select = True
		context.scene.objects.active = obj
		me.vertices[verts[0]].select = True
		me.vertices[verts[1]].select = True
		context.space_data.cursor_location = cursorCo[:]
		bpy.ops.object.mode_set(mode='EDIT')
		return {'FINISHED'}

##########
# パネル #
##########

class VIEW3D_PT_transform_orientations_EX(bpy.types.Panel):
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'UI'
	bl_label = "(拡張)トランスフォーム座標系"
	bl_options = {'DEFAULT_CLOSED'}
	
	@classmethod
	def poll(cls, context):
		view = context.space_data
		return (view)
	
	def draw(self, context):
		layout = self.layout
		
		view = context.space_data
		orientation = view.current_orientation
		
		row = layout.row(align=True)
		row.prop(view, "transform_orientation", text="")
		row.operator("transform.create_orientation", text="", icon='ZOOMIN')
		
		if orientation:
			row = layout.row(align=True)
			row.prop(orientation, "name", text="")
			row.operator("transform.delete_orientation", text="", icon='X')
		
		if (context.mode == 'EDIT_MESH'):
			row = layout.row(align=True)
			row.operator(CreateOrientationTwoVertex.bl_idname, text="2頂点の向きで作成", icon='PLUGIN')

#################
# 登録/登録解除 #
#################

def register():
	bpy.utils.register_class(VIEW3D_PT_transform_orientations_EX)

def unregister():
	bpy.utils.unregister_class(VIEW3D_PT_transform_orientations_EX)
