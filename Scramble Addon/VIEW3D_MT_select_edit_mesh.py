import bpy

##############
# その他関数 #
##############

################
# オペレーター #
################

class SelectAxisLimit(bpy.types.Operator):
	bl_idname = "mesh.select_axis_limit"
	bl_label = "X=0の頂点を選択"
	bl_description = "X=0の頂点を選択する"
	bl_options = {'REGISTER', 'UNDO'}
	
	items = [
		("0", "X軸", "", 1),
		("1", "Y軸", "", 2),
		("2", "Z軸", "", 3),
		]
	axis = bpy.props.EnumProperty(items=items, name="軸")
	offset = bpy.props.FloatProperty(name="オフセット", default=0.0, step=10, precision=3)
	threshold = bpy.props.FloatProperty(name="しきい値", default=0.0000001, min=0.0, soft_min=0.0, step=0.1, precision=10)
	
	def execute(self, context):
		bpy.ops.object.mode_set(mode="OBJECT")
		sel_mode = context.tool_settings.mesh_select_mode[:]
		context.tool_settings.mesh_select_mode = [True, False, False]
		obj = context.active_object
		me = obj.data
		if (obj.type == "MESH"):
			for vert in me.vertices:
				co = [vert.co.x, vert.co.y, vert.co.z][int(self.axis)]
				if (-self.threshold <= co - self.offset <= self.threshold):
					vert.select = True
		bpy.ops.object.mode_set(mode="EDIT")
		context.tool_settings.mesh_select_mode = sel_mode
		return {'FINISHED'}

class SelectAxisOver(bpy.types.Operator):
	bl_idname = "mesh.select_axis_over"
	bl_label = "左半分を選択"
	bl_description = "メッシュの左半分を選択します(その他設定も有)"
	bl_options = {'REGISTER', 'UNDO'}
	
	items = [
		("0", "X軸", "", 1),
		("1", "Y軸", "", 2),
		("2", "Z軸", "", 3),
		]
	axis = bpy.props.EnumProperty(items=items, name="軸")
	items = [
		("-1", "-(マイナス)", "", 1),
		("1", "+(プラス)", "", 2),
		]
	direction = bpy.props.EnumProperty(items=items, name="方向")
	offset = bpy.props.FloatProperty(name="オフセット", default=0, step=10, precision=3)
	threshold = bpy.props.FloatProperty(name="しきい値", default=0.0000001, step=0.1, precision=10)
	
	def execute(self, context):
		bpy.ops.object.mode_set(mode="OBJECT")
		sel_mode = context.tool_settings.mesh_select_mode[:]
		context.tool_settings.mesh_select_mode = [True, False, False]
		obj = context.active_object
		me = obj.data
		if (obj.type == "MESH"):
			for vert in me.vertices:
				co = [vert.co.x, vert.co.y, vert.co.z][int(self.axis)]
				direct = int(self.direction)
				if (self.offset * direct <= co * direct + self.threshold):
					vert.select = True
		bpy.ops.object.mode_set(mode="EDIT")
		context.tool_settings.mesh_select_mode = sel_mode
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(SelectAxisLimit.bl_idname, icon="PLUGIN")
	self.layout.operator(SelectAxisOver.bl_idname, icon="PLUGIN")
