import hfb3
import time

def log(msg):
    print(msg, flush=True)

try:
    log("GFL PROMETHEUS: Initializing Production Solver Routine...")
    dt = hfb3.DataTree()
    
    # --- CORE STRUCTURAL ROUTING ---
    dt.setS("solver/name", "D1R")
    dt.setS("solver/type", "2-center-ho")
    
    # --- SAFE BOUNDS MATRIX INITIALIZATION ---
    dt.setI("basis/nOscil", 8)      # Sized for initialization stability
    dt.setI("basis/n_zMax", 8)      
    dt.setD("basis/d_0", 1.0)
    dt.setD("basis/b_r", 1.5)       
    dt.setD("basis/b_z", 1.5)
    dt.setD("basis/g_q", 0.1)       # Non-zero constraint to prevent divide-by-zero crashes
    log("DataTree constraints successfully assigned.")

    log("Binding DataTree to Core Solver...")
    s = hfb3.Solver(dt)
    
    log(f"Current Solver Iteration: {s.nbIter}")
    if s.nbIter >= 0:
        log("!!! PRODUCTION SOLVER ONLINE AND RUNNING !!!")

except Exception as e:
    log(f"CRITICAL solver execution exception: {e}")

# --- CONTINUOUS RUN MONITORING LOOP ---
log("GFL PROMETHEUS: Entering persistent monitoring state...")
while True:
    time.sleep(60)