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

class ObjectModePieOperator(bpy.types.Operator):
	bl_idname = "object.object_mode_pie_operator"
	bl_label = "オブジェクト対話モード"
	bl_description = "オブジェクト対話モードのパイメニューです"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		bpy.ops.wm.call_menu_pie(name=ObjectModePie.bl_idname)
		return {'FINISHED'}
class ObjectModePie(bpy.types.Menu):
	bl_idname = "INFO_PIE_object_mode"
	bl_label = "オブジェクト対話モード"
	bl_description = "オブジェクト対話モードのパイメニューです"
	
	def draw(self, context):
		self.layout.menu_pie().operator(SetObjectMode.bl_idname, text="ポーズ", icon="POSE_HLT").mode = "POSE"
		self.layout.menu_pie().operator(SetObjectMode.bl_idname, text="スカルプト", icon="SCULPTMODE_HLT").mode = "SCULPT"
		self.layout.menu_pie().operator(SetObjectMode.bl_idname, text="ウェイトペイント", icon="WPAINT_HLT").mode = "WEIGHT_PAINT"
		self.layout.menu_pie().operator(SetObjectMode.bl_idname, text="オブジェクト", icon="OBJECT_DATAMODE").mode = "OBJECT"
		self.layout.menu_pie().operator(SetObjectMode.bl_idname, text="パーティクル編集", icon="PARTICLEMODE").mode = "PARTICLE_EDIT"
		self.layout.menu_pie().operator(SetObjectMode.bl_idname, text="編集", icon="EDITMODE_HLT").mode = "EDIT"
		self.layout.menu_pie().operator(SetObjectMode.bl_idname, text="テクスチャペイント", icon="TPAINT_HLT").mode = "TEXTURE_PAINT"
		self.layout.menu_pie().operator(SetObjectMode.bl_idname, text="頂点ペイント", icon="VPAINT_HLT").mode = "VERTEX_PAINT"
class SetObjectMode(bpy.types.Operator):
	bl_idname = "object.set_object_mode"
	bl_label = "オブジェクト対話モードを設定"
	bl_description = "オブジェクトの対話モードを設定します"
	bl_options = {'REGISTER', 'UNDO'}
	
	mode = bpy.props.StringProperty(name="対話モード", default="OBJECT")
	
	def execute(self, context):
		if (context.active_object):
			try:
				bpy.ops.object.mode_set(mode=self.mode)
			except TypeError:
				self.report(type={"WARNING"}, message=context.active_object.name+" はその対話モードに入る事が出来ません")
		return {'FINISHED'}

class SubdivisionSetPieOperator(bpy.types.Operator):
	bl_idname = "object.subdivision_set_pie_operator"
	bl_label = "サブサーフ設定"
	bl_description = "サブサーフのレベルを設定するパイメニューです"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		bpy.ops.wm.call_menu_pie(name=SubdivisionSetPie.bl_idname)
		return {'FINISHED'}
class SubdivisionSetPie(bpy.types.Menu):
	bl_idname = "INFO_PIE_subdivision_set"
	bl_label = "サブサーフ設定"
	bl_description = "サブサーフのレベルを設定するパイメニューです"
	
	def draw(self, context):
		self.layout.menu_pie().operator("object.subdivision_set", text="レベル:2", icon="MOD_SUBSURF").level = 2
		self.layout.menu_pie().operator("object.subdivision_set", text="レベル:6", icon="MOD_SUBSURF").level = 6
		self.layout.menu_pie().operator("object.subdivision_set", text="レベル:0", icon="MOD_SUBSURF").level = 0
		self.layout.menu_pie().operator("object.subdivision_set", text="レベル:4", icon="MOD_SUBSURF").level = 4
		self.layout.menu_pie().operator("object.subdivision_set", text="レベル:3", icon="MOD_SUBSURF").level = 3
		self.layout.menu_pie().operator("object.subdivision_set", text="レベル:5", icon="MOD_SUBSURF").level = 5
		self.layout.menu_pie().operator("object.subdivision_set", text="レベル:1", icon="MOD_SUBSURF").level = 1

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

class ProportionalPieOperator(bpy.types.Operator):
	bl_idname = "mesh.proportional_pie_operator"
	bl_label = "プロポーショナル編集"
	bl_description = "プロポーショナル編集のパイメニューです"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		if (context.scene.tool_settings.proportional_edit == "DISABLED"):
			bpy.ops.wm.call_menu_pie(name=ProportionalPie.bl_idname)
		else:
			context.scene.tool_settings.proportional_edit = "DISABLED"
		return {'FINISHED'}
class ProportionalPie(bpy.types.Menu):
	bl_idname = "INFO_PIE_proportional"
	bl_label = "プロポーショナル編集"
	bl_description = "プロポーショナル編集のパイメニューです"
	
	def draw(self, context):
		self.layout.menu_pie().operator(SetProportionalEdit.bl_idname, text="有効化", icon="PROP_ON").mode = "ENABLED"
		self.layout.menu_pie().operator(SetProportionalEdit.bl_idname, text="投影(2D)", icon="PROP_ON").mode = "PROJECTED"
		self.layout.menu_pie().operator(SetProportionalEdit.bl_idname, text="接続", icon="PROP_CON").mode = "CONNECTED"
class SetProportionalEdit(bpy.types.Operator):
	bl_idname = "mesh.set_proportional_edit"
	bl_label = "プロポーショナル編集のモードを設定"
	bl_description = "プロポーショナル編集のモードを設定します"
	bl_options = {'REGISTER', 'UNDO'}
	
	mode = bpy.props.StringProperty(name="モード", default="DISABLED")
	
	def execute(self, context):
		context.scene.tool_settings.proportional_edit = self.mode
		return {'FINISHED'}

################
# サブメニュー #
################

class PieMenu(bpy.types.Menu):
	bl_idname = "INFO_MT_window_pie"
	bl_label = "ショートカット登録用パイメニュー"
	bl_description = "ショートカット登録用のパイメニュー群です"
	
	def draw(self, context):
		self.layout.menu(PieObjectMenu.bl_idname, icon="PLUGIN")
		self.layout.menu(PieMeshMenu.bl_idname, icon="PLUGIN")

class PieObjectMenu(bpy.types.Menu):
	bl_idname = "INFO_MT_window_pie_object"
	bl_label = "オブジェクト"
	bl_description = "オブジェクト関係のパイメニューです(オブジェクトモードで登録して下さい)"
	
	def draw(self, context):
		self.layout.operator(ObjectModePieOperator.bl_idname, icon="PLUGIN")
		self.layout.operator(SubdivisionSetPieOperator.bl_idname, icon="PLUGIN")

class PieMeshMenu(bpy.types.Menu):
	bl_idname = "INFO_MT_window_pie_mesh"
	bl_label = "メッシュ"
	bl_description = "メッシュ関係のパイメニューです(エディトモードで登録して下さい)"
	
	def draw(self, context):
		self.layout.operator(SelectModePieOperator.bl_idname, icon="PLUGIN")
		self.layout.operator(ProportionalPieOperator.bl_idname, icon="PLUGIN")

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(ToggleJapaneseInterface.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.menu(PieMenu.bl_idname, icon="PLUGIN")
