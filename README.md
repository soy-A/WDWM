## 언제 만나조&#10067;
'학교생활 알리미' 챗봇을 만드는 팀입니다.

### 조원&#127800;
| 학번 | 201819186 | 201812755 | 201912393 | 201912352 |
| :---: | :---: | :---: | :---: | :---: |
| 이름 | 조예은 | 민소연 | 이미르 | 김자연 |
| ID | dpdms529 | soy-A | lalala5772 | nature1216 |
<br/>

## 학교생활 알리미&#127979;
전북대학교 IT정보공학과 학생들에게 필요한 정보를 전달해주는 카카오톡 챗봇입니다.
<br/>

### 학교생활 알리미 주요기능&#128172;
1. lms, khub 에 올라오는 과목들의 과제 및 과제별 제출기한을 알려줍니다.
2. IT정보공학과의 최신 공지사항을 알려줍니다.
3. 전북대학교 코로나 관련 최신 공지사항을 알려줍니다.

### 학교생활 알리미 사용하기
>IT알리미 카카오톡 채널 : http://pf.kakao.com/_Gxfzxmxb
>
>채팅 바로가기 : http://pf.kakao.com/_Gxfzxmxb/chat

위 링크를 통해 채널에 접속하거나, 카카오톡에서 **'IT알리미'** 를 검색하시면 이용하실 수 있습니다.

**'채널 추가'** 버튼을 눌러 언제 어디서나 편하게 이용해보세요!

<br/><br/>

## 팀 홈페이지&#128214;
https://dpdms529.github.io/WDWM/

### 게시글 양식&#128196;
|   | 파일명(글 제목) |
| :---: | :---: |
| 개인별 진행상황 | YYYY-MM-DD-[본인이름]-6월-n째주-진행상황.md |
| 팀 회의록 | YYYY-MM-DD-YYYYMMDD-회의록.md |

&#128293; **개인별 진행상황은 매주 일요일 안으로 업로드할 것**
<br/><br/>

## Requirements
```
pip install -r requirement.txt
```
### ChromeDriver 설치
>ChromeDriver : https://sites.google.com/a/chromium.org/chromedriver/downloads
#### 1. Chrome 버전 확인
1) 컴퓨터에서 크롬을 연다
2) 오른쪽 상단에서 **더보기** 를 클릭
3) **도움말-Chrome 정보** 를 클릭한다
#### 2. 위의 사이트에서 본인의 Chrome 버전과 일치하는 ChromeDriver파일을 다운로드
#### 3. 원하는 위치에 압축 해제한 후, chromedriver.exe파일의 경로를 복사
#### 4. 사용하고자 하는 크롤러 파일의 다음 코드를 수정:
```
driver = webdriver.Chrome("C:/Users/chromedriver_win32/chromedriver.exe") #정방향 슬래시 또는 역슬래시 2개 사용
```
