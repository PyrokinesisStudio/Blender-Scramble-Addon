# 「プロパティ」エリア > 「オブジェクト」タブ > 「表示」パネル

import bpy

################
# オペレーター #
################

class CopyDisplaySetting(bpy.types.Operator):
	bl_idname = "object.copy_display_setting"
	bl_label = "表示設定をコピー"
	bl_description = "この表示設定を他の選択オブジェクトにコピーします"
	bl_options = {'REGISTER', 'UNDO'}
	
	copy_show_name = bpy.props.BoolProperty(name="名前", default=True)
	copy_show_axis = bpy.props.BoolProperty(name="座標軸", default=True)
	copy_show_wire = bpy.props.BoolProperty(name="ワイヤーフレーム", default=True)
	copy_show_all_edges = bpy.props.BoolProperty(name="すべての辺を表示", default=True)
	copy_show_bounds = bpy.props.BoolProperty(name="バウンド", default=True)
	copy_draw_bounds_type = bpy.props.BoolProperty(name="バウンドタイプ", default=True)
	copy_show_texture_space = bpy.props.BoolProperty(name="テクスチャスペース", default=True)
	copy_show_x_ray = bpy.props.BoolProperty(name="レントゲン", default=True)
	copy_show_transparent = bpy.props.BoolProperty(name="透過", default=True)
	copy_draw_type = bpy.props.BoolProperty(name="最高描画タイプ", default=True)
	copy_color = bpy.props.BoolProperty(name="オブジェクトカラー", default=True)
	
	@classmethod
	def poll(cls, context):
		if (len(context.selected_objects) <= 1):
			return False
		return True
	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self)
	def execute(self, context):
		active_obj = context.active_object
		for obj in context.selected_objects:
			if (obj.name != active_obj.name):
				if (self.copy_show_name):
					obj.show_name = active_obj.show_name
				if (self.copy_show_axis):
					obj.show_axis = active_obj.show_axis
				if (self.copy_show_wire):
					obj.show_wire = active_obj.show_wire
				if (self.copy_show_all_edges):
					obj.show_all_edges = active_obj.show_all_edges
				if (self.copy_show_bounds):
					obj.show_bounds = active_obj.show_bounds
				if (self.copy_draw_bounds_type):
					obj.draw_bounds_type = active_obj.draw_bounds_type
				if (self.copy_show_texture_space):
					obj.show_texture_space = active_obj.show_texture_space
				if (self.copy_show_x_ray):
					obj.show_x_ray = active_obj.show_x_ray
				if (self.copy_show_transparent):
					obj.show_transparent = active_obj.show_transparent
				if (self.copy_draw_type):
					obj.draw_type = active_obj.draw_type
				if (self.copy_color):
					obj.color = active_obj.color[:]
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューのオン/オフの判定
def IsMenuEnable(self_id):
	for id in bpy.context.user_preferences.addons["Scramble Addon"].preferences.disabled_menu.split(','):
		if (id == self_id):
			return False
	else:
		return True

# メニューを登録する関数
def menu(self, context):
	if (IsMenuEnable(__name__.split('.')[-1])):
		self.layout.operator(CopyDisplaySetting.bl_idname, icon='PLUGIN')
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
