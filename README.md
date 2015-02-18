# Blender-Scramble-Addon
Blenderのかゆいところに手が届くかもしれない機能が詰まったアドオンです。

## インストール
まず→の「Download ZIP」でZIPファイルをダウンロードし、解凍して下さい。  
中の「Scramble Addon」フォルダをBlenderのaddonsフォルダに置いて下さい。  
(Windows7なら： C:\Users\ユーザー名\AppData\Roaming\Blender Foundation\Blender\バージョン\scripts\addons\Scramble Addon)  
Blenderを起動しユーザー設定のアドオンタブで「Scramble」等で検索、アドオンをオンにして「ユーザー設定の保存」クリック。  
左上の「ファイル」メニューに「全体処理」という項目が追加されていればインストール成功です。  

## 使い方
このアドオンは基本的に、既存のメニューに項目が追加されるのでそれをクリックして実行します。  
例えば「ファイル > 全体処理 > オブジェクト > 全ての「すべての辺を表示」をオン」等です。  
追加された項目には必ず![アイコン](http://i.imgur.com/OOVguPd.png)のようなアイコンが表示されています。  
色々なところに項目が追加されているので探してみてください。  

## 機能一覧
* UV/画像エディター > 「画像」メニュー
    * 全ての画像名を使用するファイル名に
        * 全ての画像の名前を、使用している外部画像のファイル名にします
    * 全ての画像を再読み込み
        * 外部ファイルを参照している画像データを全て読み込み直します
  
* UV/画像エディター > 「選択」メニュー
    * 分離している頂点を選択
        * シームによって分離している頂点を選択します
  
* UV/画像エディター > 「ビュー」メニュー
    * カーソルの位置をリセット
        * 2Dカーソルの位置を左下に移動させます
  
* 情報 > 「ファイル」メニュー
    * 再起動
        * Blenderを再起動します
    * 全ての「すべての辺を表示」をオン
        * 全てのオブジェクトの「すべての辺を表示」表示設定をオンにします(オフも可能)
    * 全ての最高描画タイプを一括設定
        * 全てのオブジェクトの「最高描画タイプ」を一括で設定します
    * 全てのデータ名をオブジェクト名と同じにする
        * 全てのオブジェクトのデータ(メッシュデータなど)の名前を、リンクしているオブジェクト名に置換します
    * 全てのマテリアルの「半透明影の受信」をオン
        * 全てのマテリアルの「半透明影を受信するかどうか」についての設定をオン(オフ)にします
    * アクティブマテリアルのカラーランプ設定を他にコピー
        * アクティブなマテリアルのカラーランプ設定を他の全マテリアル(選択オブジェクトのみも可)にコピーします
    * アクティブマテリアルのFreeStyle色を他にコピー
        * アクティブなマテリアルのFreeStyleの色設定を他の全マテリアル(選択オブジェクトのみも可)にコピーします
    * 全マテリアルのFreeStyle色をディフューズ色に
        * 全マテリアル(選択オブジェクトのみも可)のFreeStyleライン色をそのマテリアルのディフューズ色+ブレンドした色に置換します
    * 全てのバンプマップの品質を設定
        * 全てのテクスチャのバンプマップの品質を一括で設定します
    * 全てのテクスチャ名を使用する画像ファイル名に
        * 全てのテクスチャの名前を、使用している外部画像のファイル名にします
    * UV指定が空欄な場合アクティブUVで埋める
        * テクスチャのUV指定欄が空欄の場合、リンクしているメッシュオブジェクトのアクティブなUV名で埋めます
    * 全ての画像名を使用するファイル名に
        * 全ての画像の名前を、使用している外部画像のファイル名にします
    * 物理演算の開始/終了フレームを一括設定
        * 物理演算などの開始/終了フレームを設定する部分にレンダリング開始/終了フレーム数を割り当てます
  
* 情報 > 「ファイル」メニュー > 「外部データ」メニュー
    * 全ての画像を再読み込み
        * 外部ファイルを参照している画像データを全て読み込み直します
  
* 情報 > 「ヘルプ」メニュー
    * Blender-Scramble-Addonを更新
        * Blender-Scramble-Addonをダウンロード・更新を済ませます
  
* 3Dビュー > オブジェクト/メッシュ編集モード > 「追加」メニュー > 「メッシュ」メニュー
    * 四角ポリゴン球
        * 四角ポリゴンのみで構成された球体メッシュを追加します
    * 頂点のみ
        * 1頂点のみのメッシュオブジェクトを3Dカーソルの位置に追加します
  
* 情報 > 「レンダー」メニュー
    * 解像度の倍率を設定
        * 設定解像度の何パーセントの大きさでレンダリングするか設定します
    * レンダー簡略化の設定
        * レンダリングの簡略化の設定を行います(本来はシーンタブから行います)
  
* 情報 > 「ウィンドウ」メニュー
    * エディタータイプ
        * エディタータイプ変更のパイメニューです
    * エディタータイプ変更
        * エディタータイプを変更します
    * UIの英語・日本語 切り替え
        * インターフェイスの英語と日本語を切り替えます
  
* プロパティ > 「マテリアル」タブ > リスト右の▼
    * 割り当てのないマテリアルを削除
        * 面に一つも割り当てられてないマテリアルを全て削除します
    * マテリアルスロット全削除
        * このオブジェクトのマテリアルスロットを全て削除します
    * 空のマテリアルスロット削除
        * このオブジェクトのマテリアルが割り当てられていないマテリアルスロットを全て削除します
    * マテリアルスロットを移動
        * アクティブなマテリアルスロットを移動させます
    * スロットを一番上へ
        * アクティブなマテリアルスロットを一番上に移動させます
    * スロットを一番下へ
        * アクティブなマテリアルスロットを一番下に移動させます
  
* プロパティ > 「オブジェクトデータ」タブ > シェイプキー一覧右の▼
    * シェイプキーを複製
        * アクティブなシェイプキーを複製します
    * シェイプブロック名を調べる
        * シェイプブロックの名前を表示し、クリップボードにコピーします
    * シェイプブロックの名前をオブジェクト名に
        * シェイプブロックの名前をオブジェクト名と同じにします
    * 全てのシェイプにキーフレームを打つ
        * 現在のフレームに、全てのシェイプのキーフレームを挿入します
    * 最上段を選択
        * 一番上のシェイプキーを選択します
    * 最下段を選択
        * 一番下のシェイプキーを選択します
  
* プロパティ > 「オブジェクトデータ」タブ > 頂点グループ一覧右の▼
    * 空の頂点グループを削除
        * メッシュにウェイトが割り当てられていない頂点グループを削除します
    * ミラーの対になる空頂点グループを追加
        * .L .R などミラーの命令規則に従って付けられたボーンの対になる空の新規ボーンを追加します
    * 一番上を選択
        * 頂点グループの一番上の項目を選択します
    * 一番下を選択
        * 頂点グループの一番下の項目を選択します
    * 最上段へ
        * アクティブな頂点グループを一番上へ移動させます
    * 最下段へ
        * アクティブな頂点グループを一番下へ移動させます
  
* ノードエディター > 「ノード」メニュー
    * このノードを全マテリアルにコピー
        * 現在表示されているノードツリーを他の全マテリアル(選択オブジェクトのみも可)に複製します
  
* プロパティ > 「テクスチャ」タブ > リスト右の▼
    * テクスチャ名を使用する画像ファイル名に
        * アクティブなテクスチャの名前を使用している外部画像のファイル名にします
    * テクスチャスロットを全て空に
        * アクティブなマテリアルの全てのテクスチャスロットを空にします
    * 最上段へ
        * アクティブなテクスチャスロットを一番上に移動させます
    * 最下段へ
        * アクティブなテクスチャスロットを一番下に移動させます
  
* 3Dビュー > アーマチュア編集モード > 「W」キー
    * 選択ボーンをミラーリング
        * 選択中のボーンを任意の軸でミラーリングします
    * ボーン名をクリップボードにコピー
        * アクティブボーンの名前をクリップボードにコピーします
    * ボーン名を正規表現で置換
        * (選択中の)ボーン名を正規表現に一致する部分で置換します
    * 反対位置にあるボーンをリネーム
        * 選択中ボーンのX軸反対側の位置にあるボーンを「○.R ○.L」のように対にします
  
* 3Dビュー > アーマチュア編集モード > 「Shift+W」キー
    * ボーン名をまとめて設定
        * 選択中のボーンの名前をまとめて設定します
    * カーブボーンをまとめて設定
        * 選択中のボーンのカーブボーン設定をします
    * ロールをまとめて設定
        * 選択中のボーンのロールを設定します
    * アクティブのIK設定(回転制限等)をコピー
        * アクティブなボーンのIK設定(回転制限など)を他の選択ボーンにコピーします
    * IKのポールターゲットを設定
        * アクティブなボーンのIKのポールターゲットを第二選択ボーンに設定します
    * IKのチェーンの長さを設定
        * アクティブなボーンのIKのチェーンの長さを第二選択ボーンへの長さへと設定します
  
* 3Dビュー > アーマチュア編集モード > 「アーマチュア」メニュー
    * 確認無しでボーンを削除
        * ボーンを確認無しで削除します
    * ボーンをそのまま3Dカーソルの位置へ
        * 相対的なボーンの尾(根本でも可)の位置をそのままに、ボーンを3Dカーソルの位置へ移動させます
  
* 3Dビュー > メッシュ編集モード > 「メッシュ」メニュー
    * 2頂点の向きで新座標系を作成
        * 選択中の2頂点の向きから新しい座標軸の向きを追加します
    * メッシュ選択モード
        * メッシュの選択のパイメニューです
    * プロポーショナル編集
        * プロポーショナル編集のパイメニューです
    * プロポーショナル編集のモードを設定
        * プロポーショナル編集のモードを設定します
  
* 3Dビュー > メッシュ編集モード > 「X」キー
    * 選択モードと同じ要素を削除
        * 現在のメッシュ選択モードと同じ要素(頂点・辺・面)を削除します
  
* 3Dビュー > メッシュ編集モード > 「メッシュ」メニュー > 「表示/隠す」メニュー
    * 表示/隠すを反転
        * 表示状態と非表示状態を反転させます
    * 頂点のみを隠す
        * 選択状態の頂点のみを隠して固定します
    * 選択しているパーツを隠す
        * 1頂点以上を選択しているメッシュパーツを隠します
  
* 3Dビュー > メッシュ編集モード > 「W」キー
    * 選択頂点の頂点カラーを塗り潰す
        * 選択中の頂点のアクティブ頂点カラーを指定色で塗り潰します
    * 選択部分に厚みを付ける
        * 選択中の面に厚みを付けます
    * 一番上のシェイプを選択
        * リストの一番上にあるシェイプキーを選択します
    * 編集ケージへのモディファイア適用を切り替え
        * 編集中のメッシュケージにモディファイアを適用するかを切り替えます
  
* 3Dビュー > メッシュ編集モード > 「Ctrl+V」キー
    * 別オブジェクトに分離 (拡張)
        * 「別オブジェクトに分離」の拡張メニューを呼び出します
    * 選択物 (分離側をアクティブ)
        * 「選択物で分離」した後に分離した側のエディトモードに入ります
    * 選択部を複製/新オブジェクトに
        * 選択部分を複製・分離し新オブジェクトにしてからエディトモードに入ります
  
* 3Dビュー > オブジェクトモード > 「Ctrl+L」キー
    * オブジェクト名を同じに
        * 他の選択オブジェクトにアクティブオブジェクトの名前をリンクする
    * レイヤーを同じに
        * 他の選択オブジェクトにアクティブオブジェクトのレイヤーをリンクする
    * オブジェクトの表示設定を同じに
        * オブジェクトの表示パネルの設定をコピーします
  
* 3Dビュー > オブジェクトモード > 「オブジェクト」メニュー
    * コピー
        * オブジェクトに関するコピーのパイメニューです
    * オブジェクト対話モード
        * オブジェクト対話モードのパイメニューです
    * オブジェクト対話モードを設定
        * オブジェクトの対話モードを設定します
    * サブサーフ設定
        * サブサーフのレベルを設定するパイメニューです
    * 確認せずに削除
        * 削除する時の確認メッセージを表示せずにオブジェクトを削除します
    * オブジェクト名をクリップボードにコピー
        * アクティブなオブジェクトの名前をクリップボードにコピーします
    * 全モディファイア削除
        * 選択オブジェクトの全てのモディファイアを削除します
    * ブーリアンを追加
        * アクティブオブジェクトにその他選択オブジェクトのブーリアンを追加
    * ブーリアンを適用
        * アクティブオブジェクトにその他選択オブジェクトのブーリアンを適用
    * UV名を変更
        * アクティブなUVの名前を変更します(テクスチャのUV指定もそれに伴って変更します)
    * 未使用のUVを削除
        * アクティブなオブジェクトのマテリアルで未使用なUVを全削除します(他の部分に使われているUVは消してしまいます)
    * レンダリング時の細分化数を設定
        * 選択したオブジェクトのサブサーフモディファイアのレンダリング時の細分化数を設定します
    * プレビュー・レンダリングの細分化数を同じに
        * 選択したオブジェクトのサブサーフモディファイアのプレビュー時とレンダリング時の細分化数を同じに設定します
    * 最適化表示を設定
        * 選択したオブジェクトのサブサーフモディファイアの最適化表示を設定します
    * 選択オブジェクトのサブサーフを削除
        * 選択したオブジェクトのサブサーフモディファイアを削除します
    * 選択オブジェクトにサブサーフを追加
        * 選択したオブジェクトにサブサーフモディファイアを追加します
  
* 3Dビュー > オブジェクトモード > 「オブジェクト」メニュー > 「表示/隠す」メニュー
    * 表示/隠すを反転
        * オブジェクトの表示状態と非表示状態を反転させます
    * 特定の種類のオブジェクトのみを隠す
        * 表示されている特定タイプのオブジェクトを隠します
    * 特定の種類のオブジェクト以外を隠す
        * 表示されている特定タイプのオブジェクト以外を隠します
    * 選択物をレンダリングしない
        * 選択中のオブジェクトをレンダリングしない設定にします(逆も可)
    * 選択物を選択不可に
        * 選択中のオブジェクトを選択出来なくします
    * 全オブジェクトの非レンダリングを解除
        * 全てのオブジェクトのレンダリングしない設定を解除します(逆も可)
    * 全オブジェクトの選択不可を解除
        * 全てのオブジェクトの選択不可設定を解除します(逆も可)
  
* 3Dビュー > オブジェクトモード > 「W」キー
    * オブジェクト名をクリップボードにコピー
        * アクティブなオブジェクトの名前をクリップボードにコピーします
    * オブジェクト名を正規表現で置換
        * 選択中のオブジェクトの名前を正規表現で置換します
    * オブジェクト名とデータ名を同じにする
        * 選択中のオブジェクトのオブジェクト名とデータ名を同じにします
    * 頂点カラーを一括追加
        * 選択中のメッシュオブジェクト全てに色と名前を指定して頂点カラーを追加します
    * カーブからロープ状のメッシュを作成
        * アクティブなカーブオブジェクトに沿ったロープや蛇のようなメッシュを新規作成します
    * ウェイト転送
        * 他の選択中のメッシュからアクティブにウェイトペイントを転送します
    * グリースペンシルにメタボール配置
        * アクティブなグリースペンシルに沿ってメタボールを配置します
  
* 3Dビュー > ウェイトペイントモード > 「ウェイト」メニュー
    * ウェイト同士の合成
        * 選択中のボーンと同じ頂点グループのウェイトを合成します
    * ウェイト同士の減算
        * 選択中のボーンと同じ頂点グループのウェイトを減算します
    * 全頂点の平均ウェイトで塗り潰す
        * 全てのウェイトの平均で、全ての頂点を塗り潰します
    * オブジェクトが重なっている部分を塗る
        * 他の選択オブジェクトと重なっている部分のウェイトを塗ります
  
* 3Dビュー > ポーズモード > 「ポーズ」メニュー > 「コンストレイント」メニュー
    * IK回転制限をコンストレイント化
        * IKの回転制限設定をコンストレイントの回転制限設定にコピー
  
* 3Dビュー > ポーズモード > 「ポーズ」メニュー > 「表示/隠す」メニュー
    * 選択しているものを選択不可に
        * 選択しているボーンを選択不可能にします
    * 全ての選択不可を解除
        * 全ての選択不可設定のボーンを選択可能にします
  
* 3Dビュー > ポーズモード > 「W」キー
    * 選択ボーンのカスタムシェイプを作成
        * 選択中のボーンのカスタムシェイプオブジェクトを作成します
    * 選択ボーンのウェイトコピー用メッシュを作成
        * 選択中のボーンのウェイトコピーで使用するメッシュを作成します
    * ボーン名をクリップボードにコピー
        * アクティブボーンの名前をクリップボードにコピーします
    * チェーン状ボーンをグリースペンシルに沿わせる
        * チェーンの様に繋がった選択ボーンをグリースペンシルに沿わせてポーズを付けます
    * ボーン名を正規表現で置換
        * (選択中の)ボーン名を正規表現に一致する部分で置換します
  
* 3Dビュー > アーマチュア編集モード > 「選択」メニュー
    * 右半分を選択
        * ボーン群の右半分を選択します(その他設定も有)
  
* 3Dビュー > メッシュ編集モード > 「選択」メニュー
    * X=0の頂点を選択
        * X=0の頂点を選択する
    * 右半分を選択
        * メッシュの右半分を選択します(その他設定も有)
  
* 3Dビュー > ポーズモード > 「選択」メニュー
    * 同じコンストレイントのボーンを選択
        * アクティブボーンと同じ種類のコンストレイントを持ったボーンを追加選択します
  
* 3Dビュー > 「ビュー」メニュー
    * プリセットビュー
        * プリセットビュー(テンキー1,3,7とか)のパイメニューです
    * シェーディング切り替え
        * シェーディング切り替えパイメニューです
    * シェーディング切り替え
        * シェーディングを切り替えます
    * グループで表示/非表示を切り替え
        * 所属しているグループで表示/非表示を切り替えます
    * グループで表示/非表示を切り替え実行
        * 所属しているグループで表示/非表示を切り替えます
  
* 3Dビュー > 「ビュー」メニュー > 「視点を揃える」メニュー
    * 選択部分を視点の中心に
        * 選択中の物に3D視点の中心を合わせます(ズームはしません)
    * カーソルの位置をリセット
        * カーソルのXYZを0.0にします(他の位置も可)
    * 視点を中心に
        * 3Dビューの視点を座標の中心に移動します
  
