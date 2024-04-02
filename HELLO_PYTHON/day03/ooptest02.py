from day03.ooptest01 import animal
# 임포트하는 순간 이미 한번 동작이 됨
# 호풀당하는 곳에서 메인안에 집어넣어주면 됨

ani = animal()
print("ani.name2",ani.name)   
ani.named("멍멍이")
print("ani.name2",ani.name) 