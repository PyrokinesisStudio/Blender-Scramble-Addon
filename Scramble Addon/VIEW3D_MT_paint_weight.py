import bpy

################
# オペレーター #
################

class MargeSelectedVertexGroup(bpy.types.Operator):
	bl_idname = "mesh.marge_selected_vertex_group"
	bl_label = "ウェイト同士の合成"
	bl_description = "選択中のボーンと同じ頂点グループのウェイトを合成します"
	bl_options = {'REGISTER', 'UNDO'}
	
	isNewVertGroup = bpy.props.BoolProperty(name="新頂点グループ作成", default=False)
	ext = bpy.props.StringProperty(name="新頂点グループ名の末尾", default="...等の合成")
	
	def execute(self, context):
		obj = context.active_object
		me = obj.data
		if (self.isNewVertGroup):
			newVg = obj.vertex_groups.new(name=context.active_pose_bone.name+self.ext)
		else:
			newVg = obj.vertex_groups[context.active_pose_bone.name]
		boneNames = []
		for bone in context.selected_pose_bones:
			boneNames.append(bone.name)
		for vert in me.vertices:
			for vg in vert.groups:
				if (self.isNewVertGroup or newVg.name != obj.vertex_groups[vg.group].name):
					if (obj.vertex_groups[vg.group].name in boneNames):
						newVg.add([vert.index], vg.weight, 'ADD')
		bpy.ops.object.mode_set(mode="OBJECT")
		bpy.ops.object.mode_set(mode="WEIGHT_PAINT")
		obj.vertex_groups.active_index = newVg.index
		return {'FINISHED'}

class RemoveSelectedVertexGroup(bpy.types.Operator):
	bl_idname = "mesh.remove_selected_vertex_group"
	bl_label = "ウェイト同士の減算"
	bl_description = "選択中のボーンと同じ頂点グループのウェイトを減算します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		obj = context.active_object
		me = obj.data
		newVg = obj.vertex_groups[context.active_pose_bone.name]
		boneNames = []
		for bone in context.selected_pose_bones:
			boneNames.append(bone.name)
		for vert in me.vertices:
			for vg in vert.groups:
				if (newVg.name != obj.vertex_groups[vg.group].name):
					if (obj.vertex_groups[vg.group].name in boneNames):
						newVg.add([vert.index], vg.weight, 'SUBTRACT')
		bpy.ops.object.mode_set(mode="OBJECT")
		bpy.ops.object.mode_set(mode="WEIGHT_PAINT")
		return {'FINISHED'}

class VertexGroupAverageAll(bpy.types.Operator):
	bl_idname = "mesh.vertex_group_average_all"
	bl_label = "全頂点の平均ウェイトで塗り潰す"
	bl_description = "全てのウェイトの平均で、全ての頂点を塗り潰します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		obj = context.active_object
		if (obj.type == "MESH"):
			vgs = []
			for i in range(len(obj.vertex_groups)):
				vgs.append([])
			vertCount = 0
			for vert in obj.data.vertices:
				for vg in vert.groups:
					vgs[vg.group].append(vg.weight)
				vertCount += 1
			vg_average = []
			for vg in vgs:
				vg_average.append(0)
				for w in vg:
					vg_average[-1] += w
				vg_average[-1] /= vertCount
			i = 0
			for vg in obj.vertex_groups:
				vg.add(range(vertCount), vg_average[i], "REPLACE")
				i += 1
		bpy.ops.object.mode_set(mode="OBJECT")
		bpy.ops.object.mode_set(mode="WEIGHT_PAINT")
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(MargeSelectedVertexGroup.bl_idname, icon="PLUGIN")
	self.layout.operator(RemoveSelectedVertexGroup.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.operator(VertexGroupAverageAll.bl_idname, icon="PLUGIN")
