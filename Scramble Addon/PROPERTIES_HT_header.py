# プロパティ > ヘッダー

import bpy

################
# オペレーター #
################

class ChangeRightContextTab(bpy.types.Operator):
	bl_idname = "buttons.change_context_tab"
	bl_label = "プロパティタブを切り替え"
	bl_description = "プロパティのタブを順番に切り替えます"
	bl_options = {'REGISTER'}
	
	is_left = bpy.props.BoolProperty(name="左へ", default=False)
	
	def execute(self, context):
		now_tab = context.space_data.context
		tabs = ['RENDER', 'RENDER_LAYER', 'SCENE', 'WORLD', 'OBJECT', 'CONSTRAINT', 'MODIFIER', 'DATA', 'BONE', 'BONE_CONSTRAINT', 'MATERIAL', 'TEXTURE', 'PARTICLES', 'PHYSICS']
		for tab in tabs[:]:
			try:
				context.space_data.context = tab
			except TypeError:
				tabs.remove(tab)
		if (now_tab not in tabs):
			self.report(type={'ERROR'}, message="現在のタブが予期せぬ設定値です")
			return {'CANCELLED'}
		if (self.is_left):
			tabs.reverse()
		flag = False
		for tab in tabs:
			if (flag):
				context.space_data.context = tab
				break
			if (tab == now_tab):
				flag = True
		else:
			context.space_data.context = tabs[0]
		return {'FINISHED'}

################
# サブメニュー #
################

class ShortcutsMenu(bpy.types.Menu):
	bl_idname = "PROPERTIES_HT_header_shortcuts"
	bl_label = "　ショートカット登録用"
	bl_description = "ショートカットに登録すると便利かもしれない機能のメニューです"
	
	def draw(self, context):
		self.layout.operator(ChangeRightContextTab.bl_idname, text="タブを右へ", icon="PLUGIN").is_left = False
		self.layout.operator(ChangeRightContextTab.bl_idname, text="タブを左へ", icon="PLUGIN").is_left = True

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.menu(ShortcutsMenu.bl_idname, icon="PLUGIN")
