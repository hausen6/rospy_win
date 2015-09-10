# rospy_win
## 概要
rospyをwindows (多分macも)で頑張ってうごかすためのリポジトリ．
windowsの資産，windowsでしか使えないデバイスをUbuntuのROSと通信して上手くごまかすのが目的．
本格的な運用には向かないかも．
当然のことながら，``roscore``はUbuntu上で行う必要があるので，これはあくまで基本をUbuntuで行って，補助的に他のOSでノードを立ち上げる使い方を想定.


- 現時点ではros-indigoのみの対応(他のrosのバージョンで動くかは知らない)．
- 基本的にrospyはpythonでしか書かれていなそうなので，これを動かせばtopicのやりとりは可能
(まだserviceの実装/実行は未確認)
- 一応``python2.7.10``, ``python3.3.5``で動作確認済み

このリポジトリは
```python
import rospy
```
を実行するために必要な最小構成(を目指している)．

## Install
このリポジトリをpython環境にインストールすると，
```python
import rospy
```
を行うために必要な

- catkin
- genmsg
- genpy
- roscpp
- rosgraph
- rosgraph_msgs
- roslib
- std_msgs
- std_srvs
- rospkg (pip)
- catkin_pkg (pip)

のインストールも同時に行います．
``(pip)``が付いているものはpip経由でのインストールです．

インストールは

```bash
$ git clone git://github.com/hausen6/rospy_win
$ cd rospy_win
$ python setup.py install
```
でOKです．

## Tips
### ROS_MASTER_URIなどの設定
masterを立ち上げる際に
- ``ROS_MASTER_URI``
- ``ROS_IP``
を環境変数にセットする必要があるので，

**windows**
```msdos
$ set ROS_MASTER_URI=http://<ROS_MASTER_IP>:11311
$ set ROS_IP=<YOUR_IP>
```
を実行するか，
``システムのプロパティ->詳細設定->環境変数``
からこれら変数を設定しても良し．

**osx**
Ubuntuと同じ.

**共通**
運用によるけど，``rospy.init_node``は中で``os.environ``を参照して接続に行っているようなので，プログラムの中で``rospy.init_node``を呼ぶ前に
```python
os.environ["ROS_MASTER_URI"] = "http:<ROS_MASTER_IP>:11311"
os.environ["ROS_IP"] = "<YOUR_IP>"
# ...
rospy.init_node("NODE_NAME")
```
としてもOKということがわかった．
お好きな方法をどうぞ．

### トピック，サービスの追加
トピックやサービスが定義してあるpythonファイルをコピーすることで基本的に動作すると思う．
なので，元々用意されているトピックなどを使う場合は``/opt/ros/indigo/lib/python2.7/dist-packages/``以下の必要なパッケージをWindowsにコピーしてくればOK．
独自型のものを使用したければ，Ubuntu上でmakeした上で，``<YOUR_WORK_SPACE>/devel/lib/python2.7/dist-packages/``以下を同様にコピーしてくれば使えるはず．

## 既知の問題
### rospack
現在，一応使えてはいるもの，``rospy/core.py``内で行っているlogファイルの読み込みで例外排出されてしまうので，一行ほどコードをコメントアウトしている(rospackが使えないためっぽいエラー)．
今後大きな問題が発生した場合は対応を考える．
