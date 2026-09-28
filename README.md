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

## 字体（自托管，可免费商用）
- 正文中英文：**阿里巴巴普惠体**；姓名：**得意黑 Smiley Sans**，均放在 `assets/fonts/` 本地加载（不依赖 CDN，国内外都稳定）。
- 已使用**完整版字体**（非子集化），覆盖全部常用汉字，以后新增文字直接写即可，无需处理字体。详见 `assets/fonts/FONT_LICENSE.md`。

## 中英文切换
页面右上角有 **中文 / EN** 切换按钮（纯 JS 实现，无需刷新）。
- 原理：每处文字同时写有 `<span class="le">英文</span><span class="lz">中文</span>`，按钮切换 `body.zh` 类，CSS 控制显示哪套。
- **以后更新内容时记得同时改两份**（le=英文，lz=中文），选择记忆在浏览器 localStorage。
- 新增条目照抄现有条目的双语 span 结构即可。
