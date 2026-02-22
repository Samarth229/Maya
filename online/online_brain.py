import subprocess


def query_online_llm(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "phi", prompt],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            timeout=60
        )

        output = result.stdout.strip()

        if not output:
            return (
                "I tried to think about that, but didn’t get a response. "
                "Let’s continue offline."
            )

        return output

    except subprocess.TimeoutExpired:
        return (
            "My local intelligence is taking too long to respond. "
            "Let’s continue offline."
        )

    except Exception:
        return (
            "I tried to use my local intelligence, "
            "but something went wrong. Let’s continue offline."
        )

import threading
import subprocess

def warm_up_llm():
    def _warm():
        try:
            subprocess.run(
                ["ollama", "run", "phi", "hello"],
                capture_output=True,
                timeout=60
            )
        except:
            pass

    threading.Thread(target=_warm, daemon=True).start()



