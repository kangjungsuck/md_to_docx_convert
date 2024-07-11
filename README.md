# notion md to docx converter
전시 <게임사회> 부록 웹사이트 원고 편집 작업을 돕기 위함. 

## 0. 먼저 docx 또는 hwp파일을 다음과 같이 편집하여 노션으로 옮긴다 [링크](https://www.notion.so/eb483e459da24fd6aee680a36de6e3bc?pvs=4)

안녕하세요. 각 필자분들에게 안내해서 아래처럼 진행한다면, 제일 좋을 거 같습니다.

## 1. 필자 분들 최종파일 안내:

`주의:` 가능하면 워드 또는 구글문서로 진행해 주심면 고맙겠습니다. 아래아 한글로 작업하신 경우엔, .docx로 저장해 보내주시기 바랍니다.

- 다음의 스타일은 반영됩니다. :
  - 볼드, 이탤릭, 취소선, 밑줄, 헤딩 1, 2, 3
  - 불렛(닷) 리스트, 숫자 리스트. 그 외의 리스트 양식을 사용하는 경우 , 빨간 색으로 표시해주시기 바랍니다(예: 로마자 리스트)
  - 인용구
  - 각주(반드시 각주 기능을 사용해서 달아주세요)
    - 워드 각주 다는 법: `Ctrl+Alt+F` 입니다.
    - 아래아 한글 각주 다는 법: `Ctrl+N,N(2번 누른단 의미)`
    - 구글문서 각주 다는 법: `Ctrl+Alt+F`
- 이미지는 다음의 방식으로 전달해주시기 바랍니다:
  - 필자명 폴더 생성
  - 폴더에 글의 이미지를 숫자로 이름지어 넣기 `1.bmp`, `2.png`, `3.jpg`

감사합니다.

## 2. PACK에서 수정

`주의:` 내부에서 하는 경우 업무량이 좀 됩니다. 반나절 이상 뺏길 가능성이 높습니다.

### 워드에서 노션으로

- 워드에서 노션으로 복사-붙여넣기 하세요
- 자동으로 따라오는 것들:
  - 볼드, 이탤릭, 밑줄, 취소선, 헤딩1,2,3
  - 불렛 리스트, 넘버 리스트
  - 각주도 [1] 이런 모양으로 들어옴. 건드리지 않아도 됌
- 수동 작업 필요한 것들:
  - 인용(quote, blockquote 스타일 지정)은 자동으로 들어오지 않음. 수동으로 작업해주어야 함. `/quote`
  - 리스트 중 가, 나, 다, a, b, c 같은 것들.
  - 엔터 두번으로 문단 한줄 공백 넣은 부분.

### 한컴오피스(한/글)에서 노션으로

- 한글에서 노션으로 올 때는 다른 이름으로 저장해서 docx로 저장한 후, 이를 열어 복사-붙여넣기 하셔야 합니다.
- 자동으로 따라오는 것들:
  - 볼드, 이탤릭, 밑줄, 취소선, 헤딩1
  - 각주도 [1] 이런 모양으로 들어옴. 건드리지 않아도 됌
- 수동 작업 필요한 것들:
  - 인용(quote, blockquote 스타일 지정)은 자동으로 들어오지 않음. 수동으로 작업해주어야 함.
  - 헤딩 1, 2, 3 수동으로 지정해주어야 함. `/quote`
  - 리스트 중 가, 나, 다, a, b, c 같은 것들
  - 엔터 두번으로 문단 한줄 공백 넣은 부분.

### 글의 이미지 전달

- 구글 드라이브 폴더 혹은 압축파일로 받습니다 : `jungsuck@pack.systems`
- 각 필자 폴더를 만들고
- 필자 폴더 글 내 이미지 이름은 순서대로 주시면 됩니다 `1.bmp`, `2.png`, `3.jpg`

## 그리고 노션에 api만들기

### 내용

1. 완성해서 노션에 옮겨온 원고를 그대로 복붙하고,
2. 데이터베이스의 Name은 글 제목(화면에 표시 될 글 제목입니다.)
3. 데이터베이스의 Order는 각 버튼(0~10)에 매칭됩니다.
4. 데이터베이스의 Keyword는 글에 해시태그나 키워드 있는 경우에, 해당 부분 입력해주시면 됩니다.
5. 데이터베이스의 author에는 저자명, title에는 글 제목입니다.
6. 글 내 이미지는 아래와 같이 적어주시면 제일 좋을 거 같습니다.

- [image-1] 내용…
- [image-2] 내용…
- [image-3] 내용…

## 이제 이 프로그램을 쓰자.

- 이후 이 노션 api문서를 docx로 빼야 하는 경우, 주석이 반영되지 않는다. 따라서 이 프로그램을 이용하면 된다.
- 폴더 내에서 터미널 열고, 다음과 같이 권한 설정 `chmod +x md_to_docx_convert.sh`
- pandoc을 brew이용해 설치.
- 이후 폴더 내에서 `./md_to_docx_convert.sh` 실행
- 나오는 프롬프트 따라서 진행.
- 로그는 app{timestamp}.log 형식으로 같이 저장된다.
