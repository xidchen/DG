# 接口文档

## 接口描述

使用SSE调用方式请求接口，模型根据视频文案，评论内容等信息，输出对评论的回复内容

|   事项   | 说明                |
|:------:|:------------------|
|  传输方式  | http              |
|  请求地址  | TBD               |
|  调用方式  | SSE               |
|  字符编码  | UTF-8             |
| 接口请求头  | text/event-stream |
| 请求接口格式 | JSON              |
|  相应格式  | Event Stream      |
| 接口请求类型 | POST              |

## 请求说明

Body中放置请求参数，参数详情如下：

|    参数    | 是否必选 |   类型   | 说明   |
|:--------:|:----:|:------:|:-----|
|  client  |  是   | string | 客户ID |
|  config  |  是   | object | 配置对象 |
| messages |  是   | array  | 内容列表 |

其中参数config：

|          字段           |   类型   |     说明      | 可选值          |
|:---------------------:|:------:|:-----------:|:-------------|
|   character_gender    | string |    人设性别     | "男","女",""   |
|     character_age     |  int   |    人设年龄     | 1-100        |
|    character_role     | string |    人设角色     | "普通人","官方"   |
|   character_emotion   | string |    人设情绪     | "喜悦","伤心"    |
|  brand_promotion_pct  | float  |   品牌种草百分比   | 1-100        |
|     homepage_pct      | float  |  吸引查看主页百分比  | 1-100        |
|   pinned_video_pct    | string | 引导查看置顶视频百分比 | 1-100        |
|  promotion_link_pct   | float  |   推广链接百分比   | 1-100        |
|  promotion_link_list  | array  |   推广链接列表    | ["a.com"]    |
| account_promotion_pct | float  |  主账号引流百分比   | 1-100        |
|     account_list      | array  |    主账号列表    | ["account1"] |
| contact_insertion_pct | string |  添加联系方式百分比  | 1-100        |
|     contact_list      | array  |   联系方式列表    | ["contact1"] |
|    min_word_count     |  int   |   最小回复字数    | 1-100        |
|    max_word_count     |  int   |   最大回复字数    | 1-100        |

以及参数messages：

|       字段        |   类型   | 说明   |
|:---------------:|:------:|:-----|
|      uuid       | string | 唯一标识 |
| blogger_accout  | string | 博主账号 |
|  video_content  | string | 视频文案 |
| comment_content | string | 评论内容 |

## 返回说明

返回参数

|    字段    |   类型   | 说明   |
|:--------:|:------:|:-----|
|   uuid   | string | 唯一标识 |
| response | string | 回复内容 |
