# ユーザー設定 > ヘッダー

import bpy

################
# オペレーター #
################

class CloseKeyMapItems(bpy.types.Operator):
	bl_idname = "ui.close_key_map_items"
	bl_label = "キーコンフィグを全て閉じる"
	bl_description = "キーコンフィグのメニューを全て折りたたみます"
	bl_options = {'REGISTER'}
	
	def execute(self, context):
		for keyconfig in context.window_manager.keyconfigs:
			for keymap in keyconfig.keymaps:
				keymap.show_expanded_children = False
				keymap.show_expanded_items = False
				for keymap_item in keymap.keymap_items:
					keymap_item.show_expanded = False
		for area in context.screen.areas:
			area.tag_redraw()
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	if (context.user_preferences.active_section == 'INPUT'):
		self.layout.operator(CloseKeyMapItems.bl_idname, icon="PLUGIN")
