

````markdown
# 🤖 GPT-2 Chatbot — Command Line & Web UI

A simple chatbot powered by **GPT-2**, usable both from the **command line** and via a **Gradio web interface**.

---

## 📂 Project Files

- `gpt2cmd.py` → Chatbot for the **Command Line**
- `chatbotUi.py` → Chatbot with a **Web UI** (Gradio)

---

## ⚙️ Setup Instructions

### 1. 🔁 Clone the Repository

```bash
git clone https://github.com/your-username/gpt2local.git
cd gpt2local
````

> Replace `your-username` and `your-repo-name` with your actual GitHub info.

---

### 2. 🧪 Create and Activate Virtual Environment

#### ✅ On Windows:

```bash
python -m venv env
env\Scripts\activate
```

#### ✅ On Linux/macOS:

```bash
python3 -m venv env
source env/bin/activate
```

---

### 3. 📦 Install Dependencies

Create a file named `requirements.txt` with the following content:

```text
transformers
tensorflow
gradio
```

Then install all dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 🖥️ A. Run from Command Line

```bash
python gpt2cmd.py
```

You’ll be prompted with:

```
Enter your prompt:
```

Type your message and GPT-2 will respond.

---

### 🌐 B. Run Web UI (Gradio)

```bash
python chatbotUi.py
```

This will launch a local web server at:

```
http://127.0.0.1:7860
```

You can interact with GPT-2 directly in your browser.

---

## 🧠 Model Info

* **Base Model**: `gpt2` from Hugging Face
* **Framework**: TensorFlow (`TFGPT2LMHeadModel`)
* **UI**: Gradio
* **Generation Parameters**:

  * `max_length=100`
  * `temperature=0.8`
  * `top_p=0.9`
  * `top_k=50`

---

## 🧾 Example Output

**Prompt:** `hi hello`

**Generated Text:**

```
hi hello !!!

I'm from the UK, I live in the UK, so I live in the UK

I'm happy to see you there!

Thanks for your time!

Yours truly,

Kathy
```

---

## 🔧 Optional Enhancements

* Add conversation memory
* Allow prompt history
* Fine-tune GPT-2 on your own data
* Save chat logs

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🤝 Contributing

Feel free to fork, open issues, or submit pull requests to improve the chatbot.

---

## 🔗 Helpful Links

* [🤗 GPT-2 on Hugging Face](https://huggingface.co/gpt2)
* [Transformers Documentation](https://huggingface.co/docs/transformers)
* [Gradio Documentation](https://www.gradio.app/)

```

---
```
