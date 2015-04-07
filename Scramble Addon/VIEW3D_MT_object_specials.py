# 3Dビュー > オブジェクトモード > 「W」キー

import bpy, bmesh, mathutils
import re, random

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
		bpy.ops.object.transform_apply_all()
		
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
	resolution = bpy.props.FloatProperty(name="解像度", default=0.1, min=0.001, max=10, soft_min=0.001, soft_max=10, step=0.5, precision=3)
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
					meta = bpy.data.metaballs.new(self.name)
					metas.append( bpy.data.objects.new(self.name, meta) )
					meta.elements.new()
					meta.update_method = 'NEVER'
					meta.resolution = self.resolution
					metas[-1].name = self.name
					size = self.size * multi
					metas[-1].scale = (size, size, size)
					metas[-1].parent = obj
					metas[-1].parent_type = 'VERTEX'
					metas[-1].parent_vertices = (i, 0, 0)
				bpy.ops.object.select_all(action='DESELECT')
				for meta in metas:
					context.scene.objects.link(meta)
					meta.select = True
				bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
				metas[-1].parent_type = metas[-1].parent_type
				base_obj = metas[0] #context.scene.objects[re.sub(r'\.\d+$', '', metas[0].name)]
				context.scene.objects.active = base_obj
				base_obj.data.update_method = 'UPDATE_ALWAYS'
				#context.scene.update()
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
		if (is_smoothed):
			self.report(type={"INFO"}, message="メッシュオブジェクトをフラットにしました")
		else:
			self.report(type={"INFO"}, message="メッシュオブジェクトをスムーズにしました")
		return {'FINISHED'}

class SetRenderHide(bpy.types.Operator):
	bl_idname = "object.set_render_hide"
	bl_label = "選択物のレンダリングを制限"
	bl_description = "選択中のオブジェクトをレンダリングしない設定にします"
	bl_options = {'REGISTER', 'UNDO'}
	
	reverse = bpy.props.BoolProperty(name="レンダリングしない", default=True)
	
	def execute(self, context):
		for obj in context.selected_objects:
			obj.hide_render = self.reverse
		return {'FINISHED'}

class SyncRenderHide(bpy.types.Operator):
	bl_idname = "object.sync_render_hide"
	bl_label = "レンダリングするかを「表示/非表示」に同期"
	bl_description = "現在のレイヤー内のオブジェクトをレンダリングするかどうかを表示/非表示の状態と同期します"
	bl_options = {'REGISTER', 'UNDO'}
	
	isAll = bpy.props.BoolProperty(name="全オブジェクト", default=False)
	
	def execute(self, context):
		objs = []
		for obj in bpy.data.objects:
			if (self.isAll):
				objs.append(obj)
			else:
				for i in range(len(context.scene.layers)):
					if (context.scene.layers[i] and obj.layers[i]):
						objs.append(obj)
						break
		for obj in objs:
			obj.hide_render = obj.hide
		return {'FINISHED'}

class SetHideSelect(bpy.types.Operator):
	bl_idname = "object.set_hide_select"
	bl_label = "選択物の選択を制限"
	bl_description = "選択中のオブジェクトを選択出来なくします"
	bl_options = {'REGISTER', 'UNDO'}
	
	reverse = bpy.props.BoolProperty(name="選択不可に", default=True)
	
	def execute(self, context):
		for obj in context.selected_objects:
			obj.hide_select = self.reverse
			if (self.reverse):
				obj.select = not self.reverse
		return {'FINISHED'}

class SetUnselectHideSelect(bpy.types.Operator):
	bl_idname = "object.set_unselect_hide_select"
	bl_label = "非選択物の選択を制限"
	bl_description = "選択物以外のオブジェクトを選択出来なくします"
	bl_options = {'REGISTER', 'UNDO'}
	
	reverse = bpy.props.BoolProperty(name="選択不可に", default=True)
	
	def execute(self, context):
		for obj in bpy.data.objects:
			for i in range(len(context.scene.layers)):
				if (obj.layers[i] and context.scene.layers[i]):
					if (not obj.select):
						obj.hide_select = self.reverse
		return {'FINISHED'}

class AllResetHideSelect(bpy.types.Operator):
	bl_idname = "object.all_reset_hide_select"
	bl_label = "すべての選択制限をクリア"
	bl_description = "全てのオブジェクトの選択不可設定を解除します(逆も可)"
	bl_options = {'REGISTER', 'UNDO'}
	
	reverse = bpy.props.BoolProperty(name="選択不可に", default=False)
	
	def execute(self, context):
		for obj in bpy.data.objects:
			obj.hide_select = self.reverse
			if (self.reverse):
				obj.select = not self.reverse
		return {'FINISHED'}

class QuickCurveDeform(bpy.types.Operator):
	bl_idname = "object.quick_curve_deform"
	bl_label = "クイックカーブ変形"
	bl_description = "すばやくカーブモディファイアを適用します"
	bl_options = {'REGISTER', 'UNDO'}
	
	items = [
		('POS_X', "+X", "", 1),
		('POS_Y', "+Y", "", 2),
		('POS_Z', "+Z", "", 3),
		('NEG_X', "-X", "", 4),
		('NEG_Y', "-Y", "", 5),
		('NEG_Z', "-Z", "", 6),
		]
	deform_axis = bpy.props.EnumProperty(items=items, name="変形する軸")
	
	def execute(self, context):
		mesh_obj = context.active_object
		if (mesh_obj.type != 'MESH'):
			self.report(type={"ERROR"}, message="メッシュオブジェクトがアクティブな状態で実行して下さい")
			return {"CANCELLED"}
		if (len(context.selected_objects) != 2):
			self.report(type={"ERROR"}, message="メッシュ・カーブの2つのみ選択して実行して下さい")
			return {"CANCELLED"}
		for obj in context.selected_objects:
			if (mesh_obj.name != obj.name):
				if (obj.type == 'CURVE'):
					curve_obj = obj
					break
		else:
			self.report(type={"ERROR"}, message="カーブオブジェクトも選択状態で実行して下さい")
			return {"CANCELLED"}
		curve = curve_obj.data
		pre_use_stretch = curve.use_stretch
		pre_use_deform_bounds = curve.use_deform_bounds
		curve.use_stretch = True
		curve.use_deform_bounds = True
		bpy.ops.object.transform_apply_all()
		mod = mesh_obj.modifiers.new("temp", 'CURVE')
		mod.object = curve_obj
		mod.deform_axis = self.deform_axis
		for i in range(len(mesh_obj.modifiers)):
			bpy.ops.object.modifier_move_up(modifier=mod.name)
		bpy.ops.object.modifier_apply(modifier=mod.name)
		curve.use_stretch = pre_use_stretch
		curve.use_deform_bounds = pre_use_deform_bounds
		return {'FINISHED'}

class VertexGroupTransfer(bpy.types.Operator):
	bl_idname = "object.vertex_group_transfer"
	bl_label = "頂点グループの転送"
	bl_description = "アクティブなメッシュに他の選択メッシュの頂点グループを転送します"
	bl_options = {'REGISTER', 'UNDO'}
	
	vertex_group_remove_all = bpy.props.BoolProperty(name="最初に頂点グループ全削除", default=False)
	vertex_group_clean = bpy.props.BoolProperty(name="頂点グループのクリーン", default=True)
	vertex_group_delete = bpy.props.BoolProperty(name="割り当ての無い頂点グループ削除", default=True)
	
	def execute(self, context):
		if (context.active_object.type != 'MESH'):
			self.report(type={'ERROR'}, message="メッシュオブジェクトがアクティブな状態で実行して下さい")
			return {'CANCELLED'}
		source_objs = []
		for obj in context.selected_objects:
			if (obj.type == 'MESH' and context.active_object.name != obj.name):
				source_objs.append(obj)
		if (len(source_objs) <= 0):
			self.report(type={'ERROR'}, message="メッシュオブジェクトを2つ以上選択した状態で実行して下さい")
			return {'CANCELLED'}
		if (0 < len(context.active_object.vertex_groups) and self.vertex_group_remove_all):
			bpy.ops.object.vertex_group_remove(all=True)
		me = context.active_object.data
		vert_mapping = 'NEAREST'
		for obj in source_objs:
			if (len(obj.data.polygons) <= 0):
				for obj2 in source_objs:
					if (len(obj.data.edges) <= 0):
						break
				else:
					vert_mapping = 'EDGEINTERP_NEAREST'
				break
		else:
			vert_mapping = 'POLYINTERP_NEAREST'
		bpy.ops.object.data_transfer(use_reverse_transfer=True, data_type='VGROUP_WEIGHTS', use_create=True, vert_mapping=vert_mapping, layers_select_src = 'ALL', layers_select_dst = 'NAME')
		if (self.vertex_group_clean):
			bpy.ops.object.vertex_group_clean(group_select_mode='ALL', limit=0, keep_single=False)
		if (self.vertex_group_delete):
			bpy.ops.mesh.remove_empty_vertex_groups()
		return {'FINISHED'}

class CreateSolidifyEdge(bpy.types.Operator):
	bl_idname = "object.create_solidify_edge"
	bl_label = "厚み付けモディファイアで輪郭線生成"
	bl_description = "選択オブジェクトに「厚み付けモディファイア」による輪郭描画を追加します"
	bl_options = {'REGISTER', 'UNDO'}
	
	use_render = bpy.props.BoolProperty(name="レンダリングにも適用", default=False)
	thickness = bpy.props.FloatProperty(name="輪郭線の厚さ", default=0.01, min=0, max=1, soft_min=0, soft_max=1, step=1, precision=3)
	color = bpy.props.FloatVectorProperty(name="線の色", default=(0.0, 0.0, 0.0), min=0, max=1, soft_min=0, soft_max=1, step=10, precision=3, subtype='COLOR')
	use_rim = bpy.props.BoolProperty(name="ふちに面を張る", default=False)
	
	def execute(self, context):
		pre_active_obj = context.active_object
		selected_objs = []
		for obj in context.selected_objects:
			if (obj.type == 'MESH'):
				selected_objs.append(obj)
			else:
				self.report(type={'INFO'}, message=obj.name+"はメッシュオブジェクトではないので無視します")
		if (len(selected_objs) <= 0):
			self.report(type={'ERROR'}, message="1つ以上のメッシュオブジェクトを選択した状態で実行して下さい")
			return {'CANCELLED'}
		for obj in selected_objs:
			pre_mtls = []
			for i in obj.material_slots:
				if (i.material):
					pre_mtls.append(i)
			if (len(pre_mtls) <= 0):
				self.report(type={'WARNING'}, message=obj.name+"にマテリアルが割り当てられていないので無視します")
				continue
			context.scene.objects.active = obj
			
			mtl = bpy.data.materials.new(obj.name+"の輪郭線")
			mtl.use_shadeless = True
			mtl.diffuse_color = self.color
			mtl.use_nodes = True
			mtl.use_transparency = True
			
			for n in mtl.node_tree.nodes:
				if (n.bl_idname == 'ShaderNodeMaterial'):
					n.material = mtl
			node = mtl.node_tree.nodes.new('ShaderNodeGeometry')
			link_input = node.outputs[8]
			for n in mtl.node_tree.nodes:
				if (n.bl_idname == 'ShaderNodeOutput'):
					link_output = n.inputs[1]
			mtl.node_tree.links.new(link_input, link_output)
			
			slot_index = len(obj.material_slots)
			bpy.ops.object.material_slot_add()
			slot = obj.material_slots[-1]
			slot.material = mtl
			
			mod = obj.modifiers.new("輪郭線", 'SOLIDIFY')
			mod.use_flip_normals = True
			if (not self.use_rim):
				mod.use_rim = False
			mod.material_offset = slot_index
			mod.material_offset_rim = slot_index
			mod.offset = 1
			mod.thickness = self.thickness
			if (not self.use_render):
				mod.show_render = False
		context.scene.objects.active = pre_active_obj
		return {'FINISHED'}
	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self)

class ApplyObjectColor(bpy.types.Operator):
	bl_idname = "object.apply_object_color"
	bl_label = "オブジェクトカラー有効 + 色設定"
	bl_description = "選択オブジェクトのオブジェクトカラーを有効にし、色を設定します"
	bl_options = {'REGISTER', 'UNDO'}
	
	color = bpy.props.FloatVectorProperty(name="カラー", default=(0, 0, 0), min=0, max=1, soft_min=0, soft_max=1, step=10, precision=3, subtype='COLOR')
	use_random = bpy.props.BoolProperty(name="ランダムな色を使う", default=True)
	
	def execute(self, context):
		for obj in context.selected_objects:
			if (self.use_random):
				col = mathutils.Color((0.0, 0.0, 1.0))
				col.s = 1.0
				col.v = 1.0
				col.h = random.random()
				obj.color = (col.r, col.g, col.b, 1)
			else:
				obj.color = (self.color[0], self.color[1], self.color[2], 1)
			for slot in obj.material_slots:
				if (slot.material):
					slot.material.use_object_color = True
		return {'FINISHED'}

class ClearObjectColor(bpy.types.Operator):
	bl_idname = "object.clear_object_color"
	bl_label = "オブジェクトカラー無効 + 色設定"
	bl_description = "選択オブジェクトのオブジェクトカラーを無効にし、色を設定します"
	bl_options = {'REGISTER', 'UNDO'}
	
	set_color = bpy.props.BoolProperty(name="色を設定する", default=False)
	color = bpy.props.FloatVectorProperty(name="カラー", default=(1, 1, 1), min=0, max=1, soft_min=0, soft_max=1, step=10, precision=3, subtype='COLOR')
	
	def execute(self, context):
		for obj in context.selected_objects:
			if (self.set_color):
				obj.color = (self.color[0], self.color[1], self.color[2], 1)
			for slot in obj.material_slots:
				if (slot.material):
					slot.material.use_object_color = False
		return {'FINISHED'}

class CreateMeshImitateArmature(bpy.types.Operator):
	bl_idname = "object.create_mesh_imitate_armature"
	bl_label = "メッシュの変形を真似するアーマチュアを作成"
	bl_description = "アクティブメッシュオブジェクトの変形に追従するアーマチュアを新規作成します"
	bl_options = {'REGISTER', 'UNDO'}
	
	bone_length = bpy.props.FloatProperty(name="ボーンの長さ", default=0.1, min=0, max=10, soft_min=0, soft_max=10, step=1, precision=3)
	add_edge = bpy.props.BoolProperty(name="辺にもボーンを追加", default=True)
	
	def execute(self, context):
		pre_active_obj = context.active_object
		for obj in context.selected_objects:
			if (obj.type != 'MESH'):
				self.report(type={'INFO'}, message=obj.name+"はメッシュオブジェクトではないので無視します")
				continue
			arm = bpy.data.armatures.new(obj.name+"の真似をするアーマチュア")
			arm_obj = bpy.data.objects.new(obj.name+"の真似をするアーマチュア", arm)
			context.scene.objects.link(arm_obj)
			context.scene.objects.active = arm_obj
			bpy.ops.object.mode_set(mode='EDIT')
			bone_names = []
			for vert in obj.data.vertices:
				bone = arm.edit_bones.new("頂点"+str(vert.index))
				bone.head = obj.matrix_world * vert.co
				bone.tail = bone.head + (obj.matrix_world * vert.normal * self.bone_length)
				bone_names.append(bone.name)
			bpy.ops.object.mode_set(mode='OBJECT')
			for vert, name in zip(obj.data.vertices, bone_names):
				vg = obj.vertex_groups.new("頂点"+str(vert.index))
				vg.add([vert.index], 1.0, 'REPLACE')
				const = arm_obj.pose.bones[name].constraints.new('COPY_LOCATION')
				const.target = obj
				const.subtarget = vg.name
			if (self.add_edge):
				edge_bone_names = []
				bpy.ops.object.mode_set(mode='EDIT')
				for edge in obj.data.edges:
					vert0 = obj.data.vertices[edge.vertices[0]]
					vert1 = obj.data.vertices[edge.vertices[1]]
					bone = arm.edit_bones.new("辺"+str(edge.index))
					bone.head = obj.matrix_world * vert0.co
					bone.tail = obj.matrix_world * vert1.co
					bone.layers = (False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False)
					edge_bone_names.append(bone.name)
				bpy.ops.object.mode_set(mode='OBJECT')
				arm.layers[1] = True
				for edge, name in zip(obj.data.edges, edge_bone_names):
					const = arm_obj.pose.bones[name].constraints.new('COPY_LOCATION')
					const.target = arm_obj
					const.subtarget = "頂点" + str(edge.vertices[0])
					const = arm_obj.pose.bones[name].constraints.new('STRETCH_TO')
					const.target = arm_obj
					const.subtarget = "頂点" + str(edge.vertices[1])
		context.scene.objects.active = pre_active_obj
		bpy.ops.object.mode_set(mode='EDIT')
		bpy.ops.object.mode_set(mode='OBJECT')
		return {'FINISHED'}

################
# サブメニュー #
################

class RenderHideMenu(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_object_specials_render_hide"
	bl_label = "レンダリング制限"
	bl_description = "オブジェクトのレンダリング制限関係のメニューです"
	
	def draw(self, context):
		column = self.layout.column()
		column.operator(SetRenderHide.bl_idname, text="選択物のレンダリングを制限", icon="PLUGIN").reverse = True
		column.operator('object.isolate_type_render')
		column.separator()
		column.operator(SetRenderHide.bl_idname, text="選択物のレンダリングを許可", icon="PLUGIN").reverse = False
		column.operator('object.hide_render_clear_all')
		column.separator()
		column.operator(SyncRenderHide.bl_idname, icon="PLUGIN")

class HideSelectMenu(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_object_specials_hide_select"
	bl_label = "選択制限"
	bl_description = "オブジェクトの選択制限関係のメニューです"
	
	def draw(self, context):
		column = self.layout.column()
		column.operator(SetHideSelect.bl_idname, text="選択物の選択を制限", icon="PLUGIN").reverse = True
		column.operator(SetUnselectHideSelect.bl_idname, icon="PLUGIN").reverse = True
		column.separator()
		column.operator(AllResetHideSelect.bl_idname, icon="PLUGIN").reverse = False

class ObjectNameMenu(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_object_specials_object_name"
	bl_label = "オブジェクト名"
	bl_description = "オブジェクト名関係のメニューです"
	
	def draw(self, context):
		column = self.layout.column()
		column.operator(CopyObjectName.bl_idname, icon="PLUGIN")
		column.operator(RenameObjectRegularExpression.bl_idname, icon="PLUGIN")
		column.operator(EqualizeObjectNameAndDataName.bl_idname, icon="PLUGIN")
		if (len(context.selected_objects) <= 0):
			column.enabled = False

class ObjectColorMenu(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_object_specials_object_color"
	bl_label = "オブジェクトカラー"
	bl_description = "オブジェクトカラー関係のメニューです"
	
	def draw(self, context):
		column = self.layout.column()
		column.operator(ApplyObjectColor.bl_idname, icon="PLUGIN")
		column.operator(ClearObjectColor.bl_idname, icon="PLUGIN")

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.menu(RenderHideMenu.bl_idname, icon="PLUGIN")
	self.layout.menu(HideSelectMenu.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.menu(ObjectNameMenu.bl_idname, icon="PLUGIN")
	self.layout.menu(ObjectColorMenu.bl_idname, icon="PLUGIN")
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
	operator = column.operator(VertexGroupTransfer.bl_idname, icon="PLUGIN")
	column.enabled = False
	if (context.active_object.type == 'MESH'):
		i = 0
		for obj in context.selected_objects:
			if (obj.type == 'MESH'):
				i += 1
		if (2 <= i):
			column.enabled = True
	column = self.layout.column()
	column.operator('mesh.vertex_group_average_all', icon="PLUGIN")
	self.layout.separator()
	column = self.layout.column()
	column.operator(CreateRopeMesh.bl_idname, icon="PLUGIN")
	column.enabled = False
	if (context.active_object):
		if (context.active_object.type == "CURVE"):
			column.enabled = True
	column = self.layout.column()
	column.operator(QuickCurveDeform.bl_idname, icon="PLUGIN")
	column.operator(CreateSolidifyEdge.bl_idname, icon="PLUGIN")
	self.layout.separator()
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
	self.layout.separator()
	column = self.layout.column()
	column.operator(CreateMeshImitateArmature.bl_idname, icon="PLUGIN")
	for obj in context.selected_objects:
		if (obj.type == 'MESH'):
			column.enabled = True
