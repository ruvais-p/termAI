Here’s a **`README.md`** for your `termAI` project with all setup and execution instructions.

---

```markdown
# termAI

**termAI** is an AI-powered terminal assistant that converts natural language prompts into shell commands using Google's Gemini API.  
It can also fix broken shell commands and manage API keys.

---

## **Features**
- Convert natural language to Linux shell commands.
- Execute or preview commands before running.
- Fix broken commands using error messages.
- Manage your Google Gemini API key (`set`, `show`, `clear`).
- Easy-to-use CLI with `ata` command.

---

## **Project Structure**
```

termAI/
│── ai\_terminal\_assistant/
│   ├── **init**.py
│   ├── cli.py
│   ├── core.py
│   ├── config.py
│── main.py
│── geminikey.txt
│── setup.py
│── pyproject.toml
│── README.md

````

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/termAI.git
cd termAI
````

### **2. Create and Activate a Virtual Environment**

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows
```

### **3. Install the Project**

Install in editable mode for development:

```bash
pip install -e .
```

---

## **Setup API Key**

**Set your Gemini API key:**

```bash
ata key set YOUR_API_KEY
```

**Show the current key:**

```bash
ata key show
```

**Clear the key:**

```bash
ata key clear
```

---

## **Usage**

### **Run a Command**

Convert a natural language prompt into a shell command:

```bash
ata run "list all txt files in current directory"
```

Preview without executing:

```bash
ata run "list all txt files" -n
```

### **Fix a Broken Command**

```bash
ata fix "ls -l /unknown" "ls: cannot access '/unknown': No such file or directory"
```

---

## **Development**

If you modify the code, reinstall the package:

```bash
pip install -e .
```

---

## **Uninstall**

To remove `termAI`:

```bash
pip uninstall termAI -y
```

---

## **Troubleshooting**

1. **`ata: command not found`**
   Make sure you are inside the virtual environment:

   ```bash
   source .venv/bin/activate
   ```

2. **Quota Error (429)**
   The Gemini API free tier has strict limits. Upgrade your plan or wait for quota reset.

---

## **License**

This project is licensed under the MIT License.

---

## **Author**

**Ruvais P**

```

---

### **Next Step**
Would you like me to **add this README.md to your project and give you a ready-to-use `final_project.zip` (with fixed CLI and setup)?**
```
