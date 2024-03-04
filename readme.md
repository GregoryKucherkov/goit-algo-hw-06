__Task 1__

Для першого завдання було обрано частину метро New York'а, та трохи модифіковано для наглядності графів. Проведено аналіз, та з'ясовано що: в цьому графі 19 вершин та 23 ребра. Окрім цього, досліджено кількість звязків вершин/вузлів. Найбільше у Cortland:4, та WHitehall: 4. Також досліджена центральність вуздів, Чим більше з'єднань має вузол, тим більш центральним він є. Найбільше також у Cortland та WHitehall, і = 0.2222222.

__Task 2__

Дослідженно як працюють алгоритми пошук у глибину (DFS)  та Пошук у ширину (BFS). З виводу ми бачимо:
DFS traversal:
|WHitehall| |Rector| |Rector_green| |Bowling| |Borough| |Wall_st| |Cortland_green| |Cortland| |City_hall| |Canal| |Canal_green| |Chambers| |Spring| |Bleecker| |Prince| |8th_street| |14_union| |14_union_green| |3-av|

BFS traversal:
|WHitehall| |Cortland| |Bowling| |Rector| |City_hall| |Cortland_green| |Borough| |Rector_green| |Canal| |Chambers| |Wall_st| |Prince| |Canal_green| |8th_street| |Spring| |14_union| |Bleecker| |14_union_green| |3-av|

З графіка зрозуміло що, DFS переьирає вуздли двйсно "вглибину", це досягається завдяки використанні підходу LastInFirstOut, що забезпечує обхід вузлів сусідів в першу чергу. У той час як BFS обїодить своїх сусідів завдяки підходу FirstInFirstOut, і ми це можемо побачити.

__Task 3__

Тут алгоритм знаходить найкоротший шлях від станціі WHitehall:

To station: WHitehall      | Closest distance: 0 
To station: Rector         | Closest distance: 2   
To station: Bowling        | Closest distance: 1  
To station: Cortland       | Closest distance: 2 
To station: City_hall      | Closest distance: 2
To station: Rector_green   | Closest distance: 2
To station: Cortland_green | Closest distance: 3
To station: Wall_st        | Closest distance: 3
To station: Chambers       | Closest distance: 5
To station: Canal          | Closest distance: 4
To station: Canal_green    | Closest distance: 5
To station: Prince         | Closest distance: 7
To station: Spring         | Closest distance: 8
To station: Bleecker       | Closest distance: 11
To station: 8th_street     | Closest distance: 10
To station: 14_union       | Closest distance: 13
To station: 14_union_green | Closest distance: 14
To station: 3-av           | Closest distance: 18
To station: Borough        | Closest distance: 5

