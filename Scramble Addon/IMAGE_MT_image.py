# UV/画像エディター > 「画像」メニュー

import bpy

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator("image.reload_all_image", icon="PLUGIN")
