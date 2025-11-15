import time
import random
from datetime import datetime
import keyboard
import sys
import os

# ANSI barvy
ORANGE = "\033[38;5;208m"      # oranžová
LIME_GREEN = "\033[38;5;118m"  # lime green
YELLOW = "\033[93m"            # žlutá
RED = "\033[91m"               # červená
RESET = "\033[0m"

def simulate_ddos(total_loops=10, requests_per_cycle=1000, cycle_duration=10):
    print("=== DDoS Simulation (visual only, no traffic) ===\n")
    for loop in range(1, total_loops + 1):
        print(f"\n--- Cycle {loop}/{total_loops} ---")
        start = time.time()
        for req in range(1, requests_per_cycle + 1):
            # Emergency exit/restart
            if keyboard.is_pressed("ctrl+shift+p"):
                choice = input(f"\n{RED}Emergency Exit triggered! Stop script? (y/n): {RESET}")
                if choice.lower() == "y":
                    print(f"{RED}Script stopped.{RESET}")
                    sys.exit(0)

            if keyboard.is_pressed("ctrl+shift+o"):
                choice = input(f"\n{ORANGE}Emergency Restart triggered! Restart script? (y/n): {RESET}")
                if choice.lower() == "y":
                    print(f"{ORANGE}Restarting script...{RESET}")
                    os.execv(sys.executable, ["python"] + sys.argv)

            # Rozdělení výsledků podle procent
            roll = random.random()
            if roll < 0.95:
                status = f"{LIME_GREEN}SUCCESS{RESET}"
            elif roll < 0.96:
                status = f"{YELLOW}LOST{RESET}"
            else:
                status = f"{RED}ERROR{RESET}"

            # Fake metriky
            rps = random.randint(50000, 200000)   # větší čísla pro masivní provoz
            latency = random.uniform(10, 500)
            cpu = random.uniform(70, 99)

            # Date/time lime green, Req/RPS/Latency oranžově
            print(f"{LIME_GREEN}[{datetime.now().strftime('%H:%M:%S')}]{RESET} "
                  f"{ORANGE}Req {req}/{requests_per_cycle}{RESET} | "
                  f"{ORANGE}RPS={rps}{RESET} | "
                  f"{ORANGE}Latency={latency:.1f}ms{RESET} | "
                  f"CPU={cpu:.1f}% | Status={status}")

            time.sleep(cycle_duration / requests_per_cycle)

        elapsed = time.time() - start
        print(f"Cycle {loop} finished in {elapsed:.2f}s")

    print("\n=== Target ddosed===")
    print("Total requests sent:1000+")
    print("Network activity: Very High")

if __name__ == "__main__":
    simulate_ddos(total_loops=10, requests_per_cycle=1000, cycle_duration=10)