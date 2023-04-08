from tkinter import *
from tkinter import ttk
import math
 
operation = ''  #연산자 저장 변수
temp_number = 0 #이전값 저장 변수

one_value_op = ['pi','%','factorial','exp'] # 변수가 1개여야 가능한 연산자
two_value_op = ['+','-','/','*','^n'] # 변수가 2개여야 가능한 연산자


# 결과 출력 상태인지 상태저장.
answer_trigger = False

# 숫자버튼 처리 함수 
def button_pressed(value):
    global temp_number
    global answer_trigger
     # 입력값이 'AC'일때
    if value=='AC':
        number_entry.delete(0,'end')
        #AC버튼 누르면, trigger 변수도 초기화.
        operation = ''
        answer_trigger = False
        print("AC pressed")
    else: #Trigger가 True이면, Entry 초기화후 새로입력.
        if answer_trigger:
            number_entry.delete(0,"end")
            answer_trigger = False
        number_entry.insert("end",value)
        print(value,"pressed")
 
# 사칙연산 처리 
def float_filter(value):
    try:
        int(value)
        return int(value)
    except ValueError:
        return float(value)
 
# 두값이 같으면 정수로 표현가능.==> 정수값으로 반환.
def int_changer(value):
    if int(value) == float(value):
        return int(value)
    else:
        return float(value)
 
def math_button_pressed(value):
    global operation 
    global temp_number
    global answer_trigger
    if not number_entry.get() == '':
        operation = value
        temp_number = float_filter(number_entry.get())
        number_entry.delete(0,'end')
        print(temp_number,operation)

 
def equal_button_pressed1():
    global operation
    global temp_number
    global answer_trigger
    isValid = True
    if operation !='':
        if number_entry.get() !='' and operation in two_value_op :
            number = int(number_entry.get())
            if operation == '/':
                if number == 0:
                    print("0으로 나눌 수 없습니다")
                    isValid = False
                    solution = -1
                else:
                    solution = temp_number/number
            elif operation == '*':
                solution = temp_number*number
            elif operation == '+':
                solution = temp_number+number
            elif operation == '-':
                solution = temp_number-number
            elif operation == '^n':
                solution = temp_number**(number)
        elif operation in one_value_op:
            print("1연산")
            if operation == 'pi':
                solution = temp_number*(math.pi)
            elif operation == '%':
                solution = temp_number/100
            elif operation == 'exp':
                solution = math.exp(temp_number)    
            elif operation == 'factorial':
                solution = math.factorial(temp_number) 
   

        #int_changer() 함수를 한번 거쳐서, 값저장.
        solution = int_changer(solution)
        number_entry.delete(0,'end')
        number_entry.insert(0,solution)
        if isValid:
            if operation in two_value_op:
                print(temp_number,operation,number,"=",solution)
            elif operation in one_value_op:
                print(temp_number,operation,"=",solution)
        else:
            print("Err %d : 계산 불가능" %(solution))
            isValid = True # 다시 True로 초기화
        operation = ''
        temp_number = 0

        # 계산 완료후, Trigger 변수 True로 변경.
        answer_trigger = True
         
     
root = Tk()
root.title("Calculator")
root.geometry("525x150")

#텍스트창의 값 저장할 변수. 
entry_value = StringVar(root, value='')

#textvariable 속성으로 변수 설정. 
number_entry = ttk.Entry(root, textvariable = entry_value, width=20)
print(type(number_entry))
number_entry.grid(row=0, columnspan=3) 

#1번째 줄 1,2,3,+,pi,<-
button1 = ttk.Button(root, text="1", command = lambda:button_pressed('1'))
button1.grid(row=1, column=0)
button2 = ttk.Button(root, text="2", command = lambda:button_pressed('2'))
button2.grid(row=1, column=1)
button3 = ttk.Button(root, text="3", command = lambda:button_pressed('3'))
button3.grid(row=1, column=2)
button_add = ttk.Button(root, text="+", command = lambda:math_button_pressed('+'))
button_add.grid(row=1, column=3)
button_add = ttk.Button(root, text="pi", command = lambda:math_button_pressed('pi'))
button_add.grid(row=1, column=4)
button_add = ttk.Button(root, text="<-", command = lambda:math_button_pressed('<-'))
button_add.grid(row=1, column=5)

#2번째 줄 4,5,6,-, %, x!
button4 = ttk.Button(root, text="4", command = lambda:button_pressed('4'))
button4.grid(row=2, column=0)
button5 = ttk.Button(root, text="5", command = lambda:button_pressed('5'))
button5.grid(row=2, column=1)
button6 = ttk.Button(root, text="6", command = lambda:button_pressed('6'))
button6.grid(row=2, column=2)
button_sub = ttk.Button(root, text="-", command = lambda:math_button_pressed('-'))
button_sub.grid(row=2, column=3)
button_sub = ttk.Button(root, text="%", command = lambda:math_button_pressed('%'))
button_sub.grid(row=2, column=4)
button_sub = ttk.Button(root, text="x!", command = lambda:math_button_pressed('factorial'))
button_sub.grid(row=2, column=5)

#3번째 줄 7, 8, 9, * ,(, )
button7 = ttk.Button(root, text="7", command = lambda:button_pressed('7'))
button7.grid(row=3, column=0)
button8 = ttk.Button(root, text="8", command = lambda:button_pressed('8'))
button8.grid(row=3, column=1)
button9 = ttk.Button(root, text="9", command = lambda:button_pressed('9'))
button9.grid(row=3, column=2)
button_mult = ttk.Button(root, text="*", command = lambda:math_button_pressed('*'))
button_mult.grid(row=3, column=3)
button_mult = ttk.Button(root, text="(", command = lambda:math_button_pressed('('))
button_mult.grid(row=3, column=4)
button_mult = ttk.Button(root, text=")", command = lambda:math_button_pressed(')'))
button_mult.grid(row=3, column=5)

 
#4번째 줄 AC, 0, . , /, exp, ^2 
button_ac = ttk.Button(root, text="AC", command = lambda:button_pressed('AC'))
button_ac.grid(row=4, column=0)
button0 = ttk.Button(root, text="0", command = lambda:button_pressed('0'))
button0.grid(row=4, column=1)
button_div = ttk.Button(root, text=".", command = lambda:math_button_pressed('.'))
button_div.grid(row=4, column=2)
button_div = ttk.Button(root, text="/", command = lambda:math_button_pressed('/'))
button_div.grid(row=4, column=3)
button_div = ttk.Button(root, text="exp", command = lambda:math_button_pressed('exp'))
button_div.grid(row=4, column=4)
button_div = ttk.Button(root, text="^n", command = lambda:math_button_pressed('^n'))
button_div.grid(row=4, column=5)

#5번째 줄 =
button_equal = ttk.Button(root, text="=", command = lambda:equal_button_pressed1())
button_equal.grid(row=5, column = 0)
 
root.mainloop()