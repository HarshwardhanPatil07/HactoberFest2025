# 🕒 Task Scheduler (Single File Project)

A **lightweight background job scheduler** written in **pure Python**, featuring:

- 🧠 OOP-based design
- 📝 Job registration via decorators
- 🔁 Automatic retry mechanism
- 🧹 Clean logging and error handling
- ⚙️ Configuration via `dataclass`
- ✅ Single-file structure — easy to copy, run, and extend

This project is perfect for learning **clean Python architecture**, **decorators**, **logging**, and **task automation** — all in a single file.

---

## 🚀 Features

| Feature                        | Description                                            |
| ------------------------------ | ------------------------------------------------------ |
| ⚙️ **OOP Architecture**        | Uses classes for jobs, config, and scheduler logic     |
| 🧩 **Decorator-based Jobs**    | Register tasks easily with `@scheduler.job()`          |
| 🔁 **Retry Mechanism**         | Retries failed jobs automatically up to `max_retries`  |
| 📜 **Structured Logging**      | Clear log output with timestamps and levels            |
| 🧠 **Smart Interval Checking** | Executes jobs only when their time interval has passed |
| 💡 **Extensible Design**       | Add more jobs or integrate async/event-driven logic    |

---

## 📦 Requirements

- Python **3.8+**
- No external dependencies (uses only Python’s standard library)

---
