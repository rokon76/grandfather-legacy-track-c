import numpy as np

def calculate_fidelity(time_scale, energy_gap):
    """
    Measures the fidelity of a nuclear transition. 
    A higher fidelity means the system remained 'cold' (adiabatic).
    """
    # Landau-Zener probability of a non-adiabatic jump
    # P = exp(-2 * pi * gap^2 / velocity)
    # For a benchmark, we use a normalized decay function:
    fidelity = 1.0 - np.exp(-(energy_gap**2) * time_scale)
    return np.clip(fidelity, 0, 1)

def entropy_bounty_multiplier(fidelity):
    """
    Track C Incentive Logic:
    Higher fidelity simulations earn a higher accuracy multiplier.
    """
    return 10.0 * (fidelity**2)

# --- Test Case: Simulation of a U-235 Fission Barrier ---
energy_gap = 5.7  # MeV (Standard U-235 barrier)
simulated_time = 0.85 # Normalized time scale from miner

score = calculate_fidelity(simulated_time, energy_gap)
multiplier = entropy_bounty_multiplier(score)

print(f"--- GFL Track C: Entropy Bounty Report ---")
print(f"Transition Fidelity: {score:.4f}")
print(f"Bounty Multiplier: {multiplier:.2f}x")