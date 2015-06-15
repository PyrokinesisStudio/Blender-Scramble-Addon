# 「3Dビュー」エリア > 「プロパティ」パネル > 「ビュー」パネル

import bpy

################
# オペレーター #
################

class SaveView(bpy.types.Operator):
	bl_idname = "view3d.save_view"
	bl_label = "視点のセーブ"
	bl_description = "現在の3Dビューの視点をセーブします"
	bl_options = {'REGISTER', 'UNDO'}
	
	save_name = bpy.props.StringProperty(name="名前", default="視点セーブデータ")
	
	def execute(self, context):
		data = ""
		for line in context.user_preferences.addons["Scramble Addon"].preferences.view_savedata.split('|'):
			if (line == ""):
				continue
			try:
				save_name = line.split(':')[0]
			except ValueError:
				context.user_preferences.addons["Scramble Addon"].preferences.view_savedata = ""
				self.report(type={'ERROR'}, message="視点の読み込みに失敗しました、セーブデータをリセットします")
				return {'CANCELLED'}
			if (str(self.save_name) == save_name):
				continue
			data = data + line + '|'
		text = data + str(self.save_name) + ':'
		co = context.region_data.view_location
		text = text + str(co[0]) + ',' + str(co[1]) + ',' + str(co[2]) + ':'
		ro = context.region_data.view_rotation
		text = text + str(ro[0]) + ',' + str(ro[1]) + ',' + str(ro[2]) + ',' + str(ro[3]) + ':'
		text = text + str(context.region_data.view_distance) + ':'
		text = text + context.region_data.view_perspective
		context.user_preferences.addons["Scramble Addon"].preferences.view_savedata = text
		self.report(type={'INFO'}, message="現在の視点をセーブデータ"+str(self.save_name)+"に保存しました")
		for area in context.screen.areas:
			area.tag_redraw()
		return {'FINISHED'}
	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self)

class LoadView(bpy.types.Operator):
	bl_idname = "view3d.load_view"
	bl_label = "視点のロード"
	bl_description = "現在の3Dビューに視点をロードします"
	bl_options = {'REGISTER', 'UNDO'}
	
	index = bpy.props.StringProperty(name="視点セーブデータ名", default="視点セーブデータ")
	
	def execute(self, context):
		for line in context.user_preferences.addons["Scramble Addon"].preferences.view_savedata.split('|'):
			if (line == ""):
				continue
			try:
				index, loc, rot, distance, view_perspective = line.split(':')
			except ValueError:
				context.user_preferences.addons["Scramble Addon"].preferences.view_savedata = ""
				self.report(type={'ERROR'}, message="視点の読み込みに失敗しました、セーブデータをリセットします")
				return {'CANCELLED'}
			if (str(self.index) == index):
				for i, v in enumerate(loc.split(',')):
					context.region_data.view_location[i] = float(v)
				for i, v in enumerate(rot.split(',')):
					context.region_data.view_rotation[i] = float(v)
				context.region_data.view_distance = float(distance)
				context.region_data.view_perspective = view_perspective
				self.report(type={'INFO'}, message="視点セーブデータ"+str(self.index)+"を読み込みました")
				break
		else:
			self.report(type={'WARNING'}, message="視点のセーブデータ"+str(self.index)+"が存在しませんでした")
		return {'FINISHED'}

class DeleteViewSavedata(bpy.types.Operator):
	bl_idname = "view3d.delete_view_savedata"
	bl_label = "視点セーブを破棄"
	bl_description = "全ての視点セーブデータを削除します"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		if (context.user_preferences.addons["Scramble Addon"].preferences.view_savedata == ""):
			return False
		return True
	def execute(self, context):
		context.user_preferences.addons["Scramble Addon"].preferences.view_savedata = ""
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
		self.layout.prop(context.user_preferences.view, 'use_zoom_to_mouse')
		self.layout.prop(context.user_preferences.view, 'use_rotate_around_active')
		box = self.layout.box()
		col = box.column(align=True)
		col.operator(SaveView.bl_idname, icon="PLUGIN")
		col.operator(DeleteViewSavedata.bl_idname, icon="PLUGIN")
		if (context.user_preferences.addons["Scramble Addon"].preferences.view_savedata):
			col = box.column(align=True)
			col.label(text="視点セーブをロード", icon='PLUGIN')
			for line in context.user_preferences.addons["Scramble Addon"].preferences.view_savedata.split('|'):
				if (line == ""):
					continue
				try:
					index = line.split(':')[0]
				except ValueError:
					pass
				col.operator(LoadView.bl_idname, text=index, icon="PLUGIN").index = index
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
