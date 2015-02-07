import bpy

################
# オペレーター #
################

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator("image.reload_all_image", icon="PLUGIN")
