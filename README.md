# Telegram Weekly Poll Bot

ربات تلگرام برای ارسال نظرسنجی هفتگی در گروه/کانال - قابل استقرار روی GitHub Actions (رایگان، بدون سرور).

## ویژگی‌ها
- ✅ **Serverless** - اجرا روی GitHub Actions (رایگان)
- ✅ **امن** - توکن و چت‌آیدی در GitHub Secrets (repo عمومی امن)
- ✅ **نظرسنجی‌های بومی** - دکمه‌های چند انتخابی، آمار زنده
- ✅ **زمان‌بندی انعطاف‌پذیر** - Cron در workflow
- ✅ **اجرای دستی** - از تب Actions هر لحظه

## فایل‌های پروژه
```
├── questions.json          # بانک سوالات (قابل ویرایش)
├── send_poll.py            # اسکریپت ارسال نظرسنجی
├── requirements.txt        # وابستگی‌ها (aiogram)
├── .github/workflows/
│   ├── weekly-poll.yml     # زمان‌بندی هفتگی (Cron)
│   └── manual-send.yml     # ارسال دستی با انتخاب سوال
└── .gitignore
```

## راه‌اندازی (۵ دقیقه)

### ۱. Fork / Clone این ریپو
```bash
git clone https://github.com/YOUR_USERNAME/telegram-poll-bot.git
cd telegram-poll-bot
```

### ۲. توکن ربات و Chat ID را در GitHub Secrets ذخیره کنید
**Settings → Secrets and variables → Actions → New repository secret**

| Name | Value | منبع |
|------|-------|------|
| `BOT_TOKEN` | `123456:ABC-DEF...` | [@BotFather](https://t.me/BotFather) |
| `CHAT_ID` | `-1001234567890` | [@RawDataBot](https://t.me/RawDataBot) در گروه |

> **نکته:** `CHAT_ID` برای گروه/سوپرگروه با `-100` شروع می‌شود. ربات باید **ادمین** گروه باشد.

### ۳. سوالات را در `questions.json` ویرایش کنید
```json
[
  {
    "id": 1,
    "text": "سلام! امروز چطور؟",
    "options": ["عالیه!", "معمولیه", "خسته‌ام"],
    "multiple_choice": true
  }
]
```
- `multiple_choice: true` = چند انتخابی (چک‌باکس)
- `multiple_choice: false` = تک انتخابی (راديو)

### ۴. زمان‌بندی را در `.github/workflows/weekly-poll.yml` تنظیم کنید
```yaml
schedule:
  - cron: '0 6 * * 1'  # دوشنبه 06:00 UTC = 09:30 ایران (تابستانی)
```
[Cron Guru](https://crontab.guru/) برای محاسبه زمان.

### ۵. Push کنید و تست کنید
```bash
git add .
git commit -m "Setup poll bot"
git push
```
برو به تب **Actions → Weekly Poll → Run workflow** برای تست فوری.

## دستورات دستی

### ارسال نظرسنجی تصادفی
Actions → **Manual Poll Send** → Run workflow

### ارسال نظرسنجی خاص
Actions → **Manual Poll Send** → Run workflow → `question_id: "2"`

## ساختار سوال
```json
{
  "id": 1,
  "text": "متن سوال",
  "options": ["گزینه ۱", "گزینه ۲", "گزینه ۳"],
  "multiple_choice": true
}
```

## محاسبه زمان ایران
| فصل | UTC Offset | مثال Cron (دوشنبه ۹:۳۰) |
|-----|------------|------------------------|
| تابستانی ( primeros ۶ ماه) | UTC+3:30 | `0 6 * * 1` |
| زمستانی (دومین ۶ ماه) | UTC+4:30 | `0 5 * * 1` |

## عیب‌یابی
| خطا | راه‌حل |
|------|--------|
| `401 Unauthorized` | BOT_TOKEN اشتباه |
| `Bad Request: chat not found` | CHAT_ID اشتباه یا ربات در گروه نیست |
| `Forbidden: bot was kicked` | ربات را دوباره ادمین کنید |
| Poll ارسال نمی‌شود | لاگ‌های Actions را چک کنید |

## لایسنس
MIT - آزاد برای استفاده شخصی و تجاری.