stack = []

#삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력

# [:] 처음부터 끝까지
# [start:] start오프셋(인덱스)부터 끝까지
# [:end] 처음부터 end-1 오프셋(인덱스)까지
# [start : end] start오프셋부터 end-1 오프셋(인덱스)까지
# [start : end : step] step만큼 문자를 건너뛰면서, 위와 동일하게 추출