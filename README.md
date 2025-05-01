# 🔁 Real-Time Character Stream with Flask & SSE

This project demonstrates how to stream characters one-by-one from a Flask backend to a web browser using **Server-Sent Events (SSE)** — with a smooth loop and erase effect!

> 🌐 Real-time.  
> 🎬 Animated.  
> 🎨 Beautiful background.  
> 💡 Perfect for learning live data streams.

---

## 🚀 Features

- ⏳ Streams characters one by one.
- 🔄 Loops the word infinitely.
- ❌ Clears the word before restarting.
- 🎨 Stylish UI with a scenic background.
- ⚡ Built with pure Python and JavaScript (no frameworks).

---

## 📸 Preview

![preview](https://github.com/your-username/your-repo-name/assets/demo-gif.gif)  
<sup>(Replace this with a real GIF or screenshot)</sup>

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Vanilla JavaScript
- **Streaming**: Server-Sent Events (SSE)

---

## 📁 Project Structure

. ├── app.py ├── templates │ └── index.html └── static (optional)

yaml
Copy
Edit

---

## 🧪 Run Locally

### 1. Clone the repo
bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Create a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
bash

pip install flask
4. Run the server

python app.py
Visit http://localhost:5000 to see it in action!

🎨 Customize
To change the word being streamed, open app.py and modify:

python

word = "Shreyas Shridhar Kulkarni"
You can also change the background image by editing the CSS in index.html.

🤝 Contributing
Feel free to fork the repo and submit pull requests. All improvements are welcome!

