import sys
from pathlib import Path
from coder_agent import generate_code
from runner_agent import run_code

MAX_TRIES = 5
OUTPUT_DIR = Path(__file__).resolve().parent / "autofile"
OUTPUT_DIR.mkdir(exist_ok=True)

def save_code(code, attempt):
    filename = OUTPUT_DIR / f"generated_code_{attempt}.py"
    with open(filename, "w") as f:
        f.write(code)
    print(f"💾 Code written to {filename}")
    return str(filename)

def get_task():
    if len(sys.argv) > 1:
        return " ".join(sys.argv[1:])
    return input("🧠 What do you want the agent to code? ")

def main():
    task = get_task()
    error = None

    for attempt in range(1, MAX_TRIES + 1):
        print(f"\n🔁 Attempt {attempt}")
        code, _ = generate_code(task, error)
        code_file = save_code(code, attempt)
        stdout, stderr = run_code(code_file)

        if stderr:
            print("❌ Error:\n", stderr)
            error = stderr
        else:
            print("✅ Success:\n", stdout)
            print(code)
            break
    else:
        print("\n⚠️ All attempts failed.")

if __name__ == "__main__":
    main()
