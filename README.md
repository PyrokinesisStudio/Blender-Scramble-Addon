# Blender-Scramble-Addon
Blenderのかゆいところに手が届くかもしれない機能が詰まったアドオンです。  
> This add-on is packed with Blender useful features.  
> English-speaking people should be on the English translation.  
![Translation](http://i.imgur.com/U1pO6Jh.jpg)  

## インストール (Installation)
まず画面右の「Download ZIP」でZIPファイルをダウンロードし解凍。  
中の「Scramble Addon」フォルダをBlenderのaddonsフォルダに置いて下さい。  
(Windows7なら： C:\Users\ユーザー名\AppData\Roaming\Blender Foundation\Blender\バージョン\scripts\addons\Scramble Addon)  
日本語・英語を問わず、国際フォントの使用には必ずチェックを。  
Blenderを起動しユーザー設定のアドオンタブで「Scramble」等で検索、アドオンをオンにして「ユーザー設定の保存」クリック。  
左上の「ファイル」メニューに「全体処理」という項目が追加されていればインストール成功です。  
  
> Download the ZIP file first in the "Download ZIP" of right and unzip.  
> Place a "Scramble Addon" folder in the addons folder of Blender.  
> (If Windows7: C:\Users\\(UserName)\AppData\Roaming\Blender Foundation\Blender\\(Version)\scripts\addons\Scramble Addon)  
> Regardless of Japanese or English for the use of the international font by all means a check.  
> Search Start the Blender add-on tab of the user settings in the "Scramble", etc., select the add-on click "save user settings".  
> The installation is successful if it is added to item "whole process" in the "File" menu in the upper-left corner.  

## 使い方 (How to use)
このアドオンは基本的に、既存のメニューに項目が追加されるのでそれをクリックして実行します。  
例えば「ファイル > 全体処理 > オブジェクト > 全ての「すべての辺を表示」をオン」等です。  
追加された項目には必ず![アイコン](http://i.imgur.com/OOVguPd.png)のようなアイコンが表示されています。  
色々なところに項目が追加されているので探してみてください。  
  
> This add-on is basically, and then run it by clicking on it because the items to the existing menu is added.  
> For example, it is the "File> overall process> object> on all of the" Show all sides, "" and the like.  
> The added items are always displayed an icon such as ![アイコン](http://i.imgur.com/OOVguPd.png).  
> Please look because items have been added to the various places.  

## 機能一覧 (List of functions)
* **「プロパティ」エリア > 「ボーン」タブ**
* **―('Properties' area > see bones tab)**
    * **ボーン名をクリップボードにコピー**
    * **―(Copy to Clipboard bone name)**
        * ボーン名をクリップボードにコピーします
        * ―(To Clipboard copies bone name)
    * **ボーン名を左右反転**
    * **―(Flip bone name)**
        * アクティブなボーン名を左右反転します
        * ―(bone name Active Flip)
    * **ボーン名に文字列を追加**
    * **―(Add text to bone name)**
        * アクティブなボーン名に文字列を追加します
        * ―(Adds a string to active bone name)
  
* **「プロパティ」エリア > 「ボーン」タブ > 「インバースキネマティクス (IK)」パネル**
* **―("Properties" areas ""Bourne"tab >"inverse kinematics (IK)"Panel)**
    * **このIK設定をコピー**
    * **―(Copy IK set)**
        * アクティブなボーンのIK設定を、他の選択ボーンにコピーします
        * ―(Copies of other selected bone IK settings Active)
    * **最小/最大角を反転**
    * **―(Flip minimum / maximum angle)**
        * このボーンのIK設定の最小角と最大角を反転させます
        * ―(Reverses minimum and maximum angle of IK setup this bone)
    * **軸設定を他の軸にコピー**
    * **―(Copy to other axes axis settings)**
        * 1つの軸の設定を、他の軸にコピーします
        * ―(Copy other axis on one axis)
  
* **「プロパティ」エリア > 「ボーン」タブ > 「トランスフォーム」パネル**
* **―(Area "Properties" > "Bourne" tab > "transform" Panel)**
    * **ボーンの変形をコピー**
    * **―(Copy bone deformation)**
        * アクティブなボーンの変形情報を、他の選択ボーンにコピーします
        * ―(Copy selected bones of other active bone deformation information)
  
* **「プロパティ」エリア > 「アーマチュアデータ」タブ > 「ボーングループ」パネル**
* **―('Properties' area > armature data tab > bone groups Panel)**
    * **このボーングループのボーンのみ表示**
    * **―(Show only bone bones group)**
        * アクティブなボーングループのみを表示し、その他のボーンを隠します
        * ―(Group active on bones and bones of other hide)
    * **このボーングループのボーンを表示**
    * **―(Bones bones group show)**
        * アクティブなボーングループを表示、もしくは隠します
        * ―(Active bone group show or hide)
  
* **「プロパティ」エリア > 「カーブデータ」タブ > 「ジオメトリ」パネル**
* **―('Properties' area > see these curves"tab >"geometry"Panel)**
    * **テーパー指定コピー**
    * **―(Taper specified copy)**
        * アクティブカーブオブジェクトに指定されているテーパーオブジェクトを、他の選択カーブオブジェクトにコピーします
        * ―(Tapered object that is specified in active curve object copies to other selection curves)
    * **ベベル指定コピー**
    * **―(Bevel given copies)**
        * アクティブカーブオブジェクトに指定されているベベルオブジェクトを、他の選択カーブオブジェクトにコピーします
        * ―(Bevel object that is specified in active curve object copies to other selection curves)
  
* **「プロパティ」エリア > 「モディファイア」タブ**
* **―(Area properties > tab "modifiers")**
    * **全モディファイア適用**
    * **―(All modifiers applied)**
        * 選択オブジェクトの全てのモディファイアを適用します
        * ―(Applies to all modifiers of selected object)
    * **全モディファイア削除**
    * **―(Remove all modifiers)**
        * 選択オブジェクトの全てのモディファイアを削除します
        * ―(Remove all modifiers of selected object)
    * **ビューへのモディファイア適用を切り替え**
    * **―(Modifiers apply to view switching)**
        * 選択オブジェクトの全てのモディファイアのビューへの適用を切り替えます
        * ―(Shows or hides application to view all modifiers of selected object)
    * **モディファイア使用を同期**
    * **―(Synchronized modifier use)**
        * 選択オブジェクトのレンダリング時/ビュー時のモディファイア使用を同期します
        * ―(synchronized modifier used when rendering selection / view)
    * **全モディファイアの展開/閉じるを切り替え**
    * **―(All modifiers expand / collapse toggle)**
        * アクティブオブジェクトの全モディファイアを展開/閉じるを切り替え(トグル)します
        * ―(Expand / collapse all modifiers of active objects to switch (toggle))
    * **モディファイア適用+統合**
    * **―(Modifiers apply + integration)**
        * オブジェクトのモディファイアを全適用してから統合します
        * ―(integration from object's modifiers to apply all)
    * **モディファイア名を自動でリネーム**
    * **―(Modifier name auto-rename.)**
        * 選択オブジェクトのモディファイア名を参照先などの名前にリネームします
        * ―(Rename selected object modifier name refers to, for example,)
    * **ブーリアンを追加**
    * **―(Add a Boolean)**
        * アクティブオブジェクトにその他選択オブジェクトのブーリアンを追加
        * ―(Additional Boolean selected objects to an active object)
    * **ブーリアンを適用**
    * **―(Apply Boolean)**
        * アクティブオブジェクトにその他選択オブジェクトのブーリアンを適用
        * ―(Active objects for other Boolean objects)
    * **レンダリング時の細分化数を設定**
    * **―(Rendering subdivision number)**
        * 選択したオブジェクトのサブサーフモディファイアのレンダリング時の細分化数を設定します
        * ―(Sets number of subdivisions during rendering of selected object subsurfmodifaia)
    * **プレビュー・レンダリングの細分化数を同じに**
    * **―(Equivalent to a subdivision of preview rendering)**
        * 選択したオブジェクトのサブサーフモディファイアのプレビュー時とレンダリング時の細分化数を同じに設定します
        * ―(Set in same subdivision of subsurfmodifaia of selected object when you preview and rendering time)
    * **最適化表示を設定**
    * **―(Set defragmentation display)**
        * 選択したオブジェクトのサブサーフモディファイアの最適化表示を設定します
        * ―(Sets optimization for subsurfmodifaia of selected object)
    * **選択オブジェクトのサブサーフを削除**
    * **―(Delete select Subsurf)**
        * 選択したオブジェクトのサブサーフモディファイアを削除します
        * ―(Removes selected object subsurfmodifaia)
    * **選択オブジェクトにサブサーフを追加**
    * **―(Add a Subsurf on selected objects)**
        * 選択したオブジェクトにサブサーフモディファイアを追加します
        * ―(Add subsurfmodifaia to selected object)
    * **アーマチュアの「体積を維持」をまとめて設定**
    * **―(Set keep up volume armature)**
        * 選択したオブジェクトのアーマチュアモディファイアの「体積を維持」をまとめてオン/オフします
        * ―(Maintain volume in armtuamodifaia of selected objects together off and on the)
    * **クイックカーブ変形**
    * **―(Quick curve deformation)**
        * すばやくカーブモディファイアを適用します
        * ―(Quickly apply curve modifier)
    * **クイック配列複製+カーブ変形**
    * **―(Quick array replication + curve deformation)**
        * すばやく配列複製モディファイアとカーブモディファイアを適用します
        * ―(Quickly apply curve modifier with modifiers array replication)
  
* **「プロパティ」エリア > 「アーマチュアデータ」タブ > 「ポーズライブラリ」パネル**
* **―('Properties' area > armature data tab > pose library panel)**
    * **ポーズライブラリを並び替え**
    * **―(Pose library sort.)**
        * アクティブなポーズライブラリのポーズを並び替えます
        * ―(Sorts by posing for an active pose library)
    * **ポーズライブラリのポーズを最上部/最下部へ**
    * **―(Top / bottom pose pose library)**
        * アクティブなポーズライブラリのポーズを最上部、もしくは最下部へ移動させます
        * ―(Posing in an active pose library moves to top or bottom)
  
* **「プロパティ」エリア > 「オブジェクト」タブ > 「トランスフォーム」パネル**
* **―(Area "Properties" > "object" tab > "transform" Panel)**
    * **シェイプキー名をオブジェクト名に**
    * **―(Shape key name in object name)**
        * シェイプキーの名前をオブジェクト名と同じにします
        * ―(Same as object name name of shape key)
  
* **「プロパティ」エリア > 「アーマチュアデータ」タブ > 「スケルトン」パネル**
* **―('Properties' area > armature data tab > "skeleton" Panel)**
    * **全ボーンレイヤーを表示**
    * **―(View all bone layer)**
        * 全てのボーンレイヤーをオンにして表示します
        * ―(All bone layer and then displays the)
  
* **プロパティ > "メッシュデータ"タブ > "UVマップ"パネル**
* **―(Properties > "data mesh" tab > "UV map" Panel)**
    * **まとめてUVをリネーム**
    * **―(Bulk Rename with UV)**
        * 選択オブジェクト内の指定UVをまとめて改名します
        * ―(Renames selected objects within designated UV together)
    * **まとめて指定名のUVを削除**
    * **―(Bulk delete name UV)**
        * 指定した名前と同じ名のUVを、選択オブジェクトから削除します
        * ―(Removes selected object UV of same name as specified)
    * **UV名を変更**
    * **―(Rename UV)**
        * アクティブなUVの名前を変更します(テクスチャのUV指定もそれに伴って変更します)
        * ―(Renames active UV (UV texture also changes accordingly))
    * **未使用のUVを削除**
    * **―(Remove unused UV)**
        * アクティブなオブジェクトのマテリアルで未使用なUVを全削除します(他の部分に使われているUVは消してしまいます)
        * ―(Active object material (UV is used in other parts disappear) delete unused UV total)
    * **UVを移動**
    * **―(Move to UV)**
        * アクティブなオブジェクトのUVを移動して並び替えます
        * ―(Sorts, by moving active object's UV)
  
* **プロパティ > "メッシュデータ"タブ > "頂点色"パネル**
* **―(Properties > "data mesh" tab > "vertex color Panel)**
    * **頂点色を移動**
    * **―(Move vertex color)**
        * アクティブなオブジェクトの頂点色を移動して並び替えます
        * ―(Move vertex color of active objects, sorts)
    * **頂点色を塗り潰す**
    * **―(Fill vertex color)**
        * アクティブなオブジェクトの頂点色を指定色で塗り潰します
        * ―(Vertex color of active object with specified color fills)
    * **頂点カラーを一括追加**
    * **―(Bulk add vertex color)**
        * 選択中のメッシュオブジェクト全てに色と名前を指定して頂点カラーを追加します
        * ―(Specify color and name all selected mesh object, adds a vertex color)
  
* **ドープシート > 「キー」メニュー**
* **―(Dope sheet "menu"key")**
    * **キーフレームを削除 (確認しない)**
    * **―(Delete keyframes (not verified))**
        * 選択した全てのキーフレームを確認せずに削除します
        * ―(Delete without checking for all selected keyframes)
    * **全キーフレームを大掃除**
    * **―(Cleaning up all keyframes)**
        * 全てのアクションの重複したキーフレームを削除します
        * ―(Remove keyframe duplicates of all actions)
  
* **UV/画像エディター > 「画像」メニュー**
* **―(UV / image editor > image menu)**
    * **画像名を使用するファイル名に**
    * **―(Using name of image file name)**
        * アクティブな画像の名前を、使用している外部画像のファイル名にします
        * ―(External images are using name of active image file name)
    * **全ての画像名を使用するファイル名に**
    * **―(In file name to use for all image names)**
        * 全ての画像の名前を、使用している外部画像のファイル名にします
        * ―(names of all images using external image file name)
    * **全ての画像を再読み込み**
    * **―(Load all images)**
        * 外部ファイルを参照している画像データを全て読み込み直します
        * ―(Reloads all image data referring to external file)
    * **指定色で上書き**
    * **―(Over specified color)**
        * アクティブな画像を指定した色で全て上書きします
        * ―(All over colors you specify active image)
    * **指定色で塗り潰す**
    * **―(Fill with color)**
        * アクティブな画像を指定した色で全て塗り潰します
        * ―(All fill in color you specify active image)
    * **透明部分を塗り潰し**
    * **―(Fill with transparency)**
        * アクティブな画像の透明部分を指定色で塗り潰します
        * ―(transparent parts of image are active in specified color fills)
    * **画像の正規化**
    * **―(Image normalization)**
        * アクティブな画像を正規化します
        * ―(Normalizes active image)
    * **画像ファイル名を変更**
    * **―(Change name of image file)**
        * アクティブな画像のファイル名を変更します
        * ―(Change file name of active image)
    * **画像をぼかす (重いので注意)**
    * **―((Note heavy) blurs an image)**
        * アクティブな画像をぼかします
        * ―(Blurs an image of active)
    * **水平反転**
    * **―(Flip horizontally)**
        * アクティブな画像を水平方向に反転します
        * ―(Active image flips horizontally)
    * **垂直反転**
    * **―(Flip vertically)**
        * アクティブな画像を垂直方向に反転します
        * ―(Active image flips vertical)
    * **90°回転**
    * **―(Rotate 90 degrees)**
        * アクティブな画像を90°回転します
        * ―(Active image rotates 90 °)
    * **180°回転**
    * **―(Rotate 180 degrees)**
        * アクティブな画像を180°回転します
        * ―(Active image rotates 180 °)
    * **270°回転**
    * **―(Rotate 270 degrees)**
        * アクティブな画像を270°回転します
        * ―(Active image rotates 270 degrees)
    * **外部エディターで編集 (拡張)**
    * **―(Editing in an external editor (enhanced))**
        * ユーザー設定のファイルタブで設定した追加の外部エディターで画像を開きます
        * ―(Open image in an external editor of additional files page of custom)
    * **画像の拡大/縮小**
    * **―(Image zoom in / out)**
        * アクティブな画像をリサイズします
        * ―(Active image resizing)
    * **画像の複製**
    * **―(Reproduction of images)**
        * アクティブな画像を複製します
        * ―(Duplicate active picture)
    * **UVグリッドを新規作成**
    * **―(New UV grid)**
        * WEBからUVグリッドをダウンロードし、画像として新規作成します
        * ―(UV grid to download from WEB, and create new images)
    * **画像を並べる**
    * **―(Arrange images)**
        * アクティブな画像を小さくして並べます
        * ―(Arrange active image to reduce)
    * **画像の高速ぼかし**
    * **―(Fast image blurring)**
        * アクティブな画像に高速なぼかし処理を行います
        * ―(active image blur fast do)
    * **ノイズ画像を新規作成**
    * **―(Create a new image noise)**
        * ノイズ画像を新規画像として追加します
        * ―(Add as a new picture noise picture)
    * **画像を脱色**
    * **―(Bleached images)**
        * アクティブな画像をモノクロにします
        * ―(black and white image of active)
    * **画像のサイズ変更**
    * **―(Change size of image)**
        * アクティブな画像のサイズを変更します
        * ―(Change size of active image)
  
* **UV/画像エディター > 「選択」メニュー**
* **―(UV / image editor > select menu)**
    * **分離している頂点を選択**
    * **―(Select vertices are isolated)**
        * シームによって分離している頂点を選択します
        * ―(Select vertex are separated by seams)
  
* **UV/画像エディター > 「UV」メニュー**
* **―(UV / image editor > "UV" menu)**
    * **UVをメッシュに変換**
    * **―(Convert UV to mesh)**
        * アクティブなUVを新規メッシュに変換します
        * ―(Converts new mesh to UV active)
  
* **UV/画像エディター > 「ビュー」メニュー**
* **―(UV / image editor > View menu)**
    * **カーソルの位置をリセット**
    * **―(Reset position of cursor)**
        * 2Dカーソルの位置を左下に移動させます
        * ―(2D cursor moves in lower left)
    * **パネル表示切り替え(モードA)**
    * **―(Toggle Panel (mode A))**
        * プロパティ/ツールシェルフの「両方表示」/「両方非表示」をトグルします
        * ―(properties/tool shelf "both display" / "both hide" toggle)
    * **パネル表示切り替え(モードB)**
    * **―(Toggle Panel (mode B))**
        * 「パネル両方非表示」→「ツールシェルフのみ表示」→「プロパティのみ表示」→「パネル両方表示」のトグル
        * ―("Panel both hide" → show only the tool shelf → show only properties → "Panel both display" for toggle)
    * **パネル表示切り替え(モードC)**
    * **―(Toggle Panel (mode C))**
        * 「パネル両方非表示」→「ツールシェルフのみ表示」→「プロパティのみ表示」... のトグル
        * ―("Panel both hide" → "show only the tool shelf → show only the properties. The toggle)
  
* **「情報」エリア > 「ファイル」メニュー**
* **―(Area information">"file"menu)**
    * **再起動**
    * **―(Restart)**
        * Blenderを再起動します
        * ―(Restart Blender)
    * **最新の自動保存の読み込み**
    * **―(Load last AutoSave)**
        * 復元するために自動的に保存したファイルの最新ファイルを開きます
        * ―(Open file automatically in order to restore most recent file)
    * **確認せずに上書き保存**
    * **―(Save without prompting)**
        * 確認メッセージを表示せずに上書き保存します
        * ―(Save changes without displaying confirmation message)
    * **最後に使ったファイルを開く**
    * **―(Open last used file)**
        * 「最近使ったファイル」の一番上のファイルを開きます
        * ―(Opens file at top of "recent files")
    * **データ名をリネーム**
    * **―(Data name to rename.)**
        * 全てのデータを対象にしたリネームが可能です
        * ―(Rename using all of data is available)
    * **全ての「すべての辺を表示」をオン**
    * **―(All show all sides turn)**
        * 全てのオブジェクトの「すべての辺を表示」表示設定をオンにします(オフも可能)
        * ―(Show all sides of all objects (can be off) turn display settings)
    * **全ての最高描画タイプを一括設定**
    * **―(All best drawing type schemes)**
        * 全てのオブジェクトの「最高描画タイプ」を一括で設定します
        * ―("Best drawing types in object of all sets at once)
    * **全てのデータ名をオブジェクト名と同じにする**
    * **―(All data name to object name and same)**
        * 全てのオブジェクトのデータ(メッシュデータなど)の名前を、リンクしているオブジェクト名に置換します
        * ―(Replaces object name linked to name all object data (mesh data etc))
    * **全てのマテリアルの「半透明影の受信」をオン**
    * **―(On receiving Semitransparent Shadow material of all)**
        * 全てのマテリアルの「半透明影を受信するかどうか」についての設定をオン(オフ)にします
        * ―(You to receive a semi-transparent shadow?"of all material (off) on the)
    * **マテリアルのカラーランプ設定を他にコピー**
    * **―(Copy material color ramp settings)**
        * アクティブなマテリアルのカラーランプ設定を他の全マテリアル(選択オブジェクトのみも可)にコピーします
        * ―(Color ramp settings of active material is all material other (only selected objects are allowed) to copy)
    * **アクティブマテリアルのFreeStyle色を他にコピー**
    * **―(FreeStyle color of an active copy to other)**
        * アクティブなマテリアルのFreeStyleの色設定を他の全マテリアル(選択オブジェクトのみも可)にコピーします
        * ―(FreeStyle material active color for all materials other (only selected objects are allowed) to copy)
    * **全マテリアルのFreeStyle色をディフューズ色に**
    * **―(FreeStyle color of all material diffuse color)**
        * 全マテリアル(選択オブジェクトのみも可)のFreeStyleライン色をそのマテリアルのディフューズ色+ブレンドした色に置換します
        * ―(All material (only selected objects are allowed) for FreeStyle line color of material diffuse color + a blend to replace the)
    * **全マテリアルのオブジェクトカラーを有効に**
    * **―(To enable object color for all materials)**
        * 全マテリアルのオブジェクトカラーの設定をオンもしくはオフにします
        * ―(select or clear all object color settings)
    * **全てのバンプマップの品質を設定**
    * **―(Set bump of all quality)**
        * 全てのテクスチャのバンプマップの品質を一括で設定します
        * ―(Bump-map texture of all quality sets in bulk)
    * **全テクスチャ名を使用する画像ファイル名に**
    * **―(All image file names using texture name)**
        * 全てのテクスチャの名前を、使用している外部画像のファイル名にします
        * ―(names of all textures use external image file name)
    * **UV指定が空欄な場合アクティブUVで埋める**
    * **―(UV is a blank if you fill active UV)**
        * テクスチャのUV指定欄が空欄の場合、リンクしているメッシュオブジェクトのアクティブなUV名で埋めます
        * ―(Under active UV texture UV specified fields linked to an empty mesh object fills)
    * **物理演算の開始/終了フレームを一括設定**
    * **―(Set physical operation start / end frames at once)**
        * 物理演算などの開始/終了フレームを設定する部分にレンダリング開始/終了フレーム数を割り当てます
        * ―(Assign render start / end frames portions to set start / end frames, such as physics)
  
* **情報 > 「ファイル」メニュー > 「外部データ」メニュー**
* **―(Information > "file" menu > "external data" menu)**
    * **全ての画像をtexturesフォルダに保存し直す**
    * **―(Resave textures folder, all images)**
        * 外部ファイルを参照している画像データを全てtexturesフォルダに保存し直します
        * ―(All external files referenced by image data to resave textures folder)
    * **texturesフォルダ内の未使用ファイルを隔離**
    * **―(isolate unused files in textures folder)**
        * このBlendファイルのあるフォルダのtextures内で、使用していないファイルをbackupフォルダに隔離します
        * ―(Files in a textures folder with Blend files, do not use isolates them in a backup folder)
    * **「最近使ったファイル」をテキストで開く**
    * **―(Open text in "recent files")**
        * 「最近使ったファイル」をBlenderのテキストエディタで開きます
        * ―(Open "recent files" in Blender text editor)
    * **「ブックマーク」をテキストで開く**
    * **―(Open text in "bookmarks")**
        * ファイルブラウザのブックマークをBlenderのテキストエディタで開きます
        * ―(Blender text editor open file browser bookmarks)
  
* **3Dビュー > オブジェクト/メッシュ編集モード > 「追加」メニュー > 「メッシュ」メニュー**
* **―(3D view > object / mesh edit mode > "add" menu > "mesh" menu)**
    * **四角ポリゴン球**
    * **―(Rectangle polygon sphere)**
        * 四角ポリゴンのみで構成された球体メッシュを追加します
        * ―(Adds a spherical mesh is composed only of quadrilateral polygon)
    * **頂点のみ**
    * **―(Only vertices)**
        * 1頂点のみのメッシュオブジェクトを3Dカーソルの位置に追加します
        * ―(Only 1 vertex meshes 3D adds to position of cursor)
    * **頂点グループごとに分離**
    * **―(Isolated vertex groups)**
        * 頂点グループの適用されている部分ごとに分離したメッシュ群を作成します
        * ―(Create a separate each part of vertex groups applied mesh group)
  
* **情報 > 「レンダー」メニュー**
* **―(Information > "render" menu)**
    * **解像度の倍率を設定**
    * **―(Set magnification of resolution)**
        * 設定解像度の何パーセントの大きさでレンダリングするか設定します
        * ―(Set to be rendered settings resolution percentage?)
    * **レンダースロットを設定**
    * **―(Set render slots)**
        * レンダリング結果を保存するスロットを設定します
        * ―(Sets a slot to save rendering result)
    * **スレッド数を切り替え**
    * **―(Switching threads)**
        * レンダリングに使用するCPUのスレッド数を切り替えます
        * ―(Switch thread number of CPUS used to render)
    * **レンダリング時のサブサーフレベルをまとめて設定**
    * **―(Set Subsurf levels during rendering)**
        * レンダリング時に適用するサブサーフの細分化レベルをまとめて設定します
        * ―(Together sets granularity of Subsurf applied during rendering)
    * **レンダリング時のサブサーフレベルをプレビュー値と同期**
    * **―(Sync preview value when rendering Subsurf levels)**
        * 全オブジェクトのレンダリング時に適用するサブサーフの細分化レベルを、プレビューでのレベルへと設定します
        * ―(Granularity of Subsurf applied during rendering of all objects set to level in preview)
  
* **情報 > 「ウィンドウ」メニュー**
* **―(Information > window menu)**
    * **エディタータイプ**
    * **―(Editor type)**
        * エディタータイプ変更のパイメニューです
        * ―(Change editor type pie menu is)
    * **UIの英語・日本語 切り替え**
    * **―(English UI, Japanese switch)**
        * インターフェイスの英語と日本語を切り替えます
        * ―(Japan language with English interface switch)
  
* **プロパティ > 「マテリアル」タブ > リスト右の▼**
* **―(Properties > materials"tab > list right down:)**
    * **割り当てのないマテリアルを削除**
    * **―(Delete non-assignment material)**
        * 面に一つも割り当てられてないマテリアルを全て削除します
        * ―(Delete all one assigned to a surface material)
    * **マテリアルスロット全削除**
    * **―(Remove all material slots)**
        * このオブジェクトのマテリアルスロットを全て削除します
        * ―(Delete all material slots for this object)
    * **空のマテリアルスロット削除**
    * **―(Delete empty material slots)**
        * このオブジェクトのマテリアルが割り当てられていないマテリアルスロットを全て削除します
        * ―(Delete all material of this object has not been assigned material slots)
    * **裏側を透明にする**
    * **―(Transparent back.)**
        * メッシュの裏側が透明になるようにシェーダーノードを設定します
        * ―(Sets shader nodes transparently mesh back)
    * **スロットを一番上へ**
    * **―(Slot to top)**
        * アクティブなマテリアルスロットを一番上に移動させます
        * ―(Move active material slots on top)
    * **スロットを一番下へ**
    * **―(Slots to bottom)**
        * アクティブなマテリアルスロットを一番下に移動させます
        * ―(Move active material slot at bottom)
  
* **プロパティ > 「オブジェクトデータ」タブ > シェイプキー一覧右の▼**
* **―(Properties > object data tab > the right shape key list ▼)**
    * **シェイプキーを複製**
    * **―(Duplicate a shape key)**
        * アクティブなシェイプキーを複製します
        * ―(Duplicate active shape key)
    * **全てのシェイプにキーフレームを打つ**
    * **―(Hit keyframes of all shapes)**
        * 現在のフレームに、全てのシェイプのキーフレームを挿入します
        * ―(Inserts a keyframe for all shapes on current frame)
    * **最上段を選択**
    * **―(Select top)**
        * 一番上のシェイプキーを選択します
        * ―(Select top shape key)
    * **最下段を選択**
    * **―(Select bottom row)**
        * 一番下のシェイプキーを選択します
        * ―(Select bottom shape key)
    * **現在の形状を保持して全シェイプ削除**
    * **―(Remove all shape and holds shape of current)**
        * 現在のメッシュの形状を保持しながら全シェイプキーを削除します
        * ―(Remove all shape key while maintaining shape of mesh current)
  
* **プロパティ > 「オブジェクトデータ」タブ > 頂点グループ一覧右の▼**
* **―(Properties > object data tab > vertex group list right down:)**
    * **空の頂点グループを削除**
    * **―(Delete empty vertex groups)**
        * メッシュにウェイトが割り当てられていない頂点グループを削除します
        * ―(Remove weights assigned to mesh vertex groups)
    * **ミラーの対になる空頂点グループを追加**
    * **―(Add empty vertex group versus mirror)**
        * .L .R などミラーの命令規則に従って付けられたボーンの対になる空の新規ボーンを追加します
        * ―(. L... R, add new bone bones according to mandate rule in Miller vs. empty)
    * **一番上を選択**
    * **―(Select top)**
        * 頂点グループの一番上の項目を選択します
        * ―(Select item at top of vertex groups)
    * **一番下を選択**
    * **―(At bottom, select)**
        * 頂点グループの一番下の項目を選択します
        * ―(Select item at bottom of vertex groups)
    * **最上段へ**
    * **―(To top)**
        * アクティブな頂点グループを一番上へ移動させます
        * ―(Move to top active vertex groups)
    * **最下段へ**
    * **―(To bottom)**
        * アクティブな頂点グループを一番下へ移動させます
        * ―(Move to bottom vertex group active)
    * **特定文字列が含まれる頂点グループ削除**
    * **―(Delete a vertex group that contains a specific string)**
        * 指定した文字列が名前に含まれている頂点グループを全て削除します
        * ―(Removes all vertex group names contains specified string)
  
* **ノードエディター > 「ノード」メニュー**
* **―(Nordeditor > 'nodes' menu)**
    * **このシェーダーノードを他マテリアルにコピー**
    * **―(Copy to other material shader node)**
        * 表示しているシェーダーノードを他のマテリアルにコピーします
        * ―(Copies of other material shader nodes are displayed)
  
* **「ノードエディター」エリア > 「ビュー」メニュー**
* **―(Area "nordeditor" > "view" menu)**
    * **パネル表示切り替え(モードA)**
    * **―(Toggle Panel (mode A))**
        * プロパティ/ツールシェルフの「両方表示」/「両方非表示」をトグルします
        * ―(properties/tool shelf "both display" / "both hide" toggle)
    * **パネル表示切り替え(モードB)**
    * **―(Toggle Panel (mode B))**
        * 「パネル両方非表示」→「ツールシェルフのみ表示」→「プロパティのみ表示」→「パネル両方表示」のトグル
        * ―("Panel both hide" → show only the tool shelf → show only properties → "Panel both display" for toggle)
    * **パネル表示切り替え(モードC)**
    * **―(Toggle Panel (mode C))**
        * 「パネル両方非表示」→「ツールシェルフのみ表示」→「プロパティのみ表示」... のトグル
        * ―("Panel both hide" → "show only the tool shelf → show only the properties. The toggle)
  
* **「プロパティ」エリア > 「オブジェクト」タブ**
* **―(Area 'properties' > 'objects' tab)**
    * **オブジェクト名をデータ名に**
    * **―(Object names in data name)**
        * オブジェクト名をリンクしているデータ名に設定します
        * ―(Set data name linked to object name)
    * **データ名をオブジェクト名に**
    * **―(Data name in object name)**
        * データ名をリンクしているオブジェクト名に設定します
        * ―(Sets data linked to object name)
    * **オブジェクト名をコピー**
    * **―(Copy object name)**
        * オブジェクト名をクリップボードにコピーします
        * ―(Copy to Clipboard object name)
    * **データ名をコピー**
    * **―(Copy data name)**
        * データ名をクリップボードにコピーします
        * ―(Copies data to Clipboard)
  
* **「プロパティ」エリア > 「オブジェクト」タブ > 「表示」パネル**
* **―(Area "Properties" > "object" tab > "Panel")**
    * **表示設定をコピー**
    * **―(Copy display settings)**
        * この表示設定を他の選択オブジェクトにコピーします
        * ―(Copy selected objects of other display settings)
  
* **「プロパティ」エリア > 「物理演算」タブ > 「剛体」パネル**
* **―("Properties" area: "Physics" tab > "rigid" Panel)**
    * **剛体設定をコピー**
    * **―(Copy rigid set)**
        * アクティブなオブジェクトの剛体設定を、他の選択オブジェクトにコピーします
        * ―(Copy selected objects of other rigid set of active objects)
  
* **「プロパティ」エリア > 「物理演算」タブ > 「剛体コンストレイント」パネル**
* **―("Properties" area: "Physics" tab > rigid constraints Panel)**
    * **剛体コンストレイント設定をコピー**
    * **―(Copy sets rigid constraints)**
        * アクティブなオブジェクトの剛体コンストレイント設定を、他の選択オブジェクトにコピーします
        * ―(Copies selected objects for other rigid constraints on active object)
    * **剛体コンストレイントの制限を初期化**
    * **―(Initializes a rigid constraint limits)**
        * アクティブなオブジェクトの剛体コンストレイントの制限設定群を初期化します
        * ―(Initializes rigid constraints of active object limit settings group)
    * **剛体コンストレイントの制限を反転**
    * **―(Flip rigid constraints limited)**
        * アクティブなオブジェクトの剛体コンストレイントの制限設定の最小と最大を反転させます
        * ―(Minimum limit settings of rigid constraints of active object and reverses maximum)
  
* **プロパティ > ヘッダー**
* **―(Properties > header)**
    * **プロパティタブを切り替え**
    * **―(Switch to properties tab)**
        * プロパティのタブを順番に切り替えます
        * ―(Turn switch Properties tab)
  
* **「プロパティ」エリア > 「レンダー」タブ > 「ベイク」パネル**
* **―("Properties" area: "render" tab > "bake" Panel)**
    * **ベイク用の画像を作成**
    * **―(Create images for bake)**
        * ベイクに使う新規画像を素早く用意可能です
        * ―(New images used to bake quickly, is available)
  
* **「プロパティ」エリア > 「レンダー」タブ > 「レンダー」パネル**
* **―("Properties" area: "render" tab > "render" Panel)**
    * **バックグラウンドでレンダリング**
    * **―(Background rendering.)**
        * コマンドラインから現在のblendファイルをレンダリングします
        * ―(Renders current blend file from command line)
  
* **「プロパティ」エリア > 「シーン」タブ > 「剛体ワールド」パネル**
* **―(Area "Properties" > "scenes" tab > rigid World Panel)**
    * **剛体ワールドを作り直す**
    * **―(Recreate rigid world)**
        * 設定は維持して剛体ワールドを作り直します
        * ―(Keep setting, recreate rigid world)
    * **剛体ワールドの開始/終了フレームをセット**
    * **―(Set start / end frames rigid world)**
        * 剛体ワールドの開始/終了フレームをレンダリングの開始/終了フレームへと設定します
        * ―(Start / end frame rigid world of sets to start / end frame rendering)
  
* **プロパティ > 「テクスチャ」タブ > リスト右の▼**
* **―(Properties > "texture" tab > the list right down:)**
    * **テクスチャ名を使用する画像ファイル名に**
    * **―(Image file name to use texture name)**
        * アクティブなテクスチャの名前を使用している外部画像のファイル名にします
        * ―(file name of external images using name of active texture)
    * **テクスチャスロットを全て空に**
    * **―(Texture slot, all in sky)**
        * アクティブなマテリアルの全てのテクスチャスロットを空にします
        * ―(Empties all active material texture slots)
    * **最上段へ**
    * **―(To top)**
        * アクティブなテクスチャスロットを一番上に移動させます
        * ―(Move active texture slot at top)
    * **最下段へ**
    * **―(To bottom)**
        * アクティブなテクスチャスロットを一番下に移動させます
        * ―(Move active texture slot at bottom)
    * **無効なテクスチャを削除**
    * **―(Remove invalid texture)**
        * 無効にしているテクスチャを全て削除します
        * ―(Removes all textures have turned off)
    * **空のテクスチャスロットを切り詰める**
    * **―(Cut texture slot empty)**
        * テクスチャが割り当てられていない空のテクスチャスロットを埋め、切り詰めます
        * ―(No texture is assigned an empty texture slots will be filled, truncated)
    * **ここより下を削除**
    * **―(Delete below here)**
        * アクティブなテクスチャスロットより下を、全て削除します
        * ―(Remove all active texture slot below)
  
* **「プロパティ」エリア > 「テクスチャ」タブ > 「画像」パネル**
* **―(Area "Properties" > "texture" tab > "images" Panel)**
    * **テクスチャ画像をUV/画像エディターに表示**
    * **―(Texture images show in UV / image editor)**
        * アクティブなテクスチャに使われている画像を「UV/画像エディター」に表示します
        * ―(Image is used in active texture shows UV / image editor)
    * **このテクスチャでテクスチャペイント**
    * **―(This texture is a texture paint)**
        * アクティブなテクスチャでテクスチャペイントを行います
        * ―(Active texture provides a texture paint)
  
* **「プロパティ」エリア > 「テクスチャ」タブ > 「マッピング」パネル**
* **―(Area "Properties" > "texture" tab > "mapping Panel)**
    * **アクティブなUVを使う**
    * **―(Using Active UV)**
        * メッシュのアクティブなUVを、このスロットで使います
        * ―(Active UV mesh used in this slot)
  
* **テキストエディター > 「テキスト」メニュー**
* **―(Text editor > text menu)**
    * **外部エディターで編集**
    * **―(Edit with external editor)**
        * ユーザー設定のファイルタブで設定した外部エディターでテキストを開きます
        * ―(Open text in an external editor you set on files page of custom)
  
* **メニューに表示されないコマンド**
* **―(Missing menu commands)**
    * **最後までスクロール**
    * **―(Scroll to end)**
        * 画面の一番下までスクロールします
        * ―(Scroll to bottom of screen)
  
* **ユーザー設定 > ヘッダー**
* **―(User settings > header)**
    * **ユーザー設定タブを切り替え**
    * **―(Switch to custom tab)**
        * ユーザー設定のタブを順番に切り替えます
        * ―(Cycles user settings tab)
    * **キーバインド検索**
    * **―(Search key bindings)**
        * 設定したキーバインドに一致する割り当てを検索します
        * ―(Find matching key bindings you set assignment)
    * **ショートカット検索をクリア**
    * **―(Clear Search shortcuts)**
        * ショートカット検索に使用した文字列を削除します
        * ―(Remove string used to search for shortcuts)
    * **キーコンフィグを全て閉じる**
    * **―(Close all game)**
        * キーコンフィグのメニューを全て折りたたみます
        * ―(Collapses all game menu)
    * **ショートカット一覧をブラウザで閲覧**
    * **―(View in browser shortcut list)**
        * Blenderの全てのショートカットをブラウザで確認出来ます
        * ―(Please see browser all shortcuts in Blender)
    * **最後のコマンドをショートカットに登録**
    * **―(Last command create shortcut)**
        * 最後に実行したコマンドをショートカットに登録します
        * ―(Last command create shortcut)
    * **割り当ての無いショートカット一覧**
    * **―(Without assigning shortcut list)**
        * 現在の編集モードでの割り当ての無いキーを「情報」エリアに表示します
        * ―(Displays key assignments in current editing mode without information area)
    * **キーコンフィグをXMLでインポート**
    * **―(Import XML in game)**
        * キーコンフィグをXML形式で読み込みます
        * ―(game reads in XML format)
    * **キーコンフィグをXMLでエクスポート**
    * **―(Export XML in a game)**
        * キーコンフィグをXML形式で保存します
        * ―(Game save in XML format)
    * **展開しているキー割り当てのカテゴリを移動**
    * **―(Move key assignments that expand categories)**
        * 展開しているキー割り当てを、他のカテゴリに移動します
        * ―(Move key assignments that expand into other categories)
    * **Blender-Scramble-Addonを更新**
    * **―(Update Blender-Scramble-Addon)**
        * Blender-Scramble-Addonをダウンロード・更新を済ませます
        * ―(Downloads, updates and check out Blender-Scramble-Addon)
    * **「追加項目のオン/オフ」の表示切り替え**
    * **―(Toggle on/off additional items)**
        * ScrambleAddonによるメニューの末尾の「追加項目のオン/オフ」ボタンの表示/非表示を切り替えます
        * ―(Turns on/off additional items button at end of menu by ScrambleAddon)
  
* **「ユーザー設定」エリア > 「ファイル」タブ**
* **―("User settings" > "files" tab)**
    * **.blendファイルをこのバージョンに関連付け**
    * **―(the.blend file associated with this version)**
        * .blendファイルをこのBlender実行ファイルに関連付けます (WindowsOSのみ)
        * ―((WindowsOS only).blend file associates a Blender run file)
    * **バックアップをこのバージョンに関連付け**
    * **―(Backup with this version)**
        * .blend1 .blend2 などのバックアップファイルをこのBlender実行ファイルに関連付けます (WindowsOSのみ)
        * ―(associates with Blender running file backup file, such as.blend1.blend2 (WindowsOS only))
  
* **3Dビュー > アーマチュア編集モード > 「W」キー**
* **―(3D view > armature edit mode > 'W' key)**
    * **選択ボーンをミラーリング**
    * **―(Select bones mirroring.)**
        * 選択中のボーンを任意の軸でミラーリングします
        * ―(Mirrored at any axes selected bone.)
    * **ボーン名をクリップボードにコピー**
    * **―(Copy to Clipboard bone name)**
        * アクティブボーンの名前をクリップボードにコピーします
        * ―(Copies Clipboard name of active bone)
    * **ボーン名を正規表現で置換**
    * **―(Replace bone names in regular expressions)**
        * (選択中の)ボーン名を正規表現に一致する部分で置換します
        * ―(In bone name (of choice) to match regular expression replace)
    * **反対位置にあるボーンをリネーム**
    * **―(Bones in opposite position, rename.)**
        * 選択中ボーンのX軸反対側の位置にあるボーンを「○.R ○.L」のように対にします
        * ―(Bone is located opposite X axis selection in bone "1.R 1 longs.L ' of so versus the)
  
* **3Dビュー > アーマチュア編集モード > 「Shift+W」キー**
* **―(3D view > armature edit mode > Shift + W key)**
    * **ボーン名をまとめて設定**
    * **―(Set bone name)**
        * 選択中のボーンの名前をまとめて設定します
        * ―(name of selected bone sets together)
    * **カーブボーンをまとめて設定**
    * **―(Set curve ban)**
        * 選択中のボーンのカーブボーン設定をします
        * ―(selected bone curve born setting)
    * **ロールをまとめて設定**
    * **―(Set roll)**
        * 選択中のボーンのロールを設定します
        * ―(Sets selected bone roll)
    * **アクティブのIK設定(回転制限等)をコピー**
    * **―(Copy of active IK settings (rotation limits, etc.))**
        * アクティブなボーンのIK設定(回転制限など)を他の選択ボーンにコピーします
        * ―(Copy selected bone of other active bone IK settings (speed limitations))
    * **IKのポールターゲットを設定**
    * **―(Paul targeting IK)**
        * アクティブなボーンのIKのポールターゲットを第二選択ボーンに設定します
        * ―(Chose second Paul target of active bone IK bones sets)
    * **IKのチェーンの長さを設定**
    * **―(Set length of IK chain)**
        * アクティブなボーンのIKのチェーンの長さを第二選択ボーンへの長さへと設定します
        * ―(Second choice of active bone IK chain length to length to bones and set the)
  
* **3Dビュー > アーマチュア編集モード > 「アーマチュア」メニュー**
* **―(3D view > armature edit mode > "armature" menu)**
    * **確認無しでボーンを削除**
    * **―(Remove bones with no confirmation)**
        * ボーンを確認無しで削除します
        * ―(Remove bones with no verification)
    * **ボーンをそのまま3Dカーソルの位置へ**
    * **―(Bones intact to position 3D cursor)**
        * 相対的なボーンの尾(根本でも可)の位置をそのままに、ボーンを3Dカーソルの位置へ移動させます
        * ―(Position of relative born tail (even root), bone, 3 D move cursor position)
  
* **3Dビュー > メッシュ編集モード > 「メッシュ」メニュー**
* **―(3D view > mesh edit mode > mesh menu)**
    * **メッシュ選択モードの切り替え**
    * **―(Mesh selection mode)**
        * メッシュ選択モードを頂点→辺→面…と切り替えます
        * ―(Mesh selection mode → top → side surface. Switch and)
    * **メッシュ選択モード**
    * **―(Mesh selection mode)**
        * メッシュの選択のパイメニューです
        * ―(Is a pie menu selection of mesh)
    * **プロポーショナル編集**
    * **―(Proportional edit)**
        * プロポーショナル編集のパイメニューです
        * ―(Is a pie menu proportional edit)
  
* **3Dビュー > メッシュ編集モード > 「X」キー**
* **―(3D view > mesh edit mode > 'X' key)**
    * **選択モードと同じ要素を削除**
    * **―(Delete selection mode and same element)**
        * 現在のメッシュ選択モードと同じ要素(頂点・辺・面)を削除します
        * ―(Same mesh selection mode of current element (vertices, sides and faces) remove)
    * **隠している部分を削除**
    * **―(Remove covering)**
        * 隠している状態のメッシュを全て削除します
        * ―(Delete all are mesh)
  
* **3Dビュー > メッシュ編集モード > 「メッシュ」メニュー > 「表示/隠す」メニュー**
* **―(3D view > mesh edit mode > mesh menu > show / hide menu)**
    * **表示/隠すを反転**
    * **―(Show / hide flip)**
        * 表示状態と非表示状態を反転させます
        * ―(Flip display and non-display state)
    * **頂点のみを隠す**
    * **―(Hide only top)**
        * 選択状態の頂点のみを隠して固定します
        * ―(To hide selected vertices, fixed)
    * **選択しているパーツを隠す**
    * **―(Hide selected parts)**
        * 1頂点以上を選択しているメッシュパーツを隠します
        * ―(Hides mesh part more than 1 vertex is selected)
  
* **3Dビュー > メッシュ編集モード > 「W」キー**
* **―(3D view > mesh edit mode > 'W' key)**
    * **選択頂点の頂点カラーを塗り潰す**
    * **―(Fill selected vertex vertex color)**
        * 選択中の頂点のアクティブ頂点カラーを指定色で塗り潰します
        * ―(Active vertex colors for selected vertices with specified color fills)
    * **一番上のシェイプを選択**
    * **―(Select shape on top of)**
        * リストの一番上にあるシェイプキーを選択します
        * ―(Schipke is at top of list, select)
    * **編集ケージへのモディファイア適用を切り替え**
    * **―(Transition modifiers apply to editing cage)**
        * 編集中のメッシュケージにモディファイアを適用するかを切り替えます
        * ―(Toggles whether to apply modifiers to total en bloc spondylectomy in editing)
    * **ミラーモディファイアを切り替え**
    * **―(Toggle Miller modifier)**
        * ミラーモディファイアが無ければ追加、有れば削除します
        * ―(Delete if not Miller modifier added, Yes)
    * **選択頂点を平均ウェイトで塗り潰す**
    * **―(Fill selected vertex in average weighted)**
        * 選択頂点のウェイトの平均で、選択頂点を塗り潰します
        * ―(Fills selected vertex, vertices weighted average)
  
* **3Dビュー > メッシュ編集モード > 「Ctrl+V」キー**
* **―(3D view > mesh edit mode > Ctrl + V keys)**
    * **別オブジェクトに分離 (拡張)**
    * **―(Separation of different objects (extended))**
        * 「別オブジェクトに分離」の拡張メニューを呼び出します
        * ―(Isolate to another object of call extended menu)
    * **選択物 (分離側をアクティブ)**
    * **―(Choice of (active isolated-side))**
        * 「選択物で分離」した後に分離した側のエディトモードに入ります
        * ―(After "in choice of separation" enters edit mode for separation side)
    * **選択部を複製/新オブジェクトに**
    * **―(A selection of reproduction and new objects)**
        * 選択部分を複製・分離し新オブジェクトにしてからエディトモードに入ります
        * ―(Enters edit mode, replication and selection to new object from)
    * **クイック・シュリンクラップ**
    * **―(Quick shrink wrap)**
        * もう1つの選択メッシュに、選択頂点をぺったりとくっつけます
        * ―(Another one you mesh selected vertices pettanko was bonds, who)
  
* **3Dビュー > オブジェクトモード > 「Ctrl+L」キー**
* **―(3D view > mode > Ctrl + L key)**
    * **オブジェクト名を同じに**
    * **―(To same object name)**
        * 他の選択オブジェクトにアクティブオブジェクトの名前をリンクします
        * ―(Name of active object links to other selected objects)
    * **レイヤーを同じに**
    * **―(In same layer)**
        * 他の選択オブジェクトにアクティブオブジェクトのレイヤーをリンクします
        * ―(link active object layers to other selected objects)
    * **オブジェクトの表示設定を同じに**
    * **―(Visibility of objects to same)**
        * 他の選択オブジェクトにアクティブオブジェクトの表示パネルの設定をコピーします
        * ―(Copy settings of display panel of active object to other selected objects)
    * **空のUVマップをリンク**
    * **―(Link to UV map of sky)**
        * 他の選択オブジェクトにアクティブオブジェクトのUVを空にして追加します
        * ―(Empties Add UV active objects to other objects)
    * **アーマチュアの動きをリンク**
    * **―(Link motion of armature)**
        * コンストレイントによって、他の選択アーマチュアにアクティブアーマチュアの動きを真似させます
        * ―(By constraints on other selected armature mimic active armature movement)
    * **ソフトボディの設定をリンク**
    * **―(Links for soft body)**
        * アクティブオブジェクトのソフトボディの設定を、他の選択オブジェクトにコピーします
        * ―(Sets active object soft copies to other selected objects)
    * **クロスの設定をリンク**
    * **―(Links for cross-)**
        * アクティブオブジェクトのクロスシミュレーション設定を、他の選択オブジェクトにコピーします
        * ―(Cloth simulation for active object copies to other selected objects)
    * **変形をリンク**
    * **―(Link to deformation)**
        * アクティブオブジェクトの変形情報を、他の選択オブジェクトにコピーします
        * ―(Information of active object copies to other selected objects)
  
* **3Dビュー > オブジェクトモード > 「オブジェクト」メニュー**
* **―(3D view > mode > object menu)**
    * **コピー**
    * **―(Copy)**
        * オブジェクトに関するコピーのパイメニューです
        * ―(Pie of copy of object is)
    * **オブジェクト対話モード**
    * **―(Interactive objects)**
        * オブジェクト対話モードのパイメニューです
        * ―(Is a pie menu objects in interactive mode)
    * **サブサーフ設定**
    * **―(Save surf set)**
        * サブサーフのレベルを設定するパイメニューです
        * ―(Is a pie menu to set Subsurf levels)
    * **最高描画タイプ**
    * **―(Best drawing type)**
        * 最高描画タイプを設定するパイメニューです
        * ―(Is a pie menu to set up drawing type)
    * **確認せずに削除**
    * **―(Delete without confirmation)**
        * 削除する時の確認メッセージを表示せずにオブジェクトを削除します
        * ―(delete objects without displaying a confirmation message when you delete)
  
* **3Dビュー > オブジェクトモード > Ctrl+Aキー**
* **―(3D view > mode > CTRL + A)**
    * **位置/回転/拡縮を適用**
    * **―(Apply position / rotation / Pan)**
        * オブジェクトの位置/回転/拡縮を適用します
        * ―(Applies to object position / rotation / Pan)
  
* **3Dビュー > オブジェクトモード > 「オブジェクト」メニュー > 「表示/隠す」メニュー**
* **―(3D view > mode > object menu > show / hide menu)**
    * **表示/隠すを反転**
    * **―(Show / hide flip)**
        * オブジェクトの表示状態と非表示状態を反転させます
        * ―(Flips object's view state and non-State)
    * **特定の種類のオブジェクトのみを隠す**
    * **―(Hide only specific types of objects)**
        * 表示されている特定タイプのオブジェクトを隠します
        * ―(Hides object of a specific type are displayed)
    * **特定の種類のオブジェクト以外を隠す**
    * **―(Non-specific types of objects to hide)**
        * 表示されている特定タイプのオブジェクト以外を隠します
        * ―(Hides object non-specific type that is displayed)
  
* **3Dビュー > オブジェクトモード > 「W」キー**
* **―(3D view > mode > 'W' key)**
    * **ウェイト転送**
    * **―(Weight transfer)**
        * 他の選択中のメッシュからアクティブにウェイトペイントを転送します
        * ―(From mesh of selection in other active forwarding weight paint)
    * **スムーズ/フラットを切り替え**
    * **―(Toggle smooth/flat)**
        * 選択中のメッシュオブジェクトのスムーズ/フラット状態を切り替えます
        * ―(Toggles selected mesh object smooth / flat state)
    * **頂点グループの転送**
    * **―(Transport for vertex group)**
        * アクティブなメッシュに他の選択メッシュの頂点グループを転送します
        * ―(Transfers to other selected mesh vertex group active mesh)
    * **全頂点の平均ウェイトで塗り潰す**
    * **―(Fill in average weight of all vertices)**
        * 全てのウェイトの平均で、全ての頂点を塗り潰します
        * ―(average weight of all, fills all vertices)
    * **頂点にメタボールをフック**
    * **―(Top hook metaballs)**
        * 選択中のメッシュオブジェクトの頂点部分に新規メタボールを張り付かせます
        * ―(Have made new metaballs to vertices of selected mesh object)
    * **グリースペンシルにメタボール配置**
    * **―(Grease pencil to metaballs)**
        * アクティブなグリースペンシルに沿ってメタボールを配置します
        * ―(blobby align with active grease pencil)
    * **メッシュの変形を真似するアーマチュアを作成**
    * **―(Creating an armature to mimic a mesh deformation)**
        * アクティブメッシュオブジェクトの変形に追従するアーマチュアを新規作成します
        * ―(Create a new armature to follow active mesh objects)
    * **頂点グループがある頂点位置にボーン作成**
    * **―(Bones create vertices where vertex groups)**
        * 選択オブジェクトの頂点グループが割り当てられている頂点位置に、その頂点グループ名のボーンを作成します
        * ―(Create a vertex group names of bones in vertex position is choice object vertex groups assigned)
    * **厚み付けモディファイアで輪郭線生成**
    * **―(Contour line generation in thickness with modifiers)**
        * 選択オブジェクトに「厚み付けモディファイア」による輪郭描画を追加します
        * ―(Add to thicken modiﬁ contour drawing selection)
    * **選択物のレンダリングを制限**
    * **―(Limit choice of rendering)**
        * 選択中のオブジェクトをレンダリングしない設定にします
        * ―(setting does not render selected object)
    * **レンダリングするかを「表示/非表示」に同期**
    * **―(Or to render "show / hide" to sync)**
        * 現在のレイヤー内のオブジェクトをレンダリングするかどうかを表示/非表示の状態と同期します
        * ―(Synchronize display / hide status and whether or not to render objects in current layer)
    * **すべての選択制限をクリア**
    * **―(Clears all selected limits)**
        * 全てのオブジェクトの選択不可設定を解除します(逆も可)
        * ―(Removes all non-select settings (vice versa))
    * **非選択物の選択を制限**
    * **―(Limit selection of non-selection)**
        * 選択物以外のオブジェクトを選択出来なくします
        * ―(Cannot select object other than a selection of)
    * **選択物の選択を制限**
    * **―(Limit choice of selecting)**
        * 選択中のオブジェクトを選択出来なくします
        * ―(Can't select selected object)
    * **オブジェクト名を正規表現で置換**
    * **―(Replace object names in regular expressions)**
        * 選択中のオブジェクトの名前を正規表現で置換します
        * ―(Name of currently selected object in regular expression replace)
    * **オブジェクト名とデータ名を同じにする**
    * **―(To same object and data names)**
        * 選択中のオブジェクトのオブジェクト名とデータ名を同じにします
        * ―(same object and data names for selected objects)
    * **オブジェクトカラー有効 + 色設定**
    * **―(Enable object color + color)**
        * 選択オブジェクトのオブジェクトカラーを有効にし、色を設定します
        * ―(Object color of selected object and sets color,)
    * **オブジェクトカラー無効 + 色設定**
    * **―(Object color off + color)**
        * 選択オブジェクトのオブジェクトカラーを無効にし、色を設定します
        * ―(To disable object color of selected object, sets color)
    * **モディファイア適用してペアレント作成**
    * **―(Applying modifiers, create a parent)**
        * 親オブジェクトのモディファイアを適用してから、親子関係を作成します
        * ―(Creates a parent-child relationship from parent object's modifiers to apply)
    * **カーブからロープ状のメッシュを作成**
    * **―(Create a mesh of rope-like curve to)**
        * アクティブなカーブオブジェクトに沿ったロープや蛇のようなメッシュを新規作成します
        * ―(Creates a mesh like rope along curve object is active or snake new)
    * **ベベルオブジェクトを断面に移動**
    * **―(Bevel object section moved)**
        * カーブに設定されているベベルオブジェクトを選択カーブの断面へと移動させます
        * ―(Curve beveled objects that move and cross section of you curve)
  
* **3Dビュー > ウェイトペイントモード > 「ウェイト」メニュー**
* **―(3D view > weight paint mode > "weight" menu)**
    * **ウェイト同士の合成**
    * **―(Synthesis of weights with each other)**
        * 選択中のボーンと同じ頂点グループのウェイトを合成します
        * ―(synthetic weights of selected bone and same vertex groups)
    * **ウェイト同士の減算**
    * **―(Subtraction of weight between)**
        * 選択中のボーンと同じ頂点グループのウェイトを減算します
        * ―(Subtracts weight of selected bone and same vertex groups)
    * **全頂点の平均ウェイトで塗り潰す**
    * **―(Fill in average weight of all vertices)**
        * 全てのウェイトの平均で、全ての頂点を塗り潰します
        * ―(average weight of all, fills all vertices)
    * **オブジェクトが重なっている部分を塗る**
    * **―(Paint objects overlap)**
        * 他の選択オブジェクトと重なっている部分のウェイトを塗ります
        * ―(I painted weight of portion that overlaps other selected objects)
    * **頂点グループぼかし**
    * **―(Vertex group blur)**
        * アクティブ、もしくは全ての頂点グループをぼかします
        * ―(Blurs active or all vertex groups)
  
* **3Dビュー > ポーズモード > 「ポーズ」メニュー > 「コンストレイント」メニュー**
* **―(3D view "pause mode" "pause" menu > "constraint" menu)**
    * **IK回転制限をコンストレイント化**
    * **―(Constraints of IK rotation restrictions)**
        * IKの回転制限設定をコンストレイントの回転制限設定にコピー
        * ―(Copy rotation constraint restrictions IK rotation limit settings)
  
* **3Dビュー > ポーズモード > 「ポーズ」メニュー > 「表示/隠す」メニュー**
* **―(3D view "pause mode" "pause" menu > show / hide menu)**
    * **選択しているものを選択不可に**
    * **―(What is selected in selection)**
        * 選択しているボーンを選択不可能にします
        * ―(Bones are selected to choose impossible)
    * **全ての選択不可を解除**
    * **―(Unlock all selectable)**
        * 全ての選択不可設定のボーンを選択可能にします
        * ―(non-selection of all bone)
  
* **3Dビュー > ポーズモード > 「W」キー**
* **―(3D view > pause mode > 'W' key)**
    * **カスタムシェイプを作成**
    * **―(Create a custom shape)**
        * 選択ボーンのカスタムシェイプを作成します
        * ―(Creates a choice bone shape)
    * **ウェイトコピー用メッシュを作成**
    * **―(Create a mesh for weight copy)**
        * 選択中のボーンのウェイトコピーで使用するメッシュを作成します
        * ―(Creates a mesh to use with a copy of selected bone weight)
    * **ボーン名をクリップボードにコピー**
    * **―(Copy to Clipboard bone name)**
        * アクティブボーンの名前をクリップボードにコピーします
        * ―(Copies Clipboard name of active bone)
    * **チェーン状ボーンをグリースペンシルに沿わせる**
    * **―(A chain of bones around grease pencil)**
        * チェーンの様に繋がった選択ボーンをグリースペンシルに沿わせてポーズを付けます
        * ―(Select bones linked like a chain of threading to grease pencil, pose)
    * **ボーン名を正規表現で置換**
    * **―(Replace bone names in regular expressions)**
        * (選択中の)ボーン名を正規表現に一致する部分で置換します
        * ―(In bone name (of choice) to match regular expression replace)
    * **スローペアレントを設定**
    * **―(Set slow parent)**
        * 選択中のボーンにスローペアレントを設定します
        * ―(Sets selected bone slow parent)
    * **ボーン名の XXX.R => XXX_R を相互変換**
    * **―(Bone name XXX. R = > XXX_R juggling)**
        * ボーン名の XXX.R => XXX_R を相互変換します
        * ―(Bone name XXX. R = > juggling XXX_R)
    * **ボーン名の XXX.R => 右XXX を相互変換**
    * **―(Bone name XXX. R = > juggling right XXX)**
        * ボーン名の XXX.R => 右XXX を相互変換します
        * ―(Bone name XXX. R = > conversion right XXX)
    * **ポーズの有効/無効を切り替え**
    * **―(Enable / disable pause switch)**
        * アーマチュアのポーズ位置/レスト位置を切り替えます
        * ―(Toggles pause / rest position of armature)
    * **対のボーンにコンストレイントをコピー**
    * **―(Copy constraints vs. Vaughan)**
        * 「X.L」なら「X.R」、「X.R」なら「X.L」の名前のボーンへとコンストレイントをコピーします
        * ―("X.L" If "X.R", "X.R" bone "X.L" name copy constraints)
    * **ボーン名の連番を削除**
    * **―(Remove bone name serial number)**
        * 「X.001」など、連番の付いたボーン名から数字を取り除くのを試みます
        * ―(Try to get rid of numbers from bone names with sequential numbers, such as "X.001")
    * **物理演算を設定**
    * **―(Set physical operations)**
        * 選択中の繋がったボーン群に、RigidBodyによる物理演算を設定します
        * ―(Bone group led selected sets physical operations of RigidBody)
    * **現ポーズを回転制限に**
    * **―(Currently pose a rotation limit)**
        * 現在のボーンの回転状態を、IKやコンストレイントの回転制限へと設定します
        * ―(Rotational States of current bone sets to rotation limit constraints and IK)
  
* **3Dビュー > メッシュ編集モード > 「選択」メニュー**
* **―(3D view > mesh edit mode > select menu)**
    * **X=0の頂点を選択**
    * **―(Select vertex of X = 0)**
        * X=0の頂点を選択する
        * ―(Select vertex of X = 0)
    * **右半分を選択**
    * **―(Select right half)**
        * メッシュの右半分を選択します(その他設定も有)
        * ―(Select right half of mesh (other settings too))
  
* **3Dビュー > オブジェクトモード > 「選択」メニュー**
* **―(3D view > mode > select menu)**
    * **サイズで比較してオブジェクトを選択**
    * **―(In size compared to object)**
        * 最大オブジェクトに対して大きい、もしくは小さいオブジェクトを選択します
        * ―(Select maximum objects larger or smaller objects)
    * **同じ名前のオブジェクトを選択**
    * **―(Select object with same name)**
        * アクティブなオブジェクトと同じ名前 (X X.001 X.002など) の可視オブジェクトを選択します
        * ―(Select visible object of active object with same name, such as (X.001 X X.002))
    * **同じマテリアル構造のオブジェクトを選択**
    * **―(Select an object of same material structure)**
        * アクティブなオブジェクトのマテリアル構造と同じ可視オブジェクトを選択します
        * ―(Select active object material structure and same visible objects)
    * **同じモディファイア構造のオブジェクトを選択**
    * **―(Select same modifier structure objects)**
        * アクティブなオブジェクトのモディファイア構造が同じ可視オブジェクトを選択します
        * ―(Select same modifier of active objects visible objects)
    * **同じサブサーフレベルのオブジェクトを選択**
    * **―(Select Subsurf levels same object)**
        * アクティブなオブジェクトのサブサーフレベルが同じ可視オブジェクトを選択します
        * ―(Select Subsurf levels of active objects have same visible objects)
    * **同じアーマチュアで変形しているオブジェクトを選択**
    * **―(Select objects that transform in same armature)**
        * アクティブなオブジェクトと同じアーマチュアで変形している可視オブジェクトを選択します
        * ―(Select visible objects are transformed in an active object with same armature)
    * **サイズで比較してオブジェクトを選択**
    * **―(In size compared to object)**
        * アクティブオブジェクトより大きい、もしくは小さいオブジェクトを追加選択します
        * ―(Greater than active object, or select additional small objects)
    * **面のあるメッシュを選択**
    * **―(Choose a surface mesh)**
        * 面が1つ以上あるメッシュを選択します
        * ―(Select a mesh surface at least one)
    * **辺のみのメッシュを選択**
    * **―(Select only side mesh)**
        * 面が無く、辺のみのメッシュを選択します
        * ―(Surface, select only side mesh)
    * **頂点のみのメッシュを選択**
    * **―(Select mesh vertices only)**
        * 面と辺が無く、頂点のみのメッシュを選択します
        * ―(Surfaces and edges, select mesh vertices only)
    * **頂点すら無いメッシュを選択**
    * **―(Select no mesh even vertex)**
        * 面と辺と頂点が無い空のメッシュオブジェクトを選択します
        * ―(Surface and edge and select mesh object vertex is not empty)
  
* **3Dビュー > ポーズモード > 「選択」メニュー**
* **―(3D view > pause mode > select menu)**
    * **連番の付いたボーンを選択**
    * **―(Select a numbered bone.)**
        * X.001 のように番号の付いた名前のボーンを選択します
        * ―(Select name with a number X.001 in bone)
    * **対称のボーンへ選択を移動**
    * **―(Symmetrical bones move selection)**
        * X.Rを選択中ならX.Lへ選択を変更、X.LならX.Rへ
        * ―(If you choose X.R change selection to X.L, if X.L to X.R)
    * **同じコンストレイントのボーンを選択**
    * **―(Select bone of same constraints)**
        * アクティブボーンと同じ種類のコンストレイントを持ったボーンを追加選択します
        * ―(Select additional bone with active bone and same kind of constraint.)
    * **同じ名前のボーンを選択**
    * **―(Select bone of same name.)**
        * X X.001 X.002 などのボーン名を同じ名前とみなして選択します
        * ―(Regarding bone names, such as X-X.001 X.002 with same name, select)
    * **名前が対称のボーンを追加選択**
    * **―(Select Add name of symmetrical bone)**
        * X.Rを選択中ならX.Lも追加選択、X.LならX.Rも選択
        * ―(If you select X.R X.L also selected X.R X.L if additional selection)
    * **ボーンの末端まで選択**
    * **―(Until end of bone)**
        * 選択ボーンの子 → 子ボーンの子...と最後まで選択していきます
        * ―(Select bones child-child child's bones. And we will select to end)
    * **ボーンの根本まで選択**
    * **―(Select bone)**
        * 選択ボーンの親 → 親ボーンの親...と最後まで選択していきます
        * ―(Choice bones parent → parent of parent bone. And we will select to the end)
    * **ボーンの経路を選択**
    * **―(Select route of bones)**
        * 2つの選択ボーンの経路を選択します
        * ―(Select select bones of two paths)
    * **右半分を選択**
    * **―(Select right half)**
        * ボーン群の右半分を選択します(その他設定も有り)
        * ―(Select right half of bone (other settings are also available))
    * **ボーンとその経路を選択**
    * **―(Bone and its route selection)**
        * カーソル部分のボーンを選択し、そこまでの経路も選択します
        * ―(Select path to it, select cursor part bone and)
  
* **3Dビュー > Shift+S**
* **―(3Dビュー > Shift+S)**
    * **メッシュに3Dカーソルをスナップ**
    * **―(3D cursor snap to mesh)**
        * マウス下のメッシュ面上に3Dカーソルを移動させます(ショートカットに登録してお使い下さい)
        * ―((Please use shortcuts) mesh surface under mouse move 3D cursor)
    * **視点位置に3Dカーソル移動**
    * **―(3D Navigation view)**
        * 視点の中心位置に3Dカーソルを移動させます
        * ―(Move 3D cursor center position of)
    * **3Dカーソルを非表示に(遥か遠くに)**
    * **―(3D cursor invisible in (distant))**
        * 3Dカーソルを遥か遠くに移動させて非表示のように見せかけます
        * ―(Pretend to hide 3D cursor to move far far away)
  
* **3Dビュー > メッシュ編集モード > 「U」キー**
* **―(3D view > mesh edit mode > "U" key)**
    * **他のUVからコピー**
    * **―(Copied from other UV)**
        * 選択部分のアクティブなUV展開を、他のUVからコピーしてきます
        * ―(Deploying an active UV selection will copy from other UV)
  
* **3Dビュー > 「ビュー」メニュー**
* **―(3D view > View menu)**
    * **グローバルビュー/ローカルビュー(非ズーム)**
    * **―(Global view and local views (non-zoom))**
        * 選択したオブジェクトのみを表示し、視点の中央に配置します(ズームはしません)
        * ―(And show only selected objects, center point of Zoom (is not))
    * **パネル表示切り替え(モードA)**
    * **―(Toggle Panel (mode A))**
        * プロパティ/ツールシェルフの「両方表示」/「両方非表示」をトグルします
        * ―(properties/tool shelf "both display" / "both hide" toggle)
    * **パネル表示切り替え(モードB)**
    * **―(Toggle Panel (mode B))**
        * 「パネル両方非表示」→「ツールシェルフのみ表示」→「プロパティのみ表示」→「パネル両方表示」のトグル
        * ―("Panel both hide" → show only the tool shelf → show only properties → "Panel both display" for toggle)
    * **パネル表示切り替え(モードC)**
    * **―(Toggle Panel (mode C))**
        * 「パネル両方非表示」→「ツールシェルフのみ表示」→「プロパティのみ表示」... のトグル
        * ―("Panel both hide" → "show only the tool shelf → show only the properties. The toggle)
    * **シェーディング切り替え(モードA)**
    * **―(Shading switch (mode A))**
        * シェーディングを 「ワイヤーフレーム」→「ソリッド」→「テクスチャ」... と切り替えていきます
        * ―("Wireframe", "solid" → "texture" shading... We will switch)
    * **プリセットビュー**
    * **―(Preset views)**
        * プリセットビュー(テンキー1,3,7とか)のパイメニューです
        * ―(Is a pie menu of preset views or (NUMPAD 1, 3, 7))
    * **シェーディング切り替え**
    * **―(Shading transitions)**
        * シェーディング切り替えパイメニューです
        * ―(Is shading switch pie)
    * **レイヤーのパイメニュー**
    * **―(Layer pie)**
        * レイヤー表示切り替えのパイメニューです
        * ―(Is a pie menu toggle layer visibility)
  
* **3Dビュー > 「ビュー」メニュー > 「視点を揃える」メニュー**
* **―(3D view > View menu > align View menu)**
    * **選択部分を表示 (非ズーム)**
    * **―(Display selection (non-zoom))**
        * 選択中の物に3D視点の中心を合わせます(ズームはしません)
        * ―(Food choice in over center of 3D view (zoom is not))
    * **視点を原点に**
    * **―(Viewpoint at origin)**
        * 3Dビューの視点を座標の中心に移動します
        * ―(3D view perspective moves in center of coordinate)
    * **選択+視点の中心に**
    * **―(In center of selection + POV)**
        * マウス下の物を選択し視点の中心にします (Shiftを押しながらで追加選択)
        * ―(Select object under mouse, center point of (shift in additional selection))
    * **メッシュに視点をスナップ**
    * **―(Snap to point mesh)**
        * マウス下のメッシュ面上に視点の中心を移動させます(ショートカットに登録してお使い下さい)
        * ―((Please use shortcuts) move center point of mesh surface under mouse)
    * **ビューの反対側に**
    * **―(On other side of view)**
        * 現在のビューの逆側へ回りこみます
        * ―(Orbit to reverse side of current view)
    * **視点と3Dカーソルを原点に**
    * **―(3D cursor with viewpoint at origin)**
        * 視点と3Dカーソルの位置を原点(XYZ=0.0)に移動させます
        * ―(Perspective and 3D cursor position move to origin (XYZ=0.0))
    * **メッシュに視点と3Dカーソルをスナップ**
    * **―(Perspective and 3D cursor snap to mesh)**
        * マウス下のメッシュ面上に視点と3Dカーソルを移動させます (ショートカットに登録してお使い下さい)
        * ―((Please use shortcuts) move viewpoint and 3D cursor mesh surface under mouse)
  
* **3Dビュー > 「ビュー」メニュー > 「視点を揃える」メニュー > 「アクティブに視点を揃える」メニュー**
* **―(3D view > View menu > align View menu > menu align view active)**
    * **面を正面から見る**
    * **―(Viewed from front side)**
        * 選択中の面の法線方向から面を注視します
        * ―(watch face from selected surface normal direction)
  
* **「3Dビュー」エリア > プロパティ > レイヤーボタンがあるパネル**
* **―(3D view area > properties > the layer button panel)**
    * **グループで表示/非表示を切り替え**
    * **―(Toggle show / hide groups)**
        * 所属しているグループで表示/非表示を切り替えます
        * ―(Group show / hide toggles)
  
* **「3Dビュー」エリア > テクスチャペイント > ツールシェルフ > 「スロット」パネル**
* **―(3D view area > texture paint > tool shelf > see slot Panel)**
    * **アクティブなテクスチャスロットを塗る**
    * **―(Apply active texture slot)**
        * アクティブなペイントスロットをアクティブなテクスチャスロットにします
        * ―(active texture slot slot active paint)
  
* **UV/画像エディター > 「画像」メニュー**
* **―(UV / image editor > image menu)**
    * **クイック編集 (拡張)**
    * **―(Quick Edit (extend))**
        * ユーザー設定のファイルタブで設定した追加の外部エディターでクイック編集を行います
        * ―(Do quick editing in an external editor of additional files page of custom)
  
* **「3Dビュー」エリア > 「プロパティ」パネル > 「ビュー」パネル**
* **―(Area 3D view > properties panel > "view" Panel)**
    * **視点のセーブ**
    * **―(Save view)**
        * 現在の3Dビューの視点をセーブします
        * ―(Save current 3D view perspective)
    * **視点のロード**
    * **―(Point of load)**
        * 現在の3Dビューに視点をロードします
        * ―(Load current 3D view perspective)
    * **視点セーブを破棄**
    * **―(View save to discard)**
        * 全ての視点セーブデータを削除します
        * ―(Removes all viewpoints save data)
  
# ライセンス (License)
Copyright (c) 2015 saidenka.  
All rights reserved.  
  
Redistribution and use in source and binary forms are permitted  
provided that the above copyright notice and this paragraph are  
duplicated in all such forms and that any documentation,  
advertising materials, and other materials related to such  
distribution and use acknowledge that the software was developed  
by the saidenka.  The name of the  
saidenka may not be used to endorse or promote products derived  
from this software without specific prior written permission.  
THIS SOFTWARE IS PROVIDED `AS IS'' AND WITHOUT ANY EXPRESS OR  
IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE IMPLIED  
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  