# 「プロパティ」エリア > 「レンダー」タブ > 「ベイク」パネル

import bpy

################
# オペレーター #
################

class NewBakeImage(bpy.types.Operator):
	bl_idname = "image.new_bake_image"
	bl_label = "ベイク用の画像を作成"
	bl_description = "ベイクに使う新規画像を素早く用意可能です"
	bl_options = {'REGISTER', 'UNDO'}
	
	name = bpy.props.StringProperty(name="名前", default="Bake")
	width = bpy.props.IntProperty(name="幅", default=1024, min=1, max=8192, soft_min=1, soft_max=8192, step=1, subtype='PIXEL')
	height = bpy.props.IntProperty(name="高さ", default=1024, min=1, max=8192, soft_min=1, soft_max=8192, step=1, subtype='PIXEL')
	alpha = bpy.props.BoolProperty(name="アルファ", default=True)
	float = bpy.props.BoolProperty(name="32ビットFloat", default=False)
	show_image = bpy.props.BoolProperty(name="画像を確認", default=True)
	
	@classmethod
	def poll(cls, context):
		if (context.active_object):
			if (context.active_object.type == 'MESH'):
				if (len(context.active_object.data.uv_layers)):
					return True
		return False
	
	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self)
	
	def execute(self, context):
		new_image = bpy.data.images.new(self.name, self.width, self.height, self.alpha, self.float)
		me = context.active_object.data
		for data in me.uv_textures.active.data:
			data.image = new_image
		if (self.show_image):
			max = -1
			for area in context.screen.areas:
				if (area.type == 'IMAGE_EDITOR'):
					image_area = area
					break
				elif (area.type != 'VIEW_3D'):
					size = area.width * area.height
					if (max < size):
						image_area = area
						max = size
			else:
				image_area.type = 'IMAGE_EDITOR'
			for space in image_area.spaces:
				if (space.type == 'IMAGE_EDITOR'):
					space.image = new_image
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
		if (context.scene.render.bake_type == 'AO'):
			self.layout.prop(context.scene.world.light_settings, 'samples', icon='PLUGIN', text="AOサンプル数")
		self.layout.operator(NewBakeImage.bl_idname, icon='PLUGIN')
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
