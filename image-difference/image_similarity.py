import Algorithmia

input = [
  "data://Malkhan/myImages/original_01.png",
  "data://Malkhan/myImages/modified_01.png"
]
client = Algorithmia.client('simqlx+BWUUDJHHv/0VqW2vL5x71')
algo = client.algo('zskurultay/ImageSimilarity/0.1.4')
print(algo.pipe(input))