## jieba分词API
基于jieba分词和tornado提供分词API

### 关键词抽取
`POST /textrank`

请求内容
```json
{
  "content": "要抽取关键词的文本"
}
```

正常返回内容
```json
[
  {
    "name": "关键词1",
    "score": 1
  },
  {
    "name": "关键词2",
    "score": 0.99
  }
]
```

传入格式错误时,返回400状态码
```json
{
  "msg": "格式传入错误"
}
```