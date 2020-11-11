def getMaxYes(animals: dict, characteristics: dict):
  maxCount = -1
  for animal, v in animals.items():
    count = 0
    falseCount = 0
    for ele in v:
      if characteristics[ele]:
        count += 1
      else:
        falseCount += 1
    if falseCount >= 1:
      count += 1
    maxCount = max(maxCount, count)
  return maxCount


def main(inputFile: str, outputFile: str):
  guessInput = open(inputFile, 'r')
  guessOutput = open(outputFile, 'w')

  N = int(guessInput.readline().strip())

  animals = {}

  characteristics = {}
  for _ in range(N):
    line = guessInput.readline().strip().split()
    cha = set(line[2:len(line)])
    animals[line[0]] = cha
    for c in cha:
      if c in characteristics:
        characteristics[c] = False
      else:
        characteristics[c] = True

  guessOutput.write(str(getMaxYes(animals, characteristics)) + '\n')
  guessInput.close()
  guessOutput.close()


main('guess.in', 'guess.out')
