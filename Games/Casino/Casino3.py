from tkinter import *
from tkinter import ttk
from tkinter.ttk import Radiobutton
from random import randint
#импорт



#деньги переменная
money=200



#окно с вкладками
window=Tk()
window.title('Казино Тыбурция')
window.geometry('500x500')
#окно

tabs=ttk.Notebook(window)
tab0=ttk.Frame(tabs)
tab1=ttk.Frame(tabs)
tab2=ttk.Frame(tabs)
tab3=ttk.Frame(tabs)
tab4=ttk.Frame(tabs)
tabs.add(tab0, text='Информация')
tabs.add(tab1, text='Слоты')
tabs.add(tab2, text='Колесо')
tabs.add(tab3, text='Магазин')
tabs.add(tab4, text='Рынок')
tabs.pack(expand=1, fill='both')
#вкладки



###первая вкладка
info={'слоты':'Слоты\n При нажатии на кнопку три слота меняются на случайные,\n если все три слота окажутся одинаковыми, то вы выиграли.\n При проигрыше вы теряете 10 рублей.\n Выигрыши:\n 🍆 - 100\n 🍋 - 100\n 🍞 - 100\n 📄 - -50\n 🚬 - 500\n 🛡 - 1000','колесо':'Колесо Марка Антоновича\n Сначала вам нужно выбрать на какой сектор вы будете делать ставку.\n При нажатии на кнопку колесо вращается.\n Если сектор, находящийся после вращения снизу посередине,\n совпадает с вашей ставкой, вы выиграли.\n Деньги при выигрыше и проигрыше зависят от ставки:\n Ленин:\n Выигрыш - 20\n Проигрыш - 10\n Сталин:\n Выигрыш - 50\n Проигрыш - 20\n Темми:\n Выигрыш - 1000\n Проигрыш - 50\n','кейсы':'Здесь вы можете купить один из трёх кейсов.\n Все кейсы стоят 20 православных рублей.\n Из кейса вы получаете один из восьми предметов.\n Предметы различаются по редкости.\n Чтобы удалить предмет из инвентаря, введите его номер и нажмите кнопку удалить.\n Редкость:\n Кальвин кейс:\nПерцовка - 20%\nХирик - 20%\nБронежилет Кальвин Кляйна - 20%\nЯйцо фаберже - 10%\nСолнечные очки - 10%\nКрестик - 10%\nЗелёные Кальвин Кляйны - 5%\nКлей Master Klein - 5%\nРоманический кейс:n\Дубина Романиуса - 20%\nИксрос - 20%\nБронежилет Романиуса - 20%\nРомовая кислота - 10%\nДубина Романиуса + - 10%\nКнига Белиала - 10%\nЯйцо - 5%\nЛосось Алексей - 5%\n♂dungeon♂ кейс:\n♂Bondage♂ - 20%\n♂Leather glove♂ - 20%\n♂Next door♂ - 20%\n♂300 bucks♂ - 10%\nФутболка ♂Boss of this gym♂ - 10%\n♂Fucking slave♂ - 10%\nМаска ♂dungeon master♂ - 5%\nКлюч от ♂dungeon♂ - 5%\n','рынок':'Здесь вы можете продать предметы, полученные из кейсов.\n Сначала вам нужно выбрать сделку.\n Если у вас в инвентаре есть соответствующий предмет,\n то при нажатии на кнопку он исчезнет и вам начислятся деньги.\n Замена предложений стоит 10 православных рублей.\n Цена предмета зависит от редкости:\n 20% - 1-30\n 10% - 10-50\n 5% - 20-100','Тыбурций':'5'}
#словарь с информацией

def infoclicked():
    if infoentry.get()=='слоты' or infoentry.get()=='колесо' or infoentry.get()=='кейсы' or infoentry.get()=='рынок' or infoentry.get()=='Тыбурций':
        infooutput.configure(text=info[infoentry.get()])
#вывод информации

greet=Label(tab0,text='Добро пожаловать в казино Тыбурция!')
greet.grid(column=0,row=0)
#приветствие

infobutton=Button(tab0,text='Ввести',command=infoclicked)
infobutton.grid(column=0,row=3)
#кнопка для вывода информации

infoentry=Entry(tab0,width=10)
infoentry.grid(column=0,row=2)
#поле для ввода

infotext=Label(tab0,text='Введите одно из следующих слов и нажмите кнопку чтобы получить информацию:\n слоты, колесо, кейсы, рынок, Тыбурций')
infotext.grid(column=0,row=1)
#подсказка

infooutput=Label(tab0,text='')
infooutput.grid(column=0,row=4)
#вывод информации



###вторая вкладка
slotslist=['🍆','🍋','🍞','📄','🚬','🛡']
slots=['🍆','🍆','🍆']
slotprizes={'🍆':100,'🍋':100,'🍞':100,'📄':-50,'🚬':500,'🛡':1000}
#слоты списки

label1=Label(tab1,text='Слоты')
label1.grid(column=1,row=0)
#название

slotsdisplay=Label(tab1,text=slots,font=(100))
slotsdisplay.grid(column=1,row=1)
#отображение слотов

def slotsplay():
    global money
    if money>=10:
        slots[0]=slotslist[randint(0,5)]
        slots[1]=slotslist[randint(0,5)]
        slots[2]=slotslist[randint(0,5)]
        slotsdisplay.configure(text=slots)
        if slots[0]==slots[1]==slots[2]:
            money=money+slotprizes[slots[0]]
            slotsoutput.configure(text='Поздравляем, вы выиграли '+str(slotprizes[slots[0]])+' православных рублей!')
        else:
            slotsoutput.configure(text='Вы ничего не выиграли')
            money=money-10
            
            slotsbalance.configure(text='Баланс: '+str(money))
            balancewheel.configure(text='Ваш баланс: '+str(money))
            moneycrates.configure(text='Баланс: '+str(money))
            moneyshop.configure(text='Баланс: '+str(money))
    else:
        slotsoutput.configure(text='Недостаточно денег')
#слоты играть

slotsbalance=Label(tab1,text='Баланс: '+str(money))
slotsbalance.grid(column=1,row=3)
#слоты баланс

slotsbutton=Button(tab1,text='Играть',command=slotsplay)
slotsbutton.grid(column=1,row=2)
#слоты кнопка

slotsoutput=Label(tab1,text='')
slotsoutput.grid(column=1,row=4)
#слоты вывод



###третья вкладка
wheel=['Ленин','Темми','Ленин','Сталин','Ленин','Сталин','Ленин','Темми','Ленин','Сталин','Ленин','Сталин']
wheelvariants=['≠','Ленин','Сталин','Темми']
wheelW={'Ленин':20,'Сталин':50,'Темми':1000}
wheelL={'Ленин':10,'Сталин':20,'Темми':50}
wheelcolor={'Ленин':'red','Сталин':'yellow','Темми':'green'}
#колесо список

selected=IntVar()
#выбранный сектор переменная

label=Label(tab2,text='Колесо Марка Антоновича')
label.grid(column=2,row=0)
#название

###
sector0=Label(tab2,text=wheel[0],bg='red')
sector0.grid(column=1,row=1)

sector1=Label(tab2,text=wheel[1],bg='green')
sector1.grid(column=2,row=1)

sector2=Label(tab2,text=wheel[2],bg='red')
sector2.grid(column=3,row=1)

sector3=Label(tab2,text=wheel[3],bg='yellow')
sector3.grid(column=4,row=2)

sector4=Label(tab2,text=wheel[4],bg='red')
sector4.grid(column=4,row=4)

sector5=Label(tab2,text=wheel[5],bg='yellow')
sector5.grid(column=4,row=6)

sector6=Label(tab2,text=wheel[6],bg='red')
sector6.grid(column=3,row=7)

sector7=Label(tab2,text=wheel[7],bg='green')
sector7.grid(column=2,row=7)

sector8=Label(tab2,text=wheel[8],bg='red')
sector8.grid(column=1,row=7)

sector9=Label(tab2,text=wheel[9],bg='yellow')
sector9.grid(column=0,row=6)

sector10=Label(tab2,text=wheel[10],bg='red')
sector10.grid(column=0,row=4)

sector11=Label(tab2,text=wheel[11],bg='yellow')
sector11.grid(column=0,row=2)
###

point=Label(tab2,text='Δ',font=(100))
point.grid(column=2,row=8)
#стрелочка

bet1=Radiobutton(tab2,text='Ленин',value=1,variable=selected)
bet1.grid(column=2,row=2)
#ставка Ленин

bet2=Radiobutton(tab2,text='Сталин',value=2,variable=selected)
bet2.grid(column=2,row=3)
#ставка Сталин

bet3=Radiobutton(tab2,text='Темми',value=3,variable=selected)
bet3.grid(column=2,row=4)
#ставка Темми

def wheelclicked():
    global money
    global wheel
    
    if selected.get()!=0:
        if money>=wheelL[wheelvariants[selected.get()]]:
            spin=randint(1,12)
            wheel=list(wheel[spin:]+wheel[:spin])
            if wheelvariants[selected.get()]==wheel[7]:
                wheeloutput.configure(text='Поздравляем, вы выйграли '+str(wheelW[wheel[7]])+' православных рублей!')
                money=money+wheelW[wheel[7]]
            else:
                wheeloutput.configure(text='Вы проиграли '+str(wheelL[wheelvariants[selected.get()]])+' православных рублей')
                money=money-wheelL[wheelvariants[selected.get()]]
            sector0.configure(text=wheel[0],bg=wheelcolor[wheel[0]])
            sector1.configure(text=wheel[1],bg=wheelcolor[wheel[1]])
            sector2.configure(text=wheel[2],bg=wheelcolor[wheel[2]])
            sector3.configure(text=wheel[3],bg=wheelcolor[wheel[3]])
            sector4.configure(text=wheel[4],bg=wheelcolor[wheel[4]])
            sector5.configure(text=wheel[5],bg=wheelcolor[wheel[5]])
            sector6.configure(text=wheel[6],bg=wheelcolor[wheel[6]])
            sector7.configure(text=wheel[7],bg=wheelcolor[wheel[7]])
            sector8.configure(text=wheel[8],bg=wheelcolor[wheel[8]])
            sector9.configure(text=wheel[9],bg=wheelcolor[wheel[9]])
            sector10.configure(text=wheel[10],bg=wheelcolor[wheel[10]])
            sector11.configure(text=wheel[11],bg=wheelcolor[wheel[11]])

            slotsbalance.configure(text='Баланс: '+str(money))
            balancewheel.configure(text='Ваш баланс: '+str(money))
            moneycrates.configure(text='Баланс: '+str(money))
            moneyshop.configure(text='Баланс: '+str(money))
        else:
            wheeloutput.configure(text='Недостаточно денег')
    else:
        wheeloutput.configure(text='Выберите на какой сектор ставить')
#колесо играть

spinwheel=Button(tab2,text='Играть',command=wheelclicked)
spinwheel.grid(column=2,row=5)
#колесо кнопка

balancewheel=Label(tab2,text='Баланс: '+str(money))
balancewheel.grid(column=2,row=6)
#баланс колесо

wheeloutput=Label(tab2,text='')
wheeloutput.grid(column=2,row=9)
#колесо вывод



###четвёртая вкладка
crates={1:['Перцовка','Хирик','Бронежилет Кальвин Кляйна','Яйцо фаберже','Солнечные очки','Крестик','Зелёные Кальвин Кляйны','Клей Master Klein'],2:['Дубина Романиуса','Иксрос','Бронежилет Романиуса','Ромовая кислота','Дубина Романиуса +','Книга Белиала','Яйцо','Лосось Алексей'],3:['♂Bondage♂','♂Leather glove♂','♂Next door♂','♂300 bucks♂','Футболка ♂Boss of this gym♂','♂Fucking slave♂','Маска ♂dungeon master♂','Ключ от ♂dungeon♂']}
inventory=['Пусто','Пусто','Пусто','Пусто','Пусто']
rarity=[0,0,0,1,1,2,2,3,4,5]
#содержание кейсов

cratechosen=IntVar()
#выбранный кейс

namecrates=Label(tab3,text='Магазинчик Кальвин Кляйна')
namecrates.grid(column=1,row=0)
#заголовок кейсы

crate1=Radiobutton(tab3,text='Кальвин кейс',value=1,variable=cratechosen)
crate1.grid(column=1,row=1)
#кейс 1 выбрать

crate2=Radiobutton(tab3,text='Романический кейс',value=2,variable=cratechosen)
crate2.grid(column=1,row=2)
#кейс 2 выбрать

crate3=Radiobutton(tab3,text='♂dungeon♂ кейс',value=3,variable=cratechosen)
crate3.grid(column=1,row=3)
#кейс 3 выбрать

cratesoutput=Label(tab3,text='')
cratesoutput.grid(column=1,row=10)
#кейсы вывод

def buycrate():
    global money
    if money>=20:
        if 'Пусто' in inventory:
            money=money-20
            itemwon=''
            craterandom=randint(1,100)
            if cratechosen.get()==0:
                cratesoutput.configure(text='Выберите какой кейс купить')
            elif craterandom<21:
                itemwon=crates[cratechosen.get()][0]
            elif 20<craterandom<41:
                itemwon=crates[cratechosen.get()][1]
            elif 40<craterandom<61:
                itemwon=crates[cratechosen.get()][2]
            elif 60<craterandom<71:
                itemwon=crates[cratechosen.get()][3]
            elif 70<craterandom<81:
                itemwon=crates[cratechosen.get()][4]
            elif 80<craterandom<91:
                itemwon=crates[cratechosen.get()][5]
            elif 90<craterandom<96:
                itemwon=crates[cratechosen.get()][6]
            elif 95<craterandom:
                itemwon=crates[cratechosen.get()][7]
            for i in range(5):
                if inventory[i]=='Пусто':
                        inventory[i]=itemwon
                        break
            cratesoutput.configure(text='Ваш выигрыш: '+itemwon)
        else:
            cratesoutput.configure(text='Инвентарь заполнен')
    else:
        cratesoutput.configure(text='Недостаточно денег')
    
    cratesinventory.configure(text='Инвентарь:\n'+inventory[0]+'\n'+inventory[1]+'\n'+inventory[2]+'\n'+inventory[3]+'\n'+inventory[4])
    shopinventory.configure(text='Инвентарь:\n'+inventory[0]+'\n'+inventory[1]+'\n'+inventory[2]+'\n'+inventory[3]+'\n'+inventory[4])
    
    slotsbalance.configure(text='Баланс: '+str(money))
    balancewheel.configure(text='Ваш баланс: '+str(money))
    moneycrates.configure(text='Баланс: '+str(money))
    moneyshop.configure(text='Баланс: '+str(money))
#купить кейс

def deleteitem():
    if deleteentry.get()!='':
        deleteitemnumber=int(deleteentry.get())
        if deleteitemnumber==1 or deleteitemnumber==2 or deleteitemnumber==3 or deleteitemnumber==4 or deleteitemnumber==5:
            inventory[deleteitemnumber-1]='Пусто'
            cratesinventory.configure(text='Инвентарь:\n'+inventory[0]+'\n'+inventory[1]+'\n'+inventory[2]+'\n'+inventory[3]+'\n'+inventory[4])

buycratebutton=Button(tab3,command=buycrate,text='Купить')
buycratebutton.grid(column=1,row=8)
#купить кейс кнопка

cratesinventory=Label(tab3,text='Инвентарь:\n'+inventory[0]+'\n'+inventory[1]+'\n'+inventory[2]+'\n'+inventory[3]+'\n'+inventory[4])
cratesinventory.grid(column=1,row=7)

deleteentry=Entry(tab3,width=10)
deleteentry.grid(column=2,row=8)

deletebutton=Button(tab3,text='Удалить',command=deleteitem)
deletebutton.grid(column=3,row=8)

moneycrates=Label(tab3,text='Баланс: '+str(money))
moneycrates.grid(column=1,row=9)



###пятая вкладка
dealcrates=[1,1,1,1,1]
dealitems=[1,1,1,1,1]
dealprices=[1,1,1,1,1]
#информация о сделках

prices=[[1,30],[1,30],[1,30],[10,50],[10,50],[10,50],[20,100],[20,100]]
#цены предметов

def dealaccept():
    global money
    for i in range(5):
        if inventory[i]==crates[dealcrates[dealchosen.get()]][dealitems[dealchosen.get()]]:
            inventory[i]='Пусто'
            money=money+dealprices[dealchosen.get()]
            cratesinventory.configure(text='Инвентарь:\n'+inventory[0]+'\n'+inventory[1]+'\n'+inventory[2]+'\n'+inventory[3]+'\n'+inventory[4])
            shopinventory.configure(text='Инвентарь:\n'+inventory[0]+'\n'+inventory[1]+'\n'+inventory[2]+'\n'+inventory[3]+'\n'+inventory[4])
            
            deal1.configure(text=crates[dealcrates[0]][dealitems[0]]+' за '+str(dealprices[0])+' православных рублей')
            deal2.configure(text=crates[dealcrates[1]][dealitems[1]]+' за '+str(dealprices[1])+' православных рублей')
            deal3.configure(text=crates[dealcrates[2]][dealitems[2]]+' за '+str(dealprices[2])+' православных рублей')
            deal4.configure(text=crates[dealcrates[3]][dealitems[3]]+' за '+str(dealprices[3])+' православных рублей')
            deal5.configure(text=crates[dealcrates[4]][dealitems[4]]+' за '+str(dealprices[4])+' православных рублей')
            
            slotsbalance.configure(text='Баланс: '+str(money))
            balancewheel.configure(text='Ваш баланс: '+str(money))
            moneycrates.configure(text='Баланс: '+str(money))
            moneyshop.configure(text='Баланс: '+str(money))

            shopoutput.configure(text='Предмет продан')
            break
            
#продать предмет

def dealschange():
    global money
    if money>=10:
        money=money-10
        for i in range(5):
            dealcrates[i]=randint(1,3)
            dealitems[i]=randint(0,7)
            dealprices[i]=randint(prices[dealitems[i]][0],prices[dealitems[i]][1])
        
        deal1.configure(text=crates[dealcrates[0]][dealitems[0]]+' за '+str(dealprices[0])+' православных рублей')
        deal2.configure(text=crates[dealcrates[1]][dealitems[1]]+' за '+str(dealprices[1])+' православных рублей')
        deal3.configure(text=crates[dealcrates[2]][dealitems[2]]+' за '+str(dealprices[2])+' православных рублей')
        deal4.configure(text=crates[dealcrates[3]][dealitems[3]]+' за '+str(dealprices[3])+' православных рублей')
        deal5.configure(text=crates[dealcrates[4]][dealitems[4]]+' за '+str(dealprices[4])+' православных рублей')
    
        slotsbalance.configure(text='Баланс: '+str(money))
        balancewheel.configure(text='Ваш баланс: '+str(money))
        moneycrates.configure(text='Баланс: '+str(money))
        moneyshop.configure(text='Баланс: '+str(money))

        shopoutput.configure(text='Предложения изменены')
    else:
        shopoutput.configure(text='Недостаточно денег')
#поменять сделки

dealchosen=IntVar()
#выбранная сделка переменная

shoplabel=Label(tab4,text='Рынок Романиуса Агафониуса')
shoplabel.grid(column=1,row=0)
#заголовок рынок

deal1=Radiobutton(tab4,value=0,variable=dealchosen,text=crates[dealcrates[0]][dealitems[0]]+' за '+str(dealprices[0])+' православных рублей')
deal1.grid(column=1,row=1)
#сделка 1

deal2=Radiobutton(tab4,value=1,variable=dealchosen,text=crates[dealcrates[1]][dealitems[1]]+' за '+str(dealprices[1])+' православных рублей')
deal2.grid(column=1,row=2)
#сделка 2

deal3=Radiobutton(tab4,value=2,variable=dealchosen,text=crates[dealcrates[2]][dealitems[2]]+' за '+str(dealprices[2])+' православных рублей')
deal3.grid(column=1,row=3)
#сделка 3

deal4=Radiobutton(tab4,value=3,variable=dealchosen,text=crates[dealcrates[3]][dealitems[3]]+' за '+str(dealprices[3])+' православных рублей')
deal4.grid(column=1,row=4)
#сделка 4

deal5=Radiobutton(tab4,value=4,variable=dealchosen,text=crates[dealcrates[4]][dealitems[4]]+' за '+str(dealprices[4])+' православных рублей')
deal5.grid(column=1,row=5)
#сделка 5

buttondeal=Button(tab4,command=dealaccept,text='Продать')
buttondeal.grid(column=1,row=7)
#кнопка принять сделку

buttonchange=Button(tab4,command=dealschange,text='Поменять предложения')
buttonchange.grid(column=2,row=7)
#кнопка поменять сделки

shopinventory=Label(tab4,text='Инвентарь:\n'+inventory[0]+'\n'+inventory[1]+'\n'+inventory[2]+'\n'+inventory[3]+'\n'+inventory[4])
shopinventory.grid(column=1,row=6)
#инвентарь магаз

moneyshop=Label(tab4,text='Баланс: '+str(money))
moneyshop.grid(column=1,row=8)

shopoutput=Label(tab4,text='')
shopoutput.grid(column=1,row=9)



window.mainloop()
#####
