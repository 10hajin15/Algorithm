#2개 이하로 다른 비트
def solution(numbers):
    answer = []
    for number in numbers:
        binNum = format(number, 'b')
        #비트 0으로 끝남(짝수) => 끝자리 1로 바꾸기
        if number % 2 == 0:
            binNum = binNum[:-1] + '1'
            answer.append(int(binNum, 2))
        #비트 1로만 => 2번째 자리 0 넣기
        elif '0' not in binNum:
            binNum = '10' + binNum[1:]
            answer.append(int(binNum, 2))
        #그외 => 가장 오른쪽에 있는 0과 다음 1 바꾸기
        else:
            # binNum = binNum[::-1]
            # index = binNum.find('0')
            # binNum = binNum[:index-1] + binNum[index] + binNum[index-1] + binNum[index+1:]
            # answer.append(int(binNum[::-1], 2))
            index = binNum.rfind('0')
            binNum = binNum[:index] + binNum[index+1] + binNum[index] + binNum[index+2:]
            answer.append(int(binNum, 2))
    return answer

print(solution([11,12,13]))