# 搜索联想
联想/纠错
- SQL like查询
- 前缀树
- 拼音联想
- 关键词联想
- 意图识别(TODO)
- 复合模型(TODO)

## 项目依赖
- MySQL
- PostgreSQL

- pip install psycopg2-binary --no-cache-dir

## 项目部署
```commandline
docker-compose up -d
```
## 仓库地址
Github：https://github.com/Coolgiserz/SearchAssociation
Gitee：https://gitee.com/coolgiserz/SearchAssociation

## TODO
- 搜索服务通用化改造，可快速支持新增数据源的联想搜索
- 完善索引建立方式（拼音全拼、拼音首字母、拼写纠错等）
- 健全索引更新机制
- 实现联想结果精排序
- 支持百万级数据量的索引、联想查询