import bpy

##############
# その他関数 #
##############

################
# オペレーター #
################

class CreateCustomShape(bpy.types.Operator):
	bl_idname = "pose.create_custom_shape"
	bl_label = "選択ボーンのカスタムシェイプを作成"
	bl_description = "選択中のボーンのカスタムシェイプオブジェクトを作成します"
	bl_options = {'REGISTER', 'UNDO'}
	
	name =  bpy.props.StringProperty(name="オブジェクト名", default="カスタムシェイプ用オブジェクト")
	items = [
		("1", "線", "", 1),
		("2", "ひし形", "", 2),
		]
	shape = bpy.props.EnumProperty(items=items, name="形")
	isObjectMode =  bpy.props.BoolProperty(name="完了後オブジェクトモードに", default=True)
	isHide = bpy.props.BoolProperty(name="完了後アーマチュアを隠す", default=True)
	
	def execute(self, context):
		obj = bpy.context.active_object
		if (obj.type == "ARMATURE"):
			if (obj.mode == "POSE"):
				bpy.ops.object.mode_set(mode="OBJECT")
				for bone in obj.data.bones:
					if(bone.select == True):
						bpy.ops.object.select_all(action="DESELECT")
						
						#context.scene.cursor_location = bone.head_local
						bone.show_wire = True
						
						me = bpy.data.meshes.new(self.name)
						if (self.shape == "1"):
							me.from_pydata([(0,0,0), (0,1,0)], [(0,1)], [])
						elif (self.shape == "2"):
							me.from_pydata([(0,0,0), (0,1,0), (0.1,0.5,0), (0,0.5,0.1), (-0.1,0.5,0), (0,0.5,-0.1)], [(0,1), (0,2), (0,3), (0,4), (0,5), (1,2), (1,3), (1,4), (1,5), (2,3), (3,4), (4,5), (5,2)], [])
						me.update()
						meObj = bpy.data.objects.new(me.name, me)
						meObj.data = me
						context.scene.objects.link(meObj)
						meObj.select = True
						context.scene.objects.active = meObj
						
						meObj.draw_type = "WIRE"
						meObj.show_x_ray = True
						bpy.ops.object.constraint_add(type="COPY_TRANSFORMS")
						meObj.constraints[-1].target = obj
						meObj.constraints[-1].subtarget = bone.name
						bpy.ops.object.visual_transform_apply()
						meObj.constraints.remove(meObj.constraints[-1])
						obj.pose.bones[bone.name].custom_shape = meObj
						len = bone.length
						bpy.ops.transform.resize(value=(len, len, len))
				bpy.ops.object.select_all(action="DESELECT")
				obj.select = True
				context.scene.objects.active = obj
				bpy.ops.object.mode_set(mode="POSE")
				if (self.isObjectMode or self.isHide):
					bpy.ops.object.mode_set(mode="OBJECT")
				if (self.isHide):
					obj.hide = True
			else:
				self.report(type={"ERROR"}, message="ポーズモードで実行してください")
		else:
			self.report(type={"ERROR"}, message="アクティブオブジェクトがアーマチュアではありません")
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(CreateCustomShape.bl_idname, icon="PLUGIN")
