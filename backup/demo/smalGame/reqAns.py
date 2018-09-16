import easygui
import sys


name = easygui.enterbox(msg='大家好，你叫什么名字?', title='游戏对话框', default='请输入')
easygui.buttonbox(msg=f'{name},你觉得自己聪明吗？', title='游戏对话框', choices=['当然呢！', '必须啊！', '我最聪明！'])
easygui.buttonbox(msg='既然你觉得自己很聪明，那么我来考考你！', title='游戏对话框', choices=['好的！', '放马过来！'])
ans1 = easygui.buttonbox(msg='下面这幅图里是什么动物？', image='img/cat.png', title='quiz', choices=['战斗鸡', '大黄狗'])


while ans1 != '战斗鸡':
    easygui.msgbox(msg='哈哈哈，这道题都答错了...', title='游戏对话框', ok_button='再来一遍')
    ans1 = easygui.buttonbox(msg='下面这幅图里是什么动物？', image='img/chicken.png', title='游戏对话框', choices=['战斗鸡', '唐老鸭', '肯德鸡'])

easygui.msgbox('年轻人还是蛮有潜力的嘛！', image='img/panda.png')
sys.exit(0)

# 备注:
#   1. 游戏作弊
#   2. 修改游戏, 制作自己的游戏
#       1. 用自己家人照片替换现有小动物图片
#       2. 修改文字, 交互方式
