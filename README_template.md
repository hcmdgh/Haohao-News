# Haohao News

Haohao News，致力于收录公平、公正、客观的环球新闻，聚焦于中国大陆、中国港澳台、国际形势。

# 构建方法

对于每日新增的新闻，以Markdown文件形式放置在news/xxx目录下，其中xxx为当日日期，格式为“20220209”。

每一则新闻对应一个Markdown文件，文件名不限但是必须以*.md作为后缀，文件第一行必须为“#”+新闻标题。

运行Python脚本“build.py”，将自动构建完整的README.md文件。
