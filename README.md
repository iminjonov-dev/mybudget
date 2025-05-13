# 💰 MyBudget — Income & Expense Tracker

MyBudget — bu foydalanuvchilar uchun shaxsiy moliyaviy harajatlar va daromadlarni kuzatish imkonini beruvchi web ilova. Ilova yordamida foydalanuvchi oylik byudjetini boshqaradi, hisobotlar oladi, hisobni oila a'zolari bilan bo'lishadi va tahlil qiladi.

---

## 🚀 Loyiha imkoniyatlari

### 👤 Authentifikatsiya
- Oddiy ro'yxatdan o'tish va login
- Email orqali OTP bilan tasdiqlash
- Google bilan kirish (OAuth 2.0)
- Maxfiylikni saqlovchi parolni o'zgartirish sahifasi

### 💵 Income va Expense modullari
- Kirim va chiqimlarni qo'shish
- Toifalarga ajratish (Oylik, Avans, Biznes, Transport, Oziq-ovqat, boshqalar)
- Naqd, karta yoki valyutada kiritish

### 📊 Hisobot va Tahlil
- Daromad va xarajatlar ro'yxati
- Joriy balans avtomatik hisoblanadi
- Hisobotlarni PDF yoki Excel formatida yuklab olish

### 👪 Family Sharing (Family Mode)
- Oila byudjeti uchun umumiy guruh yaratish
- Guruhga a’zolar qo‘shish/olib tashlash (admin orqali)

### 🌐 Til tanlash
- Ilova 3 tilda ishlaydi: O'zbekcha 🇺🇿, Ruscha 🇷🇺, Inglizcha 🇬🇧

### ⚙️ API va DRF
- Barcha CRUD amallar DRF orqali API ko‘rinishida mavjud
- Swagger (drf-yasg) orqali hujjatlashtirilgan

---

## 🛠 Texnologiyalar

| Texnologiya         | Tavsif                              |
|---------------------|--------------------------------------|
| Python 3.12         | Backend tili                         |
| Django 5.2.1        | Asosiy web framework                 |
| Django Rest Framework | API yaratish                       |
| drf-yasg            | Swagger dokumentatsiyasi             |
| dj-rest-auth + allauth | Authentifikatsiya va social login |
| Gunicorn            | Production server                    |
| SQLite              | Ma’lumotlar bazasi (developmentda)  |
| HTML/CSS            | Frontend interfeys                   |

---

## 📦 O‘rnatish (Lokalda)

```bash
git clone https://github.com/iminjonov-dev/mybudget.git
cd mybudget
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
