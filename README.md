# Telegram English Expression Bot

GitHub Actions로 5분마다 텔레그램으로 영어 표현을 보내주는 봇입니다.

## 프로젝트 구조

```
english-daily-bot/
├── .github/workflows/daily-expression.yml
├── data/expressions.json
├── send_expression.py
├── requirements.txt
└── README.md
```

## 설정 방법

### 1. 텔레그램 봇 생성

1. 텔레그램에서 [@BotFather](https://t.me/BotFather)에게 `/newbot` 명령
2. 봇 이름과 username 설정
3. 발급받은 **Bot Token** 저장

### 2. Chat ID 확인

1. 생성한 봇에게 아무 메시지 전송
2. 브라우저에서 `https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates` 접속
3. 응답에서 `chat.id` 값 확인

### 3. GitHub Secrets 설정

리포지토리 > Settings > Secrets and variables > Actions에서:

- `TELEGRAM_BOT_TOKEN`: 봇 토큰
- `TELEGRAM_CHAT_ID`: 채팅 ID

### 4. 푸시하면 완료

코드를 GitHub에 푸시하면 5분마다 자동으로 영어 표현이 전송됩니다.

수동 실행: Actions 탭 > "Send English Expression" > "Run workflow"
