

# 🧠 AutoCoder Agent

A Python-based application that generates and executes Python code based on user prompts. It combines a code generation agent with a Flask API to receive prompts, generate code, execute it, and return results. The system retries code generation up to a maximum number of attempts if errors occur, making it robust for iterative development.

---

## 🔧 Technologies Used

- 🐍 **Python**: Core language for code generation and execution
  - **subprocess**: Runs generated Python scripts
  - **pathlib**: Handles file paths and directories
- 🚀 **Backend**: Flask (REST API for code generation and execution)
- 🔗 **Communication**: JSON-based API requests
![Architecture Diagram](flow1.png)
![Architecture Diagram](flow1.png)

---


## 📁 Folder Structure

```
autocoder/
├── autofile/                  # Directory for generated code files
├── main.py                    # Main script to handle task input and code generation
├── runner_agent.py            # Executes generated code
├── runner.py                  # Flask API server for handling prompts
└── README.md
```

*Note*: The `coder_agent.py` file (containing the `generate_code` function) is assumed to exist and is not included here. It should implement the logic for generating Python code based on a user prompt and previous errors.

---

## ⚙️ Setup Instructions

### 🔌 1. Clone the Repository

```bash
git clone https://github.com/your-username/autocoder.git
cd autocoder
```

### 🐍 2. Install Dependencies

Ensure Python 3.8+ is installed, then install the required packages:

```bash
pip install flask
```

*Note*: The `coder_agent` module may require additional dependencies (e.g., an AI model or API client for code generation). Install those as needed.

### 🔧 3. Start the Flask Server

Run the Flask API to accept code generation requests:

```bash
python3 runner.py
```

- **Runs on**: `http://localhost:5005`
- **Debug mode**: Enabled for development (disable in production).

### 💻 4. Run Directly (Optional)

To run the code generation process directly without the API:

```bash
python3 main.py "Your code generation prompt here"
```

- Alternatively, run interactively:
  ```bash
  python3 main.py
  ```
  Then enter a prompt when asked.

---

## 🧪 How It Works

1. **Prompt Input**:
   - Via the Flask API (`POST /run` with a JSON body containing a `prompt` field).
   - Or directly via `main.py` (command-line argument or interactive input).

2. **Code Generation**:
   - The `main.py` script calls `generate_code` from `coder_agent` to create Python code based on the prompt.
   - Generated code is saved to `autofile/generated_code_<attempt>.py`.

3. **Execution**:
   - The `runner_agent.py` script executes the generated code using `subprocess`.
   - Execution is timed out after 10 seconds to prevent hangs.

4. **Retries**:
   - Up to 5 attempts are made to generate and execute correct code if errors occur.
   - Errors from previous attempts are passed to `generate_code` for improvement.

5. **API Response**:
   - The Flask server returns a JSON object with the generated code, filename, output, and any errors.

---

## 🛠️ Example API Request

Send a prompt to generate and execute code using cURL:

```bash
curl -X POST http://localhost:5005/run \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Write a Python function to calculate the factorial of a number"}'
```

**Example Response**:

```json
{
  "status": "success",
  "filename": "autofile/generated_code_1.py",
  "code": "def factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n-1)",
  "output": "",
  "error": ""
}
```

---

## 💡 Future Enhancements

- Integrate an AI model (e.g., xAI's Grok API) in `coder_agent.py` for advanced code generation.
- Add support for validating generated code syntax before execution.
- Implement persistent storage for generated files and results.
- Enhance error handling with detailed debugging information.
- Add support for other programming languages.

---


