# 自定义节点文件夹

这个文件夹用于存放用户自定义的节点。

## 如何创建自定义节点

1. 在此文件夹中创建一个新的 `.py` 文件
2. 导入必要的模块：
```python
from core.base_node import BaseNode, Socket, SocketType, SocketDirection
```

3. 创建一个继承自 `BaseNode` 的类：
```python
class MyCustomNode(BaseNode):
    """我的自定义节点"""
    
    def __init__(self):
        super().__init__()
        self.title = "我的节点"
        self.description = "节点描述"
        
        # 可选：添加文本输入控件
        self.add_text_input("参数", "", "参数")
        
        # 添加输入输出端口
        self.add_input("输入1", SocketType.ANY)
        self.add_output("输出1", SocketType.ANY)
    
    def execute(self, inputs):
        """执行节点逻辑
        
        Args:
            inputs: 输入数据字典，键为输入端口名称
            
        Returns:
            输出数据字典，键为输出端口名称
        """
        input_value = inputs.get("输入1")
        # 处理逻辑...
        result = input_value
        return {"输出1": result}
```

4. 保存文件后重启应用程序，新节点将自动出现在"📦 自定义节点"分类中

## 示例

参考 `example_custom_node.py` 文件了解更多详情。

