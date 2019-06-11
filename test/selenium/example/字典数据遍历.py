list=[{'title': 'hahahahhahahah', 'content': '哈哈哈哈哈哈哈哈哈哈哈哈'}, {'title': 'lalalalalaal', 'content': '啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦'}, {'title': '', 'content': '标题为空'}, {'title': '内容少于三个字', 'content': ''}]

for item in list:
    print(item)
    print(item['title'],item['content'])