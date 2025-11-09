# Pomodoro Timer ⏱️

A simple, customizable **Pomodoro productivity timer** built with **Python** and **Tkinter**.
This app helps you stay focused by cycling between focused work sessions and short/long breaks, visually tracking progress and time remaining.

---

## ✅ Features

* ✔ 25-minute Pomodoro work sessions
* ✔ Short breaks after each Pomodoro
* ✔ Long break after a full cycle
* ✔ Visual countdown timer
* ✔ Start, Reset, and interactive UI
* ✔ Built with Python + Tkinter (no extra dependencies)

---

## 🖥️ Screenshot

```
![Pomodoro Timer Screenshot](./screenshot.png)
```



## ▶️ How to Run

From a terminal:

```bash
python main.py
```

Tkinter will launch automatically and start the app.

---

## 🧩 Project Structure

```
pomodoro/
│
├── main.py               # main application
├── README.md             # documentation
└── screenshot.png        # image
└── tomato.png            # image
```

## ⚙️ How It Works

| Mode        | Duration | Trigger                         |
| ----------- | -------- | ------------------------------- |
| Pomodoro    | 25 min   | Start button / after break ends |
| Short Break | 5 min    | After each Pomodoro             |
| Long Break  | 20 min   | After every 4 Pomodoros         |

You can modify timings directly inside `main.py` if you want custom session lengths.

Example:

```python
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
```

---

## ✅ Future Improvements

* ✅ Add sound notifications
* ✅ Add dark mode UI theme
* ✅ Add task tracking
* ✅ Add settings to customize times

---

## 🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss what you’d like to add.

---

## 📄 License

MIT License – feel free to modify and reuse.
