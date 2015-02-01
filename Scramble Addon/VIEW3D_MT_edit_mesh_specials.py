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
	self.layout.prop(context.object.data, "use_mirror_x", icon="PLUGIN", text="X軸ミラー編集")
