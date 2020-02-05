import random
from sys import exit

#牌组
cards = ['♦10', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦A', '♦J', '♦K', '♦Q',
 '♣10', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣A', '♣J', '♣K', '♣Q',
 '♥10', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥A', '♥J', '♥K', '♥Q',
 '♠10', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠A', '♠J', '♠K', '♠Q']

cards_value = {'♦10':10, '♦2':2, '♦3':3, '♦4':4, '♦5':5, '♦6':6, '♦7':7, '♦8':8, '♦9':9, '♦A':1, '♦J':10, '♦K':10, '♦Q':10,
 '♣10':10, '♣2':2, '♣3':3, '♣4':4, '♣5':5, '♣6':6, '♣7':7, '♣8':8, '♣9':9, '♣A':1, '♣J':10, '♣K':10, '♣Q':10,
 '♥10':10, '♥2':2, '♥3':3, '♥4':4, '♥5':5, '♥6':6, '♥7':7, '♥8':8, '♥9':9, '♥A':1, '♥J':10, '♥K':10, '♥Q':10,
 '♠10':10, '♠2':2, '♠3':3, '♠4':4, '♠5':5, '♠6':6, '♠7':7, '♠8':8, '♠9':9, '♠A':1, '♠J':10, '♠K':10, '♠Q':10}

Ace = ['♦A','♣A','♥A','♠A']


#开局发牌
def cards_start(cards):
    return [cards.pop(random.randint(0,len(cards)-1)),cards.pop(random.randint(0,len(cards)-1))]

#发牌
def cards_dealing(cards):
    return cards.pop(random.randint(0,len(cards)-1))

#计算点数
def points_count(handcards):
    points = 0
    for i in handcards:
        points += cards_value[i]
    for j in handcards:
        if j in Ace:
            if points + 10 <= 21:
                points += 10
    return points

#比较
def judgement(player_point,pc_point):
    if player_point > 21 and pc_point > 21:
        print('你输了')
        return ([0,1])
    elif player_point > 21 and pc_point <= 21:
        print('你输了')
        return ([0,1])
    elif player_point <= 21 and pc_point > 21:
        print('你赢了')
        return ([1,0])
    elif player_point <= 21 and pc_point <= 21:
        if player_point == 21 and pc_point == 21:
            if (('♦A' or '♣A' or '♥A' or '♠A') in player_handcards) and (('♦A' or '♣A' or '♥A' or '♠A') not in pc_handcards):
                print('你赢了')
                return ([1,0])
            elif (('♦A' or '♣A' or '♥A' or '♠A') not in player_handcards) and (('♦A' or '♣A' or '♥A' or '♠A') in pc_handcards):
                print('你输了')
                return ([0,1])
            else:
                print('平局')
                return ([0,0])
        else:
            if player_point < pc_point:
                print('你输了')
                return ([0,1])
            elif player_point > pc_point:
                print('你赢了')
                return ([1,0])
            else:
                print('平局')
                return ([0,0])
                
#判断要牌停牌
def get_stop():
    ask = input('是否叫牌?(Y/N)>>:')
    if ask.upper() == 'Y':
        return cards_dealing(cards)
    elif ask.upper() == 'N':
        print('你已经停牌')
        return False
    else:
        print('请输入Y/N!>>:')
        return get_stop()

#判断下一轮
def nextgame():
    a = input('是否开始新一轮游戏?(Y/N)>>')
    if a.upper() == 'Y':
        if len(cards) < 10:
            print('牌数不够！退出游戏')
            input('游戏结束')
            exit(1)
        else:
            return True
    elif a.upper() == 'N':
        input('游戏结束')
        exit(1)
    else:
        print('输入错误，请重新输入！>>')
        nextgame()

#一轮游戏
def game(cards):
    player_get = cards_start(cards)
    pc_get = cards_start(cards)
    print(f'你的手牌为:{player_get[0]},{player_get[1]}')
    print(f'电脑的手牌为:{pc_get[0]},?\n')
    player_cards.extend(player_get)
    pc_cards.extend(pc_get)
    points = [points_count(player_cards),points_count(pc_cards)]
    if points[0] == 21:
        print('21点 不可要牌')
        return judgement(points[0],points[1])
    else:
        while points[0] <= 21:
            player_get_cards = get_stop()
            if player_get_cards != False:
                player_cards.append(player_get_cards)
                print(f'你的手牌为:{player_cards}')
                points[0] = points_count(player_cards)
                if points[0] > 21:
                    print('你爆牌了')
                    print(f'电脑的手牌为:{pc_cards}')
                    return judgement(points[0],points[1])
                else:
                    continue
            elif player_get_cards == False:
                while points[1] < 17:
                    pc_get_cards = cards_dealing(cards)
                    pc_cards.append(pc_get_cards)
                    points[1] = points_count(pc_cards)
                print(f'电脑的手牌为:{pc_cards}')
                return judgement(points[0],points[1])

game_time = 1
player_score = 0
pc_score = 0

n = eval(input('使用几副牌?'))
cards = cards * n

while len(cards) > 10:
    input('开始游戏，祝你好运<<Enter>>\n')
    print(f'第{game_time}回合')
    print('.'*60)
    player_cards = []
    pc_cards = []
    score = game(cards)
    player_score += score[0]
    pc_score += score[1]
    print (f'游戏总比分是:{player_score}:{pc_score}')
    game_time += 1
    nextgame()
