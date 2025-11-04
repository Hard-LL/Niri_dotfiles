config.load_autoconfig(False)

c.auto_save.session = True# 重新打开时恢复站点

# ********** QT **********

# ********** URL **********

c.url.auto_search = 'dns'# 正确搜索网址，不正确直接搜索
c.url.default_page = 'about:blank'# 默认网页为空白页
c.url.incdec_segments = ['path']# 更改网页中的数字，Ctrl+a：加数字，Ctrl+x：减数字
c.url.open_base_url = True# 搜索为空时搜索会跳转到默认搜索网页
c.url.searchengines = {# 搜索引擎
    'DEFAULT': 'https://www.bing.com/search?q={}',
    'g': 'https://www.google.com/search?q={}',
    'gh': 'https://github.com/search?q={}',
    'aw': 'https://wiki.archlinux.org/index.php?search={}',
}
c.url.start_pages = ['about:blank']# 打开默认为空白页
c.url.yank_ignored_parameters = [# 复制简约url,复制命令为y（yank）
    'utm_source', 
    'utm_medium', 
    'utm_campaign', 
    'utm_term', 
    'utm_content',
    'fbclid',
    'gclid',
    'msclkid',
    'mc_eid'
]

# ********** window **********

c.window.hide_decoration = True# True:隐藏标题栏,False:显示标题栏
c.window.title_format = "{current_title}{perc}"# 标签栏当前标签页名和加载进度
