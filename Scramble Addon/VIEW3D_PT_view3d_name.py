# 「3Dビュー」エリア > プロパティパネル > 「アイテム」パネル

import bpy

################
# オペレーター #
################

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
		row = self.layout.row(align=True)
		row.alignment = 'RIGHT'
		row.label("クリップボードへ")
		row.operator('object.copy_object_name', icon='MOVE_UP_VEC', text="")
		row.operator('object.copy_data_name', icon='MOVE_DOWN_VEC', text="")
		row = self.layout.row(align=True)
		row.alignment = 'RIGHT'
		row.label("名前を同期")
		row.operator('object.object_name_to_data_name', icon='TRIA_DOWN', text="")
		row.operator('object.data_name_to_object_name', icon='TRIA_UP', text="")
		self.layout.template_ID(context.object, 'data')
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
