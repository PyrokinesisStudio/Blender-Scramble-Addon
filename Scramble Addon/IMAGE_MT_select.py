import bpy
import bmesh

################
# オペレーター #
################

class SelectSeamEdge(bpy.types.Operator):
	bl_idname = "uv.select_seam_edge"
	bl_label = "分離している頂点を選択"
	bl_description = "シームによって分離している頂点を選択します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		activeObj = context.active_object
		me = activeObj.data
		bpy.ops.object.mode_set(mode='OBJECT')
		bm = bmesh.new()
		bm.from_mesh(me)
		uv_lay = bm.loops.layers.uv.active
		verts = []
		for face in bm.faces:
			for loop in face.loops:
				uv = loop[uv_lay].uv
				index = loop.vert.index
				data = (uv, index)
				if (not data in verts):
					verts.append(data)
		for face in bm.faces:
			for loop in face.loops:
				uv = loop[uv_lay].uv
				index = loop.vert.index
				data = (uv, index)
				for co, i in verts:
					if (co != uv and i == index):
						loop[uv_lay].select = True
						break
		bm.to_mesh(me)
		bm.free()
		bpy.ops.object.mode_set(mode='EDIT')
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(SelectSeamEdge.bl_idname, icon="PLUGIN")
