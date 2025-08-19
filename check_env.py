import sys
import os

print("=== TeachOpenCADD 环境验证 ===")
print()

print("当前Python解释器路径:")
print(sys.executable)
print()

print("当前conda环境:")
conda_env = os.environ.get('CONDA_DEFAULT_ENV', '未设置')
print(f"CONDA_DEFAULT_ENV: {conda_env}")
print()

print("Python版本:")
print(f"Python {sys.version}")
print()

# 测试关键包
packages_status = {}

test_packages = [
    ('pandas', 'pd'),
    ('numpy', 'np'),
    ('matplotlib', 'plt'),
    ('rdkit.Chem', 'Chem'),
    ('sklearn', 'sklearn'),
    ('jupyter', 'jupyter'),
    ('nglview', 'nglview')
]

print("包导入测试:")
for package, alias in test_packages:
    try:
        if alias and alias != package:
            exec(f"import {package} as {alias}")
        else:
            exec(f"import {package}")
        print(f"✅ {package}")
        packages_status[package] = True
    except ImportError as e:
        print(f"❌ {package}: {str(e)[:50]}...")
        packages_status[package] = False

print()
print("=== 环境状态总结 ===")
if conda_env == 'teachopencadd':
    print("✅ 正在使用teachopencadd环境")
else:
    print(f"⚠️  当前环境: {conda_env}")

if packages_status.get('rdkit.Chem', False):
    print("✅ RDKit可用 - 可以进行化学信息学计算")
else:
    print("❌ RDKit不可用")

if packages_status.get('pandas', False) and packages_status.get('numpy', False):
    print("✅ 数据处理包可用")
else:
    print("❌ 数据处理包有问题")

if packages_status.get('jupyter', False):
    print("✅ Jupyter可用")
else:
    print("❌ Jupyter不可用")

print()
print("准备状态:", "🎉 可以开始TeachOpenCADD!" if all([
    conda_env == 'teachopencadd',
    packages_status.get('rdkit.Chem', False),
    packages_status.get('pandas', False),
    packages_status.get('jupyter', False)
]) else "⚠️  需要进一步配置")
