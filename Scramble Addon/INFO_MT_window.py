import bpy

################
# オペレーター #
################

class ToggleJapaneseInterface(bpy.types.Operator):
	bl_idname = "ui.toggle_japanese_interface"
	bl_label = "UIの英語・日本語 切り替え"
	bl_description = "インターフェイスの英語と日本語を切り替えます"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		if (not bpy.context.user_preferences.system.use_international_fonts):
			bpy.context.user_preferences.system.use_international_fonts = True
		if (bpy.context.user_preferences.system.language != "ja_JP"):
			bpy.context.user_preferences.system.language = "ja_JP"
		bpy.context.user_preferences.system.use_translate_interface = not bpy.context.user_preferences.system.use_translate_interface
		return {'FINISHED'}

################
# パイメニュー #
################

class SelectModePieOperator(bpy.types.Operator):
	bl_idname = "mesh.select_mode_pie_operator"
	bl_label = "メッシュ選択モード"
	bl_description = "メッシュの選択のパイメニューです"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		bpy.ops.wm.call_menu_pie(name=SelectModePie.bl_idname)
		return {'FINISHED'}
class SelectModePie(bpy.types.Menu):
	bl_idname = "INFO_PIE_select_mode"
	bl_label = "メッシュ選択モード"
	bl_description = "メッシュの選択のパイメニューです"
	
	def draw(self, context):
		self.layout.menu_pie().operator("mesh.select_mode", text="頂点", icon='VERTEXSEL').type = 'VERT'
		self.layout.menu_pie().operator("mesh.select_mode", text="面", icon='FACESEL').type = 'FACE'
		self.layout.menu_pie().operator("mesh.select_mode", text="辺", icon='EDGESEL').type = 'EDGE'

################
# サブメニュー #
################

class PieMenu(bpy.types.Menu):
	bl_idname = "INFO_MT_window_pie"
	bl_label = "ショートカット登録用パイメニュー"
	bl_description = "ショートカット登録用のパイメニュー群です"
	
	def draw(self, context):
		self.layout.menu(PieMeshMenu.bl_idname, icon="PLUGIN")

class PieMeshMenu(bpy.types.Menu):
	bl_idname = "INFO_MT_window_pie_mesh"
	bl_label = "メッシュ"
	bl_description = "メッシュ関係のパイメニューです(エディトモードで登録して下さい)"
	
	def draw(self, context):
		self.layout.operator(SelectModePieOperator.bl_idname, icon="PLUGIN")

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(ToggleJapaneseInterface.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.menu(PieMenu.bl_idname, icon="PLUGIN")
