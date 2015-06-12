# ユーザー設定 > ファイル

import bpy

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
		self.layout.label(text="画像エディター: 拡張")
		
		col = self.layout.column()
		
		
		col.prop(context.user_preferences.addons["Scramble Addon"].preferences, 'image_editor_path_1', text="")
		col.prop(context.user_preferences.addons["Scramble Addon"].preferences, 'image_editor_path_2', text="")
		col.prop(context.user_preferences.addons["Scramble Addon"].preferences, 'image_editor_path_3', text="")
		
		
		
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
