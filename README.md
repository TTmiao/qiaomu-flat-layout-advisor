# Qiaomu Flat Layout Advisor

一个面向平面设计的版式诊断 Skill：读取用户的海报、封面、长图、编辑页、宣传图或演示页，结合 `nevertoday/350-layout-compositions` 的案例目录，给出可执行的改稿建议。

## 能做什么

- 识别视觉层级、构图重心、网格、对齐、留白、阅读路径和图文关系
- 从 350 种排版案例中检索相近结构
- 把案例转译成可复用的版式法则，并说明适用条件与失败模式
- 按 `必须修改 / 高收益调整 / 可选实验` 排序建议
- 保留原有内容、品牌约束和设计意图

## 不做什么

- 不把案例图当作模板直接临摹
- 不在没有看到设计稿时假装完成视觉诊断
- 不默认替用户重做整张图
- 不把审美偏好写成确定性结论

## 输入建议

上传一张清晰的成稿，并尽量补充：画布尺寸、使用场景、目标受众、主标题/副标题层级、品牌限制，以及你最不满意的地方。

## 安装与验证

```bash
npx skills add TTmiao/qiaomu-flat-layout-advisor --skill qiaomu-flat-layout-advisor
python scripts/match_layout_cases.py --query "非对称 标题 留白" --limit 5
python scripts/validate_skill.py .
```

前置条件：

- [ ] 已安装 Node.js 与 npx
- [ ] 已准备一张清晰的平面成稿

你可以直接这样说：

本地安装后，用一张实际成稿发送以下请求即可验证触发：

> 诊断这张海报的视觉层级、重心和留白，引用 3 个相关案例法则，先给修改建议，不要直接重做。

## 排障

Troubleshooting

- 没有触发：明确说“海报/封面/版式诊断”和“案例对照”，并附图或结构化描述。
- 案例太泛：补充作品类型、目标和最想改善的区域；默认优先使用构图、视觉原则、出版广告、字体网格四类。
- 无法联网：给 `match_layout_cases.py` 传入本地 `catalog.json`，视觉诊断仍可基于已有案例和法则完成。

## 目录来源

上游图鉴：`https://github.com/nevertoday/350-layout-compositions`

本 Skill 默认优先使用构图逻辑、视觉原则、出版广告、字体网格四类；网页 UI、影视画面、中国传统构图和演示文稿作为按需适配器。

## 本地检索

```bash
python scripts/match_layout_cases.py --query "非对称 标题 留白" --limit 5
```

## 版权与署名

上游仓库的许可和署名信息以其仓库为准。本 Skill 不复制全部图片，只保存检索规则和稳定目录信息。

Copyright (c) 向阳乔木
X: https://x.com/vista8
GitHub: https://github.com/joeseesun/

## License

MIT

<!-- qiaomu-profile:start -->
## 关于向阳乔木

向阳乔木（乔向阳 / Joe）是一位实践型 AI 产品与内容创作者，长期把前沿 AI 变化转译成可复用的工作流、产品判断、AI 编程实践、AI 搜索实践和 GEO/AI 营销方法。

- 个人网站: https://qiaomu.ai
- 博客: https://blog.qiaomu.ai
- X: https://x.com/vista8
- GitHub: https://github.com/joeseesun/
- 微信公众号: 向阳乔木推荐看

### 支持与关注

| 打赏支持 | 微信公众号 |
|---|---|
| <img src="assets/qiaomu-profile/qiaomu_reward_qr.png" alt="向阳乔木打赏二维码" width="180" /> | <img src="assets/qiaomu-profile/qiaomu_wechat_public_account_qr.jpg" alt="向阳乔木推荐看公众号二维码" width="180" /> |
| 感谢支持乔木持续分享 AI 实践 | 扫码关注「向阳乔木推荐看」 |

<!-- qiaomu-profile:end -->
