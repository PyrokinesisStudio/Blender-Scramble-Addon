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

########################
# オペレーター(簡略化) #
########################

class SetSimplify(bpy.types.Operator):
	bl_idname = "world.set_simplify"
	bl_label = "レンダー簡略化の設定"
	bl_description = "レンダリングの簡略化の設定を行います(本来はシーンタブから行います)"
	bl_options = {'REGISTER', 'UNDO'}
	
	use = bpy.props.BoolProperty(name="簡略化を使う", default=True)
	subdivision = bpy.props.IntProperty(name="最大再分割数", default=6, min=0, max=6, soft_min=0, soft_max=6, step=1)
	shadowSamples = bpy.props.IntProperty(name="最大シャドウサンプル", default=16, min=0, max=16, soft_min=0, soft_max=16, step=1)
	childParticles = bpy.props.FloatProperty(name="子パーティクルの割合", default=1, min=0, max=1, soft_min=0, soft_max=1, step=10, precision=3)
	aoAndSss = bpy.props.FloatProperty(name="AOとSSSの割合", default=1, min=0, max=1, soft_min=0, soft_max=1, step=10, precision=3)
	triangulate = bpy.props.BoolProperty(name="四角形の三角形化をスキップ", default=False)
	
	def execute(self, context):
		context.scene.render.use_simplify = self.use
		context.scene.render.simplify_subdivision = self.subdivision
		context.scene.render.simplify_shadow_samples = self.shadowSamples
		context.scene.render.simplify_child_particles = self.childParticles
		context.scene.render.simplify_ao_sss = self.aoAndSss
		context.scene.render.use_simplify_triangulate = self.triangulate
		return {'FINISHED'}
	def invoke(self, context, event):
		wm = context.window_manager
		return wm.invoke_props_dialog(self)

################
# メニュー追加 #
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
		self.layout.separator()
		
		i = self.layout.operator(SetSimplify.bl_idname, icon="PLUGIN")
		i.use = context.scene.render.use_simplify
		i.subdivision = context.scene.render.simplify_subdivision
		i.shadowSamples = context.scene.render.simplify_shadow_samples
		i.childParticles = context.scene.render.simplify_child_particles
		i.aoAndSss = context.scene.render.simplify_ao_sss
		i.triangulate = context.scene.render.use_simplify_triangulate

class SlotsRenderMenu(bpy.types.Menu):
	bl_idname = "INFO_MT_render_slots"
	bl_label = "レンダースロット"
	bl_description = "レンダリング結果を保存するスロットを変更します"
	
	def draw(self, context):
		for i in range(len(bpy.data.images["Render Result"].render_slots)):
			self.layout.operator(SetRenderSlot.bl_idname, text="スロット"+str(i+1)).slot = i

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	if (bpy.data.images.find("Render Result") != -1):
		self.layout.menu(SlotsRenderMenu.bl_idname, text="レンダースロット (現在:スロット"+str(bpy.data.images["Render Result"].render_slots.active_index+1)+")", icon="PLUGIN")
	self.layout.menu(RenderResolutionPercentageMenu.bl_idname, text="レンダリングサイズ (現在:"+str(context.scene.render.resolution_percentage)+"%)", icon="PLUGIN")
	self.layout.prop(context.scene.world.light_settings, "samples", text="AOサンプル数", icon="PLUGIN")
	self.layout.menu(SimplifyRenderMenu.bl_idname, icon="PLUGIN")
