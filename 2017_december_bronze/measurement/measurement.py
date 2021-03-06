def getLeaders(cows):
  leaders = set()
  greatestMilk = -1000
  for name, milk in cows.items():
    if milk > greatestMilk:
      leaders = {name}
      greatestMilk = milk
    elif milk == greatestMilk:
      leaders.add(name)
  return leaders

def getNumOfTimesToChange(cowMilkLog):
  cowMilkLog = sorted(cowMilkLog)
  lastLeaders = set()
  cows = {'Bessie': 7, 'Elsie': 7, 'Mildred': 7}
  count = 0
  for cow in cowMilkLog:
    cows[cow[1]] += cow[2]
    leaders = getLeaders(cows)
    if leaders != lastLeaders:
      count += 1
      lastLeaders = leaders
  return count 

def main(inputFile, outputFile):
  measurementInput = open(inputFile, 'r')
  measurementOutput = open(outputFile, 'w')
  
  N = int(measurementInput.readline().strip())
  cowMilkLog = []
  for _ in range(N):
    line = measurementInput.readline().strip().split()
    line[0] = int(line[0])
    line[2] = int(line[2])
    
    cowMilkLog.append(line)
  
  # print(cowMilkLog)
  measurementOutput.write(str(getNumOfTimesToChange(cowMilkLog)) + '\n')
  
  measurementInput.close()
  measurementOutput.close()

main('measurement.in', 'measurement.out')