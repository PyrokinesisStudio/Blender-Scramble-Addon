# 「ノードエディター」エリア > 「ビュー」メニュー

import bpy

################
# オペレーター #
################

class TogglePanelsA(bpy.types.Operator):
	bl_idname = "node.toggle_panels_a"
	bl_label = "パネル表示切り替え(モードA)"
	bl_description = "プロパティ/ツールシェルフの「両方表示」/「両方非表示」をトグルします"
	bl_options = {'REGISTER'}
	
	def execute(self, context):
		toolW = 0
		uiW = 0
		for region in context.area.regions:
			if (region.type == 'TOOLS'):
				toolW = region.width
			if (region.type == 'UI'):
				uiW = region.width
		if (1 < toolW or 1 < uiW):
			if (1 < toolW):
				bpy.ops.node.toolbar()
			if (1 < uiW):
				bpy.ops.node.properties()
		else:
			bpy.ops.node.toolbar()
			bpy.ops.node.properties()
		return {'FINISHED'}

class TogglePanelsB(bpy.types.Operator):
	bl_idname = "node.toggle_panels_b"
	bl_label = "パネル表示切り替え(モードB)"
	bl_description = "「パネル両方非表示」→「ツールシェルフのみ表示」→「プロパティのみ表示」→「パネル両方表示」のトグル"
	bl_options = {'REGISTER'}
	
	def execute(self, context):
		toolW = 0
		uiW = 0
		for region in context.area.regions:
			if (region.type == 'TOOLS'):
				toolW = region.width
			if (region.type == 'UI'):
				uiW = region.width
		if (toolW <= 1 and uiW <= 1):
			bpy.ops.node.toolbar()
		elif (toolW <= 1 and 1 < uiW):
			bpy.ops.node.toolbar()
		else:
			bpy.ops.node.toolbar()
			bpy.ops.node.properties()
		return {'FINISHED'}

class TogglePanelsC(bpy.types.Operator):
	bl_idname = "node.toggle_panels_c"
	bl_label = "パネル表示切り替え(モードC)"
	bl_description = "「パネル両方非表示」→「ツールシェルフのみ表示」→「プロパティのみ表示」... のトグル"
	bl_options = {'REGISTER'}
	
	def execute(self, context):
		toolW = 0
		uiW = 0
		for region in context.area.regions:
			if (region.type == 'TOOLS'):
				toolW = region.width
			if (region.type == 'UI'):
				uiW = region.width
		if (toolW <= 1 and uiW <= 1):
			bpy.ops.node.toolbar()
		elif (1 < toolW and uiW <= 1):
			bpy.ops.node.toolbar()
			bpy.ops.node.properties()
		else:
			bpy.ops.node.properties()
		return {'FINISHED'}

################
# サブメニュー #
################

class ShortcutsMenu(bpy.types.Menu):
	bl_idname = "NODE_MT_view_shortcuts"
	bl_label = "ショートカット登録用"
	bl_description = "ショートカットに登録すると便利かもしれない機能群です"
	
	def draw(self, context):
		self.layout.operator(TogglePanelsA.bl_idname, icon="PLUGIN")
		self.layout.operator(TogglePanelsB.bl_idname, icon="PLUGIN")
		self.layout.operator(TogglePanelsC.bl_idname, icon="PLUGIN")

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
		self.layout.menu(ShortcutsMenu.bl_idname, icon="PLUGIN")
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.separator()
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
