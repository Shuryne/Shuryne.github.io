---
date: 2021-06-02
---





## 远端开发

### 1. SSH Configuration

1. 本地在``.ssh/config``中设置Hosts
1.  Pycharm中设置``ssh configuration``(如果设置了Hostname可以直接用)

### 2. Python Interpreter

1. 最好是不同``project``配置不同的``python``环境，这样不同项目就有不同的``Interpreter``，相互之间不会因为包产生冲突
1. 最好使用远端``Interpreter``，因为本地没有GPU
1. 使用``SSH``方式而不是``Deployment Configuration``设置``Python Interpreter``


### 2. Deployment

1. 设置``autoupload``，自动同步远端，始终保持本地和远端代码一致性 
1. data等非不必要的大文件可以加入``except path``



## 项目配置

1. 项目添加``requirement.txt``
1. 设置``file template``: 添加作者、时间、介绍等
1. 设置注释风格为``Google``
1. 设置``save action``: 保存时自动排版规范化并上传服务器



## 其他

### 1. 快捷键

1. ``option + enter``: 快速点出错误提示并进行修改
1. ``cmd + [``: 回到上一个文件光标处
1. ``cmd + shift + f``: 全局搜索
1. ``cmd + shift + r``: 全局替换


### 2. refactor

1. 可以统一更新变量名
1. 可以提取函数到新文件中


### 3. 数据处理

1. 能用正则快速处理数据的时候，尽量不用写脚本处理，节省时间
1. 熟悉vim操作能够节省数据处理的时间
