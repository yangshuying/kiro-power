---
name: "s3-file-uploader"
displayName: "S3 File Uploader"
description: "使用 upload_to_s3.py 脚本快速上传文件和目录到 AWS S3 存储桶，支持单文件和批量上传"
keywords: ["s3", "upload", "aws", "file", "storage", "boto3"]
author: "shyyang"
---

# S3 File Uploader

## Overview

S3 File Uploader 是一个简单易用的 Python CLI 工具，用于将本地文件快速上传到 AWS S3 存储桶。它支持单文件上传、批量目录上传，并提供详细的上传进度和错误提示。

**主要功能：**
- ✅ 上传单个文件到 S3
- ✅ 批量上传整个目录
- ✅ 自定义 S3 路径和前缀
- ✅ 详细的上传进度提示
- ✅ 完善的错误处理

**适用场景：**
- 快速上传项目文件到 S3
- 批量备份本地文件
- 部署静态资源到 S3
- 自动化文件同步工作流

## Onboarding

### Prerequisites

在使用此工具之前，你需要：

1. **Python 3.6+** - 确保已安装 Python 3
2. **AWS 账户** - 需要有效的 AWS 账户
3. **S3 存储桶** - 已创建的 S3 存储桶
4. **AWS 凭证** - 有 S3 上传权限的访问密钥

### Installation

#### 1. 安装 boto3 依赖

```bash
pip install boto3
```

#### 2. 配置 AWS 凭证

**方法 1: 使用 AWS CLI（推荐）**

```bash
# 安装 AWS CLI
pip install awscli

# 配置凭证
aws configure
```

输入以下信息：
- AWS Access Key ID: 你的访问密钥 ID
- AWS Secret Access Key: 你的秘密访问密钥
- Default region name: 例如 `us-east-1`
- Default output format: 直接回车（使用默认）

**方法 2: 环境变量**

```bash
export AWS_ACCESS_KEY_ID='your_access_key'
export AWS_SECRET_ACCESS_KEY='your_secret_key'
export AWS_DEFAULT_REGION='us-east-1'
```

**方法 3: 在脚本中配置（不推荐用于生产环境）**

直接修改 `upload_to_s3.py` 中的配置参数。

#### 3. 配置存储桶信息

编辑 `upload_to_s3.py` 文件，修改以下参数：

```python
BUCKET_NAME = 'your-bucket-name'  # 你的 S3 存储桶名称
REGION = 'us-east-1'  # 你的 AWS 区域
```

### Verification

验证工具是否正常工作：

```bash
# 查看帮助信息
python3 upload_to_s3.py

# 预期输出：
# 使用方法:
#   上传文件: python upload_to_s3.py <本地文件路径> [S3路径]
#   上传目录: python upload_to_s3.py -d <本地目录路径> [S3前缀]
```

## Common Workflows

### Workflow 1: 上传单个文件

**场景：** 上传一个文件到 S3 存储桶

**命令：**

```bash
# 上传到存储桶根目录（使用原文件名）
python3 upload_to_s3.py example.txt

# 上传到指定路径
python3 upload_to_s3.py local/file.txt remote/path/file.txt
```

**示例：**

```bash
# 上传图片到 images 目录
python3 upload_to_s3.py photo.jpg images/photo.jpg

# 输出：
# 正在上传: photo.jpg -> s3://your-bucket/images/photo.jpg
# ✓ 上传成功: images/photo.jpg
```

### Workflow 2: 批量上传目录

**场景：** 上传整个目录及其所有子文件到 S3

**命令：**

```bash
# 上传目录到存储桶根目录
python3 upload_to_s3.py -d local_folder

# 上传目录到指定前缀路径
python3 upload_to_s3.py -d local_folder remote_folder
```

**示例：**

```bash
# 上传 public 目录到 S3 的 assets 前缀下
python3 upload_to_s3.py -d public assets

# 输出：
# 正在上传: public/index.html -> s3://your-bucket/assets/index.html
# ✓ 上传成功: assets/index.html
# 正在上传: public/style.css -> s3://your-bucket/assets/style.css
# ✓ 上传成功: assets/style.css
# ...
# 上传完成: 成功 15 个，失败 0 个
```

### Workflow 3: 在 Python 代码中使用

**场景：** 在你的 Python 脚本中集成 S3 上传功能

**代码示例：**

```python
from upload_to_s3 import S3Uploader

# 创建上传器实例
uploader = S3Uploader('my-bucket', 'us-east-1')

# 上传单个文件
uploader.upload_file('example.txt')

# 上传到指定路径
uploader.upload_file('local/file.txt', 'remote/path/file.txt')

# 上传整个目录
uploader.upload_directory('local_folder', 'remote_folder')
```

### Workflow 4: 批量上传多个指定文件

**场景：** 上传多个不同位置的文件到不同的 S3 路径

**代码示例：**

```python
from upload_to_s3 import S3Uploader

uploader = S3Uploader('my-bucket', 'us-east-1')

# 定义文件映射：(本地路径, S3路径)
files = [
    ('file1.txt', 'uploads/file1.txt'),
    ('images/photo.jpg', 'images/photo.jpg'),
    ('docs/report.pdf', 'documents/report.pdf'),
]

# 批量上传
for local_path, s3_key in files:
    uploader.upload_file(local_path, s3_key)
```

## Command Reference

### 基本命令格式

```bash
# 上传文件
python3 upload_to_s3.py <本地文件路径> [S3路径]

# 上传目录
python3 upload_to_s3.py -d <本地目录路径> [S3前缀]
```

### 参数说明

| 参数 | 类型 | 必需 | 描述 |
|------|------|------|------|
| `<本地文件路径>` | string | 是 | 要上传的本地文件路径 |
| `[S3路径]` | string | 否 | S3 中的目标路径，不指定则使用文件名 |
| `-d` | flag | 否 | 目录上传模式标志 |
| `<本地目录路径>` | string | 是（-d模式） | 要上传的本地目录路径 |
| `[S3前缀]` | string | 否 | S3 中的前缀路径，不指定则上传到根目录 |

### 常用命令示例

```bash
# 上传单个文件到根目录
python3 upload_to_s3.py file.txt

# 上传文件到指定路径
python3 upload_to_s3.py file.txt uploads/file.txt

# 上传目录到根目录
python3 upload_to_s3.py -d my_folder

# 上传目录到指定前缀
python3 upload_to_s3.py -d my_folder backup/my_folder

# 上传当前目录的所有文件
python3 upload_to_s3.py -d . project_files
```

## Troubleshooting

### Error: "未找到 AWS 凭证"

**错误信息：**
```
错误: 未找到 AWS 凭证
请配置 AWS CLI 或设置环境变量:
  export AWS_ACCESS_KEY_ID='your_access_key'
  export AWS_SECRET_ACCESS_KEY='your_secret_key'
```

**原因：** AWS 凭证未配置或配置不正确

**解决方案：**
1. 使用 AWS CLI 配置：
   ```bash
   aws configure
   ```
2. 或设置环境变量：
   ```bash
   export AWS_ACCESS_KEY_ID='your_access_key'
   export AWS_SECRET_ACCESS_KEY='your_secret_key'
   ```
3. 验证凭证：
   ```bash
   aws s3 ls
   ```

### Error: "Access Denied"

**错误信息：**
```
✗ 上传失败: An error occurred (AccessDenied) when calling the PutObject operation: Access Denied
```

**原因：** AWS 用户没有 S3 上传权限

**解决方案：**
1. 在 AWS IAM 控制台为用户添加以下权限策略：
   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "s3:PutObject",
                   "s3:PutObjectAcl"
               ],
               "Resource": "arn:aws:s3:::your-bucket-name/*"
           }
       ]
   }
   ```
2. 或使用 AWS 托管策略：`AmazonS3FullAccess`（注意：生产环境建议使用最小权限原则）

### Error: "The specified bucket does not exist"

**错误信息：**
```
✗ 上传失败: An error occurred (NoSuchBucket) when calling the PutObject operation: The specified bucket does not exist
```

**原因：** 存储桶不存在或名称错误

**解决方案：**
1. 检查 `upload_to_s3.py` 中的 `BUCKET_NAME` 是否正确
2. 确认存储桶在指定的区域中：
   ```bash
   aws s3 ls
   ```
3. 如果存储桶不存在，创建新存储桶：
   ```bash
   aws s3 mb s3://your-bucket-name --region us-east-1
   ```

### Error: "文件不存在"

**错误信息：**
```
错误: 文件不存在 - example.txt
```

**原因：** 指定的本地文件路径不存在

**解决方案：**
1. 检查文件路径是否正确
2. 使用绝对路径或相对于当前目录的路径
3. 验证文件是否存在：
   ```bash
   ls -la example.txt
   ```

### Error: "boto3 模块未找到"

**错误信息：**
```
ModuleNotFoundError: No module named 'boto3'
```

**原因：** boto3 库未安装

**解决方案：**
```bash
pip install boto3
```

### 区域配置问题

**症状：** 上传速度慢或连接超时

**原因：** 区域配置不正确，连接到了远程区域

**解决方案：**
1. 确认存储桶所在区域：
   ```bash
   aws s3api get-bucket-location --bucket your-bucket-name
   ```
2. 修改 `upload_to_s3.py` 中的 `REGION` 参数为正确的区域
3. 或在环境变量中设置：
   ```bash
   export AWS_DEFAULT_REGION='ap-southeast-1'
   ```

## Best Practices

### 安全性

- **不要硬编码凭证**：始终使用 AWS CLI 配置或环境变量，避免在代码中硬编码访问密钥
- **使用 IAM 角色**：在 EC2 或 Lambda 中运行时，使用 IAM 角色而不是访问密钥
- **最小权限原则**：只授予必要的 S3 权限（PutObject），不要使用 FullAccess
- **定期轮换密钥**：定期更新 AWS 访问密钥

### 性能优化

- **选择正确的区域**：使用与存储桶相同的区域以获得最佳性能
- **大文件处理**：对于 >5GB 的文件，考虑使用分段上传（multipart upload）
- **并行上传**：批量上传时可以使用多线程提高速度
- **压缩文件**：对于文本文件，上传前压缩可以节省时间和成本

### 成本控制

- **选择合适的存储类**：根据访问频率选择 S3 Standard、S3-IA 或 Glacier
- **设置生命周期策略**：自动转移或删除旧文件
- **监控使用量**：定期检查 S3 使用量和费用
- **避免重复上传**：上传前检查文件是否已存在

### 文件组织

- **使用有意义的路径**：使用清晰的目录结构，如 `images/`, `documents/`, `backups/`
- **包含日期前缀**：对于备份文件，使用日期前缀如 `2024-01-25/backup.zip`
- **统一命名规范**：制定并遵循文件命名规范
- **避免特殊字符**：文件名中避免使用空格和特殊字符

### 错误处理

- **检查返回值**：在代码中使用时，检查 `upload_file()` 的返回值
- **记录日志**：保存上传日志以便追踪和调试
- **重试机制**：对于网络错误，实现自动重试逻辑
- **验证上传**：上传后验证文件是否成功存储

## Configuration

### 基本配置

在 `upload_to_s3.py` 中修改以下参数：

```python
BUCKET_NAME = 'your-bucket-name'  # 你的 S3 存储桶名称
REGION = 'us-east-1'  # AWS 区域
```

### 环境变量配置

支持以下环境变量：

- `AWS_ACCESS_KEY_ID`: AWS 访问密钥 ID
- `AWS_SECRET_ACCESS_KEY`: AWS 秘密访问密钥
- `AWS_DEFAULT_REGION`: 默认 AWS 区域

### 常用 AWS 区域

| 区域代码 | 区域名称 | 位置 |
|---------|---------|------|
| `us-east-1` | US East (N. Virginia) | 美国东部 |
| `us-west-2` | US West (Oregon) | 美国西部 |
| `ap-southeast-1` | Asia Pacific (Singapore) | 新加坡 |
| `ap-northeast-1` | Asia Pacific (Tokyo) | 东京 |
| `eu-west-1` | Europe (Ireland) | 爱尔兰 |

## Additional Resources

- **AWS S3 官方文档**: https://docs.aws.amazon.com/s3/
- **boto3 文档**: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
- **AWS CLI 文档**: https://docs.aws.amazon.com/cli/
- **S3 定价**: https://aws.amazon.com/s3/pricing/

---

**工具**: `upload_to_s3.py`
**依赖**: `boto3`
**安装**: `pip install boto3`
