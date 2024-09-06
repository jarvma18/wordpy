import sys

def count_words(sentence: str) -> int:
  words: array = sentence.split()
  return len(words)

def main():
  user_inputted_sentence: str = sys.argv[1]
  print(count_words(user_inputted_sentence))

if __name__ == "__main__":
  main()