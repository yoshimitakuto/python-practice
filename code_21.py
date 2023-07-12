"""
【ログ】
logger : ログ出力の命令
handler : 実際の出力の実行部分

StreamHandler -> コマンドに出力
FileHandler -> ファイルに出力

「ログレベル」
1、DEBUG -> 主に開発中に挙動が正しいかを確認するために使用される。プログラム内の情報を出力する。
2、INFO  -> 正常な動きをしている情報を出力する。
3、WARNING -> ちょっとまずいかも。。もしかしたらエラーが出るかもよ？という警告をしてくれる。
4、ERROE -> 問題が起きた時に出力。
5、CRITICAL -> 重大な問題が発生している時に出力

「流れ」
前提：loggerとhandlerのそれぞれで扱うログレベルが、
設定したログレベル以上のものしか扱えないものとなっている。
例：loggerがERRORレベルの場合loggeはERROR以上のログレベルを扱える。

①loggerのログレベルを確認
②handlerのログレベルを確認
③出力
※上記の1と2が通らないと出力されない
"""

from logging import getLogger, FileHandler, Formatter, DEBUG, ERROR

formatter = Formatter('[%(levelname)s] %(asctime)s - %(message)s (%(filename)s)')
logger = getLogger(__name__)

handler = FileHandler('log2.txt')
# ハンドラーへログレベルを設定
handler.setLevel(DEBUG)
handler.setFormatter(formatter)

error_handler = FileHandler('error.txt')
error_handler.setLevel(ERROR)
error_handler.setFormatter(formatter)

# ロガーにもレベルを設定
logger.setLevel(DEBUG)
# ロガーにハンドラーを設定(このロガーにはこのハンドラーを使うよ！)
logger.addHandler(handler)
logger.addHandler(error_handler)

# logger.debug('これはデバッグログです')
# logger.error('ファイルが存在していません')

logger.info('プログラムが開始しました')
logger.debug('入力値は1000です')
logger.warning('ファイルの容量が200GBを超えました')
logger.error('ファイルが存在していません')