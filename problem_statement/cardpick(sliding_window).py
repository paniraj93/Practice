<<<<<<< HEAD
#using  sliding window technique , find the minimum no of cards to pick up to pair the match card
cards = [3,4,2,3,3,5,2,4,7]
min_value = {}
min_distance = float('inf')

for i, card in enumerate(cards):
    if card in min_value:
        window_size = i - min_value[card] + 1
        min_distance = min(min_distance, window_size)
    min_value[card] = i
  
=======
#using  sliding window technique , find the minimum no of cards to pick up to pair the match card
cards = [3,4,2,3,3,5,2,4,7]
min_value = {}
min_distance = float('inf')

for i, card in enumerate(cards):
    if card in min_value:
        window_size = i - min_value[card] + 1
        min_distance = min(min_distance, window_size)
    min_value[card] = i
  
>>>>>>> 1e4374c3a874f037ba1cfe876b6707251617a4f1
print("minimum cards to pick for pair : ", min_distance)