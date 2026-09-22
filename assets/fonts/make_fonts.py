#!/usr/bin/env python3
"""
重新生成子集字体 (woff2)。
用法:  python3 make_fonts.py  [--src /path/to/full-ttf-dir]
依赖:  pip install fonttools brotli

源字体(完整版)需自行准备并放入 src 目录或通过 --src 指定:
  - AlibabaPuHuiTi-3-55-Regular.ttf   (阿里巴巴普惠体 Regular)
  - AlibabaPuHuiTi-3-85-Bold.ttf      (阿里巴巴普惠体 Bold)
  - SmileySans-Oblique.ttf.woff2       (得意黑, 官方 release)

脚本会扫描 ../../index.html 用到的汉字, 加上 ASCII/Latin-1/常用标点,
生成三个子集 woff2 覆盖本页面当前内容。改完页面文字后重跑一次即可。
"""
import os, sys, argparse
from fontTools import subset

HERE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(HERE, '..', '..', 'index.html')

ap = argparse.ArgumentParser()
ap.add_argument('--src', default=os.path.join(HERE, 'src'))
a = ap.parse_args()

def need(p):  # 源文件
    cands = [os.path.join(a.src, p), os.path.join(HERE, p)]
    for c in cands:
        if os.path.exists(c):
            return c
    raise SystemExit(f'找不到源字体 {p}，请放入 {a.src}/ 或用 --src 指定')

html = open(HTML, encoding='utf-8').read()
used = set(html)
base = set(chr(c) for c in range(0x20, 0x7f)) | set(chr(c) for c in range(0xA0, 0x100))
for lo, hi in [(0x2010,0x2027),(0x2030,0x205E),(0x2100,0x214F),(0x2190,0x21FF),
               (0x3000,0x303F),(0x2E80,0x2EFF),(0xFE30,0xFE4F),(0xFF00,0xFFEF)]:
    base |= set(chr(c) for c in range(lo, hi+1))
cjk = set(c for c in used if '\u4E00' <= c <= '\u9FFF' or '\u3400' <= c <= '\u4DBF')
codes = {ord(c) for c in (base | cjk)}

def make(src, dst, unicodes=None, text=None):
    opts = subset.Options()
    opts.flavor = 'woff2'
    opts.layout_features = ['*']
    opts.name_IDs = [0,1,2,3,4,5,6]
    opts.notdef_outline = True
    opts.recalc_bounds = True
    f = subset.load_font(src, opts)
    ss = subset.Subsetter(opts)
    ss.populate(text=text) if text else ss.populate(unicodes=unicodes)
    ss.subset(f)
    subset.save_font(f, dst, opts)
    print(dst, round(os.path.getsize(dst)/1024, 1), 'KB')

make(need('AlibabaPuHuiTi-3-55-Regular.ttf'), os.path.join(HERE, 'PuHuiTi-Regular.woff2'), unicodes=codes)
make(need('AlibabaPuHuiTi-3-85-Bold.ttf'),     os.path.join(HERE, 'PuHuiTi-Bold.woff2'),     unicodes=codes)
make(need('SmileySans-Oblique.ttf.woff2'),     os.path.join(HERE, 'SmileySans.woff2'),       text='周苏豫Suyu Zhou')
print('完成。')
