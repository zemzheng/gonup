1.Install
<pre>
#--------------------------------------------------
$ cd ~
$ mkdir gonup
$ rz -bye
$ unzip gonup.zip 
$ rm gonup.zip
$ echo "source ~/gonup/.bashrc" >> .bashrc  
</pre>


2.Configure
<pre>
#--------------------------------------------------
# default setting
$ vim ~/gonup/config.py
# 设置 go/update 的默认值

# servers target
$ vim ~/gonup/svrs.conf

# update target
$ vim ~/gonup/update.conf

# use your own go|up alias
$ vim ~/gonup/.bashrc
</pre>

3.Useage
<pre>
#--------------------------------------------------

# 列出已经配置的go目标
$ go

# 执行 go 目标 target_go_1 的内容
$ go target_go_1

# 列出已经配置的up目标
$ up

# 执行 up 目标 target_up_1 的内容
$ up target_up_1
</pre>

4.Demo
4.1 登录机器
<pre>
# ~/gonup/config.py 内已经默认设置
# port=36000
# user=root

# ~/gonup/svrs.conf
[demo]
host=127.0.0.1
pasw=123456789
path=/data/
</pre>
