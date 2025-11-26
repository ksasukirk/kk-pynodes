# 主题系统说明

## 概述

KK-PyNodes 支持完全可定制的主题系统，允许用户通过 XML 文件自定义界面的颜色和样式。

## 内置主题

系统提供以下内置主题：

1. **深色主题** (`深色主题.xml`) - 专业的深色界面，适合长时间使用
2. **亮色主题** (`亮色主题.xml`) - 清爽的亮色界面
3. **粉色主题** (`粉色主题.xml`) - 柔和的粉色+白色配色

## 如何使用主题

### 方式1：通过菜单切换
1. 启动应用程序
2. 点击菜单栏的"主题"菜单
3. 选择您想要的主题
4. 某些样式可能需要重启应用程序才能完全生效

### 方式2：在启动时设置
主题系统会自动加载 `themes` 目录下的所有 XML 主题文件，默认使用第一个找到的主题。

## 自定义主题

您可以创建自己的主题文件！

### 主题文件结构

```xml
<?xml version="1.0" encoding="UTF-8"?>
<theme name="我的主题">
    <!-- 颜色定义 -->
    <colors>
        <!-- 主色调 -->
        <window>#2D2D30</window>
        <window_text>#F1F1F1</window_text>
        <base>#1E1E1E</base>
        <highlight>#42A5F5</highlight>
        <!-- 更多颜色... -->
    </colors>
    
    <!-- 节点样式 -->
    <node>
        <background_start>#2A2A2E</background_start>
        <background_end>#252526</background_end>
        <title_bg_start>#3E3E42</title_bg_start>
        <title_bg_end>#37373D</title_bg_end>
        <title_text>#F1F1F1</title_text>
        <border_default>#3E3E42</border_default>
        <border_selected>#42A5F5</border_selected>
        <roundness>12</roundness>
    </node>
    
    <!-- Socket端口样式 -->
    <socket>
        <colors>
            <any>#FFB74D</any>
            <string>#81C784</string>
            <number>#64B5F6</number>
            <path>#BA68C8</path>
            <boolean>#E57373</boolean>
            <list>#4DD0E1</list>
            <dict>#FFF176</dict>
        </colors>
        <radius>7</radius>
    </socket>
    
    <!-- 连接线样式 -->
    <connection>
        <default>#5A5A5F</default>
        <selected>#42A5F5</selected>
        <width>3.0</width>
    </connection>
</theme>
```

### 创建自定义主题的步骤

1. 复制一个现有的主题文件（如 `深色主题.xml`）
2. 重命名文件为您的主题名称（如 `我的主题.xml`）
3. 修改 `<theme name="">` 属性为您的主题名称
4. 自定义颜色值（使用十六进制颜色代码，如 `#RRGGBB`）
5. 保存文件到 `themes` 目录
6. 重启应用程序，新主题会自动出现在主题菜单中

### 颜色参数说明

#### 全局颜色 (`<colors>`)
- `window` - 主窗口背景色
- `window_text` - 主窗口文字颜色
- `base` - 基础背景色（输入框、画布等）
- `alternate_base` - 交替背景色
- `button` - 按钮背景色
- `button_text` - 按钮文字颜色
- `highlight` - 强调色（选中、高亮等）
- `highlight_text` - 强调文字颜色
- `toolbar_bg` - 工具栏背景色
- `toolbar_border` - 工具栏边框色
- `statusbar_bg` - 状态栏背景色
- `statusbar_text` - 状态栏文字颜色
- `dock_title_bg` - Dock标题背景色
- `dock_border` - Dock边框色
- `grid_light` - 细网格颜色
- `grid_dark` - 粗网格颜色
- `menu_bg` - 菜单背景色
- `menu_text` - 菜单文字颜色
- `menu_hover` - 菜单悬停色
- `input_bg` - 输入框背景色
- `input_text` - 输入框文字颜色
- `input_border` - 输入框边框色
- `input_border_focus` - 输入框聚焦边框色
- `scrollbar_bg` - 滚动条背景色
- `scrollbar_handle` - 滚动条手柄颜色
- `scrollbar_handle_hover` - 滚动条手柄悬停色

#### 节点样式 (`<node>`)
- `background_start` - 节点背景渐变起始色
- `background_end` - 节点背景渐变结束色
- `title_bg_start` - 标题栏渐变起始色
- `title_bg_end` - 标题栏渐变结束色
- `title_text` - 标题文字颜色
- `border_default` - 默认边框颜色
- `border_selected` - 选中边框颜色
- `roundness` - 圆角半径（像素）

#### Socket端口颜色 (`<socket><colors>`)
- `any` - ANY类型端口颜色
- `string` - STRING类型端口颜色
- `number` - NUMBER类型端口颜色
- `path` - PATH类型端口颜色
- `boolean` - BOOLEAN类型端口颜色
- `list` - LIST类型端口颜色
- `dict` - DICT类型端口颜色
- `radius` - 端口半径（像素）

#### 连接线样式 (`<connection>`)
- `default` - 默认连接线颜色
- `selected` - 选中连接线颜色
- `width` - 连接线宽度

## 设计建议

### 深色主题设计
- 背景使用深灰色（#1E1E1E - #3E3E42 范围）
- 文字使用浅色（#CCCCCC - #FFFFFF 范围）
- 强调色使用明亮的蓝色、绿色等
- 保持足够的对比度以确保可读性

### 亮色主题设计
- 背景使用浅色（#F0F0F0 - #FFFFFF 范围）
- 文字使用深色（#000000 - #333333 范围）
- 强调色可以更鲜艳
- 避免使用过亮的白色，以减少眼睛疲劳

### 彩色主题设计
- 选择一个主色调（如粉色、紫色等）
- 使用该色调的不同亮度和饱和度
- 保持整体和谐统一
- 确保文字在背景上清晰可读

## 故障排除

### 主题未出现在菜单中
- 检查 XML 文件是否位于 `themes` 目录
- 确保文件扩展名为 `.xml`
- 检查 XML 语法是否正确
- 查看控制台是否有错误消息

### 主题切换后样式不正确
- 某些样式需要重启应用程序
- 检查颜色代码格式是否正确（必须是 `#RRGGBB` 格式）
- 确保所有必需的颜色参数都已定义

### 颜色显示异常
- 使用标准的 HTML 十六进制颜色代码
- 不支持颜色名称（如 "red"），必须使用 `#FF0000`
- 确保 # 号存在

## 技术细节

- 主题文件使用 XML 格式存储
- 主题在应用启动时自动加载
- 使用单例模式管理主题，全局访问
- 支持运行时切换主题（部分样式需要重启）
- 主题系统与图形渲染深度集成

## 贡献您的主题

如果您创建了精美的主题，欢迎分享！您可以：
1. 将主题文件发送给开发者
2. 在社区中分享
3. 通过 GitHub 提交 Pull Request

---

享受自定义您的 KK-PyNodes 体验！🎨

