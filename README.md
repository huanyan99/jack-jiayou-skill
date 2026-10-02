# jack-jiayou-skill

Jack 要加油的个人技能库。逐步积累可复用的 Codex / Agent Skills 工作流程。

## 目录约定

```text
skills/<skill-name>/
  SKILL.md             # 必需：YAML 元数据和技能指令
  agents/openai.yaml   # 可选：Codex 展示信息
  scripts/             # 按需：可执行辅助脚本
  references/          # 按需：详细参考资料
  assets/              # 按需：输出使用的模板或素材
templates/SKILL.md.example
scripts/validate_skills.py
```

目前尚未添加业务技能。模板不放在 skills 中，避免被当成可用技能加载。

## 添加技能

1. 创建 `skills/<skill-name>/`，名称使用小写英文、数字和连字符，最多 64 个字符。
2. 将 `templates/SKILL.md.example` 复制为该目录的 `SKILL.md`，替换所有占位内容。
3. `name` 与目录名称一致；`description` 说明能力和触发场景。
4. 正文写清目标、关键工作流程和必要约束。详细资料按需放入 `references/`，并从正文链接。
5. 只创建实际需要的资源目录。不要提交密码、令牌、个人敏感资料或环境缓存。
6. 安装 Python 3 和 PyYAML 后运行校验：

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate_skills.py
```

GitHub Actions 会在提交和 Pull Request 时自动校验。空技能库允许通过。

## 在 Codex 中使用

将需要的技能目录复制到 `~/.codex/skills/`（Windows 为 `%USERPROFILE%\.codex\skills\`），重新打开会话后可通过 `$skill-name` 调用，或由匹配场景自动触发。

例如：`skills/my-skill` 安装到 `~/.codex/skills/my-skill`。不要将整个仓库复制成单个技能。

## 标准依据

使用 Agent Skills 的 `SKILL.md` 入口和渐进披露结构；`agents/openai.yaml` 是可选的 Codex 扩展。

- [Agent Skills 规范](https://agentskills.io/specification)
- [Codex Skills 文档](https://developers.openai.com/codex/skills/)

新增内容保持一个技能解决一类明确任务，随着实际使用迭代。
