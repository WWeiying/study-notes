#! https://zhuanlan.zhihu.com/p/685502982

## linux命令自查手册
>持续更新

|        命令         |                             解释                             |
| :-----------------: | :----------------------------------------------------------: |
| watch -n 1 ifconfig | 使用 watch 命令周期性地查看 ifconfig 命令的输出，实现每秒更新一次网络接口的信息。退出按`CTRL-C` |
|    sudo nload -m    |                     查看所有网卡实时网速                     |
|    file filename    |                         识别文件类型                         |
|                     |                                                              |
|                     |                                                              |
|                     |                                                              |

### Bash快捷键

在 Bash 中，默认的快捷键设置与 Emacs 的快捷键非常相似。Bash 使用 Readline 库来处理命令行编辑，而 Readline 提供了一组与 Emacs 编辑模式相兼容的快捷键。这使得许多在 Emacs 中常用的编辑命令在 Bash 中也可以使用。

除了默认的 Emacs 模式，Bash 也支持 Vi 模式。可以通过以下命令启用 Vi 模式，在 Vi 模式下，Bash 的快捷键将遵循 Vi 的编辑命令。

```bash
set -o vi
set -o emacs
```

|           命令           |                             解释                             |
| :----------------------: | :----------------------------------------------------------: |
|      光标移动快捷键      |                                                              |
|        `Ctrl + a`        |                      将光标移动到行首。                      |
|        `Ctrl + e`        |                      将光标移动到行尾。                      |
|        `Alt + f`         |                   将光标向前移动一个单词。                   |
|        `Alt + b`         |                   将光标向后移动一个单词。                   |
|        `Ctrl + f`        |                   将光标向前移动一个字符。                   |
|        `Ctrl + b`        |                   将光标向后移动一个字符。                   |
|        编辑快捷键        |                                                              |
|        `Ctrl + k`        |                删除光标位置到行尾的所有字符。                |
|        `Ctrl + u`        |                删除光标位置到行首的所有字符。                |
|        `Ctrl + w`        |             删除光标位置到前一个单词的所有字符。             |
|        `Alt + d`         |             删除光标位置到后一个单词的所有字符。             |
|        `Ctrl + d`        |      删除光标位置的字符（或退出当前会话，如果行为空）。      |
|        `Ctrl + h`        |         删除光标前的字符（与 `Backspace` 键相同）。          |
|        `Ctrl + y`        |                     粘贴最近删除的文本。                     |
|        `Ctrl + t`        |                交换光标处和前一个字符的位置。                |
| 历史记录和命令操作快捷键 |                                                              |
|        `Ctrl + r`        |                      搜索命令历史记录。                      |
|        `Ctrl + p`        |               从命令历史记录中调用上一条命令。               |
|        `Ctrl + n`        |               从命令历史记录中调用下一条命令。               |
|        `Alt + .`         | 插入上一条命令的最后一个单词（可以重复使用以插入更早的命令的最后一个单词） |
|           其他           |                                                              |
|        `Ctrl + l`        |              清屏（相当于执行 `clear` 命令）。               |
|        `Ctrl + s`        |                  停止终端输出（冻结终端）。                  |
|        `Ctrl + q`        |                  恢复终端输出（解冻终端）。                  |
|        `Ctrl + c`        |                   终止当前正在运行的命令。                   |
|        `Ctrl + z`        |               将当前正在运行的命令挂起到后台。               |
### 压缩、解压缩

|                             命令                             |                             解释                             |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
|             tar -czvf archive.tar.gz folder_name             | -c 创建新归档<br/>-z 通过 gzip 压缩<br/>-v 显示详细信息（可选）<br/>-f 指定归档文件名 |
|            tar -cjvf archive.tar.bz2 folder_name             |                    -j 表示通过 bzip2 压缩                    |
|             tar -cJvf archive.tar.xz folder_name             |                     -J 表示使用 xz 压缩                      |
|       tar -xJvf example.tar.xz -C /path/to/destination       | 使用 xz 算法解压文件 example.tar.xz，，并以详细模式输出解压过程，同时将解压后的内容放到 /path/to/destination 目录 |
|      tar -xzvf filename.tar.gz -C /path/to/destination       | 使用 gzip 算法解压文件 filename.tar.gz，并以详细模式输出解压过程，同时将解压后的文件放入 /path/to/destination 目录 |
|                zip -r archive.zip folder_name                | -r 参数表示递归地将 folder_name 目录及其所有子目录和文件都打包到 archive.zip 中 |
|              zip archive.zip file1 file2 file3               | 将 `file1`、`file2`、`file3` 打包压缩成一个名为 `archive.zip` 的压缩包 |
|                         unzip *.zip                          |          解压当前目录下所有以 `.zip` 结尾的压缩文件          |
| `find . -name '*.zip' -exec sh -c 'for file do dirname="${file%.zip}"; unzip "$file" -d "$dirname"; done' _ {} \;` |                                                              |
| `find . -name '*.tar.gz' -exec sh -c 'for file do dirname="${file%.tar.gz}"; mkdir -p "$dirname"; tar -xzvf "$file" -C "$dirname"; done' _ {} \;` |                                                              |
|                                                              |                                                              |

### 文件操作

|              命令              |                             解释                             |
| :----------------------------: | :----------------------------------------------------------: |
| chown -R owner:group directory |     递归地改变文件夹及其所有子文件和子文件夹的属主和属组     |
|    安装.bundle为后缀的软件     | 在 Linux 中，带有 `.bundle` 后缀的文件通常是一种自解压或自安装包。安装这类文件的基本步骤如下：<br />chmod +x filename.bundle<br />sudo ./filename.bundle |
|                                |                                                              |

### find工具

|                 命令                  |               解释               |
| :-----------------------------------: | :------------------------------: |
| find [搜索路径] [搜索条件] [处理动作] |                                  |
|             **搜索路径**              |                                  |
|                  `.`                  |             当前目录             |
|         `/path/to/directory`          |             指定目录             |
|             **搜索条件**              |                                  |
|                `-name`                |            按名称搜索            |
|               `-iname`                |     按名称搜索（忽略大小写）     |
|                `-type`                | 按类型搜索（`f` 文件，`d` 目录） |
|                `-size`                |            按大小搜索            |
|               `-mtime`                |          按修改时间搜索          |
|               `-atime`                |          按访问时间搜索          |
|               `-ctime`                |        按状态变化时间搜索        |
|                `-user`                |           按所有者搜索           |
|               `-group`                |             按组搜索             |
|                `-perm`                |            按权限搜索            |
|             **处理动作**              |                                  |
|               `-print`                |      输出匹配的文件（默认）      |
|                `-exec`                |     对匹配的文件执行指定命令     |
|               `-delete`               |          删除匹配的文件          |
|                 `-ls`                 |           显示详细信息           |

### grep工具

|                            命令                            |                             解释                             |
| :--------------------------------------------------------: | :----------------------------------------------------------: |
|                 grep [选项] 模式 [文件...]                 |                  grep "pattern" example.txt                  |
|                            `-i`                            |                 忽略大小写（ignore case）。                  |
|                            `-v`                            |             反向匹配，即显示不包含匹配模式的行。             |
|                            `-c`                            |                 只输出匹配的行数（count）。                  |
|                            `-l`                            |              显示包含匹配模式的文件名（list）。              |
|                            `-n`                            |                 显示匹配行的行号（number）。                 |
|                            `-H`                            |           显示匹配的文件名（默认对多个文件生效）。           |
|                        `-r` 或 `-R`                        |                    递归搜索目录中的文件。                    |
|                            `-w`                            |                       只匹配整个单词。                       |
|                            `-o`                            |                      只显示匹配的部分。                      |
|                          `-A NUM`                          |                   匹配的行及其后 NUM 行。                    |
|                          `-B NUM`                          |                   匹配的行及其前 NUM 行。                    |
|                          `-C NUM`                          |                 匹配的行及其前后各 NUM 行。                  |
| find . -type f -name '*.lib' -exec grep -Hn 'pattern' {} + | 查找所有 .lib 文件并执行 grep 搜索![image-20250307141436207](https://raw.githubusercontent.com/WWeiying/Figurebed/master/blog-images/2025/03/07/14-14-37-193e5da6d9451c6a85607a9607ab5516-image-20250307141436207-8959d1.png?token=AT2LY23EWK47KQO7O5WRCXLHZKHQS) |
|           grep -rn --include='*.lib' 'pattern' .           | 递归搜索当前目录及子目录下所有 .lib 文件中的 "pattern"![image-20250307141509402](https://raw.githubusercontent.com/WWeiying/Figurebed/master/blog-images/2025/03/07/14-15-11-8c5b91a7866952ccae39995e32f1090c-image-20250307141509402-b707f2.png?token=AT2LY22YKWCBJBKPYD2CR7LHZKHSU) |
|         grep -rn --include='*.{lib,a}' 'pattern' .         |                       搜索多个文件类型                       |
|                                                            |                                                              |
|                                                            |                                                              |
|                                                            |                                                              |
|                                                            |                                                              |
### 后台执行

|  命令  |                                                                                解释                                                                                |
| :----: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|   fg   |    如果你在后台运行了一个程序，并且想要将其切换到前台，可以使用 `fg` 命令。首先使用 `jobs` 命令查看后台任务的编号，然后使用 `fg %job_number` 将任务切换到前台。    |
|   bg   | 如果你想将一个在后台暂停的任务重新切换到后台运行，可以使用 `bg` 命令。首先使用 `jobs` 命令查看后台任务的编号，然后使用 `bg %job_number` 将任务切换到后台继续运行。 |
| Ctrl+Z |                                                                  可以将当前正在前台运行的程序暂停                                                                  |
| nohup  |                       nohup 命令可以让程序忽略挂断（SIGHUP）信号，即使用户退出终端，程序也可以继续在后台运行。语法为：nohup ./your_program &                       |
|   &    |                                                        可以在命令行的末尾添加 `&` 符号来使命令在后台执行。                                                         |

### 定时命令

|    命令    |                             解释                             |
| :--------: | :----------------------------------------------------------: |
| crontab -e |                    编辑当前用户的定时任务                    |
| crontab -l |                    列出当前用户的定时任务                    |
| crontab -r |                删除所有定时任务（谨慎操作！）                |
|            | ![image-20250307191413788](images/image-20250307191413788.png) |
|            | ![image-20250307191512098](images/image-20250307191512098.png) |
|            |                                                              |


### 历史命令

|   命令   |                                                                                         解释                                                                                          |
| :------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| history  |                                              `history` 命令会列出之前执行过的命令历史记录，每条命令前面带有一个编号。history \| grep ls                                               |
| Ctrl + R | 按下 `Ctrl + R` 键会进入逆向搜索模式，你可以开始输入你记得的关键词，系统会自动显示最接近的匹配项。一旦找到想要的命令，按下 `Enter` 键执行，或者按下 `Ctrl + R` 继续查找下一个匹配项。 |
|    !!    |                                                                            输入 `!!` 会执行最后一条命令。                                                                             |
|    !n    |                                                                  使用 `!n` 来执行历史记录中特定编号 `n` 对应的命令。                                                                  |

### 查看系统信息

|        命令         |                      解释                      |
| :-----------------: | :--------------------------------------------: |
| cat /etc/os-release |       显示当前 Linux 系统的发行版信息等        |
|      uname -a       | 显示系统的内核版本、操作系统名称和版本号等信息 |
|      uname -r       |           显示当前系统使用的内核版本           |
|   lsb_release -a    | 显示系统的发行版信息，包括发行版名称、版本号等 |

### 查看处理器信息

|       命令        |                             解释                             |
| :---------------: | :----------------------------------------------------------: |
| cat /proc/cpuinfo |                  显示详细的 CPU 信息<br />                   |
|       lscpu       | 显示 CPU 体系结构信息<br />Socket(s): 物理处理器插槽数（即物理 CPU 数量）<br/>Core(s) per socket: 每个处理器的核心数<br/>Thread(s) per core: 每个核心的线程数（如启用了超线程则可能大于 1） |
|       nproc       | 返回系统可用的处理单元总数（逻辑处理器数），通常等于“Socket 数 × 核心数 × 每核心线程数”。 |

### 查看进程信息

|                             命令                             |            解释             |
| :----------------------------------------------------------: | :-------------------------: |
|                           ps -aux                            |   显示所有进程的详细信息    |
|                       ps -u <username>                       |     查看特定用户的进程      |
| ps -eo user,%cpu --sort=-%cpu \| awk '{arr[$1]+=$2} END {for (i in arr) print i, arr[i]"%"}' | 统计所有用户的 CPU 总使用率 |
| watch -n 5 "ps -eo user,%cpu --sort=-%cpu \| awk '{arr[\$1]+=\$2} END {for (i in arr) print i, arr[i]\"%\"}'" |        实时监控脚本         |
|                          kill <PID>                          |        终止单个进程         |
|                        kill -9 <PID>                         |        强制终止进程         |
|                       pkill -u wangwy                        |    批量终止用户所有进程     |
|                                                              |                             |

### 代码统计
| 命令 |                             解释                             |
| :--: | :----------------------------------------------------------: |
| cloc | `cloc` 是一个用于统计源代码行数的命令行工具。它可以分析多种编程语言的代码，并生成代码统计报告，包括空白行、注释行和实际代码行数。 |
|      |                                                              |

### git命令

|                       命令                        |                             解释                             |
| :-----------------------------------------------: | :----------------------------------------------------------: |
|                 **git checkout**                  |          用于切换分支、恢复工作区文件以及创建新分支          |
|            git checkout <branch-name>             |                       切换到指定的分支                       |
|          git switch -c <new-branch-name>          |                                                              |
|         git checkout -b <new-branch-name>         |                创建一个新的分支并切换到该分支                |
|              git checkout -- <file>               | 从当前分支中恢复指定的文件，放弃这些修改并恢复到最新提交的状态， |
|            git checkout <commit-hash>             |     切换到指定的提交（会使工作区进入“分离头指针”状态）。     |
|                                                   |                                                              |
|                                                   |                                                              |
|            git restore --staged <file>            |                           取消暂存                           |
|                  **git branch**                   | 用于在 Git 中管理分支，可以用于列出、创建、删除和重命名分支。 |
|                    git branch                     |                   列出本地仓库中的所有分支                   |
|                   git branch -a                   |         加上 `-a` 选项可以列出所有分支，包括远程分支         |
|                   git branch -r                   |                       列出所有远程分支                       |
|           git branch <new-branch-name>            |                       创建一个新的分支                       |
|            git branch -d <branch-name>            |                       删除一个本地分支                       |
|            git branch -D <branch-name>            | 如果分支没有被合并，使用 `-d` 会失败。这是为了防止潜在的数据丢失。如果确实要强制删除未合并的分支，可以使用 |
|                git branch -M main                 |                        重命名当前分支                        |
| git branch -m <old-branch-name> <new-branch-name> |                       重命名指定的分支                       |
|                   **git push**                    |             将本地存储库中的更改推送到远程存储库             |
|                     git push                      | 将当前分支推送到其上游分支。上游分支通常是远程仓库中的一个分支，已经通过 `git branch --set-upstream-to` 或 `git push -u` 命令进行配置。 |
|           git push -u <remote> <branch>           | 将本地分支推送到远程分支，并设置上游跟踪。如果是第一次推送该分支，这是一个很有用的选项。 |
|        git push <remote> --delete <branch>        |                    删除远程仓库中的分支。                    |
|              git push --all <remote>              |                将本地所有分支推送到远程仓库。                |
|             git push <remote> --tags              |                将本地所有标签推送到远程仓库。                |
|                                                   |                                                              |
|                                                   |                                                              |
|               git reset --hard HEAD               |        将工作区和暂存区中的文件恢复到上一次提交的状态        |
|             git reset --soft HEAD~10              | 撤销最近 10 次提交的 Git 命令，但保留所有修改内容在暂存区<br />  撤销提交历史但保留代码修改，便于重新提交，适合未推送的本地提交调整，已推送需谨慎使用 `--force` |
|                 git checkout -- .                 | 将工作区中的所有文件恢复到最近一次提交的状态，但不会影响暂存区中的文件 |
|            git restore --staged <file>            |           将暂存区中的文件恢复到工作区，即取消暂存           |
|              git restore --staged .               |                      取消所有暂存的文件                      |
|                   git clean -f                    |                  删除工作区中未被追踪的文件                  |
|                   git clean -n                    |            查看将要被删除的文件，而不实际删除它们            |
|                                                   |                                                              |
|     git update-index --assume-unchanged file      |                  暂时停止跟踪某个文件的更改                  |
|    git update-index --no-assume-unchanged file    |                    恢复追踪某个文件的修改                    |
|                                                   |                                                              |
|               git status --ignored                |                     检查哪些文件会被忽略                     |
|               git rm -r --cached .                |                                                              |
|                                                   |                                                              |

### Docker

|                             命令                             |            解释            |
| :----------------------------------------------------------: | :------------------------: |
| ` docker run -itd --hostname lizhen --mac-address 02:42:ac:11:00:02 -v /etc/localtime:/etc/localtime:ro -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/root/.Xauthority -v $HOME/mydata:/mydata -e DISPLAY=$DISPLAY -e GDK_SCALE -e GDK_DPI_SCALE --name EDA phyzli/ubuntu18.04_xfce4_vnc4server_synopsys`:w |                            |
|                   docker container rm EDA                    | 删除一个处于终止状态的容器 |
|                  docker container rm EDA -f                  |    删除一个运行中的容器    |
|                                                              |                            |
|                                                              |                            |
|                                                              |                            |
|                                                              |                            |
|                                                              |                            |
|                                                              |                            |

### VNC

|                        命令                         |     解释     |
| :-------------------------------------------------: | :----------: |
|  sudo systemctl start vncserver@:<display>.service  |   启动服务   |
|  sudo systemctl stop vncserver@:<display>.service   |   停止服务   |
| sudo systemctl restart vncserver@:<display>.service |   重启服务   |
| sudo systemctl status vncserver@:<display>.service  | 查看服务状态 |
| sudo systemctl enable vncserver@:<display>.service  | 设置开机自启 |
| sudo systemctl disable vncserver@:<display>.service | 取消开机自启 |
|                                                     |              |
|                                                     |              |



![image-20240814164419398](images/image-20240814164419398.png)