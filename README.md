

# 🍽️ BBQ Nation AI Assistant

An advanced **Conversational AI Assistant** tailored specifically for **BBQ Nation restaurants** in **Delhi** and **Bangalore**, designed to enhance customer experience by streamlining table reservations, booking modifications, and frequently asked questions.

---

## 🚀 Key Features

* 🤖 **Intelligent FAQ System**
  Context-aware responses to customer queries about timings, menu, offers, and more.

* 📅 **Effortless New Reservation Flow**
  Quickly reserve a table based on user preferences and real-time availability.

* 🔁 **Modify or Cancel Bookings**
  Easily manage existing reservations with simple interactions.

* 📍 **Location-Specific Knowledge Base**
  Smart, localized responses based on restaurant branches in Delhi and Bangalore.

* 🔄 **Real-Time State Machine Flow**
  Ensures smooth, contextual multi-turn conversations.

* 📊 **Post-Call Analysis**
  Tracks performance and user satisfaction to improve future interactions.

---

## ⚙️ Functionalities

* ✅ Create new reservations
* 🔄 Modify existing bookings
* ❌ Cancel reservations
* 📖 Provide detailed answers about:

  * Menu
  * Operating hours
  * Ongoing offers
  * Branch-specific info

---

## 🗂️ API Structure

Here are some working API endpoints used by the assistant:

* 🔗 **Properties**
  `GET http://127.0.0.1:8000/api/kb/properties`

* 🔗 **Branches**
  `GET http://127.0.0.1:8000/api/kb/branches`

* 🔗 **Categories**
  `GET http://127.0.0.1:8000/api/kb/categories`

---

## 🛠️ Installation

Follow the steps below to set up the project locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ARORA-PRACHI/Formi-Assignment.git
cd Formi-Assignment
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
uvicorn main:app --reload
```

---

## 🧰 Tech Stack

| Technology       | Description                     |
| ---------------- | ------------------------------- |
| **FastAPI**      | High-performance API framework  |
| **Pydantic**     | Schema validation & type hints  |
| **Python 3.10+** | Core backend logic              |
| **Jinja2**       | Dynamic template rendering      |
| **Uvicorn**      | ASGI server for running FastAPI |

---

## 🧪 Testing

Run unit tests using:

```bash
pytest tests/
```

---

## 🤝 Contributing

We welcome contributions from the community. Here's how you can contribute:

1. **Fork** this repository
2. **Create** a new feature branch
3. **Commit** your changes with meaningful messages
4. **Open a Pull Request** for review

---

## 📬 Contact

For questions, suggestions, or support, feel free to get in touch:

* 📧 Email: [prachi659.be22@chitkara.edu.in](mailto:prachi659.be22@chitkara.edu.in)
* 🌐 Website: [www.bbqNation.com](https://www.bbqNation.com)

---

