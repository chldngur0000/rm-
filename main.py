from tkinter import *
import Stock

#버그가 좀 많이 있어알아서 수정해
#부동산 광클하면 떡상 속도 ㅈㄴ 높아짐.
#도박 -말곤 없어 아직. 나중에 만들게
#주식이랑 상점 만들어봐 button3.grid_forget() 이거처럼 하면 버튼 숨길 수 있으니깐 잘 활용 하고 나중에 부동산이랑 도박 수정할게
#주식 만들었는데 버그가 한둘이 아니더라 개망겜 - 정우
#주식 폴더 분활, 주식 폴더 파일 불러오기(line 2) - 정우
#정우 핸썸
#test
#우혁
#sdf


money = 0
happiness = 50  # 행복지수 초기값 설정
property_value = 1000000  # 초기 건물 가격
property_owned = False  # 건물 보유 여부
tk = Tk()

    
def Money():
    global money
    money += 1000000
    label_money['text'] = 'Money: ' + str(money)  # 돈 업데이트
    label_happiness['text'] = 'Happiness: ' + str(happiness)  # 행복지수 업데이트

def Gambling():
    global money, happiness
    money -= 500000  # 도박에 실패했을 때 돈을 잃음
    happiness -= 10  # 도박으로 행복지수 감소
    label_money['text'] = 'Money: ' + str(money)
    label_happiness['text'] = 'Happiness: ' + str(happiness)

def Realestate():
    global money, happiness, property_value, property_owned
    if property_owned:
        # 건물을 팔고 돈을 받는 기능
        money += property_value
        happiness += 10  # 건물을 팔면 행복지수가 증가
        property_owned = False  # 건물 소유권이 없어짐
        label_money['text'] = 'Money: ' + str(money)
        label_happiness['text'] = 'Happiness: ' + str(happiness)
        button_realestate.config(text='부동산 구매', command=BuyRealestate)  # 버튼 텍스트 변경
    else:
        # 건물을 구매하는 기능
        if money >= property_value:
            money -= property_value
            property_owned = True
            label_money['text'] = 'Money: ' + str(money)
            label_happiness['text'] = 'Happiness: ' + str(happiness)
            button_realestate.config(text='부동산 판매', command=Realestate)  # 버튼 텍스트 변경
            # 건물 가격 상승 시작
            IncreasePropertyValue()

def BuyRealestate():
    global money, property_value, property_owned
    if money >= property_value:
        money -= property_value
        property_owned = True
        label_money['text'] = 'Money: ' + str(money)
        label_happiness['text'] = 'Happiness: ' + str(happiness)
        button_realestate.config(text='부동산 판매', command=Realestate)  # 버튼 텍스트 변경
        # 건물 가격 상승 시작
        IncreasePropertyValue()

def IncreasePropertyValue():
    global property_value
    # 가격 상승: 일정 시간마다 가격이 오르도록 설정
    def update_value():
        global property_value
        if property_owned:
            property_value += 100000  # 건물 가격 상승
            label_realestateprice['text'] = 'Realestate: ' + str(property_value)  # 라벨 업데이트
            label_realestateprice.after(5000, update_value)  # 5초마다 가격 상승

    update_value()  # 가격 상승 시작

def Start():
    global happiness
    # 돈과 행복지수 라벨을 초기화
    label_money['text'] = 'Money: ' + str(money)  # 게임 시작 시 돈 초기화
    label_happiness['text'] = 'Happiness: ' + str(happiness)  # 행복지수 초기화

    button3.grid_forget()  # 게임 시작 버튼 숨기기

    # 각 버튼을 세로로 배치
    button_gambling.grid(row=2, column=0, padx=5, pady=5, columnspan=2, sticky="ew")
    button_stock.grid(row=3, column=0, padx=5, pady=5, columnspan=2, sticky="ew")
    button_realestate.grid(row=4, column=0, padx=5, pady=5, columnspan=2, sticky="ew")
    button_mall.grid(row=5, column=0, padx=5, pady=5, columnspan=2, sticky="ew")

tk.title('rm지키우기')

# 돈과 행복지수 라벨을 같은 행(row)으로 배치
label_money = Label(tk, text='Money: ' + str(money), fg='black', font=20)
label_money.grid(row=0, column=0, padx=10, pady=10)

label_happiness = Label(tk, text='Happiness: ' + str(happiness), fg='black', font=20)
label_happiness.grid(row=0, column=1, padx=10, pady=10)

label_realestateprice = Label(tk, text='Realestate: ' + str(property_value), fg='black', font=20)
label_realestateprice.grid(row=0, column=2, padx=10, pady=10)

# 게임 시작 버튼, 아래로 꽉 차게
button3 = Button(tk, text='게임 시작', fg='white', bg='black', font=15, width=15, height=3, command=Start)
button3.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)  # 버튼을 두 열에 걸쳐서 꽉 차게 배치

# 각 버튼 세로로 배치
button_gambling = Button(tk, text='도박', fg='white', bg='black', font=15, width=15, height=3, command=Gambling)
button_stock = Button(tk, text='주식', fg='white', bg='black', font=15, width=15, height=3, command=Stock.Stock_main)
button_realestate = Button(tk, text='부동산', fg='white', bg='black', font=15, width=15, height=3, command=BuyRealestate)
button_mall = Button(tk, text='백화점', fg='white', bg='black', font=15, width=15, height=3, command=Money)

tk.mainloop()
