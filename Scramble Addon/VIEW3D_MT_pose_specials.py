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

class CreateWeightCopyMesh(bpy.types.Operator):
	bl_idname = "pose.create_weight_copy_mesh"
	bl_label = "選択ボーンのウェイトコピー用メッシュを作成"
	bl_description = "選択中のボーンのウェイトコピーで使用するメッシュを作成します"
	bl_options = {'REGISTER', 'UNDO'}
	
	name =  bpy.props.StringProperty(name="作成するオブジェクト名", default="ウェイトコピー用オブジェクト")
	items = [
		("TAIL", "末尾", "", 1),
		("HEAD", "根本", "", 2),
		]
	mode = bpy.props.EnumProperty(items=items, name="ウェイトの位置")
	
	def execute(self, context):
		obj = bpy.context.active_object
		if (obj.type == "ARMATURE"):
			if (obj.mode == "POSE"):
				bpy.ops.object.mode_set(mode="OBJECT")
				bones = []
				for bone in obj.data.bones:
					if(bone.select and not bone.hide):
						bones.append(bone)
				me = bpy.data.meshes.new(self.name)
				verts = []
				edges = []
				for bone in bones:
					co = bone.tail_local
					if (self.mode == "HEAD"):
						co = bone.head_local
					verts.append(co)
					i = 0
					for b in bones:
						if (bone.parent):
							if (bone.parent.name == b.name):
								edges.append((len(verts)-1, i))
								break
						i += 1
				me.from_pydata(verts, edges, [])
				me.update()
				meObj = bpy.data.objects.new(self.name, me)
				meObj.data = me
				context.scene.objects.link(meObj)
				bpy.ops.object.select_all(action="DESELECT")
				meObj.select = True
				context.scene.objects.active = meObj
				
				i = 0
				for bone in bones:
					meObj.vertex_groups.new(bone.name)
					meObj.vertex_groups[bone.name].add([i], 1.0, "REPLACE")
					i += 1
				
				bpy.ops.object.mode_set(mode="EDIT")
				bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 0)})
				bpy.ops.object.mode_set(mode="OBJECT")
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
	self.layout.separator()
	self.layout.operator(CreateWeightCopyMesh.bl_idname, icon="PLUGIN")
