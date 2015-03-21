# 3Dビュー > オブジェクトモード > 「W」キー

import bpy, bmesh
import re

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
	
	vertices = bpy.props.IntProperty(name="頂点数", default=32, min=3, soft_min=3, max=999, soft_max=999, step=1)
	radius = bpy.props.FloatProperty(name="半径", default=0.1, step=1, precision=3, min=0, soft_min=0, max=99, soft_max=99)
	number_cuts = bpy.props.IntProperty(name="分割数", default=32, min=2, soft_min=2, max=999, soft_max=999, step=1)
	resolution_u = bpy.props.IntProperty(name="カーブの解像度", default=64, min=1, soft_min=1, max=999, soft_max=999, step=1)
	
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

class VertexGroupTransferWeightObjmode(bpy.types.Operator):
	bl_idname = "object.vertex_group_transfer_weight_objmode"
	bl_label = "ウェイト転送"
	bl_description = "他の選択中のメッシュからアクティブにウェイトペイントを転送します"
	bl_options = {'REGISTER', 'UNDO'}
	
	isDeleteWeights = bpy.props.BoolProperty(name="ウェイト全削除してから", default=True)
	items = [
		('WT_BY_INDEX', "頂点のインデックス番号", "", 1),
		('WT_BY_NEAREST_VERTEX', "最近接頂点", "", 2),
		('WT_BY_NEAREST_FACE', "最近接面", "", 3),
		('WT_BY_NEAREST_VERTEX_IN_FACE', "面内の最近接頂点", "", 4),
		]
	method = bpy.props.EnumProperty(items=items, name="方式", default="WT_BY_NEAREST_VERTEX")
	
	def execute(self, context):
		if (self.isDeleteWeights):
			try:
				bpy.ops.object.vertex_group_remove(all=True)
			except RuntimeError:
				pass
		bpy.ops.object.vertex_group_transfer_weight(group_select_mode='WT_REPLACE_ALL_VERTEX_GROUPS', method=self.method, replace_mode='WT_REPLACE_ALL_WEIGHTS')
		return {'FINISHED'}

class AddGreasePencilPathMetaballs(bpy.types.Operator):
	bl_idname = "object.add_grease_pencil_path_metaballs"
	bl_label = "グリースペンシルにメタボール配置"
	bl_description = "アクティブなグリースペンシルに沿ってメタボールを配置します"
	bl_options = {'REGISTER', 'UNDO'}
	
	dissolve_verts_count = bpy.props.IntProperty(name="密度", default=3, min=1, max=100, soft_min=1, soft_max=100, step=1)
	radius = bpy.props.FloatProperty(name="メタボールサイズ", default=0.05, min=0, max=1, soft_min=0, soft_max=1, step=0.2, precision=3)
	resolution = bpy.props.FloatProperty(name="メタボール解像度", default=0.05, min=0.001, max=1, soft_min=0.001, soft_max=1, step=0.2, precision=3)
	
	def execute(self, context):
		if (not context.scene.grease_pencil.layers.active):
			self.report(type={"ERROR"}, message="グリースペンシルレイヤーが存在しません")
			return {"CANCELLED"}
		pre_selectable_objects = context.selectable_objects
		bpy.ops.gpencil.convert(type='CURVE', use_normalize_weights=False, use_link_strokes=False, use_timing_data=True)
		for obj in context.selectable_objects:
			if (not obj in pre_selectable_objects):
				curveObj = obj
				break
		bpy.ops.object.select_all(action='DESELECT')
		curveObj.select = True
		context.scene.objects.active = curveObj
		curveObj.data.resolution_u = 1
		bpy.ops.object.convert(target='MESH', keep_original=False)
		pathObj = context.scene.objects.active
		for vert in pathObj.data.vertices:
			if (vert.index % self.dissolve_verts_count == 0):
				vert.select = False
			else:
				vert.select = True
		bpy.ops.object.mode_set(mode='EDIT')
		bpy.ops.mesh.dissolve_verts()
		bpy.ops.object.mode_set(mode='OBJECT')
		metas = []
		for vert in pathObj.data.vertices:
			bpy.ops.object.metaball_add(type='BALL', radius=self.radius, view_align=False, enter_editmode=False, location=vert.co)
			metas.append(context.scene.objects.active)
			metas[-1].data.resolution = self.resolution
		for obj in metas:
			obj.select = True
		context.scene.objects.unlink(pathObj)
		return {'FINISHED'}

class CreateVertexToMetaball(bpy.types.Operator):
	bl_idname = "object.create_vertex_to_metaball"
	bl_label = "頂点にメタボールをフック"
	bl_description = "選択中のメッシュオブジェクトの頂点部分に新規メタボールを張り付かせます"
	bl_options = {'REGISTER', 'UNDO'}
	
	name = bpy.props.StringProperty(name="メタボール名", default="Mball")
	size = bpy.props.FloatProperty(name="サイズ", default=0.1, min=0.001, max=10, soft_min=0.001, soft_max=10, step=1, precision=3)
	resolution = bpy.props.FloatProperty(name="解像度", default=0.05, min=0.001, max=10, soft_min=0.001, soft_max=10, step=0.5, precision=3)
	isUseVg = bpy.props.BoolProperty(name="頂点グループを大きさに", default=False)
	
	def execute(self, context):
		for obj in context.selected_objects:
			if (obj.type == 'MESH'):
				me = obj.data
				metas = []
				active_vg_index = obj.vertex_groups.active_index
				for i in range(len(me.vertices)):
					multi = 1.0
					if (self.isUseVg):
						for element in me.vertices[i].groups:
							if (element.group == active_vg_index):
								multi = element.weight
								break
					bpy.ops.object.metaball_add(type='BALL', radius=self.size * multi, location=(0, 0, 0))
					metas.append(context.active_object)
					metas[-1].name = self.name
					metas[-1].data.resolution = 10000
					metas[-1].parent = obj
					metas[-1].parent_type = 'VERTEX'
					metas[-1].parent_vertices = (i, 0, 0)
					#context.scene.objects.unlink(metas[-1])
				bpy.ops.object.select_all(action='DESELECT')
				for meta in metas:
					#context.scene.objects.link(meta)
					meta.select = True
				context.scene.update()
				context.scene.objects[re.sub(r'\.\d+$', '', metas[0].name)].data.resolution = self.resolution
		return {'FINISHED'}

class ToggleSmooth(bpy.types.Operator):
	bl_idname = "object.toggle_smooth"
	bl_label = "スムーズ/フラットを切り替え"
	bl_description = "選択中のメッシュオブジェクトのスムーズ/フラット状態を切り替えます"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		activeObj = context.active_object
		if (activeObj.type == 'MESH'):
			me = activeObj.data
			is_smoothed = False
			if (1 <= len(me.polygons)):
				if (me.polygons[0].use_smooth):
					is_smoothed = True
			for obj in context.selected_objects:
				if (is_smoothed):
					bpy.ops.object.shade_flat()
				else:
					bpy.ops.object.shade_smooth()
		else:
			self.report(type={"ERROR"}, message="メッシュオブジェクトをアクティブにしてから実行して下さい")
			return {'CANCELLED'}
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	column = self.layout.column()
	column.operator(CopyObjectName.bl_idname, icon="PLUGIN")
	column.operator(RenameObjectRegularExpression.bl_idname, icon="PLUGIN")
	column.operator(EqualizeObjectNameAndDataName.bl_idname, icon="PLUGIN")
	if (len(context.selected_objects) <= 0):
		column.enabled = False
	self.layout.separator()
	column = self.layout.column()
	column.operator(ToggleSmooth.bl_idname, icon="PLUGIN")
	column.operator(AddVertexColorSelectedObject.bl_idname, icon="PLUGIN")
	column.enabled = False
	for obj in context.selected_objects:
		if (obj.type == 'MESH'):
			column.enabled = True
	self.layout.separator()
	column = self.layout.column()
	operator = column.operator('object.data_transfer', text="メッシュデータの転送 (頂点グループ用)", icon="PLUGIN")
	operator.use_reverse_transfer = True
	operator.data_type = 'VGROUP_WEIGHTS'
	operator.use_create = True
	operator.vert_mapping = 'POLYINTERP_NEAREST'
	operator.layers_select_src = 'ALL'
	operator.layers_select_dst = 'NAME'
	column.enabled = False
	if (context.active_object.type == 'MESH'):
		i = 0
		for obj in context.selected_objects:
			if (obj.type == 'MESH'):
				i += 1
		if (2 <= i):
			column.enabled = True
	self.layout.separator()
	column = self.layout.column()
	column.operator(CreateRopeMesh.bl_idname, icon="PLUGIN")
	column.enabled = False
	if (context.active_object):
		if (context.active_object.type == "CURVE"):
			column.enabled = True
	column = self.layout.column()
	column.operator(CreateVertexToMetaball.bl_idname, icon="PLUGIN")
	column.enabled = False
	for obj in context.selected_objects:
		if (obj.type == 'MESH'):
			column.enabled = True
	column = self.layout.column()
	column.operator(AddGreasePencilPathMetaballs.bl_idname, icon="PLUGIN")
	if (not context.gpencil_data):
		column.enabled = False
