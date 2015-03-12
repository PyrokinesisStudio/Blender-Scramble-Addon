# 3Dビュー > メッシュ編集モード > 「W」キー

import bpy

################
# オペレーター #
################

class PaintSelectedVertexColor(bpy.types.Operator):
	bl_idname = "mesh.paint_selected_vertex_color"
	bl_label = "選択頂点の頂点カラーを塗り潰す"
	bl_description = "選択中の頂点のアクティブ頂点カラーを指定色で塗り潰します"
	bl_options = {'REGISTER', 'UNDO'}
	
	color = bpy.props.FloatVectorProperty(name="色", default=(1, 1, 1), step=1, precision=3, subtype='COLOR', min=0, max=1, soft_min=0, soft_max=1)
	
	def execute(self, context):
		activeObj = context.active_object
		me = activeObj.data
		bpy.ops.object.mode_set(mode='OBJECT')
		i = 0
		for poly in me.polygons:
			for vert in poly.vertices:
				if (me.vertices[vert].select):
					me.vertex_colors.active.data[i].color = self.color
				i += 1
		bpy.ops.object.mode_set(mode='EDIT')
		return {'FINISHED'}

class ApplySolidify(bpy.types.Operator):
	bl_idname = "mesh.apply_solidify"
	bl_label = "選択部分に厚みを付ける"
	bl_description = "選択中の面に厚みを付けます"
	bl_options = {'REGISTER', 'UNDO'}
	
	thickness = bpy.props.FloatProperty(name="厚み", default=0.01, min=-10, soft_min=-10, step=0.1, precision=4)
	offset = bpy.props.FloatProperty(name="オフセット", default=-1, min=-1, max=1, soft_min=-1, soft_max=1, step=10, precision=4)
	
	def execute(self, context):
		activeObj = context.active_object
		me = activeObj.data
		bpy.ops.mesh.separate(type='SELECTED')
		bpy.ops.object.mode_set(mode='OBJECT')
		for obj in context.selected_objects:
			if (activeObj.name != obj.name):
				tempObj = obj
		modi = tempObj.modifiers.new("temp", 'SOLIDIFY')
		modi.thickness = self.thickness
		modi.offset = self.offset
		context.scene.objects.active = tempObj
		bpy.ops.object.mode_set(mode='EDIT')
		bpy.ops.mesh.select_all(action='SELECT')
		bpy.ops.object.mode_set(mode='OBJECT')
		bpy.ops.object.modifier_apply(apply_as='DATA', modifier=modi.name)
		bpy.ops.object.select_all(action='DESELECT')
		activeObj.select = True
		tempObj.select = True
		context.scene.objects.active = activeObj
		bpy.ops.object.join()
		bpy.ops.object.mode_set(mode='EDIT')
		return {'FINISHED'}

class SelectTopShape(bpy.types.Operator):
	bl_idname = "mesh.select_top_shape"
	bl_label = "一番上のシェイプを選択"
	bl_description = "リストの一番上にあるシェイプキーを選択します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		context.active_object.active_shape_key_index = 0
		return {'FINISHED'}

class ToggleShowCage(bpy.types.Operator):
	bl_idname = "mesh.toggle_show_cage"
	bl_label = "編集ケージへのモディファイア適用を切り替え"
	bl_description = "編集中のメッシュケージにモディファイアを適用するかを切り替えます"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		activeObj = context.active_object
		nowMode = 0
		for modi in activeObj.modifiers:
			if (modi.show_in_editmode and nowMode <= 0):
				nowMode = 1
			if (modi.show_on_cage and nowMode <= 1):
				nowMode = 2
		newMode = nowMode + 1
		if (newMode >= 3):
			newMode = 0
		for modi in activeObj.modifiers:
			if (newMode == 0):
				modi.show_in_editmode = False
				modi.show_on_cage = False
			if (newMode == 1):
				modi.show_in_editmode = True
				modi.show_on_cage = False
			if (newMode == 2):
				modi.show_in_editmode = True
				modi.show_on_cage = True
		if (newMode == 0):
			self.report(type={'INFO'}, message="ケージの表示/適応を両方オフにしました")
		if (newMode == 1):
			self.report(type={'INFO'}, message="ケージの表示のみオンにしました")
		if (newMode == 2):
			self.report(type={'INFO'}, message="ケージの表示/適応を両方オンにしました")
		return {'FINISHED'}

class ToggleMirrorModifier(bpy.types.Operator):
	bl_idname = "mesh.toggle_mirror_modifier"
	bl_label = "ミラーモディファイアを切り替え"
	bl_description = "ミラーモディファイアが無ければ追加、有れば削除します"
	bl_options = {'REGISTER', 'UNDO'}
	
	use_x = bpy.props.BoolProperty(name="X軸", default=True)
	use_y = bpy.props.BoolProperty(name="Y軸", default=False)
	use_z = bpy.props.BoolProperty(name="Z軸", default=False)
	use_mirror_merge = bpy.props.BoolProperty(name="結合", default=True)
	use_clip = bpy.props.BoolProperty(name="クリッピング", default=False)
	use_mirror_vertex_groups = bpy.props.BoolProperty(name="頂点グループミラー", default=False)
	use_mirror_u = bpy.props.BoolProperty(name="テクスチャUミラー", default=False)
	use_mirror_v = bpy.props.BoolProperty(name="テクスチャVミラー", default=False)
	merge_threshold = bpy.props.FloatProperty(name="結合距離", default=0.001, min=0, max=1, soft_min=0, soft_max=1, step=0.01, precision=6)
	
	def execute(self, context):
		activeObj = context.active_object
		is_mirrored = False
		for mod in activeObj.modifiers:
			if (mod.type == 'MIRROR'):
				is_mirrored = True
				break
		if (is_mirrored):
			for mod in activeObj.modifiers:
				if (mod.type == 'MIRROR'):
					activeObj.modifiers.remove(mod)
		else:
			new_mod = activeObj.modifiers.new("Mirror", 'MIRROR')
			new_mod.use_x = self.use_x
			new_mod.use_y = self.use_y
			new_mod.use_z = self.use_z
			new_mod.use_mirror_merge = self.use_mirror_merge
			new_mod.use_clip = self.use_clip
			new_mod.use_mirror_vertex_groups = self.use_mirror_vertex_groups
			new_mod.use_mirror_u = self.use_mirror_u
			new_mod.use_mirror_v = self.use_mirror_v
			new_mod.merge_threshold = self.merge_threshold
		return {'FINISHED'}
	def invoke(self, context, event):
		activeObj = context.active_object
		for mod in activeObj.modifiers:
			if (mod.type == 'MIRROR'):
				self.execute(context)
				return {'RUNNING_MODAL'}
		return context.window_manager.invoke_props_dialog(self)

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.operator(SelectTopShape.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.prop(context.object.data, "use_mirror_x", icon="PLUGIN", text="X軸ミラー編集")
	self.layout.operator(ToggleMirrorModifier.bl_idname, icon="PLUGIN")
	self.layout.operator(ToggleShowCage.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.operator(PaintSelectedVertexColor.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.operator(ApplySolidify.bl_idname, icon="PLUGIN")
