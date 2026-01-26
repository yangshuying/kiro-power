---
name: "ui-design-standards"
displayName: "UI 设计规范"
description: "基于 Element Plus 的 UI 设计规范，包含色彩、字体、边框、图标、按钮、表格、输入框等完整设计标准，用于指导前端 UI 开发"
keywords: ["ui", "design", "element-plus", "vue", "设计规范", "design-system"]
author: "Design Team"
---

# UI 设计规范

## Overview

这是一套完整的 UI 设计规范，基于 Element Plus 组件库，为产品提供一致的视觉体验。

当你收到产品需求文档时，请参考本规范进行 UI 设计和前端开发，确保：
- 色彩使用符合品牌规范
- 字体、字号、字重正确
- 组件样式统一
- 交互方式一致

---

## 一、色彩规范

避免视觉传达差异,使用一套特定的调色板来规定颜色,为产品提供一致的外观视觉感受

### 1. 主色

主要品牌色

- **主色**: `#2978FF` - 蓝色

### 2. 辅助色

主色外的场景色

- **辅助色-01**: `#28C840` - 绿色
- **辅助色-02**: `#FFBC2E` - 黄色  
- **辅助色-03**: `#FF5F57` - 红色
- **辅助色-04**: `#909399` - 灰色
- **辅助色-05**: `#61D3FF` - 浅蓝色
- **辅助色-06**: `#FF7903` - 橙色
- **辅助色-07**: `#6B71E5` - 紫色
- **辅助色-08**: `#CCCCCC` - 浅灰色

### 3. 中性色

用于文本、背景和边框颜色

#### (1) 文字颜色

- **主要文字**: `#303033` - 深灰色 (用于标题和重要内容)
- **常规文字**: `#606066` - 中灰色 (用于正文和常规内容)
- **次要文字**: `#909099` - 浅灰色 (用于辅助和说明文字)

#### (2) 边框颜色

- **其他文字**: `#C0C1CC` - 浅灰色
- **一级边框**: `#DDDFE6` - 浅灰色边框
- **二级边框**: `#E5E7EE` - 更浅的灰色边框
- **三级边框**: `#ECEEF5` - 极浅的灰色边框

#### (3) 其他颜色

- **四级边框**: `#F7F7FA` - 接近白色的背景色
- **基础黑色**: `#000000` - 纯黑色
- **基础白色**: `#FFFFFF` - 纯白色
- **透明色**: `Transparent` - 透明

---

## 二、字体规范

对字体进行统一规范,包括字体字号字重,各种使用场景的规范

### 1. 字体

统一整个系统的字体,正常情况下均使用**苹方字体**(Ping Fang SC),特殊情况特殊标注

#### 字重类型

| 中文名称 | 英文名称 | 用途说明 |
|---------|---------|---------|
| 常规 | Regular | 正文、辅助文字等常规内容 |
| 中等 | Medium | 小标题、需要强调的内容 |
| 粗体 | Bold | 大标题、重要强调内容 |

### 2. 字号

统一整个系统的字号使用,避免字号大小混乱主次不分,导致的页面混乱

**注意**: 字重变换可以增加层级感

| 使用场景 | 字体大小 | 参考效果 |
|---------|---------|---------|
| 辅助文字 | 12px / Extra Small | 这是最小的辅助备注文字 |
| 正文 | 14px / Regular | 这是常规使用的正文文字 |
| 小标题 | 16px / Medium | 这是小的类别标题文字 |
| 大标题 | 18px / Large | 这是大的区块标题文字 |

### 3. 下划线

统一整个系统的下划线类型

| 使用场景 | 下划线粗细 | 说明 |
|---------|-----------|------|
| 实线下划线/表格线/框线 | 1px | 实线样式 |
| 虚线下划线/表格线/框线 | 2px | 虚线样式 |

---

## 三、边框规范

对边框进行统一规范,包括圆角、阴影、描边、底色,规范各种类型的使用场景

### 1. 边框

统一整个系统的边框类型

| 使用场景 | 下划线粗细 | 说明 |
|---------|-----------|------|
| 实线下划线/表格线/框线 | 1px | 实线样式 |
| 虚线下划线/表格线/框线 | 2px | 虚线样式 |

### 2. 圆角

统一整个系统圆角类型,分情况取值使用

| 使用场景 | 圆角数值 | 说明 |
|---------|---------|------|
| -- | 无圆角 - 0px | 直角矩形 |
| 按钮/输入框圆角 | 小圆角 - 6px | 常规组件圆角 |
| 弹窗/卡片/分区 | 大圆角 - 8px | 容器类圆角 |
| 椭圆按钮/圆形圆角 | 圆形圆角 - 取值根据图形 | 胶囊形/圆形 |

### 3. 投影

按重要程度给予两种类型的投影参数,分情况取值使用

| 使用场景 | 投影参数 | CSS box-shadow |
|---------|---------|----------------|
| 卡片/弹窗 | X:0 / Y:1 / 模糊:6 / 扩展:1 / 颜色:#000000-15% | `0 1px 6px 1px rgba(0,0,0,0.15)` |
| 表单衍生二级菜单 | X:0 / Y:0 / 模糊:6 / 扩展:0 / 颜色:#000000-15% | `0 0 6px 0 rgba(0,0,0,0.15)` |

---

## 四、图标规范

对常用的图标进行统一规范

### 1. 图标库

系统统一使用 **Element Plus Icons** 图标库

#### 安装方式

```bash
# npm
npm install @element-plus/icons-vue

# yarn
yarn add @element-plus/icons-vue

# pnpm
pnpm add @element-plus/icons-vue
```

#### 全局注册

```javascript
// main.js / main.ts
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

const app = createApp(App)
// 注册所有图标
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}
```

### 2. 基础图标

总结了所有的线性通用图标,并且区分了同一图标不同的大小

#### 图标尺寸规范

系统提供三种标准图标尺寸：14px、16px、24px

| 名称 | 图标名称 | 使用示例 | 说明 |
|-----|---------|---------|------|
| 复制 | `CopyDocument` | `<el-icon><CopyDocument /></el-icon>` | 复制内容操作 |
| 删除 | `Delete` | `<el-icon><Delete /></el-icon>` | 删除内容操作 |
| 链接 | `Link` | `<el-icon><Link /></el-icon>` | 链接/超链接 |
| 导入 | `Download` | `<el-icon><Download /></el-icon>` | 数据导入 |
| 导出 | `Upload` | `<el-icon><Upload /></el-icon>` | 数据导出 |
| 添加 | `Plus` | `<el-icon><Plus /></el-icon>` | 增加操作 |
| 减少 | `Minus` | `<el-icon><Minus /></el-icon>` | 减少操作 |
| 展开 | `Expand` | `<el-icon><Expand /></el-icon>` | 列表展开 |
| 收起 | `Fold` | `<el-icon><Fold /></el-icon>` | 列表收起 |
| 日历 | `Calendar` | `<el-icon><Calendar /></el-icon>` | 日期选择 |
| 新增一行 | `CirclePlus` | `<el-icon><CirclePlus /></el-icon>` | 表格新增行 |
| 减少一行 | `Remove` | `<el-icon><Remove /></el-icon>` | 表格删除行 |
| 多选-选中 | `Select` | `<el-icon><Select /></el-icon>` | 复选框选中状态 |
| 多选-未选中 | -- | `<el-checkbox />` | 复选框未选中（组件自带） |
| 多选-部分选中 | `SemiSelect` | `<el-icon><SemiSelect /></el-icon>` | 复选框部分选中 |
| 单选-选中 | -- | `<el-radio />` | 单选框选中（组件自带） |
| 单选-未选中 | -- | `<el-radio />` | 单选框未选中（组件自带） |
| 查看 | `View` | `<el-icon><View /></el-icon>` | 显示内容 |
| 隐藏 | `Hide` | `<el-icon><Hide /></el-icon>` | 隐藏内容 |
| 注释-线性 | `ChatRound` | `<el-icon><ChatRound /></el-icon>` | 注释说明（线性） |
| 注释-面性 | `QuestionFilled` | `<el-icon><QuestionFilled /></el-icon>` | 注释说明（面性） |
| 提示-线性 | `Warning` | `<el-icon><Warning /></el-icon>` | 提示信息（线性） |
| 提示-面性 | `WarningFilled` | `<el-icon><WarningFilled /></el-icon>` | 提示信息（面性） |
| 搜索 | `Search` | `<el-icon><Search /></el-icon>` | 搜索功能 |
| 退出/关闭 | `Close` | `<el-icon><Close /></el-icon>` | 关闭/退出 |
| 编辑 | `Edit` | `<el-icon><Edit /></el-icon>` | 编辑操作 |
| 更多 | `More` | `<el-icon><More /></el-icon>` | 更多操作菜单（横向三点） |

#### 方向图标

| 类型 | 上 | 下 | 左 | 右 |
|-----|---|---|---|---|
| 线性 | `ArrowUp` | `ArrowDown` | `ArrowLeft` | `ArrowRight` |
| 面性 | `CaretTop` | `CaretBottom` | `CaretLeft` | `CaretRight` |

#### 图标尺寸设置

```vue
<!-- 通过 size 属性设置尺寸 -->
<el-icon :size="14"><Delete /></el-icon>  <!-- 14px -->
<el-icon :size="16"><Delete /></el-icon>  <!-- 16px -->
<el-icon :size="24"><Delete /></el-icon>  <!-- 24px -->

<!-- 或通过 CSS 设置 -->
<el-icon style="font-size: 14px;"><Delete /></el-icon>
```

#### 图标颜色设置

```vue
<!-- 通过 color 属性设置颜色 -->
<el-icon color="#2978FF"><Edit /></el-icon>

<!-- 继承父元素颜色 -->
<span style="color: #2978FF;">
  <el-icon><Edit /></el-icon>
</span>
```

#### 图标使用建议

- **14px**: 适用于紧凑型布局、表格内操作按钮
- **16px**: 适用于常规按钮、输入框内图标
- **24px**: 适用于导航栏、工具栏、独立操作按钮

---

## 五、按钮规范

对常用的操作按钮进行统一,包括颜色、圆角、描边及使用场景的统一

### 1. 基础用法

整个系统按钮会出现的基础情况

#### 按钮尺寸

| 尺寸 | 高度 | 圆角 | 使用场景 |
|-----|-----|-----|---------|
| 大按钮 | 40px | 6px | 登录页/弹窗按钮 |
| 中按钮 | 32px | 4px | 主要按钮（默认） |
| 小按钮 | 24px | 16px | 小按钮/特殊圆角按钮 |

#### 按钮类型

| 类型 | 说明 | Element Plus 属性 |
|-----|------|------------------|
| 主要按钮 | 蓝色填充，白色文字 | `type="primary"` |
| 成功按钮 | 绿色填充，白色文字 | `type="success"` |
| 警告按钮 | 黄色填充，白色文字 | `type="warning"` |
| 危险按钮 | 红色填充，白色文字 | `type="danger"` |
| 信息按钮 | 灰色填充，白色文字 | `type="info"` |
| 浅蓝按钮 | 浅蓝色填充 | 自定义样式 |
| 橙色按钮 | 橙色填充 | 自定义样式 |
| 紫色按钮 | 紫色填充 | 自定义样式 |

#### 按钮状态

| 状态 | 说明 | 示例 |
|-----|------|-----|
| 默认状态 | 正常显示 | 填充色按钮 |
| 朴素状态 | 白底+边框+文字颜色 | `plain` 属性 |
| 禁用状态 | 降低透明度，不可点击 | `disabled` 属性 |

#### 特殊按钮类型

| 类型 | 说明 | 示例代码 |
|-----|------|---------|
| 带图标按钮 | 图标+文字组合 | `<el-button :icon="Plus">新建</el-button>` |
| 图标文字按钮 | 纯图标+文字，无边框 | `<el-button type="primary" text :icon="Edit">编辑</el-button>` |
| 下划线按钮 | 文字带下划线 | 自定义样式 |
| 纯文字按钮 | 仅文字，无边框无背景 | `<el-button type="primary" text>主要按钮</el-button>` |

#### 代码示例

```vue
<!-- 尺寸 -->
<el-button type="primary" size="large">大按钮 40px</el-button>
<el-button type="primary">中按钮 32px</el-button>
<el-button type="primary" size="small">小按钮 24px</el-button>

<!-- 类型 -->
<el-button type="primary">主要按钮</el-button>
<el-button type="success">成功按钮</el-button>
<el-button type="warning">警告按钮</el-button>
<el-button type="danger">危险按钮</el-button>
<el-button type="info">信息按钮</el-button>

<!-- 朴素按钮 -->
<el-button type="primary" plain>主要按钮</el-button>
<el-button type="success" plain>成功按钮</el-button>

<!-- 禁用状态 -->
<el-button type="primary" disabled>主要按钮</el-button>

<!-- 带图标按钮 -->
<el-button type="primary" :icon="Plus">新建</el-button>
<el-button type="danger" :icon="Delete">删除</el-button>
<el-button type="primary" :icon="Edit">编辑</el-button>

<!-- 文字按钮 -->
<el-button type="primary" text :icon="Edit">编辑</el-button>
<el-button type="danger" text :icon="Delete">删除</el-button>
<el-button type="primary" text :icon="Link">链接</el-button>

<!-- 纯文字按钮 -->
<el-button type="primary" text>主要按钮</el-button>
```

#### 按钮颜色对照

| 按钮类型 | 背景色 | 对应色彩规范 |
|---------|-------|------------|
| 主要按钮 | `#2978FF` | 主色 |
| 成功按钮 | `#28C840` | 辅助色-01 |
| 警告按钮 | `#FFBC2E` | 辅助色-02 |
| 危险按钮 | `#FF5F57` | 辅助色-03 |
| 信息按钮 | `#909399` | 辅助色-04 |
| 浅蓝按钮 | `#61D3FF` | 辅助色-05 |
| 橙色按钮 | `#FF7903` | 辅助色-06 |
| 紫色按钮 | `#6B71E5` | 辅助色-07 |

---

## 六、表格规范

对表格的样式进行统一,包括高度及使用场景的统一

### 1. 基础用法

整个系统所有的表格会出现的基础情况

#### 表格高度

| 类型 | 行高 | 使用场景 |
|-----|-----|---------|
| 基础表格 | 40px | 常规页面表格 |
| 弹窗表格 | 36px | 弹窗内的表格（更紧凑） |

#### 表格单元格类型

| 类型 | 标题列 | 内容列 | 说明 |
|-----|-------|-------|------|
| 操作 | 操作 | 编辑 删除 ··· | 操作按钮列 |
| 序号 | 序号 | 0、1、2... | 行序号列 |
| 带标签序号 | -- | 带图标的序号 | 特殊序号展示 |
| 选择 | 全选复选框 | 行复选框 | 多选列（选中/未选中/部分选中） |
| 状态 | 状态 | 状态一、状态二 | 状态标签列 |
| 带符号-标题 | *表格标题-符号号 | 表格标题带符号 ○ | 必填标记/带图标标题 |
| 带符号-内容 | -- | 链接、限制说明等 | 带图标/链接的内容 |

#### 表格内容类型说明

| 内容类型 | 示例 | 说明 |
|---------|-----|------|
| 纯文本 | 表格标题-普通、表格内容-普通 | 普通文字内容 |
| 操作按钮 | 编辑、删除、更多(···) | 行操作按钮组 |
| 序号 | 0、1、2、3... | 自动递增序号 |
| 复选框 | ☑ ☐ | 多选操作 |
| 状态标签 | 状态一、状态二 | 不同颜色的状态标签 |
| 链接文本 | 表格内容为点击链接 | 可点击的链接文字 |
| 带图标文本 | 🔗 表格内容左侧加符号 | 左侧或右侧带图标 |
| 限制说明 | 表格最大字数限制为16位... | 带省略号的长文本 |

#### 代码示例

```vue
<!-- 基础表格 -->
<el-table :data="tableData" style="width: 100%">
  <!-- 选择列 -->
  <el-table-column type="selection" width="55" />
  
  <!-- 序号列 -->
  <el-table-column type="index" label="序号" width="60" />
  
  <!-- 普通列 -->
  <el-table-column prop="name" label="表格标题-普通" />
  <el-table-column prop="content" label="表格内容-普通" />
  
  <!-- 状态列 -->
  <el-table-column prop="status" label="状态">
    <template #default="{ row }">
      <el-tag :type="row.statusType">{{ row.status }}</el-tag>
    </template>
  </el-table-column>
  
  <!-- 操作列 -->
  <el-table-column label="操作" width="180">
    <template #default>
      <el-button type="primary" text :icon="Edit">编辑</el-button>
      <el-button type="danger" text :icon="Delete">删除</el-button>
      <el-button type="info" text :icon="More">···</el-button>
    </template>
  </el-table-column>
</el-table>

<!-- 弹窗表格（更紧凑） -->
<el-table :data="tableData" size="small">
  <!-- 列配置同上 -->
</el-table>
```

#### 表格样式配置

```css
/* 基础表格行高 40px */
.el-table {
  --el-table-row-height: 40px;
}

/* 弹窗表格行高 36px */
.dialog-table .el-table {
  --el-table-row-height: 36px;
}
```

### 2. 组合用法

各种类型的基础表格放在一起组合的表格示例

#### (1) 基础表格

表格示例

| ☐ | 序号 | 表格标题-普通 | 表格标题带符号 | *表格标题-带星号 | 表格标题-普通 | 表格标题-普通 | 表格标题-普通 | 状态 | 操作 |
|---|-----|------------|-------------|---------------|------------|------------|------------|------|------|
| ☑ | 1 | 表格内容-普通 | 表格内容-普通 | 表格内容-普通 | 表格内容左侧加符号 🔗 | 表格内容左侧加符号 🔗 | 表格最大字数限制为16位... | 状态一 | 编辑 删除 |
| ☐ | 2 | 表格内容-普通 | 表格内容-普通 | 表格内容-普通 | 表格内容左侧加符号 🔗 | 表格内容左侧加符号 🔗 | 表格最大字数限制为16位... | 状态二 | 编辑 删除 |

```vue
<template>
  <el-table :data="tableData" style="width: 100%">
    <!-- 选择列 -->
    <el-table-column type="selection" width="55" />
    
    <!-- 序号列 -->
    <el-table-column type="index" label="序号" width="60" />
    
    <!-- 普通文本列 -->
    <el-table-column prop="col1" label="表格标题-普通" />
    <el-table-column prop="col2" label="表格标题带符号" />
    
    <!-- 带星号必填标题列 -->
    <el-table-column prop="col3">
      <template #header>
        <span class="required">*</span>表格标题-带星号
      </template>
    </el-table-column>
    
    <!-- 带链接图标列 -->
    <el-table-column prop="col4" label="表格标题-普通">
      <template #default="{ row }">
        <el-icon><Link /></el-icon>
        <span>{{ row.col4 }}</span>
      </template>
    </el-table-column>
    
    <!-- 文本溢出省略列 -->
    <el-table-column 
      prop="col5" 
      label="表格标题-普通" 
      show-overflow-tooltip 
    />
    
    <!-- 状态列 -->
    <el-table-column prop="status" label="状态" width="100">
      <template #default="{ row }">
        <el-tag :type="row.statusType">{{ row.status }}</el-tag>
      </template>
    </el-table-column>
    
    <!-- 操作列 -->
    <el-table-column label="操作" width="120" fixed="right">
      <template #default>
        <el-button type="primary" text size="small">编辑</el-button>
        <el-button type="danger" text size="small">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<style scoped>
/* 必填标记样式 */
.required {
  color: #FF5F57;
  margin-right: 4px;
}
</style>
```

#### (2) 斑马纹表格

表格示例（奇偶行交替背景色，提高可读性）

| ☐ | 序号 | 表格标题-普通 | 表格标题带符号 | *表格标题-带星号 | 表格标题-普通 | 表格标题-普通 | 表格标题-普通 | 状态 | 操作 |
|---|-----|------------|-------------|---------------|------------|------------|------------|------|------|
| ☑ | 1 | 表格内容-普通 | 表格内容-普通 | 表格内容-普通 | 表格内容左侧加符号 🔗 | 表格内容左侧加符号 🔗 | 表格最大字数限制为16位... | 状态一 | 编辑 删除 |
| ☐ | 2 | 表格内容-普通 | 表格内容-普通 | 表格内容-普通 | 表格内容左侧加符号 🔗 | 表格内容左侧加符号 🔗 | 表格最大字数限制为16位... | 状态二 | 编辑 删除 |

```vue
<template>
  <!-- 斑马纹表格：添加 stripe 属性 -->
  <el-table :data="tableData" stripe style="width: 100%">
    <el-table-column type="selection" width="55" />
    <el-table-column type="index" label="序号" width="60" />
    <el-table-column prop="col1" label="表格标题-普通" />
    <el-table-column prop="col2" label="表格标题带符号" />
    <el-table-column prop="col3">
      <template #header>
        <span class="required">*</span>表格标题-带星号
      </template>
    </el-table-column>
    <el-table-column prop="col4" label="表格标题-普通">
      <template #default="{ row }">
        <el-icon><Link /></el-icon>
        <span>{{ row.col4 }}</span>
      </template>
    </el-table-column>
    <el-table-column prop="col5" label="表格标题-普通" show-overflow-tooltip />
    <el-table-column prop="status" label="状态" width="100">
      <template #default="{ row }">
        <el-tag :type="row.statusType">{{ row.status }}</el-tag>
      </template>
    </el-table-column>
    <el-table-column label="操作" width="120" fixed="right">
      <template #default>
        <el-button type="primary" text size="small">编辑</el-button>
        <el-button type="danger" text size="small">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>
```

**关键属性**: `stripe` - 添加此属性即可实现斑马纹效果，偶数行会显示浅灰色背景（`#FAFAFA`）

#### (3) 带边框表格

表格示例（带完整边框线，适用于需要清晰分隔的场景）

| ☐ | 序号 | 表格标题-普通 | 表格标题带符号 | *表格标题-带星号 | 表格标题-普通 | 表格标题-普通 | 表格标题-普通 | 状态 | 操作 |
|---|-----|------------|-------------|---------------|------------|------------|------------|------|------|
| ☑ | 1 | 表格内容-普通 | 表格内容-普通 | 表格内容-普通 | 表格内容左侧加符号 🔗 | 表格内容左侧加符号 🔗 | 表格最大字数限制为16位... | 状态一 | 编辑 删除 |
| ☐ | 2 | 表格内容-普通 | 表格内容-普通 | 表格内容-普通 | 表格内容左侧加符号 🔗 | 表格内容左侧加符号 🔗 | 表格最大字数限制为16位... | 状态二 | 编辑 删除 |

```vue
<template>
  <!-- 带边框表格：添加 border 属性 -->
  <el-table :data="tableData" border style="width: 100%">
    <el-table-column type="selection" width="55" />
    <el-table-column type="index" label="序号" width="60" />
    <el-table-column prop="col1" label="表格标题-普通" />
    <el-table-column prop="col2" label="表格标题带符号" />
    <el-table-column prop="col3">
      <template #header>
        <span class="required">*</span>表格标题-带星号
      </template>
    </el-table-column>
    <el-table-column prop="col4" label="表格标题-普通">
      <template #default="{ row }">
        <el-icon><Link /></el-icon>
        <span>{{ row.col4 }}</span>
      </template>
    </el-table-column>
    <el-table-column prop="col5" label="表格标题-普通" show-overflow-tooltip />
    <el-table-column prop="status" label="状态" width="100">
      <template #default="{ row }">
        <el-tag :type="row.statusType">{{ row.status }}</el-tag>
      </template>
    </el-table-column>
    <el-table-column label="操作" width="120" fixed="right">
      <template #default>
        <el-button type="primary" text size="small">编辑</el-button>
        <el-button type="danger" text size="small">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>
```

**关键属性**: `border` - 添加此属性即可显示纵向边框线，边框颜色使用一级边框色（`#DDDFE6`）

---

## 七、输入框规范

对输入框的样式进行统一,包括高度及使用场景的统一

### 1. 基础用法

整个系统所有的输入框会出现的基础情况

#### 输入框高度

| 类型 | 高度 | 使用场景 |
|-----|-----|---------|
| 基础输入框 | 32px | 常规表单输入（默认） |
| 次级输入框 | 28px | 表格内、紧凑布局 |

#### 输入框类型

| 类型 | 说明 | 组件 |
|-----|------|-----|
| 搜索 | 带搜索图标的输入框 | `el-input` + `suffix-icon` |
| 筛选搜索 | 带下拉筛选条件的搜索框 | `el-input` + `el-select` 组合 |
| 下拉筛选 | 下拉选择框 | `el-select` |
| 时间/日期选择 | 日期范围选择器 | `el-date-picker` |
| 输入框 | 普通文本输入框 | `el-input` |

#### 输入框状态

| 状态 | 说明 |
|-----|------|
| 默认状态 | 正常可输入 |
| 禁用状态 | 灰色背景，不可编辑（已经输入内容禁用状态） |
| 占位符 | 浅灰色提示文字（请输入、请选择等） |

#### 代码示例

```vue
<template>
  <!-- 搜索输入框 -->
  <el-input 
    v-model="searchValue" 
    placeholder="请搜索"
    :suffix-icon="Search"
  />

  <!-- 筛选搜索（下拉+输入组合） -->
  <el-input v-model="filterSearch" placeholder="请输入内容">
    <template #prepend>
      <el-select v-model="filterType" placeholder="工单编号" style="width: 115px">
        <el-option label="工单编号" value="orderNo" />
        <el-option label="工单名称" value="orderName" />
      </el-select>
    </template>
    <template #suffix>
      <el-icon><Search /></el-icon>
    </template>
  </el-input>

  <!-- 下拉筛选 -->
  <el-select v-model="selectValue" placeholder="请选择">
    <el-option label="选项一" value="1" />
    <el-option label="选项二" value="2" />
  </el-select>

  <!-- 时间/日期选择 -->
  <el-date-picker
    v-model="dateRange"
    type="daterange"
    range-separator="—"
    start-placeholder="请选择"
    end-placeholder="请选择"
  />

  <!-- 普通输入框 -->
  <el-input v-model="inputValue" placeholder="请输入" />

  <!-- 禁用状态输入框 -->
  <el-input v-model="disabledValue" disabled placeholder="已经输入内容禁用状态" />
</template>
```

#### 输入框尺寸配置

```vue
<!-- 基础输入框 32px（默认） -->
<el-input v-model="value" />

<!-- 次级输入框 28px -->
<el-input v-model="value" size="small" />
```

#### 样式配置

```css
/* 基础输入框高度 32px */
.el-input {
  --el-input-height: 32px;
}

/* 次级输入框高度 28px */
.el-input--small {
  --el-input-height: 28px;
}
```

---

## 附录A: 色彩速查表

### 主色系

| 颜色名称 | 色值 | RGB | 用途说明 |
|---------|------|-----|---------|
| 主色 | #2978FF | rgb(41, 120, 255) | 主要品牌色,用于主要按钮、链接等 |

### 辅助色系

| 颜色名称 | 色值 | RGB | 用途说明 |
|---------|------|-----|---------|
| 辅助色-01 | #28C840 | rgb(40, 200, 64) | 成功状态、确认操作 |
| 辅助色-02 | #FFBC2E | rgb(255, 188, 46) | 警告提示、重要信息 |
| 辅助色-03 | #FF5F57 | rgb(255, 95, 87) | 错误状态、危险操作 |
| 辅助色-04 | #909399 | rgb(144, 147, 153) | 禁用状态、次要信息 |
| 辅助色-05 | #61D3FF | rgb(97, 211, 255) | 信息提示、链接辅助 |
| 辅助色-06 | #FF7903 | rgb(255, 121, 3) | 强调、活动状态 |
| 辅助色-07 | #6B71E5 | rgb(107, 113, 229) | 特殊功能、高级选项 |
| 辅助色-08 | #CCCCCC | rgb(204, 204, 204) | 分隔线、背景 |

### 文字色系

| 颜色名称 | 色值 | RGB | 用途说明 |
|---------|------|-----|---------|
| 主要文字 | #303033 | rgb(48, 48, 51) | 标题、重要内容 |
| 常规文字 | #606066 | rgb(96, 96, 102) | 正文、常规内容 |
| 次要文字 | #909099 | rgb(144, 144, 153) | 辅助说明、提示文字 |

### 边框色系

| 颜色名称 | 色值 | RGB | 用途说明 |
|---------|------|-----|---------|
| 其他文字 | #C0C1CC | rgb(192, 193, 204) | 占位符文字 |
| 一级边框 | #DDDFE6 | rgb(221, 223, 230) | 主要边框 |
| 二级边框 | #E5E7EE | rgb(229, 231, 238) | 次要边框 |
| 三级边框 | #ECEEF5 | rgb(236, 238, 245) | 辅助边框 |
| 四级边框 | #F7F7FA | rgb(247, 247, 250) | 背景边框 |

### 基础色系

| 颜色名称 | 色值 | RGB | 用途说明 |
|---------|------|-----|---------|
| 基础黑色 | #000000 | rgb(0, 0, 0) | 纯黑色 |
| 基础白色 | #FFFFFF | rgb(255, 255, 255) | 纯白色 |
| 透明色 | Transparent | - | 透明背景 |

---

## 附录B: 设计原则

### 1. 一致性原则

- 保持整个系统的视觉一致性
- 统一使用规定的色彩、字体、间距
- 相同功能使用相同的交互方式

### 2. 层级原则

- 通过颜色深浅区分信息层级
- 主要文字 > 常规文字 > 次要文字
- 通过字重变化增强层级感

### 3. 可读性原则

- 确保文字与背景有足够的对比度
- 合理使用字号和行高
- 避免过长的文本行

### 4. 可访问性原则

- 色彩搭配考虑色盲用户
- 不仅依靠颜色传达信息
- 提供足够的点击/触摸区域

---

## 附录C: 使用建议

### 色彩使用建议

1. **主色使用**
   - 主要操作按钮
   - 重要链接
   - 选中状态
   - 进度指示

2. **辅助色使用**
   - 成功: 使用辅助色-01 (绿色)
   - 警告: 使用辅助色-02 (黄色)
   - 错误: 使用辅助色-03 (红色)
   - 信息: 使用辅助色-05 (浅蓝色)

3. **中性色使用**
   - 文字内容按重要程度选择对应的文字色
   - 边框按层级选择对应的边框色
   - 背景使用四级边框色或白色

### 字体使用建议

1. 统一使用苹方字体
2. 根据内容重要性调整字号和字重
3. 保持合适的行高,提升可读性

---

## 版本信息

- **文档版本**: 1.0 基础版
- **创建日期**: 2026-01-22
- **文档说明**: 本文档包含完整的 UI 设计规范，基于 Element Plus 组件库
- **使用说明**: 当收到产品需求文档时，请参考本规范进行 UI 设计和前端开发

---

> **注意事项**:
> 1. 本规范为基础版本,后续可能会有更新和补充
> 2. 在实际应用中,如遇特殊情况需要调整,请与设计团队沟通
> 3. 建议配合设计工具(如 Figma、Sketch)中的完整设计系统使用
> 4. 所有颜色值均为十六进制格式,可直接用于前端开发
