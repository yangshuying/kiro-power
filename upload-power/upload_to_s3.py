#!/usr/bin/env python3
"""
AWS S3 文件上传工具
支持单文件和批量上传
"""

import boto3
import os
import sys
from pathlib import Path
from botocore.exceptions import ClientError, NoCredentialsError


class S3Uploader:
    """S3 文件上传器"""
    
    def __init__(self, bucket_name, region_name='us-east-1'):
        """
        初始化 S3 上传器
        
        Args:
            bucket_name: S3 存储桶名称
            region_name: AWS 区域，默认 us-east-1
        """
        self.bucket_name = bucket_name
        try:
            self.s3_client = boto3.client('s3', region_name=region_name)
        except NoCredentialsError:
            print("错误: 未找到 AWS 凭证")
            print("请配置 AWS CLI 或设置环境变量:")
            print("  export AWS_ACCESS_KEY_ID='your_access_key'")
            print("  export AWS_SECRET_ACCESS_KEY='your_secret_key'")
            sys.exit(1)
    
    def upload_file(self, local_file_path, s3_key=None):
        """
        上传单个文件到 S3
        
        Args:
            local_file_path: 本地文件路径
            s3_key: S3 中的对象键（路径），如果为 None 则使用文件名
            
        Returns:
            bool: 上传成功返回 True，失败返回 False
        """
        local_path = Path(local_file_path)
        
        if not local_path.exists():
            print(f"错误: 文件不存在 - {local_file_path}")
            return False
        
        if not local_path.is_file():
            print(f"错误: 不是文件 - {local_file_path}")
            return False
        
        # 如果未指定 S3 键，使用文件名
        if s3_key is None:
            s3_key = local_path.name
        
        try:
            print(f"正在上传: {local_file_path} -> s3://{self.bucket_name}/{s3_key}")
            
            # 上传文件
            self.s3_client.upload_file(
                str(local_path),
                self.bucket_name,
                s3_key
            )
            
            print(f"✓ 上传成功: {s3_key}")
            return True
            
        except ClientError as e:
            print(f"✗ 上传失败: {e}")
            return False
    
    def upload_directory(self, local_dir_path, s3_prefix=''):
        """
        上传整个目录到 S3
        
        Args:
            local_dir_path: 本地目录路径
            s3_prefix: S3 中的前缀路径
            
        Returns:
            tuple: (成功数量, 失败数量)
        """
        local_dir = Path(local_dir_path)
        
        if not local_dir.exists():
            print(f"错误: 目录不存在 - {local_dir_path}")
            return 0, 0
        
        if not local_dir.is_dir():
            print(f"错误: 不是目录 - {local_dir_path}")
            return 0, 0
        
        success_count = 0
        fail_count = 0
        
        # 遍历目录中的所有文件
        for file_path in local_dir.rglob('*'):
            if file_path.is_file():
                # 计算相对路径作为 S3 键
                relative_path = file_path.relative_to(local_dir)
                s3_key = os.path.join(s3_prefix, str(relative_path)).replace('\\', '/')
                
                if self.upload_file(str(file_path), s3_key):
                    success_count += 1
                else:
                    fail_count += 1
        
        print(f"\n上传完成: 成功 {success_count} 个，失败 {fail_count} 个")
        return success_count, fail_count


def main():
    """主函数 - 命令行使用示例"""
    
    # 配置参数
    BUCKET_NAME = 'dify-bucket-web'  # 修改为你的存储桶名称
    REGION = 'us-east-1'  # 修改为你的区域
    
    # 创建上传器实例
    uploader = S3Uploader(BUCKET_NAME, REGION)
    
    # 示例 1: 上传单个文件
    # uploader.upload_file('example.txt')
    
    # 示例 2: 上传文件到指定路径
    # uploader.upload_file('local/file.txt', 'remote/path/file.txt')
    
    # 示例 3: 上传整个目录
    # uploader.upload_directory('local_folder', 'remote_folder')
    
    # 命令行参数处理
    if len(sys.argv) < 2:
        print("使用方法:")
        print(f"  上传文件: python {sys.argv[0]} <本地文件路径> [S3路径]")
        print(f"  上传目录: python {sys.argv[0]} -d <本地目录路径> [S3前缀]")
        sys.exit(1)
    
    if sys.argv[1] == '-d':
        # 上传目录
        if len(sys.argv) < 3:
            print("错误: 请指定目录路径")
            sys.exit(1)
        local_path = sys.argv[2]
        s3_prefix = sys.argv[3] if len(sys.argv) > 3 else ''
        uploader.upload_directory(local_path, s3_prefix)
    else:
        # 上传文件
        local_path = sys.argv[1]
        s3_key = sys.argv[2] if len(sys.argv) > 2 else None
        uploader.upload_file(local_path, s3_key)


if __name__ == '__main__':
    main()
