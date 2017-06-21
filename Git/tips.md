#### Create new branch and push to the remote repository
```
git branch <branch-name>
git push -u origin <branch-name>
```

#### Show Changed file name only
```
git diff --name-only
```
#### Move ?
```
git cherry-pic hashnumber
```

#### 工作流
三棵树
1) working dir
2) index(stage) 暂存区
3) HEAD 指向最后一次提交的结果
添加到暂存区
```
git add <filename>
git add *
```
实际提交改动
```
git commit -m "代码提交信息"
```
改动已经提交到了HEAD，但是还没到你的远端仓库

执行如下命令将改动提交到远端仓库
```
git push origin master
```
可以把master换成你想要推送的任何分支

#### 分支
创建一个叫做"feature_x"的分支，并切换过去:
```
git checkout -b feature_x
```
删除分支
```
git branch -d feature_x
```
推送分支
```
git push origin <branch>
```
#### 更新与合并
要更新你的本地仓库至最新改动
```
git pull
```
要合并其他分支到你的当前分支(例如master),执行
```
git merge <branch>
```
预览差异
```
git diff <source_branch> <target_branch>
```
#### log
```
git log --pretty=oneline
```
看看那些文件变了
```
git log --name-status
```
#### 替换本地改动
如果操作失误
```
git checkout -- <filename>
```
此命令会使用HEAD中的最新内容替换掉你的工作目录中的文件
