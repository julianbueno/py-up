#!/usr/bin/python3

from collections import defaultdict

scores = [ 
    {'hotel_id': 1001, 'user_id': 501, 'score': 7}, 
    {'hotel_id': 1001, 'user_id': 502, 'score': 7}, 
    {'hotel_id': 1001, 'user_id': 503, 'score': 7}, 
    {'hotel_id': 2001, 'user_id': 504, 'score': 10}, 
    {'hotel_id': 3001, 'user_id': 505, 'score': 5}, 
    {'hotel_id': 2001, 'user_id': 506, 'score': 5} 
]

def get_hotels(scores, min_avg_score):
    hotel_score = defaultdict(list)
    for score in scores:
        hotel_score[score['hotel_id']].append(score['score'])
    
    hotel_avg = [key for key in hotel_score \
                 if sum(hotel_score[key])/len(hotel_score[key]) \
                    >= min_avg_score]
    
    return hotel_avg

if __name__ == '__main__':
    avg_score = float(input())
    print(get_hotels(scores, avg_score))