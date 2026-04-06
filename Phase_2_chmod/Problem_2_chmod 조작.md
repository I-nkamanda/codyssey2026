## chmod에 대하여

chmod는, Unix 환경에서 파일의 권한을 변경하는 명령어이다.

shell에서 사용하는 형식은 `chmod [option] [mode] [file] 이다.

mode는 8진수로 표현할 수 있다.

각 숫자는 다음과 같은 의미를 가진다.

4: 읽기 권한

2: 쓰기 권한

1: 실행 권한

예를 들어, 755는 읽기, 쓰기, 실행 권한을 가진다.

이를 ls -la 등속으로 확인하자면 다음과 같은 형태를 보인다.

```bash
jingeollee@Jingeolui-MacBookPro codyssey2026 % ls -la 
#를 입력했을 떄...

total 48
drwxr-xr-x  16 jingeollee  staff   512  4월  3 13:02 .
drwxr-xr-x   5 jingeollee  staff   160  4월  3 13:02 ..
-rw-r--r--   1 jingeollee  staff  8196  4월  3 13:03 .DS_Store
drwxr-xr-x  12 jingeollee  staff   384  4월  3 13:02 .git
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_1_terminal
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_2_chmod
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_3_Docker Install
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_4_Docker basic command
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_5_Container Workshop
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_6_Dockerfile Custom Build
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_7_Port_Mapping
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_8_Docker Volume Continuity
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_9_Git_and_Github_Settings
-rw-r--r--   1 jingeollee  staff    51  4월  3 13:02 Problem_xx_트러블슈팅.md
-rw-r--r--   1 jingeollee  staff  2058  4월  3 13:02 README.md
-rw-r--r--   1 jingeollee  staff     1  4월  3 13:02 미션1_과제목표_서술.md
jingeollee@Jingeolui-MacBookPro codyssey2026 % 
```

맨 앞에 있는 것이 권한이다. 
d (디렉토리 여부. 파일인 경우 -로 표시된다) | rwx (소유자의 권한) | rwx (그룹의 권한) | rwx (그 외 사용자의 권한) 순으로 표시된다.

예를 들어, drwxr-xr-x는 다음과 같은 의미를 가진다.

d로 시작하니, 해당 항목은 폴더이고, 
그 뒤의 세 글자가 rwx니까 소유자는 읽기, 쓰기, 실행 권한을 가진다. (=7)
그 뒤의 세 글자는 r-x니까 그룹은 읽기, 실행 권한을 가진다. (=5)
마지막 세 글자도 r-x니까, 그 외 사용자는 읽기, 실행 권한을 가진다. (=5)

이제 8진수를 사용한 chmod를 사용해보자.

chmod 755 [file] 은 위에서 설명한 권한을 부여하는 명령어이다.

우선 touch를 활용, sth.sh 라는 파일을 생성해 보았다.

```bash
jingeollee@Jingeolui-MacBookPro codyssey2026 % touch sth.sh
jingeollee@Jingeolui-MacBookPro codyssey2026 % ls -la
total 48
drwxr-xr-x  17 jingeollee  staff   544  4월  3 13:09 .
drwxr-xr-x   5 jingeollee  staff   160  4월  3 13:02 ..
-rw-r--r--   1 jingeollee  staff  8196  4월  3 13:03 .DS_Store
drwxr-xr-x  12 jingeollee  staff   384  4월  3 13:02 .git
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_1_terminal
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_2_chmod
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_3_Docker Install
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_4_Docker basic command
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_5_Container Workshop
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_6_Dockerfile Custom Build
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_7_Port_Mapping
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_8_Docker Volume Continuity
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_9_Git_and_Github_Settings
-rw-r--r--   1 jingeollee  staff    51  4월  3 13:02 Problem_xx_트러블슈팅.md
-rw-r--r--   1 jingeollee  staff  2058  4월  3 13:02 README.md
-rw-r--r--   1 jingeollee  staff     0  4월  3 13:09 sth.sh  ## ** \<- 이 파일이다!! **
-rw-r--r--   1 jingeollee  staff     1  4월  3 13:02 미션1_과제목표_서술.md
jingeollee@Jingeolui-MacBookPro codyssey2026 % 
```

현재 sth.sh 파일의 권한은 -rw-r--r-- 이다. 

8진수로 읽어보면 644이다.

이제 이 파일을 777로 변경해 보자.

```bash
jingeollee@Jingeolui-MacBookPro codyssey2026 % ls -la
total 48
drwxr-xr-x  17 jingeollee  staff   544  4월  3 13:09 .
drwxr-xr-x   5 jingeollee  staff   160  4월  3 13:02 ..
-rw-r--r--   1 jingeollee  staff  8196  4월  3 13:03 .DS_Store
drwxr-xr-x  12 jingeollee  staff   384  4월  3 13:02 .git
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_1_terminal
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_2_chmod
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_3_Docker Install
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_4_Docker basic command
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_5_Container Workshop
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_6_Dockerfile Custom Build
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_7_Port_Mapping
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_8_Docker Volume Continuity
drwxr-xr-x   3 jingeollee  staff    96  4월  3 13:02 Phase_9_Git_and_Github_Settings
-rw-r--r--   1 jingeollee  staff    51  4월  3 13:02 Problem_xx_트러블슈팅.md
-rw-r--r--   1 jingeollee  staff  2058  4월  3 13:02 README.md
-rwxrwxrwx   1 jingeollee  staff     0  4월  3 13:09 sth.sh  ## ** \<- 이 파일이다!! **
-rw-r--r--   1 jingeollee  staff     1  4월  3 13:02 미션1_과제목표_서술.md

```
다음과 같이 sth.sh가 -rwxrwxrwx로 변경된 것을 확인할 수가 있다.

이제는 directory를 만들어 보자.

```bash
jingeollee@Jingeolui-MacBookPro Phase_2_chmod % mkdir else     
jingeollee@Jingeolui-MacBookPro Phase_2_chmod % ls -la
total 16
drwxr-xr-x   4 jingeollee  staff   128  4월  3 13:26 .
drwxr-xr-x  17 jingeollee  staff   544  4월  3 13:09 ..
drwxr-xr-x   2 jingeollee  staff    64  4월  3 13:26 else
-rw-r--r--@  1 jingeollee  staff  5651  4월  3 13:13 Problem_2_chmod 조작.md

```
else 라는 폴더가 생성되었다. 권한은 drwxr-xr-x 이다. 8진수로 읽으면 755이다. 이제 이 폴더의 권한을 777로 변경해 보자.

```bash
jingeollee@Jingeolui-MacBookPro Phase_2_chmod % chmod 777 else
jingeollee@Jingeolui-MacBookPro Phase_2_chmod % ls -la
total 16
drwxr-xr-x   4 jingeollee  staff   128  4월  3 13:26 .
drwxr-xr-x  17 jingeollee  staff   544  4월  3 13:09 ..
drwxrwxrwx   2 jingeollee  staff    64  4월  3 13:26 else
-rw-r--r--@  1 jingeollee  staff  5651  4월  3 13:13 Problem_2_chmod 조작.md
jingeollee@Jingeolui-MacBookPro Phase_2_chmod % 
```

else 폴더의 권한도 drwxrwxrwx로 변경된 것을 확인할 수가 있다.
