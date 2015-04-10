# 情報 > 「レンダー」メニュー

import bpy

################
# オペレーター #
################

class SetRenderResolutionPercentage(bpy.types.Operator):
	bl_idname = "render.set_render_resolution_percentage"
	bl_label = "解像度の倍率を設定"
	bl_description = "設定解像度の何パーセントの大きさでレンダリングするか設定します"
	bl_options = {'REGISTER', 'UNDO'}
	
	size = bpy.props.IntProperty(name="レンダリングサイズ(%)", default=100, min=1, max=1000, soft_min=1, soft_max=1000, step=1)
	
	def execute(self, context):
		context.scene.render.resolution_percentage = self.size
		return {'FINISHED'}

class SetRenderSlot(bpy.types.Operator):
	bl_idname = "render.set_render_slot"
	bl_label = "レンダースロットを設定"
	bl_description = "レンダリング結果を保存するスロットを設定します"
	bl_options = {'REGISTER', 'UNDO'}
	
	slot = bpy.props.IntProperty(name="スロット", default=1, min=0, max=100, soft_min=0, soft_max=100, step=1)
	
	def execute(self, context):
		bpy.data.images["Render Result"].render_slots.active_index = self.slot
		return {'FINISHED'}

class ToggleThreadsMode(bpy.types.Operator):
	bl_idname = "render.toggle_threads_mode"
	bl_label = "スレッド数を切り替え"
	bl_description = "レンダリングに使用するCPUのスレッド数を切り替えます"
	bl_options = {'REGISTER', 'UNDO'}
	
	threads = bpy.props.IntProperty(name="スレッド数", default=1, min=1, max=16, soft_min=1, soft_max=16, step=1)
	
	def execute(self, context):
		if (context.scene.render.threads_mode == 'AUTO'):
			context.scene.render.threads_mode = 'FIXED'
			context.scene.render.threads = self.threads
		else:
			context.scene.render.threads_mode = 'AUTO'
		return {'FINISHED'}
	def invoke(self, context, event):
		if (context.scene.render.threads_mode == 'AUTO'):
			self.threads = context.scene.render.threads
			return context.window_manager.invoke_props_dialog(self)
		else:
			return self.execute(context)

################
# サブメニュー #
################

class RenderResolutionPercentageMenu(bpy.types.Menu):
	bl_idname = "INFO_MT_render_resolution_percentage"
	bl_label = "レンダリングサイズ(%)"
	bl_description = "設定解像度の何パーセントの大きさでレンダリングするか設定します"
	
	def draw(self, context):
		x = bpy.context.scene.render.resolution_x
		y = bpy.context.scene.render.resolution_y
		self.layout.operator(SetRenderResolutionPercentage.bl_idname, text="10% ("+str(int(x*0.1))+"x"+str(int(y*0.1))+")", icon="PLUGIN").size = 10
		self.layout.operator(SetRenderResolutionPercentage.bl_idname, text="20% ("+str(int(x*0.2))+"x"+str(int(y*0.2))+")", icon="PLUGIN").size = 20
		self.layout.operator(SetRenderResolutionPercentage.bl_idname, text="30% ("+str(int(x*0.3))+"x"+str(int(y*0.3))+")", icon="PLUGIN").size = 30
		self.layout.operator(SetRenderResolutionPercentage.bl_idname, text="40% ("+str(int(x*0.4))+"x"+str(int(y*0.4))+")", icon="PLUGIN").size = 40
		self.layout.operator(SetRenderResolutionPercentage.bl_idname, text="50% ("+str(int(x*0.5))+"x"+str(int(y*0.5))+")", icon="PLUGIN").size = 50
		self.layout.operator(SetRenderResolutionPercentage.bl_idname, text="60% ("+str(int(x*0.6))+"x"+str(int(y*0.6))+")", icon="PLUGIN").size = 60
		self.layout.operator(SetRenderResolutionPercentage.bl_idname, text="70% ("+str(int(x*0.7))+"x"+str(int(y*0.7))+")", icon="PLUGIN").size = 70
		self.layout.operator(SetRenderResolutionPercentage.bl_idname, text="80% ("+str(int(x*0.8))+"x"+str(int(y*0.8))+")", icon="PLUGIN").size = 80
		self.layout.operator(SetRenderResolutionPercentage.bl_idname, text="90% ("+str(int(x*0.9))+"x"+str(int(y*0.9))+")", icon="PLUGIN").size = 90
		self.layout.separator()
		self.layout.operator(SetRenderResolutionPercentage.bl_idname, text="100% ("+str(int(x))+"x"+str(int(y))+")", icon="PLUGIN").size = 100
		self.layout.separator()
		self.layout.operator(SetRenderResolutionPercentage.bl_idname, text="150% ("+str(int(x*1.5))+"x"+str(int(y*1.5))+")", icon="PLUGIN").size = 150
		self.layout.operator(SetRenderResolutionPercentage.bl_idname, text="200% ("+str(int(x*2.0))+"x"+str(int(y*2.0))+")", icon="PLUGIN").size = 200
		self.layout.operator(SetRenderResolutionPercentage.bl_idname, text="300% ("+str(int(x*3.0))+"x"+str(int(y*3.0))+")", icon="PLUGIN").size = 300

class SimplifyRenderMenu(bpy.types.Menu):
	bl_idname = "INFO_MT_render_simplify"
	bl_label = "レンダーの簡略化"
	bl_description = "レンダリングの簡略化設定をします"
	
	def draw(self, context):
		self.layout.prop(context.scene.render, "use_simplify", icon="PLUGIN")
		self.layout.separator()
		self.layout.prop(context.scene.render, "simplify_subdivision", icon="PLUGIN")
		self.layout.prop(context.scene.render, "simplify_shadow_samples", icon="PLUGIN")
		self.layout.prop(context.scene.render, "simplify_child_particles", icon="PLUGIN")
		self.layout.prop(context.scene.render, "simplify_ao_sss", icon="PLUGIN")
		self.layout.prop(context.scene.render, "use_simplify_triangulate", icon="PLUGIN")

class SlotsRenderMenu(bpy.types.Menu):
	bl_idname = "INFO_MT_render_slots"
	bl_label = "レンダースロット"
	bl_description = "レンダリング結果を保存するスロットを変更します"
	
	def draw(self, context):
		for i in range(len(bpy.data.images["Render Result"].render_slots)):
			self.layout.operator(SetRenderSlot.bl_idname, text="スロット"+str(i+1)).slot = i

class ShadeingMenu(bpy.types.Menu):
	bl_idname = "INFO_MT_render_shadeing"
	bl_label = "シェーディング"
	bl_description = "シェーディングのオン/オフをします"
	
	def draw(self, context):
		self.layout.prop(context.scene.render, 'use_textures', icon="PLUGIN")
		self.layout.prop(context.scene.render, 'use_shadows', icon="PLUGIN")
		self.layout.prop(context.scene.render, 'use_sss', icon="PLUGIN")
		self.layout.prop(context.scene.render, 'use_envmaps', icon="PLUGIN")
		self.layout.prop(context.scene.render, 'use_raytrace', icon="PLUGIN")

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
		self.layout.separator()
		self.layout.prop(context.scene.render, 'resolution_x', text="解像度 X", icon="PLUGIN")
		self.layout.prop(context.scene.render, 'resolution_y', text="解像度 Y", icon="PLUGIN")
		if (bpy.data.images.find("Render Result") != -1):
			self.layout.menu(SlotsRenderMenu.bl_idname, text="レンダースロット (現在:スロット"+str(bpy.data.images["Render Result"].render_slots.active_index+1)+")", icon="PLUGIN")
		self.layout.menu(RenderResolutionPercentageMenu.bl_idname, text="レンダリングサイズ (現在:"+str(context.scene.render.resolution_percentage)+"%)", icon="PLUGIN")
		self.layout.separator()
		self.layout.prop(context.scene, 'frame_start', text="開始フレーム", icon="PLUGIN")
		self.layout.prop(context.scene, 'frame_end', text="最終フレーム", icon="PLUGIN")
		self.layout.prop(context.scene, 'frame_step', text="フレームステップ", icon="PLUGIN")
		self.layout.prop(context.scene.render, 'fps', text="FPS", icon="PLUGIN")
		self.layout.separator()
		self.layout.prop(context.scene.render, 'use_antialiasing', text="アンチエイリアス使用", icon="PLUGIN")
		self.layout.prop_menu_enum(context.scene.render, 'antialiasing_samples', text="アンチエイリアス サンプル数", icon="PLUGIN")
		self.layout.menu(ShadeingMenu.bl_idname, icon="PLUGIN")
		self.layout.separator()
		self.layout.prop(context.scene.world.light_settings, 'use_ambient_occlusion', text="AOを使用", icon="PLUGIN")
		self.layout.prop(context.scene.world.light_settings, 'samples', text="AOサンプル数", icon="PLUGIN")
		self.layout.separator()
		self.layout.prop(context.scene.render, 'use_freestyle', text="FreeStyleの使用", icon="PLUGIN")
		self.layout.separator()
		self.layout.prop_menu_enum(context.scene.render.image_settings, 'file_format', text="ファイルフォーマット", icon="PLUGIN")
		text = ToggleThreadsMode.bl_label
		if (context.scene.render.threads_mode == 'AUTO'):
			text = text + " (現在 自動検知)"
		else:
			text = text + " (現在 定値：" + str(context.scene.render.threads) + ")"
		self.layout.operator(ToggleThreadsMode.bl_idname, text=text, icon="PLUGIN")
		self.layout.menu(SimplifyRenderMenu.bl_idname, icon="PLUGIN")
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.separator()
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
