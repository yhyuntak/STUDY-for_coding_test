# 코딩 테스트 준비용 알고리즘 리뷰 N일차 :smirk:

표로 문제에 대한 소감을 한줄로 작성하자.

|날짜| 리뷰 |
|:--:|:--:| 
|220929|  1987 : **BFS로 푸는 것보다 DFS**로 풀어야 하는 문제. 추가적으로 **백트래킹 개념**을 필히 공부하자. :ok_woman: <br/> 2512 : 아직도 start와 end를 결정 짓는 조건문과 언제 start,mid,end를 쓸지 헷갈린다. <br/> 1715 : heapq를 이용하는 문제인데.. 속도가 너무 느리다. | 
|  221004  |  15686 : 그래프 문제와 상하좌우가 떠올리는 설명이 나오더라도, 항상 BFS가 정답은 아니다. 항상 최적의 알고리즘을 짜도록 노력하자. :ok_woman: <br/> 1520 : DFS와 DP개념이 섞인 문제이다. 나는 BFS에 익숙해져서 DFS도 같은 방식으로 생각하는데, 꼭 기억할 것은 BFS는 한번 노드를 떠나면, 다시 그 노드로 돌아오지 않는다는 것이다. 반면, DFS는 한번 떠난 노드를 재귀를 통해 다시 돌아온다. 이것을 고려해서 return을 적절히 사용한다면 좋은 알고리즘을 얻을 수 있다. :ok_woman:  <br/> 2467 : 이분 탐색처럼 while을 사용하지만, 2개의 포인터로 용액들을 지정해서 하나씩 좁혀가는 개념으로 풀었다. |
|  221024  |  2573 : BFS 개념만 알면 풀 수 있는 쉬운 문제. 근데.. 아무리 생각해도 python으로 더 효율적으로 짜는 방법은 잘 모르겠다.. <br/> 1072 : 이 문제는 컴퓨터가 숫자를 어떻게 받아들이는지 알아야 풀 수 있는 문제였다.. 일단 제일 위험한 생각은 float형 데이터를 int()를 사용해서 무식하게 소숫점을 잘라내는 것이다.. 예를 들어 $29/50 \ast 100$이면 58일 것 같지만 컴퓨터는 57.9999...를 반환하더라.. 그래서 int()를 쓰면 58이 아닌 57이 나왔다. 이럴 땐 $29 \ast 100 // 50$을 사용해야한다. <br/> 3055 : BFS를 활용하는 문제. 쉬운 문제이긴한데 문제를 대충 읽는다면 비버가 움직이는게 먼저인가? 물이 차는게 먼저인가? 모를 수 있다. 그러나 마지막에 물이 찰 예정인 곳엔 비버가 움직이지 못한다고 써있기 때문에, 물이 먼저 차는 것을 구현하는게 좋다. 그리고 VISIT을 따로 만들지 않고 비버가 움직이는 곳을 time으로 채워서 활용했다. |
