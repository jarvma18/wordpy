import unittest
from main import count_words

class TestCountWords(unittest.TestCase):
  test_sentence: str = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
                        Vivamus ultrices neque blandit purus tincidunt dapibus. \
                        Donec sit amet elit venenatis, dictum nisi non, posuere risus. \
                        Donec eu dapibus urna, in fringilla nisi. Integer vel volutpat mi. \
                        Maecenas congue erat augue, at finibus sem egestas ac. \
                        Ut vestibulum elementum ligula id porttitor. Ut viverra elit mauris, \
                        a consequat orci facilisis vitae. Etiam ac dapibus magna. Aliquam erat volutpat.\
                        Nam libero tellus, ultrices vel elit iaculis, sagittis blandit tellus. \
                        Cras non magna ipsum. Aenean neque mauris, blandit ut efficitur consectetur, \
                        fringilla nec nunc. Integer vitae velit volutpat erat lacinia egestas in ac lorem. \
                        Sed efficitur venenatis faucibus. In hac habitasse platea dictumst. \
                        Vestibulum dictum elementum magna sed posuere. Pellentesque habitant morbi tristique senectus et netus.'

  def test_count_words(self):
    words: int = count_words(self.test_sentence)
    self.assertEqual(words, 123);

if __name__ == '__main__':
  unittest.main()