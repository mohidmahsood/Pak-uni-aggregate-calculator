def calculate_nust(matric_pct: float, fsc_pct: float, net_score: float) -> float:
    """NUST Formula: 75% NET + 15% FSc + 10% Matric"""
    net_pct = (net_score / 200) * 100
    return (net_pct * 0.75) + (fsc_pct * 0.15) + (matric_pct * 0.10)


def calculate_fast(matric_pct: float, fsc_pct: float, nu_score: float) -> float:
    """FAST-NUCES Formula: 50% NU Test + 40% FSc + 10% Matric"""
    return (nu_score * 0.50) + (fsc_pct * 0.40) + (matric_pct * 0.10)


def calculate_comsats(matric_pct: float, fsc_pct: float, nts_score: float) -> float:
    """COMSATS Formula: 50% NTS NAT + 40% FSc + 10% Matric"""
    return (nts_score * 0.50) + (fsc_pct * 0.40) + (matric_pct * 0.10)


def main():
    print("=== Pakistani CS/Engineering University Aggregate Calculator ===")
    matric_obt = float(input("Matric Obtained Marks: "))
    matric_tot = float(input("Matric Total Marks (e.g., 1100): "))
    fsc_obt = float(input("FSc / ICS Obtained Marks: "))
    fsc_tot = float(input("FSc / ICS Total Marks (e.g., 560 or 1100): "))

    matric_pct = (matric_obt / matric_tot) * 100
    fsc_pct = (fsc_obt / fsc_tot) * 100

    print("\n--- Enter Test Scores (enter 0 if not taken yet) ---")
    net_score = float(input("NUST NET Score (out of 200): "))
    nu_score = float(input("FAST NU Test Score (out of 100): "))
    nts_score = float(input("NTS NAT Score (out of 100): "))

    print("\n=== Your Calculated Aggregates ===")
    if net_score > 0:
        print(f"NUST Aggregate:    {calculate_nust(matric_pct, fsc_pct, net_score):.2f}%")
    if nu_score > 0:
        print(f"FAST Aggregate:    {calculate_fast(matric_pct, fsc_pct, nu_score):.2f}%")
    if nts_score > 0:
        print(f"COMSATS Aggregate: {calculate_comsats(matric_pct, fsc_pct, nts_score):.2f}%")


if __name__ == "__main__":
    main()
