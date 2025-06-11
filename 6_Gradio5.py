import gradio as gr
def add(num1, num2):
    return num1 * num2

#블록이 아닌 하나의 인터페이스를 만들 때 사용
interface = gr.Interface(  
    
    fn=add,
    inputs = ['number', 'number'],
    outputs = 'number',
    title='계산기',
    description='숫자 두 개를 입력하세요',
    flagging_mode="never" # flag를 하지 않음
    #flag -> 타임스탬프와 로그가 남음
)

interface.launch()