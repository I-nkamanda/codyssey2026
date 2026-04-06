# Problem 1: 터미널 조작

## 1. 터미널 조작 로그 기록

### [현재 위치 확인] 

> 'pwd' 라는 명령어를 사용해서 할 수 있다. <br>
> **pwd**는 print(출력하시오) working directory (현재 작업중인 디렉토리를) 라는 명령이다.
다음과 같은 예시를 보자.

```
jingeollee@Jingeolui-MacBookPro sunbal % pwd
# % 이후에 pwd를 입력해보면

/Users/jingeollee/Desktop/cody/sunbal
# 다음과 같이 전체 경로를 보여준다.
```




### [목록 확인(숨김파일포함)] 
> 여기에서는 'ls'을 쓴다. ls 의 뜻은 현재 디렉토리에 무엇이 있는지 list를 이야기한다.<br> 다만 숨김 파일을 포함하기 위해서는 'ls -a'를 퍼서 목록을 확인할 수 있다. <br>
> 여기서는 (그리고 후에 이야기할 chmod도 아우르기 위해서) 'ls -la'를 써보겠다.
>
> argument로 -a 를 넣을 때는 숨김 파일도 포함해서 모두 (all) 보여주고, -l을 넣으면, 자세히 길게(long format)으로 보여준다.<br>
> 이외에도 -d (directory 자체만 표시), -h (human-readable, 파일 크기를 사람이 읽기 쉽게 표시), -S(Size별로 정렬해서 표시), -t (time, 최근 수정된 순서로 정렬해서 표시) 등이 있다.

다음과 같은 예시를 보자.

단순히 ls 를 입력했을 때:
```
jingeollee@Jingeolui-MacBookPro codyssey2026 % ls  
Phase_1_terminal			Phase_8_Docker Volume Continuity
Phase_2_chmod				Phase_9_Git_and_Github_Settings
Phase_3_Docker Install			Problem_xx_트러블슈팅.md
Phase_4_Docker basic command		README.md
Phase_5_Container Workshop		sth.sh
Phase_6_Dockerfile Custom Build		미션1_과제목표_서술.md
Phase_7_Port_Mapping
```


ls -a 를 입력했을 때:
    숨어있는 .git이나 .DS_Store 등이 표시된다.
```
jingeollee@Jingeolui-MacBookPro codyssey2026 % ls -a
.					Phase_6_Dockerfile Custom Build
..					Phase_7_Port_Mapping
.DS_Store				Phase_8_Docker Volume Continuity
.git					Phase_9_Git_and_Github_Settings
Phase_1_terminal			Problem_xx_트러블슈팅.md
Phase_2_chmod				README.md
Phase_3_Docker Install			sth.sh
Phase_4_Docker basic command		미션1_과제목표_서술.md
Phase_5_Container Workshop
```

ls -la를 입력했을 때:
    숨어있는 .git이나 .DS_Store 등이 표시되고, 권한, 소유자, 그룹, 파일 크기, 최종 수정일, 파일명 등이 표시된다.

```
jingeollee@Jingeolui-MacBookPro codyssey2026 % ls -la
total 48
drwxr-xr-x  17 jingeollee  staff   544  4월  3 13:09 .
drwxr-xr-x   5 jingeollee  staff   160  4월  3 13:02 ..
-rw-r--r--   1 jingeollee  staff  8196  4월  3 13:03 .DS_Store
drwxr-xr-x  13 jingeollee  staff   416  4월  3 13:32 .git
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_1_terminal
drwxr-xr-x   4 jingeollee  staff   128  4월  3 13:26 Phase_2_chmod
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_3_Docker Install
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_4_Docker basic command
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_5_Container Workshop
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_6_Dockerfile Custom Build
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_7_Port_Mapping
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_8_Docker Volume Continuity
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_9_Git_and_Github_Settings
-rw-r--r--   1 jingeollee  staff    51  4월  3 13:02 Problem_xx_트러블슈팅.md
-rw-r--r--@  1 jingeollee  staff  2060  4월  3 13:32 README.md
-rwxrwxrwx   1 jingeollee  staff     0  4월  3 13:09 sth.sh
-rw-r--r--   1 jingeollee  staff     1  4월  3 13:02 미션1_과제목표_서술.md
jingeollee@Jingeolui-MacBookPro codyssey2026 % 

```


### [이동]

> mv라는 커맨드를 사용한다. <br>
> mv는 move의 약자로, 파일이나 디렉토리를 이동할 때 사용한다.<br>
> mv [option] [source] [destination] 형태로 사용한다.<br>
>예를 들자면, mv sth.sh(파일 이름)) else(폴더 이름))


```


```

### [생성]

> touch 명령어를 사용하여 빈 파일을 생성할 수 있다.
> touch [option] [file] 형태로 사용한다.

```
jingeollee@Jingeolui-MacBookPro tests % ls -la
total 0
drwxr-xr-x   2 jingeollee  staff   64  4월  3 14:49 .
drwxr-xr-x  18 jingeollee  staff  576  4월  3 14:49 ..
jingeollee@Jingeolui-MacBookPro tests % touch sth.sh
jingeollee@Jingeolui-MacBookPro tests % ls
sth.sh
jingeollee@Jingeolui-MacBookPro tests % ls -la
total 0
drwxr-xr-x   3 jingeollee  staff   96  4월  3 14:49 .
drwxr-xr-x  18 jingeollee  staff  576  4월  3 14:49 ..
-rw-r--r--   1 jingeollee  staff    0  4월  3 14:49 sth.sh

```

### [복사]
>cp 영령어를 사용한다. <br>
>cp [option] [source] [destination] 형태로 사용한다.<br>
>예를 들자면, cp sth.sh(파일 이름)) else(폴더 이름))

> 실행 예시: sth.sh 폴더에 else 폴더를 만든 뒤 시작해보겠다.
```

jingeollee@Jingeolui-MacBookPro tests % mkdir else
jingeollee@Jingeolui-MacBookPro tests % ls -la
total 0
drwxr-xr-x   4 jingeollee  staff  128  4월  3 15:42 .
drwxr-xr-x  18 jingeollee  staff  576  4월  3 14:49 ..
drwxr-xr-x   2 jingeollee  staff   64  4월  3 15:42 else
-rw-r--r--   1 jingeollee  staff    0  4월  3 14:49 sth.sh

```
이제 sth.sh 파일을 else 폴더에 복사해 보았다.
```
jingeollee@Jingeolui-MacBookPro tests % cp sth.sh else
jingeollee@Jingeolui-MacBookPro tests % cd else
jingeollee@Jingeolui-MacBookPro else % ls -la
total 0
drwxr-xr-x  3 jingeollee  staff   96  4월  3 15:44 .
drwxr-xr-x  4 jingeollee  staff  128  4월  3 15:42 ..
-rw-r--r--  1 jingeollee  staff    0  4월  3 15:44 sth.sh
jingeollee@Jingeolui-MacBookPro else % 




```


### [이동/이름변경]
터미널을 사용한 파일 이동을 위해서:
> mv [option] [source] [destination] 형태로 사용한다.<br>
#### 파일 옮기기 예시
```
ersatzvitamin9579@c4r3s1 test % ls #첫 상황은 bil.sh 파일과 move 폴더가 있다.
bil.sh	move
ersatzvitamin9579@c4r3s1 test % mv bil.sh move #bil.sh 파일을 move 폴더로 옮겨보았다.
ersatzvitamin9579@c4r3s1 test % ls #다시 폴더 파일을 살펴보니
move #bil.sh 파일이 사라졌다!
ersatzvitamin9579@c4r3s1 test % cd move #move 폴더 안으로 들어가서
ersatzvitamin9579@c4r3s1 move % ls  # 확인해 보면 
bil.sh #move 폴더 안에 있는 것을 확인할 수 있다.

```
#### 파일 이름 바꾸기 예시
터미널을 사용, 파일 이름 변경을 위해서는 
> mv [바꿀 파일] [바꿀 이름] 형태로 사용한다.<br>
move 폴더 안에서 시작해보겠다.
```
ersatzvitamin9579@c4r3s1 move % ls #폴더 내부를 들여다 보면
bil.sh #bil.sh이 있다.
ersatzvitamin9579@c4r3s1 move % mv bil.sh mil.sh #mv [바꿀 파일] [바꿀 이름]명령어를 입력!
ersatzvitamin9579@c4r3s1 move % ls #다시 파일 내부를 보면
mil.sh # mil.sh로 바뀜을 확인할 수 있다!

```



### [삭제]
> rm [option] [file] 형태로 사용한다.<br>
> 실행 예시: move 폴더에 있는 mil.sh 파일을 삭제해 보겠다.

```
ersatzvitamin9579@c4r3s1 move % ls #파일 내용 확인
mil.sh
ersatzvitamin9579@c4r3s1 move % rm mil.sh # mil.sh 삭제
ersatzvitamin9579@c4r3s1 move % ls #파일 내용 확인 시 아무것도 안 나옴
ersatzvitamin9579@c4r3s1 move % ls -la  #ls -la 명령어로 자세히 확인
total 0 #파일 갯수 0. 폴더가 빈 것을 확인할 수 있음.
drwxr-xr-x  2 ersatzvitamin9579  ersatzvitamin9579  64  4  6 15:51 .
drwxr-xr-x  3 ersatzvitamin9579  ersatzvitamin9579  96  4  6 15:44 ..
ersatzvitamin9579@c4r3s1 move % 

```


### [파일 내용 확인]
> cat [파일명] 으로 파일 내용 확인 가능함.

비어있는 move 폴더에서 확인해 보자.
```
ersatzvitamin9579@c4r3s1 move % ls
ersatzvitamin9579@c4r3s1 move % echo Hello World > test.txt # echo [내용] > [파일명]
ersatzvitamin9579@c4r3s1 move % ls  #test.txt 가 생김을 확인
test.txt
ersatzvitamin9579@c4r3s1 move % cat test.txt #cat 명령어를 사용해 test.txt 내용을 불러오면
Hello World #내용이 잘 출력됨을 확인할 수 있다!
ersatzvitamin9579@c4r3s1 move % 

```



### [빈 파일 생성]

> touch [파일명] 명령어를 사용한다.
```
ersatzvitamin9579@c4r3s1 move % ls                              
test.txt
ersatzvitamin9579@c4r3s1 move % touch tes.t #명령어를 사용해서 tes.t 라는 파일을 만들어 보자.
ersatzvitamin9579@c4r3s1 move % ls -la #체크해 보면....
total 8
drwxr-xr-x  4 ersatzvitamin9579  ersatzvitamin9579  128  4  6 15:58 .
drwxr-xr-x  3 ersatzvitamin9579  ersatzvitamin9579   96  4  6 15:44 ..
-rw-r--r--  1 ersatzvitamin9579  ersatzvitamin9579    0  4  6 15:58 tes.t #생성 완료!
-rw-r--r--  1 ersatzvitamin9579  ersatzvitamin9579   12  4  6 15:53 test.txt
ersatzvitamin9579@c4r3s1 move % 

```





