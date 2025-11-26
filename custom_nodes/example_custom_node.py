"""
示例自定义节点
这个文件展示了如何创建自定义节点
"""
from core.base_node import BaseNode, SocketType


class ExampleCustomNode(BaseNode):
    """示例：文本转大写节点"""
    
    def __init__(self):
        super().__init__()
        self.title = "文本转大写"
        self.description = "将输入文本转换为大写，并可添加前缀"
        
        # 添加文本输入控件
        self.add_text_input("前缀", "", "前缀")
        
        # 添加输入输出端口
        self.add_input("文本", SocketType.STRING)
        self.add_output("结果", SocketType.STRING)
    
    def execute(self, inputs):
        """执行节点逻辑"""
        input_text = inputs.get("文本", "")
        prefix = getattr(self, "前缀", "")
        
        # 转换为大写并添加前缀
        result = str(prefix) + str(input_text).upper()
        
        print(f"[文本转大写] 输入: {input_text}, 前缀: {prefix}, 结果: {result}")
        return {"结果": result}


class ExampleMathNode(BaseNode):
    """示例：数值求平方节点"""
    
    def __init__(self):
        super().__init__()
        self.title = "数值求平方"
        self.description = "计算输入数值的平方"
        
        # 添加输入输出端口
        self.add_input("数值", SocketType.NUMBER)
        self.add_output("平方", SocketType.NUMBER)
    
    def execute(self, inputs):
        """执行节点逻辑"""
        value = inputs.get("数值", 0)
        
        try:
            result = float(value) ** 2
            print(f"[数值求平方] 输入: {value}, 结果: {result}")
            return {"平方": result}
        except (ValueError, TypeError):
            print(f"[数值求平方] 错误: 无法将 {value} 转换为数字")
            return {"平方": 0}

