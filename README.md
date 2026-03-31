# 🔗 URL Shortener (Offline)

A simple Python-based URL shortener that allows you to store, retrieve, and delete shortened URLs using a local JSON file.

## 🚀 Features

* ✅ Save long URLs with custom short names
* 🔍 Retrieve original URLs using short names
* 🗑️ Delete saved URLs
* 💾 Persistent storage using JSON
* ⚠️ Error handling for missing or corrupted files
* 📋automaticlly copies long url to clipboard
* 🌐automattically open website in broswer

## 🧠 How It Works

This program stores URL mappings in a file called `short_urls.json`.

Each entry looks like:

```json
{
    "yt": "https://youtube.com",
    "gh": "https://github.com"
}
```

## 🖥️ Usage

Run the program:

```bash
python main.py
```

Then choose an option:

```
1 → Save new URL  
2 → Retrieve URL  
3 → Delete URL  
4 → Exit  
```

## 📂 Project Structure

```
.
├── main.py
├── short_urls.json
└── README.md
```

## 🛠️ Technologies Used

* Python 3
* JSON (for storage)

## 📈 Future Improvements

* 🔒 Prevent duplicate short names
* 🎲 Auto-generate short URLs
* 🖼️ Add GUI (Tkinter)
* 📋 List all saved URLs

## 👨‍💻 Author

**Hasan**
Aspiring AI & Robotics Engineer 🚀

---

## ⭐ Notes

This project is part of my journey to learn Python, build real-world applications, and work toward advanced fields like AI and robotics.
