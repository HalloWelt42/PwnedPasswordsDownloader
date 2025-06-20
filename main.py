import os
import hashlib
import requests
import threading
from queue import Queue
from tqdm import tqdm

API_URL = "https://api.pwnedpasswords.com/range/{}"
OUTPUT_DIR = "hashes"
NUM_THREADS = os.cpu_count() or 4

def download_prefix(prefix, session):
    url = API_URL.format(prefix)
    resp = session.get(url, timeout=10)
    resp.raise_for_status()
    path = os.path.join(OUTPUT_DIR, prefix + ".txt")
    with open(path, "wb") as f:
        f.write(resp.content)

def worker(queue, session):
    while True:
        prefix = queue.get()
        if prefix is None:
            break
        try:
            download_prefix(prefix, session)
        except Exception as e:
            print(f"Fehler bei {prefix}: {e}")
            queue.put(prefix)  # Neu versuchen
        queue.task_done()

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Alle möglichen 5-stelligen hex-Präfixe
    prefixes = [f"{i:05X}" for i in range(0x00000, 0x100000)]

    q = Queue()
    for p in prefixes:
        q.put(p)

    session = requests.Session()
    threads = []
    for _ in range(NUM_THREADS):
        t = threading.Thread(target=worker, args=(q, session), daemon=True)
        t.start()
        threads.append(t)

    # Fortschrittsanzeige
    with tqdm(total=len(prefixes)) as pbar:
        last_done = 0
        while last_done < len(prefixes):
            done = len([name for name in os.listdir(OUTPUT_DIR) if name.endswith(".txt")])
            pbar.update(done - last_done)
            last_done = done

    q.join()
    for _ in threads:
        q.put(None)
    for t in threads:
        t.join()
    print("Alle Dateien wurden heruntergeladen.")

if __name__ == "__main__":
    main()
