# 📘 Quizora

**Quizora** is a modern, AI-enhanced learning platform that helps learners prepare smarter for exams through adaptive learning, dynamic mock quizzes, collaborative tools, and intelligent study aids.

> 🚀 Empowering students through personalized learning experiences.

---

## 🧠 Key Features

### 🎯 mock quiz Engine
- Dynamic mock quiz generation based on user performance
- Question pool management with tagging (topic, difficulty, etc.)
- Exam session tracking (pause/resume support)

### 📊 Adaptive Learning
- Mastery, maturity, and growth metric calculations
- Personalized analytics by topic/module
- AI-powered study suggestions and feedback

### ✍️ Study Tools
- Auto-generated notes from mistakes
- Flashcard creation (manual or auto)
- Export notes and flashcards as PDF or Markdown

### 👥 Community & Collaboration
- Upload and share mock quizzes via the marketplace
- Tag and filter shared modules (subject, grade level, popularity)
- Rate/review content and participate in community forums

### 🧩 Gamification
- XP system and achievements for milestones
- Leaderboards (global and school-based)
- Limited-time challenges/quests with rewards

### 📱 Mobile Features
- Voice-to-text search
- Offline access for downloaded materials
- Sync on reconnection

### 📈 Analytics & Reports
- mock quiz performance reports (PDF, CSV exports)
- Usage analytics for platform improvement

### 🔐 Security & System
- Full encryption (at-rest and in-transit)
- API rate limiting/throttling
- Secure payment and licensing for premium content

---

## 📦 Tech Stack

| Layer       | Tech                                                                 |
|-------------|----------------------------------------------------------------------|
| Frontend    | React, TailwindCSS, Framer Motion                                    |
| Backend     | Django (REST Framework)                                              |
| Realtime    | Flutter (cross-platform)                                             |
| Database    | PostgreSQL (profile, structure), MongoDB (logs, attempts, comments)  |
| Auth        | Auth0                                                                |
| AI Features | OpenAI API (notes, summaries, tag suggestions)                       |
| Mobile      | Flutter (cross-platform)                                             |
| Core Lib    | Samocka (Python-based open-source core logic module)                 |
| Payment     | Stripe                                                               |


---

## ⚙️ Setup Guide

### 1. Clone the Repository

```
git clone https://github.com/your-org/quizora.git
cd quizora
```

### 2. Backend Setup (Django)

```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 3. Database Setup

#### ➤ PostgreSQL

```
# Install and create database
createdb quizora_profile_db
```

#### ➤ MongoDB

```
# Local Mongo or Atlas
MONGODB_URI=mongodb://localhost:27017/quizora_logs
```

### 4. Frontend (React)

```
cd frontend
npm install
npm run dev
```

### 5. Mobile (Flutter)

```
cd mobile
flutter pub get
flutter run
```

---

## 🧪 Testing

```
# Run backend tests
pytest

# Frontend tests
npm test

# Mobile tests
flutter test
```

---

## 🤝 Open Source & Collaboration

Quizora is proudly open source and welcomes **contributors, testers, educators, and learners** from around the world. Whether you're here to fix a bug, build a new feature, or improve documentation — you're invited.

**Ways to contribute:**

* Submit PRs and issues
* Suggest improvements to the AI logic
* Share mock quiz content modules
* Translate or localize the platform

*We believe in building this platform for and with the community.*

---

## 🏷️ Suggested Labels

| Type         | Examples                                      |
| ------------ | --------------------------------------------- |
| Feature Type | `feature`, `enhancement`, `refactor`, `fix`   |
| Priority     | `priority: high`, `priority: medium`          |
| Status       | `in progress`, `needs review`, `blocked`      |
| Module       | `mock-exam`, `study-tools`, `analytics`, etc. |

---

## 📄 License

This project is licensed under the **Apache License 2.0**.

You may obtain a copy of the License at
[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

---

## 🙌 Acknowledgments

Thanks to:
- **Students and Users** who tested early versions, shared feedback, and proved that adaptive learning works.
- **Contributors and Developers** who committed their code, ideas, and time to help build a better learning experience.
- And to anyone who’s shared, contributed, or tested — you rock. 💙

---

## 📬 Contact

💌 **[team@quizora.io](mailto:razstviendev@gmail.com)**
🌐 [https://quizora.io](https://quizora.io)