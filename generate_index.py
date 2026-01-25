import os

# 排除不需要显示的文件
EXCLUDE = ['index.html']

def generate():
    # 获取当前目录下所有 html 文件
    files = [f for f in os.listdir('.') if f.endswith('.html') and f not in EXCLUDE]
    files.sort() # 按字母顺序排序

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write('<html><head><title>我的文档列表</title>')
        f.write('<meta name="viewport" content="width=device-width, initial-scale=1">')
        f.write('<style>body{font-family:sans-serif;padding:20px;line-height:1.6;} a{color:#0366d6;text-decoration:none;} a:hover{text-decoration:underline;} li{margin-bottom:10px;}</style>')
        f.write('</head><body>')
        f.write('<h1>📑 自动更新的文档索引</h1><ul>')
        
        for file in files:
            # 去掉后缀作为显示文字
            display_name = file.replace('.html', '').replace('_', ' ')
            f.write(f'<li><a href="./{file}">{display_name}</a></li>')
        
        f.write('</ul></body></html>')

if __name__ == '__main__':
    generate()
