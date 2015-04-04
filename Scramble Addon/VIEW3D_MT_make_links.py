# 3Dビュー > オブジェクトモード > 「Ctrl+L」キー

import bpy, bmesh

################
# オペレーター #
################

class MakeLinkObjectName(bpy.types.Operator):
	bl_idname = "object.make_link_object_name"
	bl_label = "オブジェクト名を同じに"
	bl_description = "他の選択オブジェクトにアクティブオブジェクトの名前をリンクします"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		name = context.active_object.name
		for obj in context.selected_objects:
			if (obj.name != name):
				obj.name = "temp"
				obj.name = name
		bpy.context.active_object.name = name
		return {'FINISHED'}

class MakeLinkLayer(bpy.types.Operator):
	bl_idname = "object.make_link_layer"
	bl_label = "レイヤーを同じに"
	bl_description = "他の選択オブジェクトにアクティブオブジェクトのレイヤーをリンクします"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		for obj in context.selected_objects:
			if (obj.name != context.active_object.name):
				obj.layers = context.active_object.layers
		return {'FINISHED'}

class MakeLinkDisplaySetting(bpy.types.Operator):
	bl_idname = "object.make_link_display_setting"
	bl_label = "オブジェクトの表示設定を同じに"
	bl_description = "他の選択オブジェクトにアクティブオブジェクトの表示パネルの設定をコピーします"
	bl_options = {'REGISTER', 'UNDO'}
	
	isSameType = bpy.props.BoolProperty(name="同タイプのオブジェクトのみ", default=True)
	show_name = bpy.props.BoolProperty(name="名前", default=True)
	show_axis = bpy.props.BoolProperty(name="座標軸", default=True)
	show_wire = bpy.props.BoolProperty(name="ワイヤーフレーム", default=True)
	show_all_edges = bpy.props.BoolProperty(name="すべての辺を表示", default=True)
	show_bounds = bpy.props.BoolProperty(name="バウンド", default=True)
	show_texture_space = bpy.props.BoolProperty(name="テクスチャ スペース", default=True)
	show_x_ray = bpy.props.BoolProperty(name="レントゲン", default=True)
	show_transparent = bpy.props.BoolProperty(name="透過", default=True)
	draw_bounds_type = bpy.props.BoolProperty(name="バウンドのタイプ", default=True)
	draw_type = bpy.props.BoolProperty(name="最高描画タイプ", default=True)
	color = bpy.props.BoolProperty(name="オブジェクトカラー", default=True)
	
	def execute(self, context):
		activeObj = context.active_object
		for obj in context.selected_objects:
			if (not self.isSameType or activeObj.type == obj.type):
				if (obj.name != activeObj.name):
					if (self.show_name):
						obj.show_name = activeObj.show_name
					if (self.show_axis):
						obj.show_axis = activeObj.show_axis
					if (self.show_wire):
						obj.show_wire = activeObj.show_wire
					if (self.show_all_edges):
						obj.show_all_edges = activeObj.show_all_edges
					if (self.show_bounds):
						obj.show_bounds = activeObj.show_bounds
					if (self.show_texture_space):
						obj.show_texture_space = activeObj.show_texture_space
					if (self.show_x_ray):
						obj.show_x_ray = activeObj.show_x_ray
					if (self.show_transparent):
						obj.show_transparent = activeObj.show_transparent
					if (self.draw_bounds_type):
						obj.draw_bounds_type = activeObj.draw_bounds_type
					if (self.draw_type):
						obj.draw_type = activeObj.draw_type
					if (self.color):
						obj.color = activeObj.color
		return {'FINISHED'}

class MakeLinkUVNames(bpy.types.Operator):
	bl_idname = "object.make_link_uv_names"
	bl_label = "空のUVマップをリンク"
	bl_description = "他の選択オブジェクトにアクティブオブジェクトのUVを空にして追加します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		active_obj = context.active_object
		if (active_obj.type != 'MESH'):
			self.report(type={'ERROR'}, message="アクティブオブジェクトはメッシュである必要があります")
			return {'CANCELLED'}
		target_objs = []
		for obj in context.selected_objects:
			if (obj.type == 'MESH' and active_obj.name != obj.name):
				target_objs.append(obj)
		if (len(target_objs) <= 0):
			self.report(type={'ERROR'}, message="リンクすべきメッシュオブジェクトがありません")
			return {'CANCELLED'}
		for obj in target_objs:
			bm = bmesh.new()
			bm.from_mesh(obj.data)
			for uv in active_obj.data.uv_layers:
				bm.loops.layers.uv.new(uv.name)
			bm.to_mesh(obj.data)
			bm.free()
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(MakeLinkObjectName.bl_idname, text="オブジェクト名", icon="PLUGIN")
	self.layout.operator(MakeLinkLayer.bl_idname, text="レイヤー", icon="PLUGIN")
	self.layout.operator(MakeLinkDisplaySetting.bl_idname, text="表示設定", icon="PLUGIN")
	self.layout.operator(MakeLinkUVNames.bl_idname, text="空UV", icon="PLUGIN")
