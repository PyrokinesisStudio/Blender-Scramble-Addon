# 3Dビュー > ウェイトペイントモード > 「ウェイト」メニュー

import bpy

################
# オペレーター #
################

class MargeSelectedVertexGroup(bpy.types.Operator):
	bl_idname = "paint.marge_selected_vertex_group"
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
		if (not context.selected_pose_bones or len(context.selected_pose_bones) < 2):
			self.report(type={"ERROR"}, message="ボーンを2つ以上選択してから実行して下さい")
			return {"CANCELLED"}
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
	bl_idname = "paint.remove_selected_vertex_group"
	bl_label = "ウェイト同士の減算"
	bl_description = "選択中のボーンと同じ頂点グループのウェイトを減算します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		obj = context.active_object
		me = obj.data
		newVg = obj.vertex_groups[context.active_pose_bone.name]
		boneNames = []
		if (not context.selected_pose_bones or len(context.selected_pose_bones) < 2):
			self.report(type={"ERROR"}, message="ボーンを2つ以上選択してから実行して下さい")
			return {"CANCELLED"}
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

class ApplyDynamicPaint(bpy.types.Operator):
	bl_idname = "mesh.apply_dynamic_paint"
	bl_label = "オブジェクトが重なっている部分を塗る"
	bl_description = "他の選択オブジェクトと重なっている部分のウェイトを塗ります"
	bl_options = {'REGISTER', 'UNDO'}
	
	isNew = bpy.props.BoolProperty(name="新しい頂点グループに", default=False)
	distance = bpy.props.FloatProperty(name="距離", default=1.0, min=0, max=100, soft_min=0, soft_max=100, step=10, precision=3)
	items = [
		("ADD", "加算", "", 1),
		("SUBTRACT", "減算", "", 2),
		("REPLACE", "置換", "", 3),
		]
	mode = bpy.props.EnumProperty(items=items, name="塗り潰し方法")
	
	def execute(self, context):
		activeObj = context.active_object
		preActiveVg = activeObj.vertex_groups.active
		isNew = self.isNew
		if (not preActiveVg):
			isNew = True
		brushObjs = []
		for obj in context.selected_objects:
			if (activeObj.name != obj.name):
				brushObjs.append(obj)
		bpy.ops.object.mode_set(mode="OBJECT")
		for obj in brushObjs:
			context.scene.objects.active = obj
			bpy.ops.object.modifier_add(type='DYNAMIC_PAINT')
			obj.modifiers[-1].ui_type = 'BRUSH'
			bpy.ops.dpaint.type_toggle(type='BRUSH')
			obj.modifiers[-1].brush_settings.paint_source = 'VOLUME_DISTANCE'
			obj.modifiers[-1].brush_settings.paint_distance = self.distance
		context.scene.objects.active = activeObj
		bpy.ops.object.modifier_add(type='DYNAMIC_PAINT')
		bpy.ops.dpaint.type_toggle(type='CANVAS')
		activeObj.modifiers[-1].canvas_settings.canvas_surfaces[-1].surface_type = 'WEIGHT'
		bpy.ops.dpaint.output_toggle(output='A')
		bpy.ops.object.modifier_apply(apply_as='DATA', modifier=activeObj.modifiers[-1].name)
		dpVg = activeObj.vertex_groups[-1]
		if (not isNew):
			me = activeObj.data
			for vert in me.vertices:
				for vg in vert.groups:
					print(activeObj.vertex_groups[vg.group].name, dpVg.name)
					if (activeObj.vertex_groups[vg.group].name == dpVg.name):
						preActiveVg.add([vert.index], vg.weight, self.mode)
						break
			activeObj.vertex_groups.remove(dpVg)
			activeObj.vertex_groups.active_index = preActiveVg.index
		bpy.ops.object.mode_set(mode='WEIGHT_PAINT')
		for obj in brushObjs:
			obj.modifiers.remove(obj.modifiers[-1])
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
	self.layout.separator()
	self.layout.operator(ApplyDynamicPaint.bl_idname, icon="PLUGIN")
