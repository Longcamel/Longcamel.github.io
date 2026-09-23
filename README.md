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
- 为减小体积做了**子集化**，只含页面当前用到的字符。**以后新增文字后**，运行：
  ```bash
  cd assets/fonts
  python3 make_fonts.py   # 需先 pip install fonttools brotli，并把完整源字体放入 src/ 或 --src 指定
  ```
  否则新写的字可能显示为方块。详见 `assets/fonts/FONT_LICENSE.md`。

## 中英文切换
页面右上角有 **中文 / EN** 切换按钮（纯 JS 实现，无需刷新）。
- 原理：每处文字同时写有 `<span class="le">英文</span><span class="lz">中文</span>`，按钮切换 `body.zh` 类，CSS 控制显示哪套。
- **以后更新内容时记得同时改两份**（le=英文，lz=中文），选择记忆在浏览器 localStorage。
- 新增条目照抄现有条目的双语 span 结构即可。

## 待办（TODO，index.html 内有注释标记）
1. 替换真实头像照片
2. 取消注释并填写 GitHub / Google Scholar / LinkedIn 链接
3. 以后更新 About 与 Education
4. 有论文发表后在 Patents 处新增 Publications 版块
