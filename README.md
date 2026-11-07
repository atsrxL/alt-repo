# atsrxL Apps

个人 iOS / iPadOS 应用统一分发源，可添加到 AltStore Classic、SideStore 或 Feather。

**订阅地址：**

```text
https://raw.githubusercontent.com/atsrxL/alt-repo/main/source.json
```

[一键添加到 AltStore](altstore://source?url=https%3A%2F%2Fraw.githubusercontent.com%2FatsrxL%2Falt-repo%2Fmain%2Fsource.json)

## 应用清单

| 应用 | 整理时版本 | 最低系统 | 用途 | 原分发仓库 |
| --- | --- | --- | --- | --- |
| Scatter | 0.8.0 | iOS 17 | 加密剪贴板与文件同步 | [scatter-altstore](https://github.com/atsrxL/scatter-altstore) |
| SendIt | 1.0.1 | iOS 16 | 分享上传到 SMB / WebDAV NAS | [sendit](https://github.com/atsrxL/sendit) |
| F50 Manager | 0.1.0 | iOS 17 | F50 蓝牙管理 | [F50Manager-iOS](https://github.com/atsrxL/F50Manager-iOS) |
| 映流 FlowStream | 0.9.2 | iOS 16 | SMB / WebDAV 视频播放器 | [FlowStream](https://github.com/atsrxL/FlowStream) |
| Pi VNC | 0.1.2 | iPadOS 18（仅 iPad） | 原生 PiKVM 远程控制 | 源码私有；IPA 在本仓库 [Releases](https://github.com/atsrxL/alt-repo/releases?q=pi-vnc) |

Pi VNC 源码仓库为私有，其元数据保存在 `apps/pi-vnc/app.json`，IPA 发布在本仓库 Release；更新时修改该文件并上传新 IPA。

## 安装与版本

以上 IPA 需要使用自己的签名方式安装；此源适用于 AltStore Classic，不是 AltStore PAL 公证源。保留原项目版本记录、权限、截图和下载地址。F50 Manager 发布包为原有 0.1.0，不代表私有开发分支的后续更新。

此仓库汇总公开分发信息，源码仍在各自项目维护。已有项目源和下载链接继续有效。

## 更新

GitHub Actions 每天自动同步四个公开上游并合并 `apps/*/app.json`，也可在 Actions → Sync public app sources → Run workflow 手动同步。任一上游读取失败时不会覆盖现有源。

本地更新（Python 标准库，无需编译应用）：

```sh
python3 scripts/sync.py
```

最新版本以 [source.json](source.json) 为准。
