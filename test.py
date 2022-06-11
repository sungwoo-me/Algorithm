def solution(cards):
    cards_len = len(cards)
    visited = [False]*cards_len
    answer = 0 

    for i in range(cards_len) :
        if visited[i] :
            continue
        min_card = min(cards[i])
        min_card_i = cards[i].index(min_card)

        for j in range(i,cards_len):
            if visited[j] :
                continue

            n_min_card = min(cards[j])
            n_min_card_i = cards[j].index(n_min_card)            



            if n_min_card_i != min_card_i and min_card != 0 and n_min_card != 0:
                if min_card != cards[i][n_min_card_i]-1 and n_min_card != cards[j][min_card_i]-1 :
                    cards[i][min_card_i]+=1
                    cards[j][min_card_i]-=1

                    cards[i][n_min_card_i]-=1

                    
                    cards[j][n_min_card_i]+=1

                    visited[i] = True
                    visited[j] = True
                    break 

    print(cards)
    for i in cards :
        answer += min(i)


    return answer