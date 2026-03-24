"""
Entry point for running all validation checks against a dataset directory.

Usage:
    python run_all_checks.py --dataset ../datasets/incident_dataset/
    python run_all_checks.py --dataset ../datasets/ --all
"""
import argparse, sys, os

def main():
    parser = argparse.ArgumentParser(description="Run all data validation checks")
    parser.add_argument("--dataset", required=True, help="Path to dataset directory to validate")
    parser.add_argument("--all", action="store_true", help="Run against all datasets")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed output")
    args = parser.parse_args()

    if not os.path.isdir(args.dataset):
        print(f"Directory not found: {args.dataset}")
        sys.exit(1)

    # TODO: Import and run each validator
    print(f"Validating: {args.dataset}")
    print("Validators not yet implemented - see validators/ for contribution guide")

if __name__ == "__main__":
    main()
