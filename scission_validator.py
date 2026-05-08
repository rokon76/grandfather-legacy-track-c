import numpy as np

def calculate_sawtooth_fidelity(mass_fragment, simulated_spin):
    """
    Validates if the fragment spin follows the 2026 'Sawtooth' distribution.
    Light fragments (Mass ~90-110) vs Heavy fragments (Mass ~130-150).
    """
    # Idealized Sawtooth curve from 2026 TDDFT data
    # (High spin for light fragments, lower/stable spin for heavy)
    if mass_fragment < 120:
        target_spin = 8.5 - (mass_fragment - 90) * 0.05
    else:
        target_spin = 6.0 + (mass_fragment - 130) * 0.12
    
    error = abs(simulated_spin - target_spin)
    fidelity = np.exp(-error) # 1.0 is perfect match
    return fidelity

# --- Test Case: U-235 Fission Event ---
fragment_mass = 96.0 
miner_predicted_spin = 8.2  # In h-bar units

fidelity_score = calculate_sawtooth_fidelity(fragment_mass, miner_predicted_spin)
print(f"--- Track C Scission Report ---")
print(f"Fragment Mass: {fragment_mass} | Fidelity: {fidelity_score:.4f}")