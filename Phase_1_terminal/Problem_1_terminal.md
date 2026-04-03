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
> mv [option] [source] [destination] 형태로 사용한다.<br>


```


```

### [삭제]
> rm [option] [file] 형태로 사용한다.<br>
> 실행 예시: else 폴더에 있는 sth.sh 파일을 삭제해 보겠다.


```

```


### [파일 내용 확인]
```



```



### [빈 파일 생성]
```




```





