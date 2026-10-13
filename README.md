# Nezha-Live 哪吒节点实况主题 (Komari & Cyber Probe)

工业蓝图风格的实时节点看板主题，面向 **Cyber Probe**，可通过 Komari 兼容的主题管理安装。全屏 WebGL 地图（地球 / Equal Earth 平面）叠加工程 HUD，节点按地区落点，点击可打开详情大屏。

## 功能

- 地球与平面地图两种视图，可拖拽、缩放，支持减弱动效偏好。
- 节点按地区聚合，显示在线状态、实时速率和资源占用。
- 详情大屏：CPU / 内存 / 磁盘 / 网络四项仪表、硬件规格、网络探测目标、计费与流量配额。
- 全部为真实数据：节点列表来自 `/api/v1/nodes`，实时状态来自 `/api/v1/client/ws` 推送；告警由节点离线 / 恢复、CPU 高负载与流量配额（≥80%）的实际变化产生，没有演示或模拟数据。
- 依赖 Cyber Probe 的原生接口，不支持只提供 Komari 接口的服务端。私有站点未登录时跳转到 `/admin` 登录。

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
