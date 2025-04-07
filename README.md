
# 🌐 Language Learning Chatbot

A Django-based chatbot that helps users learn new languages interactively using AI from Hugging Face. It simulates real-life conversations, corrects mistakes, tracks progress, and provides personalized feedback.

**Repo:** https://github.com/nakulsejwar/language_bot

---

## 🚀 Features

- Choose a language to learn + your current level
- AI-generated interactive conversations using Hugging Face
- Real-time grammar correction
- Tracks user mistakes with SQLite
- Final review and feedback for improvement
- Minimal, clean CSS-styled UI

---

## 🧠 Tech Stack

- **Backend:** Django (Python)
- **AI:** Hugging Face Transformers
- **Database:** SQLite
- **Frontend:** HTML & CSS (no JS)

---

## 📁 Project Structure

```
language_bot/
├── chatbot/
│   ├── templates/
│   │   └── chatbot.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── ...
├── language_bot/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── static/
│   └── style.css
├── ui.png
├── manage.py
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/nakulsejwar/language_bot.git
cd language_bot
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Run database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to chat with the bot.

---

## 🖼 UI Preview

Here’s what the chatbot UI looks like:

![Chatbot UI](https://github.com/nakulsejwar/language_bot/blob/main/ui.png)

---

## 💬 How it Works

1. User enters language preferences and level
2. AI sets a conversation scene and chats in the chosen language
3. Bot tracks and saves grammar/vocab mistakes using SQLite
4. At the end, a summary is shown to help users improve

---

## ✅ Submission Checklist

- Django backend with AI chatbot logic
- Mistake tracking using SQLite
- Hugging Face NLP model integration
- Clean form-based CSS UI
- Final README + video + architecture doc

---

## 👨‍💻 Author

**Nakulsingh Sejwar**  
🔗 [GitHub](https://github.com/nakulsejwar)  
📧 sejwarnakulsingh@gmail.com

---

## 📄 License

Free to use for learning, demo, and educational purposes.

---

## 🙌 Acknowledgements

- [Hugging Face](https://huggingface.co/)
- Django Project Docs
