#!/usr/bin/env python
# coding: utf-8

# # 파이썬을 이용한 퀀트 투자 포트폴리오 만들기
# 
# ## 지은이 소개
# 
# 이현열
# 
# 한양대학교에서 경영학을 전공하고, 카이스트 대학원에서 금융공학 석사 학위 취득 후 한양대학교 재무금융 박사 과정을 수료했다. 국내 증권사, 운용사, 보험사를 거치며 각각 주식 운용, 퀀트 포트폴리오 매니저, 데이터 분석 업무를 경험했고, 현재는 데이터 기술 기반의 핀테크 기업인 두물머리에서 데이터 분석 및 퀀트 업무를 담당하고 있다. 또한 한양대학교에서 겸임교수로 재직중이며 데이터분석과 퀀트 관련 수업을 맡고 있다.
# 
# 지은 책으로는 《스마트베타》(2017), 《R을 이용한 퀀트 투자 포트폴리오 만들기》(2019),《감으로 하는 투자 데이터로 하는 투자》(2022)가 있으며, 번역한 책으로는 《효율적으로 비효율적인 시장》(2021)이 있다.
# 
# 본 책의 강의영상은 유튜브에 업로드 될 예정이다.
# 
# - 채널명: 헨리의 퀀토피아
# 
# ```{figure} image/qr.png
# ---
# scale: 15%
# name: qr
# ---
# ```
# 
# ## 머리말
# 
# 2019년 'R을 이용한 퀀트 투자 포트폴리오 만들기'의 출간 이후 너무나 많은 분들이 파이썬 버전의 출간을 문의하셨습니다. 그때부터 틈틈히 코드와 글을 작성하기 시작해 3년이라는 긴 시간이 지나서야 이번 책이 완성될 수 있었습니다. 단순히 R로 작성되었던 내용을 파이썬으로 바꾼것에 그친것이 아니라, 많은 부분을 업데이트 하였습니다. 먼저, 파이썬을 처음 접하는 분들을 위해 기초적인 사용법에서부터  데이터 분석에 대한 내용에 이르기까지 기본적인 내용을 모두 다루었습니다. 또한 수집한 각종 데이터를 엑셀이나 CSV 파일로 저장하는 방법이 아닌 데이터베이스에 저장하고 SQL을 통해 꺼내쓰도록 하였습니다. 이를 통해 효율적으로 데이터를 관리할 수 있고, 실무에서 사용하는 퀀트 투자 프로세스와 유사한 환경을 구축할 수 있습니다.
# 
# 기존의 책은 국내 주식 데이터만을 수집하던 것에 그쳤던 반면, 이번에는 전 세계 모든 주식의 데이터를 수집하는 방법도 다루었습니다. 또한 퀀트 전략을 이용한 종목선정 뿐만 아니라, 기술적 지표를 이용한 트레이딩 방법과 백테스트도 다루었습니다. 마지막으로 어떤 종목에 투자할지 선택하는데 그치지 않고 증권사 API를 이용해 자동으로 매매 및 리밸런싱을 하는 방법까지 다루었습니다.
# 
# 이 책을 통해 독자분들도 파이썬을 이용한 금융 데이터 수집 및 처리, 퀀트 모델 개발, 포트폴리오 분석 및 자동매매 등이 가능하리라 생각합니다. 또한 실제 전문 투자자들이 사용하는 기술들도 포함했으니 책의 내용을 넘어 더욱 훌륭한 모델을 만드는 데 도움이 되시리라 생각합니다. 후배들에게 몇 년에 걸쳐 배워야 하는 퀀트 투자 프로세스를 단계별로 알려준다는 마음으로 책을 썼습니다. 퀀트 투자를 시작하는 여러분들에게 좋은 길잡이가 되었으면 좋겠습니다. 험난한 투자의 세상에서 데이터를 이용한 객관적이고 장기적인 투자로 성공하시길 기원합니다.
# 
# 2022년 8월
# 
# 이현열
# 
# ## 이 책의 구성
# 
# 이 책은 크게 세 부분으로 구성되어 있다.
# 
# 먼저 첫번째 부분은 퀀트에 대한 이해 및 본 책의 이해를 위해 파이썬과 SQL의 기본적인 사용법에 대해 배운다.
# 
# - 1장: 퀀트가 무엇인지에 대해 알아보며, 프로그래밍을 사용해야 하는 이유에 대해 알아본다.
# - 2장: 파이썬의 기초에 대해 배운다.
# - 3장: pandas 패키지를 이용한 데이터 분석에 대해 배운다.
# - 4장: 데이터를 시각화로 나타내는법에 대해 배운다.
# - 5장: SQL의 기초에 대해 배운다.
# - 6장: 파이썬에서 SQL을 연결한 후 사용하는 법에 대해 배운다.
# 
# 두번째 부분은 크롤링을 이용해 각종 데이터를 수집하는 법에 대해 배운다.
# 
# - 7장: 크롤링을 통한 데이터 수집에 앞서 인코딩, 웹의 동작 방식, HTML에 대한 기본 정보에 대해 배운다.
# - 8장: 정적 크롤링을 하는 방법에 대해 배운다.
# - 9장: 동적 크롤링을 하는 방법과 정규 표현식을 이용하는 방법에 대해 배운다.
# - 10장: 국내 주식과 관련된 종목코드, 섹터정보, 주가, 재무제표, 가치지표를 수집하는 법에 대해 배운다.
# - 11장: 미국 뿐만 아니라 전 세계 주식 데이터를 수집하는 법에 대해 배운다.
# - 12장: 투자에 필요한 공시 정보 및 각종 지표를 수집하는 법에 대해 배운다.
# 
# 세번째 부분은 종목 선정, 포트폴리오를 구성, 백테스트 및 실제 매매를 하는 법에 대해 배운다.
# 
# - 13장: 각종 퀀트 전략을 이용해 기본적인 종목선정부터 고급 방법론까지 배운다.
# - 14장: 최적의 포트폴리오를 구성하는 방법에 대해 배운다.
# - 15장: 기술적 지표에는 어떠한 것이 있는지에 대해 배운다.
# - 16장: 백테스팅을 하고 결과를 해석하는 법에 대해 배운다.
# - 17장: 증권사에서 제공하는 API를 이용해 포트폴리오를 자동 매매하는 법에 대해 배운다.
# 
# ## 이 책의 지원 페이지
# 
# 이 책은 파이썬의 jupyterbook 패키지로 작성되어 웹페이지 및 GitHub 저장소에 공유되어 있다. 따라서 책에 포함되어 있는 각종 코드를 웹페이지에 방문하여 얻을 수 있으며, 하단의 댓글 부분을 통해 질문사항을 남길수도 있다. 이 외에도 퀀트 투자 및 파이썬, R을 이용한 투자 활용법 등의 내용은 저자의 블로그에 많은글들이 있으니 참조하기 바란다.
# 
# - 웹페이지: https://hyunyulhenry.github.io/quant_py/
# - GitHub 저장소: https://github.com/hyunyulhenry/quant_py
# - Henry's Quantopia: https://blog.naver.com/leebisu
# 
# ## 종목과 관련된 유의사항
# 
# 종목선정과 관련된 장에서 나오는 결과는 해당 종목에 대한 매수 추천이 아님을 밝히며, 데이터를 받은 시점의 종목이기에 독자 여러분이 책을 읽는 시점에서 선택된 종목과는 상당한 차이가 있다. 또한 이 책에서 다루는 모델을 이용하여 투자를 할 경우, 이로 인한 이익과 손해는 본인에게 귀속됨을 알린다.