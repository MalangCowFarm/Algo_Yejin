# ⭐Git 기본 사용법⭐



## Git config 설정

깃 설치를 완료했다면 git config 설정을 통해 사용 환경을 세팅할 수 있습니다.

- 사용자 설정 깃을 커밋할 때 입력되는 사용자의 이메일과 이름 정보를 등록하는 방법입니다.
  
  ```
  git config --global user.name "your_name"
  git config --global user.email example@example.com
  ```

- git config 설정 확인 git config 설정이 제대로 되었는지 확인하고 싶다면 아래와 같은 명령어를 입력하면 됩니다.
  
  ```
   git config --list
  ```



#### Git fork

기존 원격 레파지토리를 본인 git 레파지토리로 복제한다고 생각하면됩니다.

**화살표 누르면 포크됨!!!**

<img title="" src="file:///C:/Users/kdann/AppData/Roaming/marktext/images/2023-01-30-00-04-46-image.png" alt="" width="536" data-align="center">

## Git 저장소 설정

> Git remote 명령어를 사용

아마 fork 후 개인 repository를 클론했다면 origin은 개인 원격 repository가 되어있을거임.

```shell
git remote add (저장소 별칭) (저장소 url)
ex)git remote add mainrepo https://github.com/username/AlgorithmStudy.git
```

## Git 커밋후 push까지

**add**

```shell
/*전체 변경내용 add*/
git add .    
/*git 특정폴더 add*/
git add 폴더이름/
```

**commit**

```shell
git commit -m "커밋메시지"  
```

**push** : 현재 로컬커밋 다 올린다보면됨.

```shell
git push (repository) (브랜치이름)
/*왠만하면 아래처럼 하면됨 origin repository에 마스터브랜치로 push*
/git push origin master
```

**pull** : 현재 원격저장소의 커밋까지 로컬로 가져옴

```shell
git pull (repository) (브랜치이름)/
*왠만하면 아래처럼 하면됨 본인 origin으로 등록된 repository의 master브랜치 에서 pull 땡김*/
git pull origin master
```



✔️ 여기서 우리 스터디의 경우

push 는 본인 repository에서 

pull 은 yeseul0722가 생성한 repository에서 하면됨.

**그리고 항상 push 하기전에 pull 해서 충돌안나게 조심!**

```shell
git push origin master
/*이름1*/
git pull dongwook master
/*이름2*/
git pull others master
```
