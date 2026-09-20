# Suyu Zhou — Academic Homepage

学术风个人主页（纯静态 HTML/CSS，无需 Jekyll，无构建步骤）。

## 文件结构
- `index.html` — 主页内容（About / Research / Education / Experience / Projects / Patents / Awards / Skills）
- `style.css` — 样式（学术衬线风、响应式、可打印）
- `assets/avatar.svg` — 占位头像（**请替换为真实照片**，如 `assets/photo.jpg` 并改 `index.html` 中的 `src`）
- `cv/` — 中英文简历 PDF
- `.nojekyll` — 让 GitHub Pages 直接托管静态文件

## 部署到 GitHub Pages
```bash
cd homepage
git init && git add -A && git commit -m "Academic homepage"
# 在 GitHub 新建名为  <你的用户名>.github.io  的仓库后：
git remote add origin git@github.com:<你的用户名>/<你的用户名>.github.io.git
git branch -M main && git push -u origin main
```
约 1 分钟后访问 `https://<你的用户名>.github.io`。

## 待办（TODO，index.html 内有注释标记）
1. 替换真实头像照片
2. 取消注释并填写 GitHub / Google Scholar / LinkedIn 链接
3. 获得博士学位后更新 About 与 Education
4. 有论文发表后在 Patents 处新增 Publications 版块
