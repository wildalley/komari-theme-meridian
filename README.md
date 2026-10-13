# Nezha-Live 哪吒节点实况主题 (Komari & Cyber Probe)

工业蓝图风格的实时节点看板主题，面向 **Cyber Probe**，兼容 **Komari** 数据接口。全屏 WebGL 地图（地球 / Equal Earth 平面）叠加工程 HUD，节点按地区落点，点击可打开详情大屏。

## 功能

- 地球与平面地图两种视图，可拖拽、缩放，支持减弱动效偏好。
- 节点按地区聚合，显示在线状态、实时速率和资源占用。
- 详情大屏：CPU / 内存 / 磁盘 / 网络四项仪表、硬件规格、网络探测目标、计费与流量配额。
- 数据来源：优先使用 Cyber Probe 原生接口（`/api/v1/nodes`、`/api/v1/client/ws`），取不到时回退到 Komari 兼容的 `/api/nodes`；都没有数据时显示演示节点。

## 安装

### Cyber Probe

Cyber Probe 服务端已内嵌本主题，启动后会自动装到主题目录。在管理后台 `/admin` → 主题管理中启用 **Nezha Live** 即可。

### 手动上传

1. 下载 [`nezha-live.zip`](https://raw.githubusercontent.com/wildalley/komari-theme-nezha-live/main/nezha-live.zip)；
2. 管理后台 → 主题管理 → 上传本地主题包；
3. 设为生效。

## 开发

```bash
npm install
npm run dev     # 本地预览
npm run build   # 生成 dist/ 和 nezha-live.zip
```

页面源码是 `index.html`，three.js 放在 `public/vendor/`，通过 import map 在运行时加载（构建时不打包）。`public/map-data.json` 是地图轮廓数据。

发布新版本时，同时提升 `komari-theme.json` 和 `package.json` 的 `version`：Cyber Probe 只在内嵌版本与已装版本不同时才会覆盖安装。

## 许可证

MIT
