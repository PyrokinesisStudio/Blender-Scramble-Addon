# 「プロパティ」エリア > 「ボーン」タブ > 「インバースキネマティクス (IK)」パネル

import bpy

################
# オペレーター #
################

class CopyIKSettings(bpy.types.Operator):
	bl_idname = "pose.copy_ik_settings"
	bl_label = "Copy the IK set"
	bl_description = "Copies of other selected bone IK settings Active"
	bl_options = {'REGISTER', 'UNDO'}
	
	lock_ik_x = bpy.props.BoolProperty(name="Lock", default=True)
	ik_stiffness_x = bpy.props.BoolProperty(name="Rigid", default=True)
	use_ik_limit_x = bpy.props.BoolProperty(name="Limit", default=True)
	ik_min_x = bpy.props.BoolProperty(name="Smallest", default=True)
	ik_max_x = bpy.props.BoolProperty(name="Biggest", default=True)
	
	lock_ik_y = bpy.props.BoolProperty(name="Lock", default=True)
	ik_stiffness_y = bpy.props.BoolProperty(name="Rigid", default=True)
	use_ik_limit_y = bpy.props.BoolProperty(name="Limit", default=True)
	ik_min_y = bpy.props.BoolProperty(name="Smallest", default=True)
	ik_max_y = bpy.props.BoolProperty(name="Biggest", default=True)
	
	lock_ik_z = bpy.props.BoolProperty(name="Lock", default=True)
	ik_stiffness_z = bpy.props.BoolProperty(name="Rigid", default=True)
	use_ik_limit_z = bpy.props.BoolProperty(name="Limit", default=True)
	ik_min_z = bpy.props.BoolProperty(name="Smallest", default=True)
	ik_max_z = bpy.props.BoolProperty(name="Biggest", default=True)
	
	ik_stretch = bpy.props.BoolProperty(name="Stretch", default=True)
	
	@classmethod
	def poll(cls, context):
		if (2 <= len(context.selected_pose_bones)):
			return True
		return False
	
	def draw(self, context):
		for axis in ['x', 'y', 'z']:
			self.layout.label(axis.upper())
			row = self.layout.row()
			row.prop(self, 'lock_ik_'+axis)
			row.prop(self, 'ik_stiffness_'+axis)
			row = self.layout.row()
			row.prop(self, 'use_ik_limit_'+axis)
			row.prop(self, 'ik_min_'+axis)
			row.prop(self, 'ik_max_'+axis)
		self.layout.label("")
		self.layout.prop(self, 'ik_stretch')
	
	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self)
	
	def execute(self, context):
		source = context.active_pose_bone
		for target in context.selected_pose_bones[:]:
			if (source.name != target.name):
				for axis in ['x', 'y', 'z']:
					if (self.__getattribute__('lock_ik_'+axis)):
						target.__setattr__('lock_ik_'+axis, source.__getattribute__('lock_ik_'+axis))
					if (self.__getattribute__('ik_stiffness_'+axis)):
						target.__setattr__('ik_stiffness_'+axis, source.__getattribute__('ik_stiffness_'+axis))
					if (self.__getattribute__('use_ik_limit_'+axis)):
						target.__setattr__('use_ik_limit_'+axis, source.__getattribute__('use_ik_limit_'+axis))
					if (self.__getattribute__('ik_min_'+axis)):
						target.__setattr__('ik_min_'+axis, source.__getattribute__('ik_min_'+axis))
					if (self.__getattribute__('ik_max_'+axis)):
						target.__setattr__('ik_max_'+axis, source.__getattribute__('ik_max_'+axis))
				if (self.ik_stretch):
					target.ik_stretch = source.ik_stretch
		return {'FINISHED'}

class ReverseMinMax(bpy.types.Operator):
	bl_idname = "pose.reverse_min_max"
	bl_label = "Flip the minimum / maximum angle"
	bl_description = "Reverses the minimum and maximum angle of IK setup this bone"
	bl_options = {'REGISTER', 'UNDO'}
	
	is_x = bpy.props.BoolProperty(name="Flip X", default=False)
	is_y = bpy.props.BoolProperty(name="Flip Y", default=False)
	is_z = bpy.props.BoolProperty(name="Z invert", default=False)
	
	@classmethod
	def poll(cls, context):
		if (context.active_pose_bone):
			return True
		return False
	
	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self)
	
	def execute(self, context):
		bone = context.active_pose_bone
		if (self.is_x):
			ik_min = bone.ik_min_x
			ik_max = bone.ik_max_x
			bone.ik_min_x = -ik_max
			bone.ik_max_x = -ik_min
		if (self.is_y):
			ik_min = bone.ik_min_y
			ik_max = bone.ik_max_y
			bone.ik_min_y = -ik_max
			bone.ik_max_y = -ik_min
		if (self.is_z):
			ik_min = bone.ik_min_z
			ik_max = bone.ik_max_z
			bone.ik_min_z = -ik_max
			bone.ik_max_z = -ik_min
		for area in context.screen.areas:
			area.tag_redraw()
		return {'FINISHED'}

class CopyAxisSetting(bpy.types.Operator):
	bl_idname = "pose.copy_axis_setting"
	bl_label = "Copy to other axes axis settings"
	bl_description = "Copy the other axis on one axis"
	bl_options = {'REGISTER', 'UNDO'}
	
	items = [
		('x', "The x axis", "", 1),
		('y', "Y軸", "", 2),
		('z', "Z軸", "", 3),
		]
	source_axis = bpy.props.EnumProperty(items=items, name="Source-axis")
	target_x = bpy.props.BoolProperty(name="X", default=True)
	target_y = bpy.props.BoolProperty(name="To Y", default=True)
	target_z = bpy.props.BoolProperty(name="To Z", default=True)
	
	lock_ik = bpy.props.BoolProperty(name="Lock", default=True)
	ik_stiffness = bpy.props.BoolProperty(name="Rigid", default=True)
	use_ik_limit = bpy.props.BoolProperty(name="Limit", default=True)
	ik_min = bpy.props.BoolProperty(name="Smallest", default=True)
	ik_max = bpy.props.BoolProperty(name="Biggest", default=True)
	
	@classmethod
	def poll(cls, context):
		if (context.active_pose_bone):
			return True
		return False
	
	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self)
	
	def draw(self, context):
		self.layout.prop(self, 'source_axis')
		row = self.layout.row()
		row.prop(self, 'target_x')
		row.prop(self, 'target_y')
		row.prop(self, 'target_z')
		self.layout.label("Copying settings")
		row = self.layout.row()
		row.prop(self, 'lock_ik')
		row.prop(self, 'ik_stiffness')
		row = self.layout.row()
		row.prop(self, 'use_ik_limit')
		row.prop(self, 'ik_min')
		row.prop(self, 'ik_max')
	
	def execute(self, context):
		bone = context.active_pose_bone
		source_axis = self.source_axis
		for axis in ['x', 'y', 'z']:
			if (source_axis == axis):
				continue
			if (self.__getattribute__('target_' + axis)):
				if (self.lock_ik):
					value = bone.__getattribute__('lock_ik_' + source_axis)
					bone.__setattr__('lock_ik_' + axis, value)
				if (self.ik_stiffness):
					value = bone.__getattribute__('ik_stiffness_' + source_axis)
					bone.__setattr__('ik_stiffness_' + axis, value)
				if (self.use_ik_limit):
					value = bone.__getattribute__('use_ik_limit_' + source_axis)
					bone.__setattr__('use_ik_limit_' + axis, value)
				if (self.ik_min):
					value = bone.__getattribute__('ik_min_' + source_axis)
					bone.__setattr__('ik_min_' + axis, value)
				if (self.ik_max):
					value = bone.__getattribute__('ik_max_' + source_axis)
					bone.__setattr__('ik_max_' + axis, value)
		for area in context.screen.areas:
			area.tag_redraw()
		return {'FINISHED'}

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
		row.operator(CopyIKSettings.bl_idname, icon='COPY_ID', text="Copy the IK set")
		row.operator(ReverseMinMax.bl_idname, icon='ARROW_LEFTRIGHT', text="Flip angle limit")
		row.operator(CopyAxisSetting.bl_idname, icon='LINKED', text="Axis configuration copy")
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
