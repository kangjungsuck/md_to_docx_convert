# notion md to docx

- 먼저 docx 또는 hwp파일을 다음과 같이 편집하여 노션으로 옮긴다 [링크](https://www.notion.so/eb483e459da24fd6aee680a36de6e3bc?pvs=4)

- 그리고 노션에 api만들기

1. 완성해서 노션에 옮겨온 원고를 그대로 복붙하고,
2. 데이터베이스의 Name은 글 제목(화면에 표시 될 글 제목입니다.)
3. 데이터베이스의 Order는 각 버튼(0~10)에 매칭됩니다.
4. 데이터베이스의 Keyword는 글에 해시태그나 키워드 있는 경우에, 해당 부분 입력해주시면 됩니다.
5. 데이터베이스의 author에는 저자명, title에는 글 제목입니다.
6. 글 내 이미지는 아래와 같이 적어주시면 제일 좋을 거 같습니다.

- [image-1] 내용…
- [image-2] 내용…
- [image-3] 내용…

- 이후 이 노션 api문서를 docx로 빼야 하는 경우, 주석이 반영되지 않는다. 따라서 이 프로그램을 이용하면 된다.
- 폴더 내에서 터미널 열고, 다음과 같이 권한 설정 chmod +x md_to_docx_convert.sh
- pandoc을 brew이용해 설치.
- 이후 폴더 내에서 ./md_to_docx_convert.sh 실행
- 나오는 프롬프트 따라서 진행.
- 로그는 app{timestamp}.log 형식으로 같이 저장된다.
