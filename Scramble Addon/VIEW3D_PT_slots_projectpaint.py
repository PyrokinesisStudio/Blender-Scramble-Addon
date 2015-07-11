# 「3Dビュー」エリア > テクスチャペイント > ツールシェルフ > 「スロット」パネル

import bpy

################
# オペレーター #
################

class ActiveTextureSlotToActivePaintSlot(bpy.types.Operator):
	bl_idname = "texture.active_texture_slot_to_active_paint_slot"
	bl_label = "Apply active texture slot"
	bl_description = "active texture slot slot active paint"
	bl_options = {'REGISTER'}
	
	@classmethod
	def poll(cls, context):
		if (not context.object):
			return False
		if (not context.object.active_material):
			return False
		if (not context.object.active_material.active_texture):
			return False
		return True
	def execute(self, context):
		context.object.active_material.paint_active_slot = context.object.active_material.active_texture_index
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
		if (context.object):
			if (context.object.active_material):
				if (context.object.active_material.use_nodes):
					self.layout.prop(context.object.active_material, 'use_nodes', icon='PLUGIN', text="Impossible, Because nodes used")
				else:
					self.layout.operator(ActiveTextureSlotToActivePaintSlot.bl_idname, icon='PLUGIN', text="Active texture slots")
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
